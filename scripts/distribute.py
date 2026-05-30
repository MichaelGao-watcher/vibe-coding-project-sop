#!/usr/bin/env python3
"""
母库知识分发脚本
将母库（vibe-coding-project-sop）的最新经验条目合并到下游项目。
按规则去重，来源标注，不覆盖下游项目自己的独有内容。

用法:
    python scripts/distribute.py <下游项目路径1> [路径2 ...]

分发流程:
    1. 解析母库的三个知识文件（decisions.md、lessons-learned.md、troubleshooting.md）
    2. 对每个下游项目：
       a. 合并母库新条目（按标题/关键词去重）
       b. 重建 experience-index.md
       c. Git commit + push（可选）
    3. 汇报结果
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path
from typing import List, Optional, Tuple


MOTHER_LABEL = "vibe-coding-project-sop"
KNOWLEDGE_FILES = ["decisions.md", "lessons-learned.md", "troubleshooting.md"]


def log(msg: str) -> None:
    print(f"[distribute] {msg}")


def warn(msg: str) -> None:
    print(f"[distribute] ⚠️  {msg}", file=sys.stderr)


def error(msg: str) -> None:
    print(f"[distribute] ❌ {msg}", file=sys.stderr)


# ── 解析函数（与 sync-knowledge.py 一致） ──


def parse_adr_entries(text: str) -> list[dict]:
    """从 decisions.md 中提取 ADR 条目。"""
    entries = []
    pattern = r"^## (ADR-\d+[:：]\s*.+?)\n(.*?)(?=\n## |\Z)"
    for m in re.finditer(pattern, text, re.MULTILINE | re.DOTALL):
        title = m.group(1).strip()
        body = m.group(2).strip()
        entries.append({"title": title, "body": body, "raw": m.group(0)})
    return entries


def parse_lesson_entries(text: str) -> list[dict]:
    """从 lessons-learned.md 中提取经验条目。"""
    entries = []
    for line in text.splitlines():
        m = re.match(r"^\|\s*\|\s*(.+?)\s*(?:\[来源:.+?\])?\s*\|\s*(.*?)\s*\|$", line)
        if m and not line.strip().startswith("|---"):
            desc = m.group(1).strip()
            if _is_valid_lesson(desc):
                entries.append({"description": desc, "source": m.group(2).strip()})
    # 也匹配列表形式的经验
    for line in text.splitlines():
        m = re.match(r"^[-*]\s+(.+)$", line)
        if m:
            desc = m.group(1).strip()
            if _is_valid_lesson(desc):
                entries.append({"description": desc, "source": ""})
    return entries


def _is_valid_lesson(desc: str) -> bool:
    if not desc or desc.startswith("[") and desc.endswith("]"):
        return False
    if desc.startswith("❌"):
        return False
    if desc.startswith("**AI 助手**") or desc.startswith("**人类把控者**"):
        return False
    if re.match(r"^\[\s*[xX\s]\]\s*$", desc) or desc in ("[ ] xxx", "[ ] 无"):
        return False
    if re.match(r"^\*\*(启动|优势|限制|完整功能验证)\*\*", desc):
        return False
    exclude_keywords = ["不记录的内容", "排除标准", "何时记录", "记录时机",
                        "与 troubleshooting.md 的分界"]
    if any(kw in desc for kw in exclude_keywords):
        return False
    return True


def parse_trouble_entries(text: str) -> list[dict]:
    """从 troubleshooting.md 中提取问题条目。"""
    entries = []
    pattern = r"^### (.+?)\n(.*?)(?=\n### |\Z)"
    for m in re.finditer(pattern, text, re.MULTILINE | re.DOTALL):
        title = m.group(1).strip()
        body = m.group(2).strip()
        entries.append({"keyword": title, "body": body, "raw": m.group(0)})
    return entries


def _similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def read_file(path: Path) -> str:
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ── 合并函数（母库 → 下游） ──


def _clean_title(title: str) -> str:
    """去掉来源标签后的纯标题。"""
    return re.sub(r"\s*\[来源:.+?\]", "", title).strip()


def _clean_keyword(keyword: str) -> str:
    """去掉来源标签后的纯关键词。"""
    return re.sub(r"\s*\[来源:.+?\]", "", keyword).strip()


def merge_decisions(local_text: str, mother_entries: list[dict]) -> Tuple[str, int, int]:
    """
    将母库的 ADR 条目合并到下游项目。
    返回 (新文本, 新增数, 跳过数)。
    """
    today = datetime.now().strftime("%Y-%m-%d")
    source_tag = f"[来源:{MOTHER_LABEL} @{today}]"
    added = 0
    skipped = 0

    # 提取下游已有的标题
    existing_titles = re.findall(r"^##\s+(.+?)$", local_text, re.MULTILINE)

    blocks = []
    for e in mother_entries:
        title_clean = _clean_title(e["title"])

        # 精确匹配
        if title_clean in local_text:
            skipped += 1
            continue

        # 相似度去重
        dup = False
        for existing in existing_titles:
            existing_clean = _clean_title(existing)
            if existing_clean and _similarity(title_clean, existing_clean) > 0.75:
                skipped += 1
                dup = True
                break
        if dup:
            continue

        new_entry = f"## {title_clean} {source_tag}\n\n{e['body']}\n"
        blocks.append(new_entry)
        added += 1

    if not blocks:
        return local_text, 0, skipped

    # 插入到 "新增决策时复制上方模板" 之前（如果有）
    template_marker = re.search(r"\*新增决策时复制上方模板\*", local_text)
    if template_marker:
        insert_pos = template_marker.end()
        new_text = (local_text[:insert_pos] + "\n\n" +
                    "\n".join(blocks) + "\n" +
                    local_text[insert_pos:])
    else:
        # 追加到文件末尾
        new_text = local_text.rstrip() + "\n\n" + "\n".join(blocks) + "\n"

    return new_text, added, skipped


def merge_lessons(local_text: str, mother_entries: list[dict]) -> Tuple[str, int, int]:
    """
    将母库的经验条目合并到下游项目。
    返回 (新文本, 新增数, 跳过数)。
    """
    today = datetime.now().strftime("%Y-%m-%d")
    source_tag = f"[来源:{MOTHER_LABEL} @{today}]"
    added = 0
    skipped = 0

    # 提取下游已有的经验描述
    existing_descs = re.findall(r"^\|\s*\|\s*(.+?)\s*(?:\[来源:.+?\])?\s*\|\s*(.*?)\s*\|$",
                                local_text, re.MULTILINE)

    lines_to_add = []
    for e in mother_entries:
        desc = e["description"]
        if not desc or desc.startswith("[") and desc.endswith("]"):
            continue

        # 精确匹配
        if desc in local_text:
            skipped += 1
            continue

        # 相似度去重
        dup = False
        for existing_desc, _ in existing_descs:
            existing_clean = re.sub(r"\[来源:.+?\]", "", existing_desc).strip()
            if existing_clean and _similarity(desc, existing_clean) > 0.75:
                skipped += 1
                dup = True
                break
        if dup:
            continue

        line = f"| | {desc} {source_tag} | {e.get('source', '')} |"
        lines_to_add.append(line)
        added += 1

    if not lines_to_add:
        return local_text, 0, skipped

    # 找到第一个表格行后面的位置（在表头之后插入）
    # 尝试在技术经验表格末尾插入
    table_end = local_text.rfind("|\n\n")
    if table_end == -1 or table_end < local_text.find("## "):
        # 没有找到表格，直接追加到最后
        new_text = local_text.rstrip() + "\n" + "\n".join(lines_to_add) + "\n"
    else:
        new_text = (local_text[:table_end] + "\n".join(lines_to_add) + "\n" +
                    local_text[table_end:])

    return new_text, added, skipped


def merge_troubleshooting(local_text: str, mother_entries: list[dict]) -> Tuple[str, int, int]:
    """
    将母库的 troubleshooting 条目合并到下游项目。
    返回 (新文本, 新增数, 跳过数)。
    """
    today = datetime.now().strftime("%Y-%m-%d")
    source_tag = f"[来源:{MOTHER_LABEL} @{today}]"
    added = 0
    skipped = 0

    # 提取下游已有的关键词
    existing_keywords = re.findall(r"^###\s+(.+?)$", local_text, re.MULTILINE)

    blocks = []
    for e in mother_entries:
        keyword_clean = _clean_keyword(e["keyword"])

        # 精确匹配
        if keyword_clean in local_text:
            skipped += 1
            continue

        # 相似度去重
        dup = False
        for existing in existing_keywords:
            existing_clean = _clean_keyword(existing)
            if existing_clean and _similarity(keyword_clean, existing_clean) > 0.75:
                skipped += 1
                dup = True
                break
        if dup:
            continue

        new_block = f"### {keyword_clean} {source_tag}\n\n{e['body']}\n"
        blocks.append(new_block)
        added += 1

    if not blocks:
        return local_text, 0, skipped

    # 追加到文件末尾
    new_text = local_text.rstrip() + "\n\n" + "\n".join(blocks) + "\n"
    return new_text, added, skipped


# ── Git 操作 ──


def git_commit_push(project_dir: Path, project_name: str) -> bool:
    """对项目执行 git add + commit + push，返回是否成功。"""
    try:
        # 检查是否有 .git
        if not (project_dir / ".git").exists():
            warn(f"{project_name} 没有 .git 目录，跳过 Git")
            return True  # 不算失败

        # 检查是否有变更
        result = subprocess.run(
            ["git", "-C", str(project_dir), "status", "--porcelain"],
            capture_output=True, text=True, timeout=30
        )
        if not result.stdout.strip():
            log(f"{project_name} 无变更，跳过 Git")
            return True

        # git add -A
        subprocess.run(
            ["git", "-C", str(project_dir), "add", "-A"],
            capture_output=True, timeout=30
        )

        # git commit
        commit_msg = f"[distribute] 同步母库经验 {datetime.now().strftime('%Y-%m-%d')}"
        result = subprocess.run(
            ["git", "-C", str(project_dir), "commit", "-m", commit_msg],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            if "nothing to commit" in result.stderr or "nothing to commit" in result.stdout:
                return True
            warn(f"{project_name} commit 失败: {result.stderr.strip()}")
            return False

        # git push
        result = subprocess.run(
            ["git", "-C", str(project_dir), "push"],
            capture_output=True, text=True, timeout=60
        )
        if result.returncode != 0:
            warn(f"{project_name} push 失败: {result.stderr.strip()}")
            return False

        log(f"{project_name} Git commit + push 成功")
        return True

    except subprocess.TimeoutExpired:
        warn(f"{project_name} Git 操作超时")
        return False
    except Exception as e:
        warn(f"{project_name} Git 操作异常: {e}")
        return False


# ── 重建索引 ──


def rebuild_index(project_dir: Path, project_name: str) -> bool:
    """在下游项目中运行 build-experience-index.py 重建索引。"""
    index_script = project_dir / "scripts" / "build-experience-index.py"
    if not index_script.exists():
        warn(f"{project_name} 没有 scripts/build-experience-index.py，跳过索引重建")
        return False

    try:
        result = subprocess.run(
            [sys.executable, str(index_script)],
            capture_output=True, text=True, cwd=str(project_dir), timeout=30
        )
        if result.returncode == 0:
            log(f"{project_name} 经验索引已重建")
            return True
        else:
            warn(f"{project_name} 索引重建失败: {result.stderr.strip()}")
            return False
    except subprocess.TimeoutExpired:
        warn(f"{project_name} 索引重建超时")
        return False


# ── 主流程 ──


def distribute(mother_dir: Path, project_dirs: List[Path], skip_git: bool = False) -> int:
    """将母库知识分发到下游项目。"""
    today = datetime.now().strftime("%Y-%m-%d")
    source_tag = f"[来源:{MOTHER_LABEL} @{today}]"

    log(f"母库路径: {mother_dir}")
    log(f"下游项目: {len(project_dirs)} 个")
    log(f"来源标签: {source_tag}")
    log("")

    # 1. 加载母库文件
    mother_files = {}
    for fname in KNOWLEDGE_FILES:
        path = mother_dir / fname
        if not path.exists():
            error(f"母库文件缺失: {path}")
            return 1
        mother_files[fname] = read_file(path)

    # 2. 解析母库条目
    mother_entries = {}
    mother_entries["decisions.md"] = parse_adr_entries(mother_files["decisions.md"])
    mother_entries["lessons-learned.md"] = parse_lesson_entries(mother_files["lessons-learned.md"])
    mother_entries["troubleshooting.md"] = parse_trouble_entries(mother_files["troubleshooting.md"])

    log(f"母库条目数: decisions={len(mother_entries['decisions.md'])}, "
        f"lessons={len(mother_entries['lessons-learned.md'])}, "
        f"troubleshooting={len(mother_entries['troubleshooting.md'])}")
    log("")

    # 3. 处理每个下游项目
    total_added = {"decisions.md": 0, "lessons-learned.md": 0, "troubleshooting.md": 0}
    total_skipped = {"decisions.md": 0, "lessons-learned.md": 0, "troubleshooting.md": 0}
    git_ok = 0
    index_ok = 0

    for proj_dir in project_dirs:
        proj_name = proj_dir.name
        log(f"── {proj_name} ──")

        if not proj_dir.is_dir():
            warn(f"目录不存在: {proj_dir}")
            continue

        for fname in KNOWLEDGE_FILES:
            local_text = read_file(proj_dir / fname)
            if not local_text.strip():
                # 下游项目没有该文件，创建一份
                write_file(proj_dir / fname, mother_files[fname])
                total_added[fname] += len(mother_entries[fname])
                log(f"  {fname}: 新建 ({len(mother_entries[fname])} 条)")
                continue

            if fname == "decisions.md":
                new_text, added, skipped = merge_decisions(local_text,
                                                            mother_entries[fname])
            elif fname == "lessons-learned.md":
                new_text, added, skipped = merge_lessons(local_text,
                                                          mother_entries[fname])
            elif fname == "troubleshooting.md":
                new_text, added, skipped = merge_troubleshooting(local_text,
                                                                  mother_entries[fname])
            else:
                continue

            total_added[fname] += added
            total_skipped[fname] += skipped

            if added > 0:
                write_file(proj_dir / fname, new_text)
                log(f"  {fname}: +{added} 条（跳过 {skipped} 条重复）")
            else:
                log(f"  {fname}: 无新增（跳过 {skipped} 条重复）")

        # 重建索引
        if rebuild_index(proj_dir, proj_name):
            index_ok += 1

        # Git 操作
        if not skip_git:
            if git_commit_push(proj_dir, proj_name):
                git_ok += 1

        log("")

    # 4. 汇报汇总
    log("=" * 40)
    log(f"分发完成")
    log(f"  项目数:     {len(project_dirs)}")
    log(f"  索引重建:   {index_ok}/{len(project_dirs)}")
    if not skip_git:
        log(f"  Git 提交:    {git_ok}/{len(project_dirs)}")
    log(f"")
    log(f"  decisions.md:      +{total_added['decisions.md']} 条, "
        f"跳过 {total_skipped['decisions.md']} 条重复")
    log(f"  lessons-learned.md: +{total_added['lessons-learned.md']} 条, "
        f"跳过 {total_skipped['lessons-learned.md']} 条重复")
    log(f"  troubleshooting.md: +{total_added['troubleshooting.md']} 条, "
        f"跳过 {total_skipped['troubleshooting.md']} 条重复")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="将母库知识分发到下游项目"
    )
    parser.add_argument("projects", nargs="+",
                        help="下游项目路径，可指定多个")
    parser.add_argument("--skeleton", default=None,
                        help="母库路径（默认自动检测）")
    parser.add_argument("--skip-git", action="store_true",
                        help="跳过 Git commit + push")
    args = parser.parse_args()

    # 定位母库路径
    if args.skeleton:
        mother_dir = Path(args.skeleton).resolve()
    else:
        # 默认为本脚本所在项目的根目录
        mother_dir = Path(__file__).resolve().parent.parent

    if not (mother_dir / "scripts" / "distribute.py").exists():
        # 检查脚本自身位置
        mother_dir = Path(__file__).resolve().parent.parent

    # 验证母库
    missing = [f for f in KNOWLEDGE_FILES if not (mother_dir / f).exists()]
    if missing:
        error(f"母库文件缺失: {', '.join(missing)}")
        error(f"请确认母库路径: {mother_dir}")
        return 1

    # 验证下游项目
    project_dirs = []
    for p in args.projects:
        path = Path(p).resolve()
        if not path.is_dir():
            error(f"下游项目目录不存在: {path}")
            return 1
        project_dirs.append(path)

    return distribute(mother_dir, project_dirs, skip_git=args.skip_git)


if __name__ == "__main__":
    sys.exit(main())

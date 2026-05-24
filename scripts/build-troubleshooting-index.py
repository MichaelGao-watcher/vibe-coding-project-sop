#!/usr/bin/env python3
"""
Troubleshooting 搜索索引生成脚本
解析 troubleshooting.md，自动生成 troubleshooting-index.md

用法:
    python scripts/build-troubleshooting-index.py
    python scripts/build-troubleshooting-index.py --check

--check 模式：验证索引与源文件是否同步（CI 用）
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Optional, Tuple


SOURCE_FILE = "troubleshooting.md"
INDEX_FILE = "troubleshooting-index.md"

# 技术栈关键词映射（不区分大小写）
TECH_STACK_KEYWORDS: dict[str, list[str]] = {
    "Rust / Tauri": [
        "rust", "cargo", "tauri", "rustc", "crate", "webview2",
        "filetime", "getdiskfreespaceexw", "mingw", "ucrt", "dll",
        "0xc0000139", "0xc0000005", "status_entrypoint",
    ],
    "JavaScript / React / Vitest": [
        "javascript", "react", "jsx", "node", "npm", "vitest", "vite",
        "jest", "dom", "chess.js", "canvas", "svg", "queryselector",
        "queryselectorall", "addeventlistener", "event",
        "unexpected identifier", "cannot update",
    ],
    "Python": ["python", "pip", "pytest"],
    "网络 / 环境 / 权限": [
        "网络", "cdn", "dns", "代理", "proxy", "timeout", "连接超时",
        "防火墙", "firewall", "path", "编码", "utf", "权限",
        "中文路径", "huggingface", "modelscope", "github pages",
        "access is denied",
    ],
    "AI 工具链 / LLM": [
        "llm", "ollama", "llama", "llama-server", "model",
        "deepseek", "qwen", "gguf", "modelscope", "huggingface",
    ],
    "Git / GitHub": [
        "git", "github", "ssh", "push", "pull", "commit", "merge",
        "gh auth", "permission denied",
    ],
    "Windows / PowerShell": [
        "powershell", "windows", "ucrt", "dll", "mingw", "exe",
        "unexpectedtoken", "bom", "防火墙",
    ],
    "Chess / 引擎": [
        "stockfish", "chess", "uci", "pgn", "engine",
        "gomultipv", "candidate", "move",
    ],
}


def log(msg: str) -> None:
    print(f"[build-index] {msg}")


def extract_source(text: str) -> tuple[str, str]:
    """从标题中提取来源，返回 (纯标题, 来源)"""
    m = re.search(r"\[来源:([^\]]+)\]", text)
    if m:
        source = m.group(1).strip()
        clean = re.sub(r"\s*\[来源:[^\]]+\]", "", text).strip()
        return clean, source
    return text.strip(), ""


def parse_table_row(line: str) -> Optional[Tuple[str, str]]:
    """解析 Markdown 表格行，返回 (字段名, 字段值)"""
    if not line.startswith("|"):
        return None
    # 跳过分隔行
    if re.match(r"^\|[-\s|:]+\|$", line):
        return None
    cells = [c.strip() for c in line.split("|")[1:-1]]
    if len(cells) < 2:
        return None
    field_name = re.sub(r"\*\*", "", cells[0]).strip()
    field_value = cells[1]
    if not field_name:
        return None
    return field_name, field_value


def parse_troubleshooting(path: str) -> list[dict]:
    """解析 troubleshooting.md，返回条目列表"""
    entries: list[dict] = []
    current_category = ""
    current_entry: Optional[dict] = None

    with open(path, "r", encoding="utf-8") as f:
        for line_no, raw in enumerate(f, start=1):
            line = raw.rstrip("\n")

            if line.startswith("## ") and not line.startswith("### "):
                current_category = line[3:].strip()
                continue

            if line.startswith("### "):
                if current_entry:
                    entries.append(current_entry)
                title_line = line[4:].strip()
                title, source = extract_source(title_line)
                current_entry = {
                    "category": current_category,
                    "title": title,
                    "source": source,
                    "status": None,
                    "symptom": None,
                    "cause": None,
                    "solution": None,
                    "line_start": line_no,
                }
                continue

            if current_entry is None:
                continue

            parsed = parse_table_row(line)
            if parsed:
                field_name, field_value = parsed
                mapping = {
                    "状态": "status",
                    "现象": "symptom",
                    "原因": "cause",
                    "解决": "solution",
                }
                key = mapping.get(field_name)
                if key and current_entry.get(key) is None:
                    current_entry[key] = field_value

        if current_entry:
            entries.append(current_entry)

    return entries


def infer_tech_stacks(entry: dict) -> list[str]:
    """根据标题和现象推断技术栈标签"""
    text = f"{entry['title']} {entry.get('symptom', '') or ''}".lower()
    # 去掉 URL，避免域名中的技术关键词误匹配（如 blindfold-chess 中的 chess）
    text = re.sub(r"https?://\S+", "", text)
    stacks: list[str] = []
    for stack, keywords in TECH_STACK_KEYWORDS.items():
        for kw in keywords:
            if kw.lower() in text:
                stacks.append(stack)
                break
    return stacks if stacks else ["其他"]


def generate_index(entries: list[dict]) -> str:
    """生成索引 Markdown 内容"""
    lines: list[str] = [
        "# Troubleshooting 搜索索引",
        "",
        "> 本文件由 `scripts/build-troubleshooting-index.py` 自动生成。",
        "> 每次修改 `troubleshooting.md` 后，运行 `python scripts/build-troubleshooting-index.py` 重建。",
        "",
        f"> 当前收录 **{len(entries)}** 条问题记录，按分类 + 关键词排序。",
        "",
        "---",
        "",
        "## 快速搜索表",
        "",
        "| 关键词 | 分类 | 来源 | 状态 | 定位 |",
        "|--------|------|------|------|------|",
    ]

    for e in entries:
        status = (e.get("status") or "—").replace("|", "\\|")
        source = e.get("source", "—")
        # 简化来源显示
        source_short = source.split(" @")[0] if " @" in source else source
        category = e['category'] or "未分类"
        lines.append(
            f"| {e['title']} | {category} | {source_short} | {status} | {SOURCE_FILE}#L{e['line_start']} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 按技术栈分组",
        "",
        "> 一个条目可能同时属于多个技术栈。",
        "",
    ])

    # 按技术栈收集条目
    stack_map: dict[str, list[dict]] = {}
    for e in entries:
        for stack in infer_tech_stacks(e):
            stack_map.setdefault(stack, []).append(e)

    # 固定顺序 + 动态顺序
    preferred_order = [
        "Rust / Tauri",
        "JavaScript / React / Vitest",
        "Python",
        "AI 工具链 / LLM",
        "Git / GitHub",
        "网络 / 环境 / 权限",
        "Windows / PowerShell",
        "Chess / 引擎",
        "其他",
    ]
    sorted_stacks = sorted(
        stack_map.keys(),
        key=lambda s: (preferred_order.index(s) if s in preferred_order else 999, s),
    )

    for stack in sorted_stacks:
        lines.append(f"### {stack}")
        lines.append("")
        for e in stack_map[stack]:
            category = e['category'] or "未分类"
            lines.append(f"- [{e['title']}]({SOURCE_FILE}#L{e['line_start']}) — `{category}`")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build troubleshooting search index")
    parser.add_argument("--check", action="store_true", help="Check if index is up-to-date")
    args = parser.parse_args()

    src = Path(SOURCE_FILE)
    idx = Path(INDEX_FILE)

    if not src.exists():
        log(f"ERROR: {SOURCE_FILE} not found")
        return 1

    entries = parse_troubleshooting(str(src))
    log(f"Parsed {len(entries)} entries from {SOURCE_FILE}")

    new_content = generate_index(entries)

    if args.check:
        if not idx.exists():
            log(f"ERROR: {INDEX_FILE} does not exist")
            return 1
        current = idx.read_text(encoding="utf-8")
        if current.strip() == new_content.strip():
            log("Index is up-to-date")
            return 0
        log("ERROR: Index is out of date. Run without --check to rebuild.")
        return 1

    idx.write_text(new_content, encoding="utf-8")
    log(f"Wrote {INDEX_FILE} ({len(new_content)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

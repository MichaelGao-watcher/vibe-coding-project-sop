#!/usr/bin/env python3
"""
骨架一键初始化脚本
将 vibe-coding-project-sop 的基础设施文件复制到目标项目目录。

用法:
    python init-skeleton.py [--skeleton SKELETON_PATH] [--with-knowledge] [--force] [--target TARGET_DIR]

环境变量:
    SOP_SKELETON_PATH  骨架项目根目录路径（优先级低于 --skeleton）
"""

import argparse
import os
import sys
from pathlib import Path


# 从 templates/ 复制的文件
TEMPLATE_FILES = [
    "vibe-coding-sop.md",
    "status.md",
    "session-log.md",
    "decisions.md",
    "troubleshooting.md",
    "lessons-learned.md",
]

# 从骨架根目录复制的文件（规则模板）
ROOT_FILES = [
    "AGENTS.md",
]

# 母库经验文件（--with-knowledge 时从骨架根目录复制）
KNOWLEDGE_FILES = [
    "lessons-learned.md",
    "troubleshooting.md",
    "decisions.md",
]

# 检测目标目录是否已有代码项目的线索
CODE_INDICATORS = [
    "src", "lib", "app", "dist", "build",
    ".git", "package.json", "Cargo.toml", "pyproject.toml",
    "go.mod", "pom.xml", "CMakeLists.txt", "Makefile",
]


def log(msg: str) -> None:
    print(f"[init-skeleton] {msg}")


def error(msg: str) -> None:
    print(f"[init-skeleton] ERROR: {msg}", file=sys.stderr)


def _is_valid_skeleton(path: Path) -> bool:
    """校验路径是否为有效的骨架项目"""
    return path.is_dir() and (path / "templates").is_dir() and (path / "AGENTS.md").is_file()


def find_skeleton_path(args_path: str | None) -> Path | None:
    """定位骨架项目路径，优先级：参数 > 环境变量 > 交互询问"""
    # 1. 命令行参数
    if args_path:
        p = Path(args_path).resolve()
        if _is_valid_skeleton(p):
            return p
        error(f"--skeleton 指定的路径无效: {p}")
        return None

    # 2. 环境变量
    env_path = os.environ.get("SOP_SKELETON_PATH")
    if env_path:
        p = Path(env_path).resolve()
        if _is_valid_skeleton(p):
            return p
        error(f"SOP_SKELETON_PATH 环境变量指向无效路径: {p}")
        return None

    # 3. 交互式询问
    while True:
        try:
            user_input = input(
                "请输入骨架项目根目录路径（如 D:/Vibe-Code/vibe-coding-project-sop）: "
            ).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return None
        if not user_input:
            return None
        p = Path(user_input).resolve()
        if _is_valid_skeleton(p):
            return p
        error(f"路径无效或缺少必要的模板目录: {p}")
        # 继续询问，不退出


def detect_conflicts(target_dir: Path) -> list[str]:
    """检测目标目录中已存在的冲突文件"""
    conflicts = []
    all_files = set(TEMPLATE_FILES + ROOT_FILES)
    for fname in all_files:
        if (target_dir / fname).exists():
            conflicts.append(fname)
    return conflicts


def detect_existing_code(target_dir: Path) -> bool:
    """检测目标目录是否已有代码项目"""
    for indicator in CODE_INDICATORS:
        if (target_dir / indicator).exists():
            return True
    # 检测常见源码文件（只检查根目录，不递归，避免在大仓库中太慢）
    for ext in [".py", ".js", ".ts", ".tsx", ".java", ".go", ".rs", ".cpp", ".c", ".h"]:
        if list(target_dir.glob(f"*{ext}")):
            return True
    return False


def copy_file(src: Path, dst: Path, force: bool = False) -> str:
    """
    复制文件，返回操作结果："created", "skipped", "overwritten"
    """
    if dst.exists() and not force:
        return "skipped"

    result = "overwritten" if dst.exists() else "created"
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="一键初始化 vibe-coding-project-sop 骨架"
    )
    parser.add_argument(
        "--skeleton",
        help="骨架项目根目录路径",
    )
    parser.add_argument(
        "--with-knowledge",
        action="store_true",
        help="同时复制母库经验（lessons-learned.md / troubleshooting.md / decisions.md）",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="覆盖目标目录已有的同名文件",
    )
    parser.add_argument(
        "--target",
        default=".",
        help="目标项目目录（默认当前目录）",
    )
    args = parser.parse_args()

    target_dir = Path(args.target).resolve()
    if not target_dir.is_dir():
        error(f"目标目录不存在: {target_dir}")
        return 1

    # 定位骨架
    skeleton_path = find_skeleton_path(args.skeleton)
    if not skeleton_path:
        error("无法定位骨架项目路径")
        return 1

    log(f"骨架路径: {skeleton_path}")
    log(f"目标路径: {target_dir}")

    # 检测冲突
    conflicts = detect_conflicts(target_dir)
    if conflicts and not args.force:
        log(f"检测到以下文件已存在，将跳过（使用 --force 覆盖）: {', '.join(conflicts)}")

    # 复制基础设施
    results: list[tuple[str, str]] = []
    templates_dir = skeleton_path / "templates"

    # 确定模板文件列表：如果 --with-knowledge，重叠文件用母库版本替代空模板
    template_files_to_copy = list(TEMPLATE_FILES)
    if args.with_knowledge:
        template_files_to_copy = [
            f for f in TEMPLATE_FILES if f not in KNOWLEDGE_FILES
        ]

    # 从 templates/ 复制
    for fname in template_files_to_copy:
        src = templates_dir / fname
        dst = target_dir / fname
        if src.exists():
            result = copy_file(src, dst, args.force)
            results.append((fname, result))
        else:
            error(f"骨架模板文件缺失: {src}")

    # 从根目录复制 AGENTS.md
    for fname in ROOT_FILES:
        src = skeleton_path / fname
        dst = target_dir / fname
        if src.exists():
            result = copy_file(src, dst, args.force)
            results.append((fname, result))
        else:
            error(f"骨架文件缺失: {src}")

    # 可选：复制母库经验
    if args.with_knowledge:
        log("正在复制母库经验...")
        for fname in KNOWLEDGE_FILES:
            src = skeleton_path / fname
            dst = target_dir / fname
            if src.exists():
                result = copy_file(src, dst, args.force)
                results.append((f"{fname} (母库)", result))
            else:
                error(f"母库文件缺失: {src}")

    # 输出报告
    print("\n" + "=" * 50)
    print("初始化报告")
    print("=" * 50)

    created = [f for f, r in results if r == "created"]
    skipped = [f for f, r in results if r == "skipped"]
    overwritten = [f for f, r in results if r == "overwritten"]

    if created:
        print(f"\n[+] 已创建 ({len(created)}):")
        for f in created:
            print(f"    {f}")

    if skipped:
        print(f"\n[-] 已跳过 ({len(skipped)})（使用 --force 可覆盖）:")
        for f in skipped:
            print(f"    {f}")

    if overwritten:
        print(f"\n[~] 已覆盖 ({len(overwritten)}):")
        for f in overwritten:
            print(f"    {f}")

    # 已完成项目提示
    if detect_existing_code(target_dir):
        print("\n[i] 提示: 检测到目标目录已有代码文件。")
        print("    建议从 vibe-coding-sop.md 阶段五开始，让 AI 逆向补全文档。")

    print("\n[>] 下一步:")
    print("    1. 编辑 AGENTS.md，按项目填空（项目名、技术栈等）")
    print("    2. 读取 vibe-coding-sop.md，判断项目当前阶段")
    print("    3. 按 SOP 五阶段推进")

    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""
starter 安全安装向导。

用法：
    python install.py

功能：
- 检查 AGENTS.md 是否正确包含母库经验指令
- 检查关键文件是否齐全
- 提示修复方法（如有冲突）

运行时机：将 starter/ 复制到本项目后执行。
"""

import shutil
import sys
import io
from pathlib import Path

# Windows 终端 UTF-8 支持
if sys.platform == "win32":
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    except Exception:
        pass


def check_agents() -> bool:
    """检查 AGENTS.md 是否包含母库经验指令。"""
    agents_path = Path("AGENTS.md")
    if not agents_path.exists():
        print("❌ AGENTS.md 不存在")
        return False

    content = agents_path.read_text(encoding="utf-8")

    # 检查是否包含母库经验相关触发词
    if "拉取母库" in content and "母库经验指令" in content:
        print("✅ AGENTS.md 已包含母库经验指令")
        return True
    else:
        print("⚠️  AGENTS.md 存在，但未包含母库经验指令")
        print("   原因：本项目已有 AGENTS.md，复制 starter/ 时未合并母库规则")
        print("\n🔧 修复方法（二选一）：")
        print("   方法 A：将 starter/AGENTS.md 中的「3.7 母库经验指令」章节")
        print("          复制粘贴到您的 AGENTS.md 中")
        print("   方法 B：删除当前 AGENTS.md，直接复制 starter/AGENTS.md 替换")
        print("          （会丢失原有规则，谨慎操作）")
        return False


def check_existing_knowledge() -> bool:
    """检测是否已有经验内容（半成品项目）。"""
    knowledge_files = {
        "decisions.md": "决策记录",
        "lessons-learned.md": "经验沉淀",
        "troubleshooting.md": "问题索引",
    }
    has_content = False
    for path, desc in knowledge_files.items():
        p = Path(path)
        if p.exists() and p.stat().st_size > 100:  # 粗略判断：大于100字节视为有内容
            print(f"⚠️  检测到已有{desc}: {path}（非空）")
            has_content = True
    if has_content:
        print("\n💡 提示：继续拉取母库将使用智能去重")
        print("   - 标题/描述完全相同 → 自动跳过")
        print("   - 相似度 > 75% → 自动跳过")
        print("   - 其余内容 → 追加到文件末尾")
    return has_content


def ensure_files() -> bool:
    """检查并补全关键文件。"""
    required = {
        "config/github-sync.json": "母库同步配置",
        "scripts/pull.py": "拉取脚本",
        "scripts/sync-knowledge.py": "同步引擎",
        "status.md": "状态看板",
        "session-log.md": "会话记录",
        "vibe-coding-sop.md": "五阶段工作流",
        "anti-patterns-checklist.md": "反模式检查清单",
    }

    all_ok = True
    for path, desc in required.items():
        if Path(path).exists():
            print(f"✅ {desc}: {path}")
        else:
            print(f"❌ {desc} 缺失: {path}")
            all_ok = False

    return all_ok


def main() -> int:
    print("=" * 50)
    print("starter 安全安装向导")
    print("=" * 50)
    print()

    agents_ok = check_agents()
    print()
    check_existing_knowledge()
    print()
    files_ok = ensure_files()
    print()

    if agents_ok and files_ok:
        print("=" * 50)
        print("✅ 安装检查通过")
        print("=" * 50)
        print("\n使用方式：")
        print("  对 AI 说：拉取母库")
        print("  或手动运行：python scripts/pull.py")
        return 0
    else:
        print("=" * 50)
        print("⚠️  安装检查未通过，请按上方提示修复")
        print("=" * 50)
        return 1


if __name__ == "__main__":
    sys.exit(main())

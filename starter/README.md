# [项目名]

> 从 [母库/来源] 复制的工作区。

## 快速开始

### 1. 安装 starter/ 工作区

```bash
# 复制 starter/ 到本项目
cp -r vibe-coding-project-sop/starter ./my-project
cd my-project

# 运行安全安装向导
python install.py
```

`install.py` 会自动检查：
- AGENTS.md 是否包含母库经验指令（如有冲突会提示修复方法）
- 关键文件是否齐全

### 2. 拉取母库经验

对 AI 说：
```
拉取母库
```

或手动运行：
```bash
python scripts/pull.py
```

### 3. 填写项目信息

- 修改 `AGENTS.md` 中的「1. 项目定位」
- 修改 `status.md` 中的项目名和环境备忘

### 4. 按五阶段推进

参考 `vibe-coding-sop.md`，根据项目当前状态选择切入阶段。

## 文件说明

| 文件 | 职责 |
|------|------|
| `AGENTS.md` | 硬规则 + 自然语言触发词（恢复 / 存档 / 拉取母库） |
| `status.md` | 当前进度、待办清单 |
| `session-log.md` | 会话历史记录 |
| `vibe-coding-sop.md` | 五阶段工作流参考 |
| `anti-patterns-checklist.md` | 阶段二设计自检 |
| `config/github-sync.json` | 母库同步配置（已预填） |
| `scripts/pull.py` | 拉取母库经验 |
| `scripts/sync-knowledge.py` | 同步引擎 |

## 母库来源

- 仓库：[MichaelGao1999/vibe-coding-project-sop](https://github.com/MichaelGao1999/vibe-coding-project-sop)
- 模板库：[templates/](https://github.com/MichaelGao1999/vibe-coding-project-sop/tree/master/templates)

# vibe-coding-project-sop — 项目状态看板

> 这是骨架母库的活文档，每次变更后更新。

---

## 当前阶段

**基础设施完善 100% 完成 | 下一步：根据实际使用反馈迭代脚本**

---

## 进度总览

`P1 跨项目知识同步 SOP ✅ | P2 自动化同步脚本 ✅ | P3 模板更新 ✅ | P4 AGENTS.md 规则更新 ✅ | P5 实际测试 ✅`

> 图例：✅ 已完成 | 🔄 进行中 | ⚠️ 阻塞/待修复

---

## 待办 📋

> **清理规则**：存档时先删除所有 `[x]` 已打勾的待办，再勾选本轮完成的待办。

### 优先级 3 — 优化
- [ ] 脚本增加 `--dry-run` 模式，预览变更但不写入
- [ ] 脚本增加 `--since` 参数，只同步某日期后的新增内容

### 优先级 4 — Playwright
- [ ] 探索 Playwright MCP 其他用途（天猫后台搁置，配置保留）

---

## 技术债务 🏚️

> 技术债务 = 需要解决但暂时搁置的难题。解决后记录到 `lessons-learned.md`，并从本表删除。

| 问题 | 影响 | 解决路径 | 预计时间 | 状态 |
|------|------|---------|---------|------|
| sync-knowledge.py 的 Markdown 解析是启发式的 | 可能漏掉某些格式变体（如嵌套列表、特殊字符）| 引入 `markdown` 库进行精确解析 | 未来（暂无具体时间）| 搁置 |

### 已解决债务
<!-- 解决后从上方表格删除，追加到这里，并记录到 lessons-learned.md -->

---

## 环境备忘

- **语言/框架版本**：Python 3.x + requests
- **编译/构建命令**：`python scripts/sync-knowledge.py`
- **测试命令**：手动单元测试（见 session-log）
- **已知限制**：Windows 环境需使用 `python` 而非 `python3`

---

## 核心规则（不可违反）

见 `AGENTS.md` 完整版。关键几条：
- **RULE-01**：必须先建立基础设施层，再按阶段创建产出层
- **RULE-05**：跨项目知识同步时必须备份、标注来源、按规则去重

---

## 推荐策略

1. 用户配置 `config/github-sync.json` 后，运行脚本测试真实同步效果
2. 同步成功后，本项目即成为跨项目知识母库
3. 后续其他项目初始化时，可选择从母库同步已有经验

---

## 更新记录

| 日期 | 更新内容 |
|------|---------|
| 2026-05-30 | **工具调研 + CodeBuddy 修复**：安装 Reasonix v0.53.2、分析 khazix-skills、对比 Agent 本地记忆系统、修复 CodeBuddy 安装损坏（重装 v2.100.0） |
| 2026-05-30 | **Node.js 环境隔离**：修复 hermes-agent 合并冲突（v0.14.0→v0.15.2）、安装 nvm + Node.js 22、清理 Hermes Node.js 泄漏、重新安装 CodeBuddy 到 nvm 管理的独立环境 |
| 2026-05-30 | **完整性修复**：删除冗余 `build-troubleshooting-index.py` + `troubleshooting-index.md`（被 `experience-index.md` 替代）；`skeleton-manifest.json` 补充 `.gitattributes` + `config/github-sync.json`；`config/github-sync.json` 的 `branch` 设为占位字段（由运行时自动获取）；`templates/` 补齐 `TRIGGERS.md`；`opencode.json` Playwright 配置禁用（天猫已搁置） |
| 2026-05-30 | **状态文档机制重构**：重构 status.md 待办机制（存档时先删除已打勾，再勾选本轮完成）、重构技术债务章节（表格化 + 已解决债务）、新增 RULE-09（技术债务解决后记录到 lessons-learned.md） |
| 2026-05-31 | **分发逻辑重写 + 冗余清理**：`.backup/` 从 15 份精简到 3 份；`TRIGGERS.md` 移到根目录；新建 `scripts/distribute.py`（按条目合并替代覆盖）；更新 AGENTS.md 3.9；向 4 个下游项目分发成功 |

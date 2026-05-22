# Session Log

## 2026-05-22

**用户指令**：恢复 → 确认知识同步状态 → 修复分支问题 → 新增母库分发模式 → 分离 AGENTS 设计 → 存档

**实际执行**：

1. **恢复摘要**：汇报当前阶段（基础设施完善 100%）、母库状态（94 条经验已标签化）、待办清单
2. **确认全 pull**：发现 `vibe-coding-project-sop` 仓库因默认分支为 `master` 而被跳过，仅同步了 2 个仓库
3. **澄清母库定位**：用户确认跨项目母库模式（A 模式），但强调"恢复"指令只应读取本地状态，不应触发网络同步
4. **修复分支自适应**：修改 `scripts/sync-knowledge.py`，优先读取 GitHub API 返回的 `default_branch`，不再硬编码 `main`
5. **新增 syncFrom 配置**：`config/github-sync.json` 新增 `syncFrom` 字段，实现单仓库分发模式。验证通过：聚合模式遍历 3 仓库，分发模式仅拉取母库
6. **分离 AGENTS 设计**：新建 `templates/agents-for-others.md`，将母库专用指令与其他项目专用指令物理分离
7. **文档用词修正**：统一"子项目"→"其他项目"，明确平级目录关系
8. **更新 README.md**：新增"场景 D：其他平级项目使用母库规则更新"章节
9. **存档**：更新 status.md、创建 session-log.md、追加 decisions.md

**关键决策**：
- 同步脚本优先使用 `default_branch` 而非硬编码 `main`
- `syncFrom` 与 `includeRepos` 互斥，实现聚合/分发双模式
- AGENTS.md 与 `templates/agents-for-others.md` 分离，母库/消费端各取所需
- 统一"其他项目"用词，消除物理层级误解

**遗留问题/下轮开始点**：
- 优先级 2 待办：为 `lessons-learned.md` 增加标签/分类系统（实际已完成但待办未勾选）
- 优先级 3 待办：`--dry-run` 和 `--since` 参数尚未实现

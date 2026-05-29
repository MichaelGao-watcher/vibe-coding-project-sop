## 3.7 母库经验指令（「拉取母库」）

> 本章节为**其他项目专用**。由 `pull.py` 自动拉取母库经验。
> 其他项目从母库 `vibe-coding-project-sop` 获取已沉淀的跨项目经验。
> 母库本身不需要此指令，母库使用「聚合」（聚合模式）。

**触发词**：`拉取母库`、`拉取经验`、`更新经验`（去除标点后精确匹配任一）

**防误触**：
- 消息精确匹配上述任一触发词 → 执行母库经验同步流程
- 消息包含触发词但还有其他内容 → 视为正常对话，不触发

**前置条件**：
- 项目根目录存在 `scripts/pull.py`（或 `scripts/sync-knowledge.py`）
- 项目根目录存在 `config/github-sync.json` 且 `syncFrom` 已填写母库仓库名（如 `vibe-coding-project-sop`）

**确认流程**：
1. 读取 `config/github-sync.json` 中的 `syncFrom` 字段
2. 输出将要同步的母库仓库名和当前项目路径
3. 等待用户二次确认

**标准动作序列**：
1. 检查 `scripts/pull.py` 是否存在
   - 如存在 → 运行 `python pull.py`
   - 如不存在 → 下载 `https://raw.githubusercontent.com/MichaelGao1999/vibe-coding-project-sop/master/scripts/pull.py`，然后运行
2. 读取脚本输出，汇报同步结果：
   - 母库仓库名
   - 拉取到的文件数
   - 新增条目数 / 全部已存在
5. 解析脚本输出，汇报同步结果：
   - 母库仓库名
   - 拉取到的文件数
   - 新增条目数 / 全部已存在
6. 如有新增内容，提示用户查看 `decisions.md`、`lessons-learned.md`、`troubleshooting.md`
7. 如脚本报错，按 troubleshooting.md 格式记录问题

**与母库「聚合」的区别**：
- 母库「聚合」是**聚合模式**：把多个仓库的经验汇总到当前项目（用于维护母库）
- 本指令是**分发模式**：从指定母库获取经验到当前项目（用于消费经验）
- 两者触发词不同，使用场景不同，不可混淆

**反哺母库**：
如其他项目在开发过程中产生了新的可复用经验，可手动提交到母库仓库，供所有项目共享。

---

## 附录：推荐技能与工具

> 以下资源非母库产出，但经评估对特定类型的消费端项目有显著价值，按需参考。

### 前端设计：Anthropic frontend-design skill

**适用场景**：项目有浏览器前端、Tauri 桌面应用、React/Vue 组件等 UI 开发需求。

**核心价值**：
- 避免 AI 生成前端的"千篇一律"（generic AI slop）
- 强制选择 BOLD 美学方向（极简/极繁/复古未来/有机自然等），然后精确执行
- 具体约束：禁用 Inter/Arial/系统字体、禁用紫色渐变白色背景、禁用可预测布局

**获取方式**：
- GitHub：`https://github.com/adryanmoldokkr32-pixel/anthropics-skills/tree/main/skills/frontend-design`
- 或作为 Claude Code skill 安装

**使用建议**：在阶段五（开发实现）中，如子任务涉及前端 UI 开发，可在 subAgent 的接力指令中引用此 skill，确保输出界面具有独特设计感而非模板化痕迹。

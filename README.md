# AI 项目文档骨架

> 🎯 **AI 开发助手**：请直接阅读 [`AGENTS.md`](./AGENTS.md)，本文件（README）是人类使用说明。

> 专为 AI 辅助开发设计的项目文档体系。每次会话接力时，5 分钟内搞清楚"规则、状态、历史、决策、问题"。

---

## 快速开始

### ⚠️ 核心原则：先建基础设施，再按阶段推进

本骨架分为两层：
- **基础设施层**（项目启动时立刻建立）：通用机制文件，从第一天起就需要
- **阶段产出层**（按 SOP 五阶段逐步创建）：各阶段的交付物，根据项目状态选择切入点

---

### 第一步：初始化项目基础设施（所有项目都需要）

以下 7 个文件是项目的**通用基础设施**，无论新项目、已有项目还是半成品，都应该在项目启动时立刻建立。

#### 推荐：一键初始化脚本

```bash
# 进入新项目根目录，运行初始化脚本
cd /path/to/your-project
python /path/to/vibe-coding-project-sop/scripts/init-skeleton.py \
    --skeleton /path/to/vibe-coding-project-sop \
    --with-knowledge
```

脚本会自动：
- 从 `templates/` 复制 6 个基础设施模板（status.md、session-log.md 等）
- 从骨架根目录复制 `AGENTS.md` 模板（需后续按项目填空）
- 复制母库经验（94 条 lessons-learned / troubleshooting / decisions）
- 检测冲突文件，避免覆盖已有内容
- 输出初始化报告，提示下一步操作

**常用快捷方式**（设置环境变量后不用每次写路径）：

```bash
# Linux/macOS
export SOP_SKELETON_PATH=/path/to/vibe-coding-project-sop
python $SOP_SKELETON_PATH/scripts/init-skeleton.py --with-knowledge

# Windows
set SOP_SKELETON_PATH=D:\Vibe-Code\vibe-coding-project-sop
python %SOP_SKELETON_PATH%\scripts\init-skeleton.py --with-knowledge
```

#### 备选：手动复制

如果无法运行脚本，可手动从 `templates/` 和骨架根目录复制：

| 文件 | 来源 | 说明 |
|------|------|------|
| `AGENTS.md` | 骨架根目录 | 按项目填空 |
| `vibe-coding-sop.md` | `templates/` | 原样复制，不修改 |
| `status.md` | `templates/` | 后续填充 |
| `session-log.md` | `templates/` | 后续追加 |
| `decisions.md` | `templates/` | 后续追加 ADR |
| `troubleshooting.md` | `templates/` | 后续追加问题 |
| `lessons-learned.md` | `templates/` | 后续追加经验 |

---

**场景 B：已有项目（已有 AGENTS.md）**
- **不要替换**现有的 `AGENTS.md`
- 把骨架 `AGENTS.md` 中的「2. 必读上下文」和「0. 骨架消费协议」章节**插入**到现有文件中
- 建议插入位置：「项目定位」之后、「硬规则」之前
- 运行初始化脚本（它会检测已有文件并跳过，只补充缺失的）

> ⚠️ **不要与 `prompt-next-session.md` 混用**。如果项目已有 `prompt-next-session.md`，建议迁移到本骨架体系后删除旧文件（或改名为 `.bak` 归档），避免双文件冗余。

**场景 C：半成品项目（已有代码）**
- 保留现有代码，运行初始化脚本补充缺失的基础设施文件
- 从 `vibe-coding-sop.md` **阶段五**开始：先让 AI 评估现有代码，再决定是继续开发还是回溯补文档
- 如需回溯：根据代码反推 → 补 `docs/design.md` → 补 `docs/tasks/*.md` → 继续阶段五

**场景 D：其他平级项目使用母库规则更新**

> 母库（`vibe-coding-project-sop`）与其他项目是**平级目录关系**，非物理父子。其他项目按需获取母库的最新规则和经验。

**获取母库经验文件（自动）**：

配置 `config/github-sync.json` 的 `syncFrom` 字段指向母库，运行 `python scripts/sync-knowledge.py` 即可自动拉取母库的 `decisions.md`、`lessons-learned.md`、`troubleshooting.md`。

```bash
# 1. 复制同步脚本和配置
 cp ../vibe-coding-project-sop/scripts/sync-knowledge.py ./scripts/
 cp ../vibe-coding-project-sop/config/github-sync.json ./config/

# 2. 修改配置：只从母库拉取
# config/github-sync.json → "syncFrom": "vibe-coding-project-sop"

# 3. 运行同步
python scripts/sync-knowledge.py
```

**获取母库 AGENTS.md 规则（手动）**：

`AGENTS.md` 包含项目特定内容（项目定位、模块速查表等），**不适合自动同步**。其他项目应手动参考母库 AGENTS.md，按需插入通用规则章节：

| 通用规则章节 | 来源 | 适用场景 |
|-------------|------|---------|
| 3.5 存档指令 | 母库 `AGENTS.md` | 所有项目 |
| 3.6 恢复指令 | 母库 `AGENTS.md` | 所有项目 |
| 3.7 母库经验指令 | 母库 `templates/agents-for-others.md` | 需要从母库消费经验的项目 |

```bash
# 从 GitHub 拉取母库通用规则，手动插入自己项目的 AGENTS.md
curl https://raw.githubusercontent.com/MichaelGao1999/vibe-coding-project-sop/master/AGENTS.md
curl https://raw.githubusercontent.com/MichaelGao1999/vibe-coding-project-sop/master/templates/agents-for-others.md
```

---

### （可选）从母库获取经验

骨架根目录的 `lessons-learned.md` 是**跨项目知识母库**（当前已聚合 94 条经验），新项目初始化时建议一并继承。

**初始化时直接继承（推荐）**

```bash
python /path/to/vibe-coding-project-sop/scripts/init-skeleton.py \
    --skeleton /path/to/vibe-coding-project-sop \
    --with-knowledge
```

`--with-knowledge` 会把母库的 `lessons-learned.md`、`troubleshooting.md`、`decisions.md` 作为初始种子复制过去，新项目自己的经验后续追加到「技术经验」表格即可。

**后续增量同步（母库更新后）**

若母库后续新增了经验，新项目可以用 `sync-knowledge.py` 拉取增量：

```bash
# 1. 复制脚本和配置
mkdir -p scripts config
cp /path/to/vibe-coding-project-sop/scripts/sync-knowledge.py scripts/
cp /path/to/vibe-coding-project-sop/config/github-sync.json config/

# 2. 修改 config/github-sync.json，只包含母库仓库
#    "includeRepos": ["vibe-coding-project-sop"]

# 3. 运行同步
python scripts/sync-knowledge.py
```

> **分工**：`init-skeleton.py` 负责**首次一键初始化**（基础设施 + 可选母库种子）；`sync-knowledge.py` 负责**后续增量同步**（保持与母库更新同步）。

---

### 第二步：判断项目状态，选择 SOP 切入阶段

基础设施建好后，根据项目当前状态进入 `vibe-coding-sop.md` 的对应阶段：

| 项目状态 | 切入阶段 | 本阶段需要创建的产出文件 |
|---------|---------|------------------------|
| **纯新项目**（只有想法，无代码无文档） | 阶段一 | `docs/proposal.md` |
| **有需求文档**（已有 PRD/需求说明） | 阶段二 | `docs/design.md`、`docs/brief.md` |
| **有设计文档**（已有架构/接口设计） | 阶段三 | `docs/tasks/task-{module}.md`、`docs/tasks/task-progress.md` |
| **有 Prompt**（已有 orchestrator 指令） | 阶段五 | 直接执行开发，产出代码 |
| **半成品项目**（已有代码，文档不全） | 阶段五 | 先评估代码，再决定回溯还是继续 |

> 详细阶段定义见 `vibe-coding-sop.md`「项目起点判断」

---

### 第三步：按 SOP 阶段推进

**各阶段产出文件清单：**

| 阶段 | 产出文件 | 说明 |
|------|---------|------|
| 阶段一 | `docs/proposal.md` | AI 与用户讨论后生成 |
| 阶段二 | `docs/design.md`、`docs/brief.md` | 基于 `proposal.md` 生成 |
| 阶段三 | `docs/tasks/*.md`、`docs/tasks/task-progress.md` | 基于设计文档拆分 |
| 阶段四 | `prompt.md` | 基于前文所有文档生成 |
| 阶段五 | `src/`、`tests/` | 按批次逐个实现模块 |

**执行规则：**
- **每阶段结束后结束当前会话**，不要主动推进到下一阶段
- **下阶段由用户开启新会话触发**，新会话的 Agent 先按 `AGENTS.md`「必读上下文」顺序读取，再开工
- 阶段边界不可跨越，这是防止「一把梭」的核心防线

---

## 骨架文件说明

| 文件 | 职责 | 更新时机 | 回答什么问题 |
|------|------|----------|-------------|
| `AGENTS.md` | 硬规则 + 模块速查 + **极简文档索引** | 规则变更时 | "规则是什么？先读什么？" |
| `status.md` | 现在在哪、下一步去哪 | **用户说「存储」时** | "现在在哪？" |
| `session-log.md` | 怎么走到这里的 | **用户说「存储」时追加** | "Context 丢失后怎么恢复？" |
| `decisions.md` | 为什么这样设计 | **用户说「存储」时评估追加**（如本轮有关键决策） | "为什么选 A 而不是 B？" |
| `troubleshooting.md` | 遇到问题怎么救 | **用户说「存储」时评估追加**（如本轮有报错） | "这个报错怎么修？" |
| `lessons-learned.md` | 什么可以跨项目复用 | **用户说「存储」时评估追加**（如本轮有可复用经验） | "下个项目怎么避免？" |
| `vibe-coding-sop.md` | 五阶段 Vibe Coding 工作流 | 新项目启动时 | "完整开发流程是什么？" |

---

## 文档体系详细说明

### 为什么需要 6 个文件？

| 问题 | 文件 | 原因 |
|------|------|------|
| "现在该做什么？" | `status.md` | 只看状态和待办 |
| "前几轮做了什么？" | `session-log.md` | context 会丢失，需要外部记忆 |
| "为什么这样设计？" | `decisions.md` | 防止重复争论同一决策 |
| "这个报错怎么修？" | `troubleshooting.md` | 按错误关键词秒查 |
| "什么可以复用？" | `lessons-learned.md` | 跨项目知识沉淀 |
| "规则是什么？" | `AGENTS.md` | 总入口，必读 |

### AGENTS.md 为什么必须精简？

AGENTS.md 是**每次会话必读的入口**。如果它本身太冗长，就会：
- 占用大量 context，挤压代码空间
- 失去"速查"意义

**因此**：
- AGENTS.md 只保留**项目定位 + 极简索引 + 硬规则 + 模块速查**
- 详细的"文档体系说明"放在 **本 README.md** 中，供查阅而非每次必读
- 详细的"session-log 原理"放在 **session-log.md** 自身中

### session-log 与 status 的区别

| | **Status** | **Session Log** |
|---|---|---|
| **内容** | 当前状态、待办清单 | 每次会话的决策过程、阻碍、解决路径 |
| **更新频率** | 任务完成时更新 | **每次会话结束后追加** |
| **作用** | 知道"现在在哪" | 知道"怎么走到这里的" |
| **读者** | 接力的下一个自己 | **Context 丢失后的自己** |
| **类比** | Jira 看板 | Git 提交日志 |

### 何时记录 session-log

**会话结束时记**（不是开始时）。

原因：开始时不确定本轮能完成什么。只有结束后回顾，才能准确记录实际发生了什么。

时机：代码提交/测试通过 → 用户说「存储」→ AI 执行存档流程 → 更新 `status.md` → **追加 `session-log.md`** → Git 提交推送。

---

## 与 `prompt-next-session.md` 的区别

| | `prompt-next-session.md` | 本文档骨架 |
|---|---|---|
| 维护成本 | 高（每次重写环境、模块表等不变内容） | 低（只更新变化的部分） |
| Context 恢复 | 弱（只有状态快照） | 强（session-log 记录过程） |
| 决策追溯 | 无 | 有（decisions.md） |
| 错误索引 | 无 | 有（troubleshooting.md） |
| 推荐场景 | 单轮任务、快速原型 | 多轮接力、长期项目 |

---

*骨架版本：v1.2.0 | 来源：French Exit 项目实践总结*

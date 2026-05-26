# vibe-coding-project-sop — Agent 启动指令

> 本文件供 AI 开发助手读取。接手本项目时，**必须先读完下面列出的上下文文件**，再开始任何代码操作。
> 其他项目如需从母库获取经验，请参考 `templates/agents-for-others.md`，按需插入自己的 `AGENTS.md`。

---

## 0. ⚠️ 骨架消费协议（硬规则）

**本骨架不是静态模板，禁止无脑全盘复制。**

> **目录结构**：根目录只保留规则文件（`AGENTS.md`、`README.md`、`skeleton-manifest.json`）。所有模板文件在 `templates/` 子目录下，消费时按需复制，禁止直接复制整个目录。

### 基础设施层（项目启动时立刻建立）

以下文件是项目的**通用机制**，从第一天起就需要存在（模板位于骨架 `templates/` 目录下）：

| 文件 | 职责 |
|------|------|
| `AGENTS.md` | 项目硬规则 + 模块速查 |
| `vibe-coding-sop.md` | 五阶段工作流参考（从 `templates/` 复制，不修改） |
| `status.md` | 当前进度、待办清单 |
| `session-log.md` | 会话历史记录 |
| `decisions.md` | 关键决策记录 |
| `troubleshooting.md` | 问题索引 |
| `lessons-learned.md` | 跨项目经验沉淀 |
| `.gitattributes` | 统一换行符(LF) + 标记二进制文件 |
| `config/github-sync.json` | 跨项目知识同步配置（可选，按需建立） |

### 阶段产出层（按 SOP 五阶段逐步创建）

| 阶段 | 产出文件 |
|------|---------|
| 阶段一 | `docs/proposal.md` |
| 阶段二 | `docs/design.md`、`docs/brief.md` |
| 阶段三 | `docs/tasks/task-{module}.md`、`docs/tasks/task-progress.md` |
| 阶段四 | `prompt.md` |
| 阶段五 | `src/`、`tests/`、各模块源码 |

### 消费步骤

1. **建立基础设施层**：运行 `scripts/init-skeleton.py` 一键初始化（或从 `templates/` 手动复制 8 个文件到项目根目录）
2. **读取 `vibe-coding-sop.md`** → 查看「项目起点判断」，确定切入阶段
3. **按阶段边界逐步推进**：每阶段完成后结束，等待用户开启新会话进入下一阶段

---

## 1. 项目定位

vibe-coding-project-sop 是 AI 辅助开发的骨架母库，沉淀跨项目可复用的规则、模板、脚本和经验。

- **形态**：文档 + 脚本工具
- **技术栈**：Python 3.x + Markdown
- **目标用户**：使用 AI 开发助手进行软件工程的个人开发者或团队

> 环境详情（版本号、构建/测试命令）见 `status.md`「环境备忘」。

---

## 2. 必读上下文（按顺序，5 分钟）

1. `AGENTS.md` — 本文件（硬规则）
2. `status.md` — 当前进度、待办清单、环境备忘（版本/构建/测试命令）
3. `session-log.md` — 前几轮怎么走到这里的
4. `docs/design.md` — 概要设计（如需改架构或接口）
5. `troubleshooting.md`（条件性）— 如用户当前遇到具体报错，先读取 `troubleshooting-index.md` 快速定位，再读取 `troubleshooting.md` 详细内容
6. `config/github-sync.json`（条件性）— 如项目已配置跨项目知识同步，读取配置了解同步范围

> **新项目启动时额外阅读**：`vibe-coding-sop.md` — 五阶段 Vibe Coding 工作流 SOP（需求→设计→任务→Prompt→开发）。

**禁止**：在未阅读 `status.md` 前直接写代码。

> 详细文档体系说明见 `README.md`（各文件职责边界、接力流程）。

---

## 3. 核心约束（硬规则，不可违反）

| 规则 ID | 规则内容 | 违反后果 |
|---------|---------|---------|
| **RULE-01** | **必须先建立基础设施层，再按阶段创建产出层；禁止在未建基础设施前直接生成阶段产出** | 过程无记录、状态不可追踪；需求/设计/开发缺乏决策依据，产出偏离用户预期 |
| **RULE-02** | **阶段边界 = 会话边界，每阶段完成后结束，不主动推进下一阶段** | 超长会话导致上下文丢失、任务堆积、接力困难 |
| **RULE-03** | **可选产出（如 database.md、deploy.md）的创建必须由阶段一的技术需求确认（T-01~T-04）驱动；触发条件满足时必须产出，不满足时不得产出** | 文档体系与项目实际需求不匹配：要么过度设计（纯前端项目出了数据库文档），要么遗漏关键设计（后端项目没出数据库文档） |
| **ARCHIVE-01** | **用户说「存档」时，执行标准存档流程，不要提前结束会话** | 文档与 Git 状态不一致，接力丢失上下文 |
| **ARCHIVE-02** | **「存档」触发后必须先输出确认清单，等待用户二次确认** | 误触导致非预期提交 |
| **RULE-04** | **严禁在 C 盘（系统盘）创建、修改或删除任何文件。只允许读取 C 盘上已存在的配置和工具。所有项目测试与产出必须限定在当前工作区内。** | 系统文件被污染、项目文件散落在非预期位置、回滚/清理困难 |
| **RULE-05** | **跨项目知识同步时，必须先备份母库文件，合并后必须标注来源 `[来源:仓库名 @日期]`；lessons-learned 按描述去重、troubleshooting 按关键词去重、decisions 保留全部。** | 母库内容来源不清、重复堆积、失去可追溯性 |
| **RULE-06** | **`status.md` 中已完成的待办项应在存档时删除；历史完成记录由「更新记录」章节承担，待办清单只保留未完成项。** | 待办清单膨胀、恢复时噪音过大、重点模糊 |
| **RULE-07** | **troubleshooting 条目只需写入 `troubleshooting.md`；`troubleshooting-index.md` 由 `scripts/build-troubleshooting-index.py` 自动生成，禁止手动编辑索引文件。** | 索引与源文件不同步、维护负担翻倍 |

---

## 3.5 存档指令（「存档」）

**触发词**：`存档`（去除标点后精确等于这两个字）

**防误触**：
- 消息精确匹配「存档」→ 进入存档确认流程
- 消息包含「存档」但还有其他内容 → 视为正常对话，不触发

**确认流程**：输出存档确认清单（列明将更新的文档和 Git 操作），等待用户二次确认。

**标准动作序列**（用户确认后执行）：
1. 回顾本轮内容，生成 session-log 草稿
2. 更新 `status.md`（删除已完成的待办项，保留并排序未完成项，新增下轮待办；历史完成记录写入「更新记录」）
3. 有具体报错 → 追加 `troubleshooting.md` → 运行 `python3 scripts/build-troubleshooting-index.py` 重建索引
4. 有可复用经验 → 追加 `lessons-learned.md`
5. 有关键决策 → 追加 `decisions.md`
6. 定稿并追加 `session-log.md`
7. Git 全量提交：`git add -A` → `git commit -m "[session] 摘要"` → `git push`
8. 汇报完成

**Git 错误处理**：无 `.git` 目录 → 跳过 Git；无变更 → 跳过 commit；push 失败 → 报错暂停。

---

## 3.6 恢复指令（「恢复」）

**触发词**：`恢复`（去除标点后精确等于这两个字）

**防误触**：
- 消息精确匹配「恢复」→ 执行恢复流程
- 消息包含「恢复」但还有其他内容 → 视为正常对话，不触发

**核心原则**：
> **恢复摘要以 `status.md` 为主，`session-log.md` 为辅。**
> `status.md` 回答"现在在哪、下一步去哪"。`session-log.md` 只用于验证一致性。
> **不要复述上轮历史。**

**标准动作序列**：
1. **Git 同步**：如项目有 `.git` 目录，先执行 `git pull` 拉取最新状态；如有冲突则暂停并报错，等待用户解决
2. 读取 `status.md`（主数据源）：阶段、进度、待办、阻塞项
3. 读取 `session-log.md` 最后一条（辅数据源）：只取「遗留问题/下轮开始点」一句话
4. 搜索 troubleshooting（条件性）：如用户遇到报错，先读取 `troubleshooting-index.md` 快速定位相关条目，再读取 `troubleshooting.md` 详细内容。索引由 `scripts/build-troubleshooting-index.py` 自动生成，含按技术栈分组视图。
5. 判断内容有效性：关键字段是否为占位符？session-log 是否无实际记录？
6. 综合分析：结合 status.md 优先级、session-log 遗留问题、troubleshooting.md 匹配结果，给出建议
7. 汇报恢复摘要
8. 等待用户下一步指令

---

## 3.7 知识同步指令（「同步知识」）

> **本指令仅母库需要。** 其他项目使用「母库经验」指令，见 `templates/agents-for-others.md`。

**触发词**：`同步知识`、`拉取经验`、`聚合知识`（去除标点后精确匹配任一）

**防误触**：
- 消息精确匹配上述任一触发词 → 进入知识同步确认流程
- 消息包含触发词但还有其他内容 → 视为正常对话，不触发

**前置条件**：
- 项目根目录存在 `config/github-sync.json` 且已填写 `username`
- 如缺少配置，提示用户先填写配置，再执行同步

**确认流程**：
1. 读取 `config/github-sync.json`，输出将要同步的仓库范围（用户名、包含/排除列表）
2. 等待用户二次确认

**标准动作序列**（用户确认后执行）：
1. 备份本项目的 `decisions.md`、`lessons-learned.md`、`troubleshooting.md` 到 `.backup/`
2. 遍历 GitHub 用户/组织的仓库（使用 API 或 raw 拉取）
3. 对每个仓库拉取三个目标文件
4. 按合并策略解析、去重、标注来源
5. 合并到本项目的对应母库文件中
6. 输出同步报告（仓库数、文件数、新增条目数）
7. 更新 `status.md` 记录本次同步摘要
8. 如用户要求，执行 Git 提交

**合并策略**（不可违反）：
- `lessons-learned.md`：按「经验描述」去重，相同技术点合并来源标签
- `troubleshooting.md`：按「错误关键词」去重，保留解决方案最全的一条，或并列保留不同场景的解决方案
- `decisions.md`：不去重，全部追加（不同项目的 ADR 即使标题相同，上下文也可能不同）
- 所有并入内容必须标注 `[来源:仓库名 @YYYY-MM-DD]`

**Git 错误处理**：无 `.git` 目录 → 跳过 Git；无变更 → 跳过 commit；push 失败 → 报错暂停。

---

## 4. 模块速查表

| ID | 模块名 | 职责 | 技术要点 |
|----|--------|------|---------|
| M01 | init-skeleton | 一键初始化脚本，复制基础设施 + 可选母库经验 | `python scripts/init-skeleton.py --skeleton <path> --with-knowledge` |
| M02 | sync-knowledge | 跨项目知识同步脚本，聚合其他仓库经验到母库 | `python scripts/sync-knowledge.py` |
| M03 | build-troubleshooting-index | 自动生成 troubleshooting 搜索索引 | `python3 scripts/build-troubleshooting-index.py` |

---

## 5. 环境备忘索引

> 编译命令、PATH、已知限制见 `status.md` → 环境备忘

---

## 6. 更新记录

| 日期 | 更新内容 |
|------|---------|
| 2026-05-21 | 新增 RULE-05 跨项目知识同步规则、3.7 知识同步指令、config/github-sync.json 基础设施 |
| 2026-05-21 | 新增 `scripts/init-skeleton.py` 一键初始化脚本，支持 `--with-knowledge` 复制母库经验 |
| 2026-05-22 | 修复恢复指令增加 `git pull` 步骤；AGENTS 分离设计（`templates/agents-for-others.md`）；文档用词修正（"子项目"→"其他项目"） |
| 2026-05-22 | 同步脚本分支自适应（优先读取 `default_branch`）；新增 `syncFrom` 母库分发模式 |
| 2026-05-23 | GitHub push 通路修复（SSH → HTTPS + GitHub CLI） |
| 2026-05-24 | **新增 RULE-06**（status.md 已完成待办删除规则）、**RULE-07**（troubleshooting 索引自动生成规则）；3.5 存档指令更新（删除已完成待办、重建索引步骤）；3.6 恢复指令更新（troubleshooting-index.md 快速定位） |
| 2026-05-24 | AGENTS.md 精简：删除占位符、章节重排（3.5→3.6→3.7）、补充更新记录 |
| 2026-05-24 | **vibe-coding-sop.md 吸收 Karpathy 编码规范**：在「阶段五：开发实现」中新增「编码行为规范」子章节（先想后写 / 极简优先 / 手术刀式修改 / 目标驱动），作为阶段五的硬约束写入 prompt.md |
| 2026-05-26 | 新增 `.gitattributes` 模板分发，`init-skeleton.py` 自动复制到新项目 |

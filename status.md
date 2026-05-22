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

### 优先级 1 — 阻塞项
- [x] 在真实 GitHub 仓库上测试 `scripts/sync-knowledge.py` ✅
- [x] 确认用户的 GitHub 用户名并填入 `config/github-sync.json` ✅

### 优先级 2 — 功能
- [ ] 考虑为 `lessons-learned.md` 增加标签/分类系统，便于跨项目检索
- [ ] 为 troubleshooting 增加搜索索引（按关键词快速定位）

### 优先级 3 — 优化
- [ ] 脚本增加 `--dry-run` 模式，预览变更但不写入
- [ ] 脚本增加 `--since` 参数，只同步某日期后的新增内容

---

## 技术债务 🏚️

### 临时 workaround
- 无

### 待重构模块
- 无

### 已知缺陷（暂不修复）
- `scripts/sync-knowledge.py` 的 Markdown 解析是启发式的，可能无法完美处理所有格式变体。暂时够用，未来如需更精确的解析可考虑引入 `markdown` 库。

---

## 环境备忘

- **语言/框架版本**：Python 3.x + requests
- **编译/构建命令**：`python scripts/sync-knowledge.py`
- **测试命令**：手动单元测试（见 session-log）
- **已知限制**：Windows 环境需使用 `python` 而非 `python3`

---

## 关键代码入口

```
vibe-coding-project-sop/
├── config/
│   └── github-sync.json      # 跨项目同步配置
├── scripts/
│   └── sync-knowledge.py     # 自动化同步脚本
├── templates/
│   ├── decisions.md          # 决策模板（含跨项目来源格式）
│   ├── lessons-learned.md    # 经验模板（含跨项目来源格式）
│   ├── troubleshooting.md    # 问题模板（含跨项目来源格式）
│   └── vibe-coding-sop.md    # 五阶段 SOP（含附录 B 知识同步）
├── AGENTS.md                 # 硬规则（含 RULE-05、3.7 知识同步指令）
├── skeleton-manifest.json    # 骨架元数据（含 knowledgeSync 段）
└── status.md                 # 本文件
```

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
| 2026-05-21 | 新增跨项目知识同步 SOP：config/github-sync.json、scripts/sync-knowledge.py、AGENTS.md RULE-05、vibe-coding-sop.md 附录 B、模板跨项目来源格式、skeleton-manifest.json knowledgeSync 段 |
| 2026-05-21 | **首次知识同步成功**：从 MichaelGao1999 的 blindfold-chess、french-exit 仓库拉取知识，合并为母库。decisions.md 304行、lessons-learned.md 94条经验、troubleshooting.md 238行。发现并修复了 lessons-learned 模板内容混入问题，脚本增加 `_is_valid_lesson` 过滤逻辑。 |
| 2026-05-21 | **lessons-learned 标签化完成**：94 条经验全部打标签（CRITICAL 8 条 / WARNING 33 条 / INFO 53 条），新增 `templates/anti-patterns-checklist.md` 作为阶段二设计自检模板。母库表格增加「标签」「严重度」两列。 |
| 2026-05-22 | **同步脚本分支自适应**：修复 `vibe-coding-project-sop` 因默认分支为 `master` 而被 404 跳过的问题。脚本优先读取 GitHub API 返回的 `default_branch`，不再硬编码 `main`。 |
| 2026-05-22 | **新增 syncFrom 母库分发模式**：`config/github-sync.json` 新增 `syncFrom` 字段，配置后脚本只从指定单一仓库拉取（分发模式），与原有聚合模式（遍历所有仓库）共存。验证通过：聚合模式遍历 3 个仓库，分发模式只拉取母库。 |
| 2026-05-22 | **AGENTS 分离设计**：新建 `templates/agents-for-others.md`，将母库专用指令（3.7 同步知识）与其他项目专用指令（3.7 母库经验）物理分离。母库 AGENTS.md 保留聚合指令，其他项目按需插入分发指令。 |
| 2026-05-22 | **文档用词修正**：统一将"子项目"改为"其他项目"，明确母库与其他项目为平级目录关系，消除物理层级误解。更新 `AGENTS.md`、`templates/agents-for-others.md`、`README.md`。 |

---

## 存档提示

**用户说「存储」时**，AI 应回顾本轮会话内容，更新本文件的以下章节：
- **当前阶段**：如有进展，更新百分比和下一步
- **进度总览**：更新各模块状态图标
- **待办**：勾选已完成项，新增下轮待办
- **更新记录**：追加本轮更新摘要

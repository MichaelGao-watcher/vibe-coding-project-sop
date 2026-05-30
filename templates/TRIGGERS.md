# 快捷指令

> 每次会话开始时复制本文件给 AI，确保触发词生效。

| 触发词（精确匹配） | AI 动作 |
|-------------------|---------|
| `拉取母库` / `拉取经验` / `更新经验` | 运行 `python scripts/pull.py` |
| `聚合` | 聚合其他仓库经验到母库（仅母库使用） |
| `存档` | 执行标准存档流程（更新 status.md、session-log.md、Git 提交） |
| `恢复` | 读取 status.md 和 session-log.md，汇报当前状态 |

---

### 使用示例

**用户**：拉取母库

**AI**：
1. 检查 `scripts/pull.py` 是否存在
2. 运行 `python scripts/pull.py`
3. 读取输出并汇报结果

---

**用户**：聚合

**AI**：
1. 读取 `config/github-sync.json`
2. 确认仓库范围
3. 运行 `python scripts/sync-knowledge.py`

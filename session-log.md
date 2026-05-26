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


## 2026-05-22 第二轮

**用户指令**：French Exit 提交验证 → qianniu_business_analytics 项目评估与改造 → 存档

**实际执行**：

1. **French Exit 状态验证**：提交并 push（63ecbef），确认母库同步 0 新增 = 内容已是最新
2. **qianniu_business_analytics 项目评估**：
   - 输出完整评估报告：阶段五 85% / 6 个 Python 脚本 1466 行 / 无 Git 仓库 / 无 proposal.md
   - 执行方案 A 最小修复：git init + requirements.txt + 母库拉取机制 + 存档触发词修正
3. **品牌名全面清理**：
   - agentone → qianniu（8 文件，11 处）
   - 瓴羊·One / 瓴羊 → 平台（17 处）
   - lydaas / jycm.lydaas.com → api.example.com（9 处）
   - AgentOne → 自包含技能包 / 开发生态（4 处）
4. **GitHub 上传**：使用 gh CLI 创建仓库并推送，共 7 个 commit
5. **SOP 骨架补全**：
   - 添加 AGENTS.md 3.7 母库经验指令
   - 同步母库经验：lessons-learned.md 新增 31 条
   - 生成 docs/proposal.md（阶段一需求提案，122 行）
6. **母库本地修复**：config/github-sync.json 补逗号

**关键决策**：
- 未上传 GitHub 的项目按「方案 A：最小修复」处理，不推翻重建
- 品牌名清理采用「先全局替换 → 再修复格式」的两步法
- 新项目接入母库的标准流程：pull.py + sync-knowledge.py + config/github-sync.json + AGENTS 3.7

**遗留问题 / 下轮开始点**：
- qianniu_business_analytics 的 docs/design.md / docs/brief.md / prompt.md 待补全
- 母库 P2/P3 待办（搜索索引、--dry-run、--since）尚未启动

---

## 2026-05-22

**会话类型**：基础设施完善 + 跨项目知识同步机制部署

**完成内容**：
1. 恢复指令修复：AGENTS.md 3.6 增加 `git pull` 步骤（用户指出后修复）
2. Superpowers B 方案安装：
   - 克隆 obra/superpowers 到 ~/.kimi/superpowers/
   - 创建 14 个 skills 符号链接到 ~/.kimi/skills/
   - Patch using-superpowers/SKILL.md 适配 Kimi Code CLI（ReadFile 调用方式）
   - 向用户解释调用方式、对工作流的影响、回滚方法
3. 用户决定暂不启用 Superpowers，待明天试用
4. 评估 frontend-design skill：当前项目无前端 UI，用不上，但"避免 generic output"理念可借鉴
5. 将"拉取母库"全套逻辑写入 blindfold-chess 项目：
   - 新增 config/github-sync.json、scripts/sync-knowledge.py
   - AGENTS.md 新增 RULE-07、存档确认流程、恢复 git pull、同步知识触发词
   - lessons-learned.md / troubleshooting.md 增加来源标注格式
   - 首次同步因 GitHub API rate limit 未执行（需配置 token）

**评估结论**：blindfold-chess 文档骨架完整，缺失的跨项目知识同步机制已全部补齐。

**遗留问题/下轮开始点**：
- 用户明天计划试用 Superpowers skills（已写入 status.md 待办）
- blindfold-chess 需配置 GitHub token 后运行首次母库同步

---

## 2026-05-22

**会话类型**：LLM 服务部署 + 环境诊断

**完成内容**：
1. 诊断老设备硬件（i7-7500U/8GB/无独显），评估本地部署可行性
2. 原计划用 Ollama，因 GitHub 完全超时、2GB 安装包不可下载而放弃
3. 改用 llama.cpp 方案：18MB 二进制通过 gh.llkk.cc 加速镜像下载（2MB/s）
4. Qwen2.5-0.5B 模型通过 ModelScope CDN 下载（2.95MB/s，469MB/48秒）
5. 成功启动 llama-server，加载模型，监听 0.0.0.0:11434
6. 中英文推理测试通过，速度约 20 tokens/s（纯 CPU）
7. 环境变量配置（OLLAMA_HOST=0.0.0.0，OLLAMA_NUM_THREAD=4）
8. 发现 PowerShell 5.1 UTF-8 无 BOM 解析陷阱，修复 start-llm-server.ps1 编码
9. 创建 llm-server/ 目录，整理所有脚本和文档
10. 删除 Ollama 安装包半成品（73MB）

**评估结论**：老设备已成功部署为局域网 LLM 服务器，llama.cpp 方案在 8GB 内存限制下运行良好。

**遗留问题/下轮开始点**：
- 防火墙规则需首次以管理员身份运行 start-llm-server.ps1 添加
- 老设备 IP 变动时需更新 macbook-connect.md


---

## 2026-05-23

**会话类型**：macOS 新设备接入 + Hermes Agent 配置 + DeepSeek 模型升级

**完成内容**：
1. macOS 端恢复流程：读取 `status.md` 和 `session-log.md`，汇报当前状态
2. 确认用户意图：只想了解老设备 LLM 连接问题，场景一/二/三已解决
3. Hermes Agent 安装与配置（pipx 方案）：
   - 通过 `uv tool install pipx` 安装 pipx（无 Homebrew）
   - `pipx install hermes-agent` → v0.14.0
   - 配置 custom provider 指向老设备 `192.168.18.122:11434`
4. 两个必要 patch（解决 llama.cpp 兼容性）：
   - `agent/model_metadata.py`: `MINIMUM_CONTEXT_LENGTH` 64K → 32K（0.5B 模型只有 32K 上下文）
   - `agent/transports/chat_completions.py`: 强制移除 `tools` + 强制 `stream=False`（llama.cpp 不支持 streaming+tools）
5. Hermes 成功调用老设备 LLM，返回中文回复（非 stream 模式，1 分 41 秒）
6. 将 `~/.local/bin` 加入 `~/.bashrc` PATH，确保新开终端可直接运行 `hermes`
7. 更新 `llm-server/` 文件准备切换 DeepSeek 模型：
   - `start-llm-server.ps1`：模型路径改为 `deepseek-r1-distill-qwen-1.5b.Q4_K_M.gguf`
   - `macbook-connect.md`：模型名称和工具配置更新
   - `README.md`：服务信息更新
8. macOS 端 Hermes `config.yaml` 模型名更新为 DeepSeek
9. `status.md` 新增「老设备接力」待办清单，含完整 PowerShell 命令
10. 还原 `MINIMUM_CONTEXT_LENGTH` patch（DeepSeek 1.5B 有 128K 上下文，满足 64K 限制）

**关键决策**：
- 老设备 8GB 内存只能稳妥运行 1.5B 模型（7B 会内存吃紧 + 速度极慢）
- Hermes 的两个 transport patch 必须保留（llama.cpp server 的 OpenAI API 不支持 tools + streaming）

**遗留问题 / 下轮开始点**：
- **老设备端**：`git pull` → 下载 DeepSeek 模型 → 停止旧服务 → 运行 `start-llm-server.ps1`
  - 操作指令已写入 `status.md`「老设备接力」待办清单
  - 用户在老设备上说「恢复」后，AI 读取 status.md 按清单执行
- macOS 端验证：Hermes 连通性测试（`hermes chat --query "你好"`）


---

## 2026-05-23

**会话类型**：环境问题修复（GitHub push 通路恢复）

**完成内容**：
1. 诊断 GitHub push 失败：`ssh -T git@github.com` → `Permission denied (publickey)`
2. 发现 SSH agent 无 identities，GitHub 账户未注册公钥
3. 用户决定不走 SSH 密钥路，改用 GitHub CLI
4. macOS 安装 GitHub CLI（无 Homebrew）：
   - 通过代理下载 gh v2.69.0 zip 包（12MB）
   - 解压到 `/tmp/`，复制到 `~/bin/gh`
   - 将 `~/bin` 永久加入 `~/.zshrc` 和 `~/.bashrc` PATH
5. 解决 `gh auth login` 直连超时：设置 `HTTPS_PROXY`/`HTTP_PROXY` 环境变量指向本地代理
6. 用户浏览器完成 device flow 授权（https://github.com/login/device）
7. `gh auth setup-git` 配置凭证助手，git 远程 URL 从 SSH 切换为 HTTPS
8. `git fetch origin` 测试成功，push 通路恢复

**关键决策**：
- 放弃 SSH 认证，全面切换到 GitHub CLI + HTTPS 协议
- `~/bin` 作为无 sudo 权限下的用户级工具安装目录

**遗留问题 / 下轮开始点**：
- 无。push 通路已恢复，可正常使用 `git push`

---

## 2026-05-24

**会话类型**：老设备接力清单执行

**完成内容**：
1. 执行恢复摘要，确认当前在 Windows 老设备端
2. `git pull` — 已是最新
3. 下载 DeepSeek-R1-Distill-Qwen-1.5B Q4_K_M GGUF 模型：
   - HuggingFace 直接连接超时（21秒无响应）
   - hf-mirror.com 返回 404
   - 改用 ModelScope CDN 成功，1.1GB / 6分19秒 / 平均 2.8MB/s
4. 停止旧 llama-server 进程（Qwen2.5-0.5B）
5. PowerShell 运行 `start-llm-server.ps1` 启动新模型
6. API 验证通过：`/v1/models` 返回 DeepSeek 模型信息，`/health` 返回 ok

**关键决策**：
- HuggingFace 国内不可达时，优先 fallback 到 ModelScope 而非 hf-mirror（后者可能 404）
- 非管理员运行 PowerShell 脚本时，llama-server 本身可正常启动，仅防火墙规则添加失败（非阻塞）

**遗留问题 / 下轮开始点**：
- 防火墙规则需首次以管理员身份运行 `start-llm-server.ps1` 添加
- macOS 端 Hermes 连通性验证：`hermes chat --query "你好"`

---

## 2026-05-24

**会话类型**：P2 功能开发 — troubleshooting 搜索索引

**完成内容**：
1. 编写 `scripts/build-troubleshooting-index.py`（~160 行）
   - 解析 `troubleshooting.md` 的 Markdown 结构（分类、条目、表格字段）
   - 提取 27 个条目的关键词、来源、状态、行号
   - 技术栈推断：Rust/Tauri、JS/React、AI 工具链、GitHub、网络/环境、Windows、Chess
2. 生成 `troubleshooting-index.md`（110 行）
   - 快速搜索表：关键词 | 分类 | 来源 | 状态 | 行号链接
   - 按技术栈分组视图，支持一个条目多分组
3. 修复脚本问题
   - 空分类条目显示为 "未分类"
   - URL 去重避免域名中的技术关键词误匹配（如 blindfold-chess 中的 chess 被误认为 Chess/引擎）
4. 更新 `status.md`：勾选 P2 待办，追加更新记录
5. 更新 `AGENTS.md`：恢复指令 3.6 节改为「先读索引，再读详情」

**关键决策**：
- 索引采用**独立文件**（`troubleshooting-index.md`）而非插入同文件顶部
  - 理由：AI 读取成本低（~110 行 vs 288 行）、零内容污染、行号链接可靠
- 定位使用**行号链接**（`troubleshooting.md#L8`）而非标题锚点
  - 理由：GitHub 对中文标题的锚点生成算法不稳定，行号 100% 可靠且脚本重建时自动更新

**遗留问题 / 下轮开始点**：
- 技术栈映射为启发式硬编码，未来可扩展为模糊匹配或 LLM 辅助分类
- 考虑将索引重建集成到 `sync-knowledge.py` 作为同步后自动钩子

---

## 2026-05-26

**会话类型**：恢复 + CBC 环境配置

**完成内容**：
1. 恢复摘要：基础设施完善 100%，P1~P5 全部完成
2. 删除 Superpowers skills 待办（用户决定不使用）
3. 查阅 CBC 快捷键文档，向用户输出速查表
4. 创建 `~/.codebuddy/statusline.sh` 状态行脚本（模型+目录+Git分支+费用+耗时）
5. 更新 `~/.codebuddy/settings.json` 启用状态行，验证脚本运行正常

**关键决策**：
- 放弃 Superpowers skills，不融入 vibe-sop 工作流
- 状态行采用 bash + jq 方案，显示模型、目录、Git、费用、耗时五项信息

**遗留问题 / 下轮开始点**：
- 重启 CBC 会话后验证状态行实际显示效果
- P3 待办（`--dry-run`、`--since`）尚未启动

# 一次性标签化处理文档

> 本文档记录 lessons-learned 母库 94 条经验的标签分配和结构更新方案。
> 执行完后可删除。

---

## Part 1 — 标签分配表

标准标签词汇：

| 标签 | 含义 | 典型场景 |
|------|------|---------|
| TAG:pagination | 分页/懒加载 | 列表、表格、无限滚动 |
| TAG:state-management | 状态管理 | React/Vue 状态、全局状态、选中状态 |
| TAG:i18n | 国际化 | 多语言、翻译、字典管理 |
| TAG:testing | 测试策略 | 单元测试、集成测试、Mock |
| TAG:dom | DOM 操作 | 事件监听、节点替换、渲染 |
| TAG:api-design | API/接口设计 | 向后兼容、接口契约、数据格式 |
| TAG:build-env | 构建/环境 | 编译、路径、工具链、跨平台 |
| TAG:ux | 用户体验 | UI 布局、交互、焦点管理 |
| TAG:security | 安全 | 删除确认、权限、输入校验、默认安全 |
| TAG:data | 数据/持久化 | 数据格式、迁移、一致性、引号嵌套 |
| TAG:architecture | 架构设计 | 配置层、模块边界、重构影响范围 |
| TAG:debugging | 调试 | 崩溃定位、浏览器特有 bug、MinGW |
| TAG:ai-workflow | AI 工作流 | 会话管理、翻译检查、文档维护、SOP |
| TAG:cross-platform | 跨平台 | Windows/Node/git bash 路径差异 |
| TAG:performance | 性能 | 内存、DOM 渲染压力、加载策略 |

严重度定义：
- `CRITICAL`：已造成实际损失或高风险（误删、数据丢失、安全漏洞、死循环）
- `WARNING`：可能导致明显 bug 或返工（翻译遗漏、DOM 竞争、测试雪崩）
- `INFO`：最佳实践或优化建议（配置层设计、向后兼容、调试技巧）

---

| 编号 | 标签 | 严重度 | 经验摘要 |
|------|------|--------|---------|
| 1 | TAG:build-env TAG:testing | INFO | 纯 HTML+CSS+JS 无需 npm，Web Worker 需 HTTP 服务器 |
| 2 | TAG:dom TAG:api-design | WARNING | IIFE 模块 window 暴露 API，下划线前缀私有变量 |
| 3 | TAG:testing | INFO | 浏览器集成测试用 TestRunner，与 Node 同一套断言 |
| 4 | TAG:testing | INFO | Canvas 浏览器测试，Node Mock 2D context |
| 5 | TAG:data TAG:api-design | INFO | PGN 解析器空输入返回 [] 而非 null |
| 6 | TAG:dom | WARNING | cloneNode(true) 替换含 SVG 按钮导致渲染异常 |
| 7 | TAG:dom | WARNING | 匿名事件监听器无法移除，必须用命名函数 |
| 8 | TAG:dom TAG:ux | WARNING | 屏幕切换不能只隐藏上一个，须遍历全部隐藏 |
| 9 | TAG:dom | INFO | SVG path 密集参数保留空格 |
| 10 | TAG:dom | WARNING | document 级监听器引用旧 DOM 元素导致逻辑错误 |
| 11 | TAG:ai-workflow | INFO | 存档前先 ls/glob 确认文件系统现状 |
| 12 | TAG:ux | CRITICAL | UI 布局不要猜测用户意图，设计阶段出草图确认 |
| 13 | TAG:api-design | CRITICAL | 引擎候选走法调用时机决定产品逻辑正确性 |
| 14 | TAG:data TAG:api-design | WARNING | 引擎 UCI 转 SAN 才能给用户阅读 |
| 15 | TAG:dom | WARNING | 静态 HTML 与动态渲染模块 DOM 冲突 |
| 16 | TAG:testing | WARNING | 删除功能必须同步删除对应测试 |
| 17 | TAG:ux | WARNING | 焦点管理是盲棋核心体验 |
| 18 | TAG:i18n | CRITICAL | i18n 分散架构必然导致翻译遗漏，单一字典源 |
| 19 | TAG:i18n | WARNING | JS 硬编码字符串是翻译遗漏重灾区 |
| 20 | TAG:i18n | WARNING | 复制粘贴是 i18n 错误常见来源 |
| 21 | TAG:i18n TAG:architecture | WARNING | 模块内部字典从不更新 DOM 则纯属冗余 |
| 22 | TAG:i18n TAG:dom | WARNING | settings.js 与 common.js 字典竞争导致 key 名闪烁 |
| 23 | TAG:build-env | WARNING | 删除 JS 文件不从 index.html 移除引用导致 404 |
| 24 | TAG:testing | WARNING | Node 测试不对 UI 文本断言无法捕获翻译错误 |
| 25 | TAG:testing TAG:architecture | CRITICAL | 删除 fallback 函数前评估测试依赖，否则测试雪崩 |
| 26 | TAG:testing | WARNING | localStorage mock 必须支持 setItem 持久化 |
| 27 | TAG:dom TAG:i18n | WARNING | updateTexts() 与 _updateXxx() DOM 竞争 |
| 28 | TAG:ux | INFO | 弹窗选择优于循环切换 |
| 29 | TAG:dom | WARNING | cloneNode 无法移除旧事件监听器 |
| 30 | TAG:ux TAG:architecture | WARNING | UI 风格不一致根因是硬编码颜色 |
| 31 | TAG:ux TAG:architecture | WARNING | 功能入口迁移需同步更新正向+反向路径 |
| 32 | TAG:data TAG:architecture | INFO | 数据双语字段与代码硬编码分支是两个问题 |
| 33 | TAG:testing | WARNING | 测试中断言文本值是重构敏感点 |
| 34 | TAG:data TAG:build-env | WARNING | 数据文件引号嵌套是语法陷阱 |
| 35 | TAG:testing | WARNING | Node 测试全过不等于浏览器表现正常 |
| 36 | TAG:testing TAG:debugging | INFO | playwright 定位浏览器特有 bug |
| 37 | TAG:architecture | INFO | 通用配置层降低新增模式边际成本 |
| 38 | TAG:api-design | INFO | 向后兼容接口减少重构连锁反应 |
| 39 | TAG:testing TAG:dom | INFO | 浏览器集成测试发现 DOM 事件绑定遗漏 |
| 40 | TAG:testing | INFO | Node 测试覆盖逻辑，浏览器覆盖 DOM |
| 41 | TAG:ai-workflow | INFO | AGENTS.md 定义触发词，status.md 记录进度 |
| 42 | TAG:ai-workflow | INFO | 每批次开发后更新进度文档 |
| 43 | TAG:data | INFO | 手工构建100条结构化数据不现实 |
| 44 | TAG:ai-workflow | WARNING | WriteFile 不适合超大特殊字符内容 |
| 45 | TAG:cross-platform TAG:ai-workflow | WARNING | Shell here-doc 在 Windows git bash 不可靠 |
| 46 | TAG:i18n TAG:ai-workflow | WARNING | 翻译检查必须是独立任务 |
| 47 | TAG:ai-workflow | INFO | 7+文件重构应新开会话执行 |
| 48 | TAG:build-env | INFO | GitHub Pages 国内需代理 |
| 49 | TAG:cross-platform | WARNING | Windows 路径在 git bash/Node/cmd 转义规则不同 |
| 50 | TAG:api-design | INFO | windows-rs 错误处理统一用 .map_err |
| 51 | TAG:api-design | INFO | GetDiskFreeSpaceExW 参数传递方式 |
| 52 | TAG:api-design | INFO | CPU% 精确计算只需 GetProcessTimes |
| 53 | TAG:api-design | INFO | FILETIME 转 u64 公式 |
| 54 | TAG:api-design | INFO | Arc<dyn Fn> Rust 回调标准方式 |
| 55 | TAG:testing | INFO | Tauri vitest 必须 vi.mock() API 模块 |
| 56 | TAG:build-env | INFO | vite alias 指向本地 mock |
| 57 | TAG:testing | INFO | Controlled checkbox 测试用 user-event |
| 58 | TAG:api-design | INFO | tokio try_send 非阻塞进度回调 |
| 59 | TAG:state-management | CRITICAL | setState updater 内不要 dispatch 其他 setState |
| 60 | TAG:state-management | CRITICAL | useEffect 依赖 size===0 容易死循环 |
| 61 | TAG:state-management | WARNING | useRef 作为只执行一次标志比依赖数组可靠 |
| 62 | TAG:testing | INFO | 测试驱动暴露默认勾选死循环 |
| 63 | TAG:testing | INFO | 单元测试最有效发现状态管理 bug |
| 64 | TAG:ai-workflow | INFO | prompt-next-session.md 重写不变内容问题 |
| 65 | TAG:ai-workflow | INFO | status.md + AGENTS.md 改进方案 |
| 66 | TAG:ai-workflow | INFO | 新会话读2份文件开工 |
| 67 | TAG:ai-workflow | WARNING | 横跨工具层词汇必须确认语境 |
| 68 | TAG:ai-workflow | WARNING | 工具硬性限制直接给结论+风险+替代方案 |
| 69 | TAG:ai-workflow | WARNING | SOP 模板必须逐字核对关键字段 |
| 70 | TAG:cross-platform TAG:build-env | CRITICAL | 中文路径 + MinGW = 链接器失败 |
| 71 | TAG:cross-platform TAG:build-env | INFO | cargo check --lib 中文路径可跑 |
| 72 | TAG:debugging | INFO | 0xc0000139 先跑最简单 lib 测试排除工具链问题 |
| 73 | TAG:debugging | WARNING | cargo test --bin 能过 --lib 崩溃 = 定位信号 |
| 74 | TAG:debugging | INFO | 定位代码最快方法：清空 lib.rs 逐步 pub mod |
| 75 | TAG:cross-platform TAG:build-env | CRITICAL | tauri::AppHandle + MinGW = STATUS_ENTRYPOINT_NOT_FOUND |
| 76 | TAG:testing TAG:cross-platform | INFO | #[cfg(not(test))] 隔离问题代码 |
| 77 | TAG:dom TAG:ux | INFO | useRef + mousedown 实现点击外部关闭 |
| 78 | TAG:ux | INFO | CSS @keyframes 淡入+位移动画 |
| 79 | TAG:ux | INFO | 年月日联动限制 |
| 80 | TAG:build-env | INFO | cargo tauri dev 需交互式 Windows 桌面 |
| 81 | TAG:build-env | INFO | npm run dev 替代方案预览前端 |
| 82 | TAG:build-env | INFO | 完整功能验证仍需 cargo tauri dev |
| 83 | TAG:data TAG:performance | WARNING | 不要一次性加载所有完整 TraceItem 到前端 |
| 84 | TAG:architecture TAG:data | INFO | 后端提供轻量摘要接口 |
| 85 | TAG:pagination TAG:architecture | WARNING | 分页浏览与全选全部解耦 |
| 86 | TAG:pagination TAG:state-management TAG:security | CRITICAL | 事故：默认勾选误删 17,706 个文件 |
| 87 | TAG:pagination TAG:state-management | CRITICAL | 根因链：默认勾选 × 只清当前页 × 遍历 scanResults |
| 88 | TAG:security TAG:ux | CRITICAL | 默认安全 > 默认便利 |
| 89 | TAG:pagination TAG:state-management | WARNING | deselectAll 只遍历 searchedItems |
| 90 | TAG:pagination TAG:state-management | INFO | deselectAll 清空 selectedIds + decisions |
| 91 | TAG:pagination TAG:state-management | WARNING | 取消与全选必须范围对称 |
| 92 | TAG:pagination TAG:state-management | WARNING | ConfirmPage 遍历 scanResults 导致分页丢失 |
| 93 | TAG:pagination TAG:state-management | INFO | 遍历 decisions 兜底 name:id |
| 94 | TAG:pagination TAG:architecture | WARNING | 用户操作集合是主数据源，展示数据是从属 |

---

统计：
- CRITICAL: 8 条
- WARNING: 33 条
- INFO: 53 条

---

## Part 2 — 更新后的母库 lessons-learned.md

以下内容是替换根目录 `lessons-learned.md` 的完整版本。



---

## Part 2 — 母库更新状态

母库 `lessons-learned.md` 已按上方标签分配表完成更新：
- ✅ 增加「标签」「严重度」两列
- ✅ 顶部增加标签速查索引
- ✅ 94 条经验全部打标
- ✅ 流程经验部分保持不变

更新后的文件位于：`E:/work-space/vs-code/vibe-coding-project-sop/lessons-learned.md`

---

## Part 3 — anti-patterns-checklist 模板

模板已创建：`templates/anti-patterns-checklist.md`

内容要点：
- 阶段二设计时的强制检查框架
- 预置 7 个 CRITICAL 级检查项（分页、useEffect 死循环、默认安全、i18n、UI 猜测、测试依赖、中文路径）
- 汇总表：按标签统计涉及数、规避方案、design.md 章节
- 自定义检查项扩展区

新项目使用本骨架时，可将此模板复制为 `docs/anti-patterns-checklist.md`，按需增删检查项。

---

*本文档已完成使命，可删除。*

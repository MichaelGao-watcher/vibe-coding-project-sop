# Troubleshooting 搜索索引

> 本文件由 `scripts/build-troubleshooting-index.py` 自动生成。
> 每次修改 `troubleshooting.md` 后，运行 `python scripts/build-troubleshooting-index.py` 重建。

> 当前收录 **27** 条问题记录，按分类 + 关键词排序。

---

## 快速搜索表

| 关键词 | 分类 | 来源 | 状态 | 定位 |
|--------|------|------|------|------|
| Stockfish 加载超时 / 引擎不启动 | 未分类 | blindfold-chess | 已知限制 | troubleshooting.md#L8 |
| GitHub Pages 国内打不开 | 未分类 | blindfold-chess | 已知限制 | troubleshooting.md#L17 |
| Node.js 测试运行时 chess.js 未定义 | 开发/测试 | blindfold-chess | 已修复（测试已适配） | troubleshooting.md#L30 |
| CLI subAgent 并行超时 | 开发/测试 | blindfold-chess | 已修复（改为 IDE 串行） | troubleshooting.md#L39 |
| 设置面板一闪而过 | 开发/测试 | blindfold-chess | 已修复 | troubleshooting.md#L48 |
| 旧代码与新模块冲突 | 运行时 | blindfold-chess | 已知未修复（逐步迁移中） | troubleshooting.md#L61 |
| 引擎候选走法未集成 | 运行时 | blindfold-chess | 已知未修复 | troubleshooting.md#L70 |
| JS 数据文件嵌套单引号导致 `Unexpected identifier` | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L81 |
| 设置面板点击无反应（panel toggle 测试失败） | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L91 |
| mock DOM 中 `querySelector` / `querySelectorAll` 缺失 | 运行时 | blindfold-chess | 已修复（测试已适配） | troubleshooting.md#L101 |
| `cargo check --lib` 报错：`GetDiskFreeSpaceExW` 未定义 | 运行时 | french-exit | — | troubleshooting.md#L113 |
| `cargo check --lib` 报错：`FILETIME` 未定义 | 运行时 | french-exit | — | troubleshooting.md#L121 |
| `cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失） | 运行时错误 | french-exit | ✅ 已修复 | troubleshooting.md#L133 |
| 运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime` | 运行时错误 | french-exit | — | troubleshooting.md#L145 |
| 运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll` | 运行时错误 | french-exit | — | troubleshooting.md#L153 |
| `cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32) | 运行时错误 | french-exit | — | troubleshooting.md#L161 |
| vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"` | 测试错误 | french-exit | — | troubleshooting.md#L171 |
| vitest 报错：`act is not a function` | 测试错误 | french-exit | — | troubleshooting.md#L180 |
| vitest 报错：React 警告 `Cannot update a component while rendering` | 测试错误 | french-exit | — | troubleshooting.md#L188 |
| checkbox 点击后状态不变化 | 测试错误 | french-exit | — | troubleshooting.md#L197 |
| 中文路径下编译失败 | 环境问题 | french-exit | — | troubleshooting.md#L210 |
| cargo tauri dev 在后台任务中崩溃 | 环境问题 | french-exit | — | troubleshooting.md#L221 |
| PowerShell 执行中文脚本报 "UnexpectedToken" | 存档提示 | vibe-coding-project-sop | — | troubleshooting.md#L242 |
| GitHub push 报错 `Permission denied (publickey)` | 存档提示 | vibe-coding-project-sop | 已修复 | troubleshooting.md#L254 |
| `gh auth login` 超时：`read tcp ... operation timed out` | 存档提示 | vibe-coding-project-sop | 已修复 | troubleshooting.md#L263 |
| HuggingFace 模型下载连接超时 `curl: (28) Could not connect to server` | 存档提示 | vibe-coding-project-sop | 已解决 | troubleshooting.md#L272 |
| PowerShell 添加防火墙规则权限不足 `Access is denied` | 存档提示 | vibe-coding-project-sop | 已知限制 | troubleshooting.md#L281 |

---

## 按技术栈分组

> 一个条目可能同时属于多个技术栈。

### Rust / Tauri

- [`cargo check --lib` 报错：`GetDiskFreeSpaceExW` 未定义](troubleshooting.md#L113) — `运行时`
- [`cargo check --lib` 报错：`FILETIME` 未定义](troubleshooting.md#L121) — `运行时`
- [`cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失）](troubleshooting.md#L133) — `运行时错误`
- [运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime`](troubleshooting.md#L145) — `运行时错误`
- [运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll`](troubleshooting.md#L153) — `运行时错误`
- [`cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32)](troubleshooting.md#L161) — `运行时错误`
- [vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"`](troubleshooting.md#L171) — `测试错误`
- [中文路径下编译失败](troubleshooting.md#L210) — `环境问题`
- [cargo tauri dev 在后台任务中崩溃](troubleshooting.md#L221) — `环境问题`

### JavaScript / React / Vitest

- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L30) — `开发/测试`
- [JS 数据文件嵌套单引号导致 `Unexpected identifier`](troubleshooting.md#L81) — `运行时`
- [设置面板点击无反应（panel toggle 测试失败）](troubleshooting.md#L91) — `运行时`
- [mock DOM 中 `querySelector` / `querySelectorAll` 缺失](troubleshooting.md#L101) — `运行时`
- [vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"`](troubleshooting.md#L171) — `测试错误`
- [vitest 报错：`act is not a function`](troubleshooting.md#L180) — `测试错误`
- [vitest 报错：React 警告 `Cannot update a component while rendering`](troubleshooting.md#L188) — `测试错误`
- [checkbox 点击后状态不变化](troubleshooting.md#L197) — `测试错误`

### AI 工具链 / LLM

- [PowerShell 执行中文脚本报 "UnexpectedToken"](troubleshooting.md#L242) — `存档提示`
- [HuggingFace 模型下载连接超时 `curl: (28) Could not connect to server`](troubleshooting.md#L272) — `存档提示`
- [PowerShell 添加防火墙规则权限不足 `Access is denied`](troubleshooting.md#L281) — `存档提示`

### Git / GitHub

- [GitHub Pages 国内打不开](troubleshooting.md#L17) — `未分类`
- [GitHub push 报错 `Permission denied (publickey)`](troubleshooting.md#L254) — `存档提示`
- [`gh auth login` 超时：`read tcp ... operation timed out`](troubleshooting.md#L263) — `存档提示`

### 网络 / 环境 / 权限

- [GitHub Pages 国内打不开](troubleshooting.md#L17) — `未分类`
- [中文路径下编译失败](troubleshooting.md#L210) — `环境问题`
- [HuggingFace 模型下载连接超时 `curl: (28) Could not connect to server`](troubleshooting.md#L272) — `存档提示`
- [PowerShell 添加防火墙规则权限不足 `Access is denied`](troubleshooting.md#L281) — `存档提示`

### Windows / PowerShell

- [`cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失）](troubleshooting.md#L133) — `运行时错误`
- [运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime`](troubleshooting.md#L145) — `运行时错误`
- [运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll`](troubleshooting.md#L153) — `运行时错误`
- [`cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32)](troubleshooting.md#L161) — `运行时错误`
- [中文路径下编译失败](troubleshooting.md#L210) — `环境问题`
- [PowerShell 执行中文脚本报 "UnexpectedToken"](troubleshooting.md#L242) — `存档提示`
- [PowerShell 添加防火墙规则权限不足 `Access is denied`](troubleshooting.md#L281) — `存档提示`

### Chess / 引擎

- [Stockfish 加载超时 / 引擎不启动](troubleshooting.md#L8) — `未分类`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L30) — `开发/测试`
- [引擎候选走法未集成](troubleshooting.md#L70) — `运行时`

### 其他

- [CLI subAgent 并行超时](troubleshooting.md#L39) — `开发/测试`
- [设置面板一闪而过](troubleshooting.md#L48) — `开发/测试`
- [旧代码与新模块冲突](troubleshooting.md#L61) — `运行时`

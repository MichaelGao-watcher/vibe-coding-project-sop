# Troubleshooting 搜索索引

> 本文件由 `scripts/build-troubleshooting-index.py` 自动生成。
> 每次修改 `troubleshooting.md` 后，运行 `python scripts/build-troubleshooting-index.py` 重建。

> 当前收录 **105** 条问题记录，按分类 + 关键词排序。

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
| Stockfish 加载超时 / 引擎不启动 | 存档提示 | blindfold-chess | 已知限制 | troubleshooting.md#L291 |
| GitHub Pages 国内打不开 | 存档提示 | blindfold-chess | 已知限制 | troubleshooting.md#L300 |
| Node.js 测试运行时 chess.js 未定义 | 开发/测试 | blindfold-chess | 已修复（测试已适配） | troubleshooting.md#L313 |
| CLI subAgent 并行超时 | 开发/测试 | blindfold-chess | 已修复（改为 IDE 串行） | troubleshooting.md#L322 |
| 设置面板一闪而过 | 开发/测试 | blindfold-chess | 已修复 | troubleshooting.md#L331 |
| 旧代码与新模块冲突 | 运行时 | blindfold-chess | 已知未修复（逐步迁移中） | troubleshooting.md#L344 |
| 引擎候选走法未集成 | 运行时 | blindfold-chess | 已知未修复 | troubleshooting.md#L353 |
| JS 数据文件嵌套单引号导致 `Unexpected identifier` | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L364 |
| 设置面板点击无反应（panel toggle 测试失败） | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L374 |
| Stockfish 加载超时 / 引擎不启动 | 运行时 | blindfold-chess | 已知限制 | troubleshooting.md#L384 |
| GitHub Pages 国内打不开 | 运行时 | blindfold-chess | 已知限制 | troubleshooting.md#L393 |
| Node.js 测试运行时 chess.js 未定义 | 开发/测试 | blindfold-chess | 已修复（测试已适配） | troubleshooting.md#L406 |
| CLI subAgent 并行超时 | 开发/测试 | blindfold-chess | 已修复（改为 IDE 串行） | troubleshooting.md#L415 |
| 设置面板一闪而过 | 开发/测试 | blindfold-chess | 已修复 | troubleshooting.md#L424 |
| 旧代码与新模块冲突 | 运行时 | blindfold-chess | 已知未修复（逐步迁移中） | troubleshooting.md#L437 |
| 引擎候选走法未集成 | 运行时 | blindfold-chess | 已知未修复 | troubleshooting.md#L446 |
| JS 数据文件嵌套单引号导致 `Unexpected identifier` | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L457 |
| 设置面板点击无反应（panel toggle 测试失败） | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L467 |
| `cargo check --lib` 报错：`GetDiskFreeSpaceExW` 未定义 | 运行时 | french-exit | — | troubleshooting.md#L477 |
| `cargo check --lib` 报错：`FILETIME` 未定义 | 运行时 | french-exit | — | troubleshooting.md#L485 |
| `cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失） | 运行时错误 | french-exit | ✅ 已修复 | troubleshooting.md#L497 |
| 运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime` | 运行时错误 | french-exit | — | troubleshooting.md#L509 |
| 运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll` | 运行时错误 | french-exit | — | troubleshooting.md#L517 |
| `cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32) | 运行时错误 | french-exit | — | troubleshooting.md#L525 |
| vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"` | 测试错误 | french-exit | — | troubleshooting.md#L535 |
| vitest 报错：`act is not a function` | 测试错误 | french-exit | — | troubleshooting.md#L544 |
| vitest 报错：React 警告 `Cannot update a component while rendering` | 测试错误 | french-exit | — | troubleshooting.md#L552 |
| checkbox 点击后状态不变化 | 测试错误 | french-exit | — | troubleshooting.md#L561 |
| 中文路径下编译失败 | 环境问题 | french-exit | — | troubleshooting.md#L574 |
| cargo tauri dev 在后台任务中崩溃 | 环境问题 | french-exit | — | troubleshooting.md#L585 |
| PowerShell 执行中文脚本报 "UnexpectedToken" | 存档提示 | vibe-coding-project-sop | — | troubleshooting.md#L606 |
| GitHub push 报错 `Permission denied (publickey)` | 存档提示 | vibe-coding-project-sop | 已修复 | troubleshooting.md#L618 |
| `gh auth login` 超时：`read tcp ... operation timed out` | 存档提示 | vibe-coding-project-sop | 已修复 | troubleshooting.md#L627 |
| HuggingFace 模型下载连接超时 `curl: (28) Could not connect to server` | 存档提示 | vibe-coding-project-sop | 已解决 | troubleshooting.md#L636 |
| PowerShell 添加防火墙规则权限不足 `Access is denied` | 存档提示 | vibe-coding-project-sop | 已知限制 | troubleshooting.md#L645 |
| Node.js 报 SyntaxError: Unexpected identifier（i18n 中文字符串） | 存档提示 | blindfold-chess | 已解决 | troubleshooting.md#L654 |
| sed 批量修改误改结构体定义 | 存档提示 | french-exit | — | troubleshooting.md#L664 |
| French Exit 进程锁定 exe 导致复制失败 | 存档提示 | french-exit | — | troubleshooting.md#L673 |
| Stockfish 加载超时 / 引擎不启动 | 存档提示 | blindfold-chess | 已知限制 | troubleshooting.md#L691 |
| GitHub Pages 国内打不开 | 存档提示 | blindfold-chess | 已知限制 | troubleshooting.md#L700 |
| Node.js 测试运行时 chess.js 未定义 | 开发/测试 | blindfold-chess | 已修复（测试已适配） | troubleshooting.md#L713 |
| CLI subAgent 并行超时 | 开发/测试 | blindfold-chess | 已修复（改为 IDE 串行） | troubleshooting.md#L722 |
| 设置面板一闪而过 | 开发/测试 | blindfold-chess | 已修复 | troubleshooting.md#L731 |
| 旧代码与新模块冲突 | 运行时 | blindfold-chess | 已知未修复（逐步迁移中） | troubleshooting.md#L744 |
| 引擎候选走法未集成 | 运行时 | blindfold-chess | 已知未修复 | troubleshooting.md#L753 |
| JS 数据文件嵌套单引号导致 `Unexpected identifier` | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L764 |
| 设置面板点击无反应（panel toggle 测试失败） | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L774 |
| Stockfish 加载超时 / 引擎不启动 | 运行时 | blindfold-chess | 已知限制 | troubleshooting.md#L784 |
| GitHub Pages 国内打不开 | 运行时 | blindfold-chess | 已知限制 | troubleshooting.md#L793 |
| Node.js 测试运行时 chess.js 未定义 | 开发/测试 | blindfold-chess | 已修复（测试已适配） | troubleshooting.md#L806 |
| CLI subAgent 并行超时 | 开发/测试 | blindfold-chess | 已修复（改为 IDE 串行） | troubleshooting.md#L815 |
| 设置面板一闪而过 | 开发/测试 | blindfold-chess | 已修复 | troubleshooting.md#L824 |
| 旧代码与新模块冲突 | 运行时 | blindfold-chess | 已知未修复（逐步迁移中） | troubleshooting.md#L837 |
| 引擎候选走法未集成 | 运行时 | blindfold-chess | 已知未修复 | troubleshooting.md#L846 |
| JS 数据文件嵌套单引号导致 `Unexpected identifier` | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L857 |
| 设置面板点击无反应（panel toggle 测试失败） | 运行时 | blindfold-chess | 已修复 | troubleshooting.md#L867 |
| mock DOM 中 `querySelector` / `querySelectorAll` 缺失 | 运行时 | blindfold-chess | 已修复（测试已适配） | troubleshooting.md#L877 |
| `cargo check --lib` 报错：`GetDiskFreeSpaceExW` 未定义 | 运行时 | french-exit | — | troubleshooting.md#L889 |
| `cargo check --lib` 报错：`FILETIME` 未定义 | 运行时 | french-exit | — | troubleshooting.md#L897 |
| `cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失） | 运行时错误 | french-exit | ✅ 已修复 | troubleshooting.md#L909 |
| 运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime` | 运行时错误 | french-exit | — | troubleshooting.md#L921 |
| 运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll` | 运行时错误 | french-exit | — | troubleshooting.md#L929 |
| `cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32) | 运行时错误 | french-exit | — | troubleshooting.md#L937 |
| vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"` | 测试错误 | french-exit | — | troubleshooting.md#L947 |
| vitest 报错：`act is not a function` | 测试错误 | french-exit | — | troubleshooting.md#L956 |
| vitest 报错：React 警告 `Cannot update a component while rendering` | 测试错误 | french-exit | — | troubleshooting.md#L964 |
| checkbox 点击后状态不变化 | 测试错误 | french-exit | — | troubleshooting.md#L973 |
| 中文路径下编译失败 | 环境问题 | french-exit | — | troubleshooting.md#L986 |
| cargo tauri dev 在后台任务中崩溃 | 环境问题 | french-exit | — | troubleshooting.md#L997 |
| Cookie 过期 / 401 认证失败 | 存档提示 | qianniu_business_analytics | 已修复（有自动刷新机制） | troubleshooting.md#L1018 |
| Digest 刷新失败 | 存档提示 | qianniu_business_analytics | 已知处理方案 | troubleshooting.md#L1027 |
| auth/jycm.json 缺失字段 | 存档提示 | qianniu_business_analytics | 已修复（有写入验证） | troubleshooting.md#L1036 |
| 日期区间多返回一天 | 取数相关 | qianniu_business_analytics | 已修复（有强制约束） | troubleshooting.md#L1049 |
| getAllShopList 返回空数组 | 取数相关 | qianniu_business_analytics | 已知未修复（业务侧问题） | troubleshooting.md#L1058 |
| createAndDownload 返回失败 | 取数相关 | qianniu_business_analytics | 已知未修复（需具体 case 分析） | troubleshooting.md#L1067 |
| openpyxl 未安装 | 报告相关 | qianniu_business_analytics | 临时绕过 | troubleshooting.md#L1080 |
| 钉钉推送失败 | 报告相关 | qianniu_business_analytics | 已知未修复（需用户侧配置） | troubleshooting.md#L1089 |
| Windows Git Bash LF/CRLF 警告 | 环境相关 | qianniu_business_analytics | 已知未修复（不影响功能） | troubleshooting.md#L1102 |

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
- [`cargo check --lib` 报错：`GetDiskFreeSpaceExW` 未定义](troubleshooting.md#L477) — `运行时`
- [`cargo check --lib` 报错：`FILETIME` 未定义](troubleshooting.md#L485) — `运行时`
- [`cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失）](troubleshooting.md#L497) — `运行时错误`
- [运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime`](troubleshooting.md#L509) — `运行时错误`
- [运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll`](troubleshooting.md#L517) — `运行时错误`
- [`cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32)](troubleshooting.md#L525) — `运行时错误`
- [vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"`](troubleshooting.md#L535) — `测试错误`
- [中文路径下编译失败](troubleshooting.md#L574) — `环境问题`
- [cargo tauri dev 在后台任务中崩溃](troubleshooting.md#L585) — `环境问题`
- [sed 批量修改误改结构体定义](troubleshooting.md#L664) — `存档提示`
- [`cargo check --lib` 报错：`GetDiskFreeSpaceExW` 未定义](troubleshooting.md#L889) — `运行时`
- [`cargo check --lib` 报错：`FILETIME` 未定义](troubleshooting.md#L897) — `运行时`
- [`cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失）](troubleshooting.md#L909) — `运行时错误`
- [运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime`](troubleshooting.md#L921) — `运行时错误`
- [运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll`](troubleshooting.md#L929) — `运行时错误`
- [`cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32)](troubleshooting.md#L937) — `运行时错误`
- [vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"`](troubleshooting.md#L947) — `测试错误`
- [中文路径下编译失败](troubleshooting.md#L986) — `环境问题`
- [cargo tauri dev 在后台任务中崩溃](troubleshooting.md#L997) — `环境问题`

### JavaScript / React / Vitest

- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L30) — `开发/测试`
- [JS 数据文件嵌套单引号导致 `Unexpected identifier`](troubleshooting.md#L81) — `运行时`
- [设置面板点击无反应（panel toggle 测试失败）](troubleshooting.md#L91) — `运行时`
- [mock DOM 中 `querySelector` / `querySelectorAll` 缺失](troubleshooting.md#L101) — `运行时`
- [vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"`](troubleshooting.md#L171) — `测试错误`
- [vitest 报错：`act is not a function`](troubleshooting.md#L180) — `测试错误`
- [vitest 报错：React 警告 `Cannot update a component while rendering`](troubleshooting.md#L188) — `测试错误`
- [checkbox 点击后状态不变化](troubleshooting.md#L197) — `测试错误`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L313) — `开发/测试`
- [JS 数据文件嵌套单引号导致 `Unexpected identifier`](troubleshooting.md#L364) — `运行时`
- [设置面板点击无反应（panel toggle 测试失败）](troubleshooting.md#L374) — `运行时`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L406) — `开发/测试`
- [JS 数据文件嵌套单引号导致 `Unexpected identifier`](troubleshooting.md#L457) — `运行时`
- [设置面板点击无反应（panel toggle 测试失败）](troubleshooting.md#L467) — `运行时`
- [vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"`](troubleshooting.md#L535) — `测试错误`
- [vitest 报错：`act is not a function`](troubleshooting.md#L544) — `测试错误`
- [vitest 报错：React 警告 `Cannot update a component while rendering`](troubleshooting.md#L552) — `测试错误`
- [checkbox 点击后状态不变化](troubleshooting.md#L561) — `测试错误`
- [Node.js 报 SyntaxError: Unexpected identifier（i18n 中文字符串）](troubleshooting.md#L654) — `存档提示`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L713) — `开发/测试`
- [JS 数据文件嵌套单引号导致 `Unexpected identifier`](troubleshooting.md#L764) — `运行时`
- [设置面板点击无反应（panel toggle 测试失败）](troubleshooting.md#L774) — `运行时`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L806) — `开发/测试`
- [JS 数据文件嵌套单引号导致 `Unexpected identifier`](troubleshooting.md#L857) — `运行时`
- [设置面板点击无反应（panel toggle 测试失败）](troubleshooting.md#L867) — `运行时`
- [mock DOM 中 `querySelector` / `querySelectorAll` 缺失](troubleshooting.md#L877) — `运行时`
- [vitest 报错：`Failed to resolve import "@tauri-apps/api/fs"`](troubleshooting.md#L947) — `测试错误`
- [vitest 报错：`act is not a function`](troubleshooting.md#L956) — `测试错误`
- [vitest 报错：React 警告 `Cannot update a component while rendering`](troubleshooting.md#L964) — `测试错误`
- [checkbox 点击后状态不变化](troubleshooting.md#L973) — `测试错误`

### AI 工具链 / LLM

- [PowerShell 执行中文脚本报 "UnexpectedToken"](troubleshooting.md#L242) — `存档提示`
- [HuggingFace 模型下载连接超时 `curl: (28) Could not connect to server`](troubleshooting.md#L272) — `存档提示`
- [PowerShell 添加防火墙规则权限不足 `Access is denied`](troubleshooting.md#L281) — `存档提示`
- [PowerShell 执行中文脚本报 "UnexpectedToken"](troubleshooting.md#L606) — `存档提示`
- [HuggingFace 模型下载连接超时 `curl: (28) Could not connect to server`](troubleshooting.md#L636) — `存档提示`
- [PowerShell 添加防火墙规则权限不足 `Access is denied`](troubleshooting.md#L645) — `存档提示`

### Git / GitHub

- [GitHub Pages 国内打不开](troubleshooting.md#L17) — `未分类`
- [GitHub push 报错 `Permission denied (publickey)`](troubleshooting.md#L254) — `存档提示`
- [`gh auth login` 超时：`read tcp ... operation timed out`](troubleshooting.md#L263) — `存档提示`
- [GitHub Pages 国内打不开](troubleshooting.md#L300) — `存档提示`
- [GitHub Pages 国内打不开](troubleshooting.md#L393) — `运行时`
- [GitHub push 报错 `Permission denied (publickey)`](troubleshooting.md#L618) — `存档提示`
- [`gh auth login` 超时：`read tcp ... operation timed out`](troubleshooting.md#L627) — `存档提示`
- [GitHub Pages 国内打不开](troubleshooting.md#L700) — `存档提示`
- [GitHub Pages 国内打不开](troubleshooting.md#L793) — `运行时`
- [Windows Git Bash LF/CRLF 警告](troubleshooting.md#L1102) — `环境相关`

### 网络 / 环境 / 权限

- [GitHub Pages 国内打不开](troubleshooting.md#L17) — `未分类`
- [中文路径下编译失败](troubleshooting.md#L210) — `环境问题`
- [HuggingFace 模型下载连接超时 `curl: (28) Could not connect to server`](troubleshooting.md#L272) — `存档提示`
- [PowerShell 添加防火墙规则权限不足 `Access is denied`](troubleshooting.md#L281) — `存档提示`
- [GitHub Pages 国内打不开](troubleshooting.md#L300) — `存档提示`
- [GitHub Pages 国内打不开](troubleshooting.md#L393) — `运行时`
- [中文路径下编译失败](troubleshooting.md#L574) — `环境问题`
- [HuggingFace 模型下载连接超时 `curl: (28) Could not connect to server`](troubleshooting.md#L636) — `存档提示`
- [PowerShell 添加防火墙规则权限不足 `Access is denied`](troubleshooting.md#L645) — `存档提示`
- [GitHub Pages 国内打不开](troubleshooting.md#L700) — `存档提示`
- [GitHub Pages 国内打不开](troubleshooting.md#L793) — `运行时`
- [中文路径下编译失败](troubleshooting.md#L986) — `环境问题`
- [Digest 刷新失败](troubleshooting.md#L1027) — `存档提示`

### Windows / PowerShell

- [`cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失）](troubleshooting.md#L133) — `运行时错误`
- [运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime`](troubleshooting.md#L145) — `运行时错误`
- [运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll`](troubleshooting.md#L153) — `运行时错误`
- [`cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32)](troubleshooting.md#L161) — `运行时错误`
- [中文路径下编译失败](troubleshooting.md#L210) — `环境问题`
- [PowerShell 执行中文脚本报 "UnexpectedToken"](troubleshooting.md#L242) — `存档提示`
- [PowerShell 添加防火墙规则权限不足 `Access is denied`](troubleshooting.md#L281) — `存档提示`
- [`cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失）](troubleshooting.md#L497) — `运行时错误`
- [运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime`](troubleshooting.md#L509) — `运行时错误`
- [运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll`](troubleshooting.md#L517) — `运行时错误`
- [`cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32)](troubleshooting.md#L525) — `运行时错误`
- [中文路径下编译失败](troubleshooting.md#L574) — `环境问题`
- [PowerShell 执行中文脚本报 "UnexpectedToken"](troubleshooting.md#L606) — `存档提示`
- [PowerShell 添加防火墙规则权限不足 `Access is denied`](troubleshooting.md#L645) — `存档提示`
- [French Exit 进程锁定 exe 导致复制失败](troubleshooting.md#L673) — `存档提示`
- [`cargo test --lib` 报错 `0xc0000139`（UCRT DLL 缺失）](troubleshooting.md#L909) — `运行时错误`
- [运行 `french-exit.exe` 报错：`Could not find the WebView2 Runtime`](troubleshooting.md#L921) — `运行时错误`
- [运行 `french-exit.exe` 报错：`找不到 WebView2Loader.dll`](troubleshooting.md#L929) — `运行时错误`
- [`cargo tauri build` 失败：`另一个程序正在使用此文件` (os error 32)](troubleshooting.md#L937) — `运行时错误`
- [中文路径下编译失败](troubleshooting.md#L986) — `环境问题`
- [Windows Git Bash LF/CRLF 警告](troubleshooting.md#L1102) — `环境相关`

### Chess / 引擎

- [Stockfish 加载超时 / 引擎不启动](troubleshooting.md#L8) — `未分类`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L30) — `开发/测试`
- [引擎候选走法未集成](troubleshooting.md#L70) — `运行时`
- [Stockfish 加载超时 / 引擎不启动](troubleshooting.md#L291) — `存档提示`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L313) — `开发/测试`
- [引擎候选走法未集成](troubleshooting.md#L353) — `运行时`
- [Stockfish 加载超时 / 引擎不启动](troubleshooting.md#L384) — `运行时`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L406) — `开发/测试`
- [引擎候选走法未集成](troubleshooting.md#L446) — `运行时`
- [Stockfish 加载超时 / 引擎不启动](troubleshooting.md#L691) — `存档提示`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L713) — `开发/测试`
- [引擎候选走法未集成](troubleshooting.md#L753) — `运行时`
- [Stockfish 加载超时 / 引擎不启动](troubleshooting.md#L784) — `运行时`
- [Node.js 测试运行时 chess.js 未定义](troubleshooting.md#L806) — `开发/测试`
- [引擎候选走法未集成](troubleshooting.md#L846) — `运行时`

### 其他

- [CLI subAgent 并行超时](troubleshooting.md#L39) — `开发/测试`
- [设置面板一闪而过](troubleshooting.md#L48) — `开发/测试`
- [旧代码与新模块冲突](troubleshooting.md#L61) — `运行时`
- [CLI subAgent 并行超时](troubleshooting.md#L322) — `开发/测试`
- [设置面板一闪而过](troubleshooting.md#L331) — `开发/测试`
- [旧代码与新模块冲突](troubleshooting.md#L344) — `运行时`
- [CLI subAgent 并行超时](troubleshooting.md#L415) — `开发/测试`
- [设置面板一闪而过](troubleshooting.md#L424) — `开发/测试`
- [旧代码与新模块冲突](troubleshooting.md#L437) — `运行时`
- [CLI subAgent 并行超时](troubleshooting.md#L722) — `开发/测试`
- [设置面板一闪而过](troubleshooting.md#L731) — `开发/测试`
- [旧代码与新模块冲突](troubleshooting.md#L744) — `运行时`
- [CLI subAgent 并行超时](troubleshooting.md#L815) — `开发/测试`
- [设置面板一闪而过](troubleshooting.md#L824) — `开发/测试`
- [旧代码与新模块冲突](troubleshooting.md#L837) — `运行时`
- [Cookie 过期 / 401 认证失败](troubleshooting.md#L1018) — `存档提示`
- [auth/jycm.json 缺失字段](troubleshooting.md#L1036) — `存档提示`
- [日期区间多返回一天](troubleshooting.md#L1049) — `取数相关`
- [getAllShopList 返回空数组](troubleshooting.md#L1058) — `取数相关`
- [createAndDownload 返回失败](troubleshooting.md#L1067) — `取数相关`
- [openpyxl 未安装](troubleshooting.md#L1080) — `报告相关`
- [钉钉推送失败](troubleshooting.md#L1089) — `报告相关`

# 老设备 LLM 局域网服务

本目录包含老设备（i7-7500U/8GB）部署为局域网大模型服务器的全部脚本和配置。

---

## 📁 文件说明

| 文件 | 用途 | 是否需要修改 |
|------|------|-------------|
| `start-llm-server.ps1` | **核心脚本**：启动 llama.cpp 服务 + 添加防火墙规则 | 一般不需要 |
| `macbook-connect.md` | MacBook Air 连接本服务的配置指南 | 如果 IP 变了需要更新 |
| `ollama-setup.ps1` | 备用：Ollama 服务化配置脚本（未使用） | 备用 |
| `Modelfile-qwen2.5-0.5b` | 备用：Ollama 模型定义文件（未使用） | 备用 |

> **明天打开这个目录，只看 `start-llm-server.ps1` 和 `macbook-connect.md` 即可。**

---

## ⚡ 快速启动（老设备）

**以管理员身份打开 PowerShell**，复制执行以下命令：

```powershell
cd "D:\Vibe-Code\vibe-coding-project-sop\llm-server"
.\start-llm-server.ps1
```

执行后会：
- 检查并启动 llama-server（如果已在运行则提示）
- 添加防火墙入站规则（首次运行需要管理员权限）
- 显示本机 IP 和 API 端点

---

## 🔌 MacBook Air 连接

打开终端，执行：

```bash
export OPENAI_API_KEY="dummy"
export OPENAI_BASE_URL="http://192.168.18.122:11434/v1"
```

详细配置（aider、Continue.dev、OpenAI SDK）见 `macbook-connect.md`。

---

## 📊 服务信息

| 项目 | 值 |
|------|-----|
| 模型 | Qwen2.5-0.5B-Instruct (Q4_K_M) |
| 本机 IP | `192.168.18.122` |
| API 端点 | `http://192.168.18.122:11434/v1` |
| 推理速度 | 约 20 tokens/s（纯 CPU） |

---

## ⚠️ 注意事项

1. **每次开机后**，老设备需要重新运行 `start-llm-server.ps1`
2. 如果老设备 IP 变了，需要更新 `macbook-connect.md` 中的 IP 地址
3. 8GB 内存限制，不要同时运行其他大程序

# MacBook Air 连接老设备 LLM 服务

## 服务信息
| 项目 | 值 |
|------|-----|
| **服务** | llama.cpp server |
| **IP** | `192.168.18.122` |
| **端口** | `11434` |
| **模型** | DeepSeek-R1-Distill-Qwen-1.5B (Q4_K_M) |
| **API 格式** | OpenAI Compatible |

## 通用环境变量
```bash
export OPENAI_API_KEY="dummy"
export OPENAI_BASE_URL="http://192.168.18.122:11434/v1"
```

## 常用工具配置

### aider（AI 编程助手）
```bash
aider --model openai/deepseek-r1-distill-qwen-1.5b.Q4_K_M.gguf \
  --api-key dummy \
  --openai-api-base http://192.168.18.122:11434/v1
```

### Continue.dev（VS Code 插件）
在 `~/.continue/config.json` 中：
```json
{
  "models": [
    {
      "title": "Local DeepSeek-R1",
      "provider": "openai",
      "model": "deepseek-r1-distill-qwen-1.5b.Q4_K_M.gguf",
      "apiBase": "http://192.168.18.122:11434/v1",
      "apiKey": "dummy"
    }
  ]
}
```

### 通用 OpenAI SDK 调用
```python
from openai import OpenAI

client = OpenAI(
    base_url="http://192.168.18.122:11434/v1",
    api_key="dummy"
)

response = client.chat.completions.create(
    model="deepseek-r1-distill-qwen-1.5b.Q4_K_M.gguf",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

## 测试连通性
```bash
curl http://192.168.18.122:11434/v1/models
curl http://192.168.18.122:11434/health
```

## 注意事项
- 老设备无独立 GPU，纯 CPU 推理，速度约 8-15 tokens/s（1.5B 模型，纯 CPU）
- 8GB 内存限制，建议只运行这一个模型服务
- 如需重启服务，在老设备上运行 `start-llm-server.ps1`

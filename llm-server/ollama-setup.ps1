# Ollama 局域网服务化配置脚本
# 以管理员身份运行 PowerShell 后执行此脚本

Write-Host "=== Ollama 局域网服务化配置 ===" -ForegroundColor Cyan

# 1. 设置环境变量（用户级）
Write-Host "[1/4] 配置环境变量..." -ForegroundColor Yellow
[Environment]::SetEnvironmentVariable("OLLAMA_HOST", "0.0.0.0:11434", "User")
[Environment]::SetEnvironmentVariable("OLLAMA_NUM_THREAD", "4", "User")
Write-Host "  ✓ OLLAMA_HOST = 0.0.0.0:11434"
Write-Host "  ✓ OLLAMA_NUM_THREAD = 4"

# 2. 关闭现有 Ollama 进程
Write-Host "[2/4] 重启 Ollama 服务..." -ForegroundColor Yellow
Stop-Process -Name "ollama" -Force -ErrorAction SilentlyContinue
Start-Sleep -Seconds 2

# 3. 启动 Ollama（后台）
$ollamaPath = "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe"
if (Test-Path $ollamaPath) {
    Start-Process -FilePath $ollamaPath -ArgumentList "serve" -WindowStyle Hidden
    Write-Host "  ✓ Ollama 已启动"
} else {
    Write-Error "未找到 ollama.exe，请确认 Ollama 已安装: $ollamaPath"
    exit 1
}

Start-Sleep -Seconds 3

# 4. 检查端口监听
Write-Host "[3/4] 验证端口监听..." -ForegroundColor Yellow
$listener = netstat -an | Select-String "0.0.0.0:11434"
if ($listener) {
    Write-Host "  ✓ Ollama 正在监听 0.0.0.0:11434"
} else {
    Write-Warning "  ⚠ 未检测到 0.0.0.0:11434 监听，可能仍在启动中"
}

# 5. 防火墙放行
Write-Host "[4/4] 配置防火墙..." -ForegroundColor Yellow
$ruleName = "Ollama-Server-11434"
$existing = Get-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue
if (-not $existing) {
    New-NetFirewallRule -DisplayName $ruleName `
        -Direction Inbound `
        -Protocol TCP `
        -LocalPort 11434 `
        -Action Allow `
        -Profile Any | Out-Null
    Write-Host "  ✓ 防火墙规则已添加: $ruleName"
} else {
    Write-Host "  ✓ 防火墙规则已存在"
}

# 6. 获取本机 IP
$ip = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object { $_.IPAddress -notmatch "^127\." -and $_.IPAddress -notmatch "^169\.254" } | Select-Object -First 1).IPAddress

Write-Host ""
Write-Host "=== 配置完成 ===" -ForegroundColor Green
Write-Host "本机 IP: $ip"
Write-Host "API 端点: http://${ip}:11434"
Write-Host "兼容端点: http://${ip}:11434/v1"
Write-Host ""
Write-Host "接下来可以拉取模型:"
Write-Host "  ollama pull phi3:mini     # 推荐，3.8B，约 2.3GB"
Write-Host "  ollama pull qwen2.5:1.5b  # 中文友好，约 1GB"
Write-Host "  ollama pull llama3.2:1b   # 最快，约 700MB"

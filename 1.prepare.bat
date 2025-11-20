@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

cd /d "%~dp0"

echo ========================================================
echo      📚 批量电子书整合工具 - 环境初始化向导
echo ========================================================
echo.

:: 1. 检查 UV 是否存在
echo [1/3] 正在检查 uv 包管理器...
where uv >nul 2>nul
if %errorlevel% neq 0 (
    echo    -> 未检测到 uv，正在自动安装...
    echo    -> 正在请求 https://astral.sh/uv/install.ps1 ...
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    
    if %errorlevel% neq 0 (
        echo.
        echo [错误] uv 安装失败，请检查网络连接。
        pause
        exit /b
    )
    echo    -> uv 安装完成。
) else (
    echo    -> 检测到 uv 已安装。
)

:: 2. 同步依赖
echo.
echo [2/3] 正在创建虚拟环境并同步依赖 (读取 pyproject.toml)...
echo    -> 这可能需要一点时间下载 PyMuPDF 等库，请耐心等待...
echo.

:: 尝试直接调用 uv，如果刚安装可能不在 PATH 里，这里尝试显式调用
where uv >nul 2>nul
if %errorlevel% neq 0 (
    :: 如果 PATH 还没刷新，尝试使用默认安装路径
    set "UV_PATH=%USERPROFILE%\.cargo\bin\uv.exe"
    if exist "!UV_PATH!" (
        "!UV_PATH!" sync --no-install-project
    ) else (
        echo [警告] 找不到 uv.exe，请尝试关闭此窗口重新运行，或手动重启电脑。
        pause
        exit /b
    )
) else (
    uv sync
)

if %errorlevel% neq 0 (
    echo.
    echo [错误] 依赖同步失败。
    pause
    exit /b
)

echo.
echo [3/3] 环境准备就绪！
echo ========================================================
echo    现在你可以直接双击 "2_启动程序.bat" 来使用了！
echo ========================================================
echo.
pause
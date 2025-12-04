@echo off
cd /d "%~dp0"
chcp 65001 >nul

echo ========================================================
echo  Auto-installing dependencies and starting...
echo  依存関係を自動インストールして起動します...
echo  正在自动检查依赖并启动...
echo ========================================================
echo.

uv run --with Pillow --with natsort image2pdf.py

echo.
echo ========================================================
echo  Done. Press any key to exit.
echo  完了。何かキーを押して終了してください。
echo  运行结束，按任意键退出。
echo ========================================================
pause >nul
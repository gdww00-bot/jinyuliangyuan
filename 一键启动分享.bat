@echo off
title 今遇莨缘官网 - 启动中...
color 0A
echo.
echo  ===================================
echo   今遇莨缘香云纱 官网启动器
echo  ===================================
echo.
echo  [1/2] 正在启动网站服务器...
start "网站服务器" cmd /k "cd /d d:\jinyuliangyuan && npx --yes serve -l 8080 ."
timeout /t 4 /nobreak >nul

echo  [2/2] 正在启动 ngrok 分享隧道...
start "ngrok分享隧道" cmd /k "cd /d d:\jinyuliangyuan && ngrok http 8080"
timeout /t 5 /nobreak >nul

echo.
echo  ✓ 启动完成！
echo.
echo  请查看 ngrok 窗口中的链接（Forwarding 那一行）
echo  把链接发给朋友即可访问官网！
echo.
echo  提示：关闭两个黑色窗口后，朋友将无法访问。
echo.
pause

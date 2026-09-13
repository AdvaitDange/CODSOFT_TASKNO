@echo off
title Launch CodSoft AI in Chrome Browser - Advait Dange
cd /d "%~dp0"
cls
echo ============================================================
echo   Launching CodSoft AI Web Dashboard in Google Chrome...
echo   Developer: Advait Dange
echo   Repository: https://github.com/AdvaitDange/CODSOFT_TASKNO
echo ============================================================
echo.
start "" chrome "%~dp0index.html"
echo Dashboard launched in Chrome!
timeout /t 3 >nul
exit

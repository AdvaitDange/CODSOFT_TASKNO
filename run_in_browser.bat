@echo off
title Launch CodSoft AI in Chrome Browser - Advait Dange
cls
echo ============================================================
echo   Launching CodSoft AI Web Dashboard in Google Chrome...
echo   Developer: Advait Dange
echo   Repository: https://github.com/AdvaitDange/CODSOFT_TASKNO
echo ============================================================
echo.
echo Opening browser at http://localhost:8501 ...
echo Press Ctrl+C in this terminal when you want to stop the server.
echo.
python -m streamlit run web_app.py --browser.serverAddress localhost --server.port 8501
pause

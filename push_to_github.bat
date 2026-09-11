@echo off
title Push CodSoft Tasks to GitHub - Advait Dange
echo ============================================================
echo   Uploading CodSoft AI Tasks to GitHub for Advait Dange
echo   Repository: https://github.com/AdvaitDange/CODSOFT_TASKNO
echo ============================================================
echo.
echo Please ensure you have created the empty repository:
echo   https://github.com/new -> Name: CODSOFT_TASKNO (Public)
echo.
echo Starting git push...
git push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo ============================================================
    echo   SUCCESS! All files uploaded successfully!
    echo   View your repository at:
    echo   https://github.com/AdvaitDange/CODSOFT_TASKNO
    echo ============================================================
) else (
    echo ============================================================
    echo   If you saw an error:
    echo   1. Make sure you created the repo 'CODSOFT_TASKNO' on GitHub.
    echo   2. If prompted, log into GitHub in the browser window.
    echo ============================================================
)
echo.
pause

@echo off
title Push With GitHub Token - Advait Dange
echo ============================================================
echo   Push CodSoft Tasks with Personal Access Token
echo   Account: AdvaitDange
echo   Repository: CODSOFT_TASKNO
echo ============================================================
echo.
set /p TOKEN="Paste your GitHub Personal Access Token (PAT): "
if "%TOKEN%"=="" (
    echo Token cannot be empty.
    pause
    exit /b
)
echo.
echo Pushing to https://github.com/AdvaitDange/CODSOFT_TASKNO.git ...
git push https://AdvaitDange:%TOKEN%@github.com/AdvaitDange/CODSOFT_TASKNO.git main
echo.
pause

@echo off
cd /d "%~dp0"
:menu
cls
title CodSoft AI Internship - Task Launcher (Advait Dange)
echo ============================================================
echo      CodSoft AI Internship - Task Launcher Menu
echo      Developer: Advait Dange
echo      Repository: https://github.com/AdvaitDange/CODSOFT_TASKNO
echo ============================================================
echo.
echo Select which task you want to run:
echo.
echo   [1] Task 1: Rule-Based Chatbot (Terminal Chat)
echo   [2] Task 2: Tic-Tac-Toe AI (Interactive GUI Window - Best for Demo!)
echo   [3] Task 2: Tic-Tac-Toe AI (Terminal Version)
echo   [4] Task 3: Movie Recommendation System (ML Cosine Similarity)
echo   [5] Exit
echo.
set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    cls
    python Task_1_Rule_Based_Chatbot\chatbot.py
    pause
    goto menu
)
if "%choice%"=="2" (
    cls
    echo Starting Tic-Tac-Toe GUI Window...
    python Task_2_Tic_Tac_Toe_AI\tictactoe_gui.py
    goto menu
)
if "%choice%"=="3" (
    cls
    python Task_2_Tic_Tac_Toe_AI\tictactoe_cli.py
    pause
    goto menu
)
if "%choice%"=="4" (
    cls
    python Task_3_Movie_Recommendation_System\recommender.py
    pause
    goto menu
)
if "%choice%"=="5" (
    exit
)

echo Invalid choice, please try again.
timeout /t 2 >nul
goto menu

@echo off
REM Активация виртуального окружения
call .venv\Scripts\activate.bat

REM Запуск uvicorn
uvicorn main:app --reload

REM Ожидание, чтобы окно не закрылось мгновенно
pause

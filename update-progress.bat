@echo off
echo TryHackMe Progress Updater
echo.
set /p rooms=Enter how many rooms you've completed: 
PowerShell -ExecutionPolicy Bypass -File update-progress.ps1 -RoomCount %rooms%
echo.
echo Update complete! Check your progress-tracker.md file.
pause

# Simple Progress Updater
param(
    [int]$RoomCount = 10
)

# Update progress tracker with current date
$Date = Get-Date -Format "yyyy-MM-dd"
Write-Host "Updating progress tracker..." -ForegroundColor Yellow

# Add a new update entry to the progress tracker
$UpdateEntry = "`n*Last update: $Date - Rooms completed: $RoomCount*"
Add-Content -Path "tryhackme\progress-tracker.md" -Value $UpdateEntry

Write-Host "SUCCESS: Progress tracker updated!" -ForegroundColor Green
Write-Host "Rooms completed: $RoomCount" -ForegroundColor Cyan
Write-Host "Date recorded: $Date" -ForegroundColor Yellow

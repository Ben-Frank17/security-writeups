# Simple Progress Updater
param(
    [int]$RoomCount = 10
)

# Update progress tracker date
$Date = Get-Date -Format "yyyy-MM-dd"
Write-Host "Updating progress tracker..." -ForegroundColor Yellow
Add-Content -Path "tryhackme\progress-tracker.md" -Value "`n*Last script update: $Date - Rooms: $RoomCount*"

Write-Host "✅ Progress tracker updated!" -ForegroundColor Green
Write-Host "📊 Room count: $RoomCount" -ForegroundColor Cyan

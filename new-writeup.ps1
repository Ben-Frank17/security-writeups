param(
    [string]$RoomName,
    [string]$Difficulty = "Easy"
)

# Create the writeup file with template
$WriteupContent = @"
# TryHackMe: $RoomName
*Difficulty: $Difficulty*  
*Date Completed: $(Get-Date -Format "yyyy-MM-dd")*

## 🎯 What I Learned
- 
- 
- 

## 🔧 Tools & Commands
- 

## 💡 Real-World Application


*Room completed successfully!*
"@

$SafeFileName = $RoomName -replace " ", "-" -replace "[^a-zA-Z0-9-]", ""
$FilePath = "tryhackme\easy-rooms\$SafeFileName-writeup.md"

$WriteupContent | Out-File -FilePath $FilePath -Encoding UTF8

Write-Host "✅ Writeup template created for: $RoomName" -ForegroundColor Green
Write-Host "📁 Location: $FilePath" -ForegroundColor Cyan
Write-Host "✏️  Open the file and fill in your learnings!" -ForegroundColor Yellow

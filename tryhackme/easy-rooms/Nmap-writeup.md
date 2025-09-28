# TryHackMe: Nmap
*Difficulty: Easy*  
*Date Completed: $(Get-Date -Format "yyyy-MM-dd")*

## 🎯 What I Learned
- Different Nmap scan types and when to use them
- How to read and interpret Nmap output
- Service version detection and OS fingerprinting
- Script scanning with NSE (Nmap Scripting Engine)

## 🔧 Tools & Commands
- nmap -sS [target] - Stealth SYN scan
- nmap -sV [target] - Service version detection  
- nmap -O [target] - OS fingerprinting
- nmap -sC [target] - Default script scan
- nmap -p- [target] - Scan all ports

## 💡 Real-World Application
Nmap is essential for network reconnaissance in penetration testing - understanding what services are running helps identify potential attack vectors.

*Mastering Nmap is foundational for any cybersecurity professional!*

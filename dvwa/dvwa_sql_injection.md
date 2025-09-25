# DVWA — SQL Injection (low)

**Target:** http://127.0.0.1/dvwa/vulnerabilities/sqli/  
**Date:** 2025-09-25  
**Severity:** Low

## PoC
Payload used: 1' OR '1'='1
explorer "C:\Users\beckb\Documents\security-writeups\dvwa"
# Paths
C:\Users\beckb\Documents\security-writeups = "C:\Users\beckb\Documents\security-writeups"
C:\Users\beckb\Documents\security-writeups\dvwa = Join-Path C:\Users\beckb\Documents\security-writeups "dvwa"
C:\Users\beckb\Pictures\ORCID.png = "C:\Users\beckb\Pictures\Screenshots\dvwa_sqli.png"  # your file

# Create folder and copy screenshot
New-Item -ItemType Directory -Path C:\Users\beckb\Documents\security-writeups\dvwa -Force | Out-Null
if (-Not (Test-Path C:\Users\beckb\Pictures\ORCID.png)) { Write-Host "ERROR: source not found: C:\Users\beckb\Pictures\ORCID.png"; exit 1 }
Copy-Item C:\Users\beckb\Pictures\ORCID.png -Destination (Join-Path C:\Users\beckb\Documents\security-writeups\dvwa "dvwa_sqli.png") -Force
Write-Host "Copied screenshot -> C:\Users\beckb\Documents\security-writeups\dvwa\dvwa_sqli.png"

# Create markdown writeup
 = @"
# DVWA — SQL Injection (low)

**Target:** http://127.0.0.1/dvwa/vulnerabilities/sqli/  
**Date:** 2025-09-25  
**Severity:** Low

## PoC
Payload used: 1' OR '1'='1  
Reproduction steps:
1. Open DVWA → Vulnerabilities → SQL Injection.
2. Enter payload into User ID field and click Submit.
3. Multiple user rows are returned showing successful injection. (see screenshot)

![dvwa_sqli](dvwa_sqli.png)

## Commands & outputs
- nmap scan: dvwa_nmap.txt  
- ffuf results: fuf.json  
- sqlmap dump: sqlmap_output/

## Impact
Remote unauthenticated SQL injection allows disclosure of database rows.

## Fix
Use prepared statements / parameterized queries and strict input validation.

## Notes
Lab target. No real systems tested.

# DVWA — Command Injection (low)

**Target:** http://127.0.0.1/dvwa/vulnerabilities/exec/  
**Date:** 2025-09-26  
**Severity:** Low

## Summary
A command injection vulnerability allows unsanitized user input to be executed by the server shell. This lab demonstrates remote command execution in a controlled environment.

## PoC (reproducible)
**Payload:** `127.0.0.1 && whoami`  
**Steps**
1. Login to DVWA (`admin` / `password`) and set Security = **low**.  
2. Navigate to **Vulnerabilities → Command Injection**.  
3. Enter the payload in the IP field and click **Submit**.  
4. The application executes the shell command and returns the `whoami` output `veritaspc\beckb`. (see screenshot)

**Evidence**
- Screenshot: `dvwa_cmd_injection.png` (shows `veritaspc\beckb`).

## Technical notes
The application passes user input directly to a shell without proper sanitization or whitelisting. This enables command chaining and arbitrary command execution.

## Impact
An attacker able to reach this endpoint can execute arbitrary OS commands as the web server user. This can lead to system compromise, data exposure, or privilege escalation depending on server configuration.

## Remediation (developer-ready)
1. Do not pass raw user input to shell commands. Use safe APIs that avoid shell interpretation.  
2. Implement strict input validation with a whitelist of allowed values (e.g., IP-only regex).  
3. Run any required commands in a restricted, non-privileged environment and drop privileges.  
4. Add monitoring and alerting for unexpected command execution patterns.

## Retest
After fixes, retest using the same payload. Verify the server does not execute the command and returns a safe validation error.

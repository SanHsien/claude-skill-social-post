[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repoRoot

$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
if (Test-Path -LiteralPath $venvPython) {
    $pythonExe = $venvPython
} else {
    $pythonExe = (Get-Command python -ErrorAction Stop).Source
}

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

function Invoke-Step {
    param(
        [Parameter(Mandatory)]
        [string]$Label,
        [Parameter(Mandatory)]
        [string]$Command,
        [Parameter(Mandatory)]
        [string[]]$Arguments
    )

    Write-Host "==> $Label"
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Label failed with exit code $LASTEXITCODE"
    }
}

Invoke-Step -Label "1. Product self_test" -Command $pythonExe -Arguments @(
    "social-post\scripts\self_test.py"
)
Invoke-Step -Label "2. Social data validation" -Command $pythonExe -Arguments @(
    "social-post\scripts\social_data.py", "validate"
)
Invoke-Step -Label "3. Social data coverage" -Command $pythonExe -Arguments @(
    "social-post\scripts\social_data.py", "coverage"
)
Invoke-Step -Label "4. Comment assistant validation" -Command $pythonExe -Arguments @(
    "social-post\scripts\comment_assistant.py", "validate"
)
Invoke-Step -Label "5. Comment capability gate" -Command $pythonExe -Arguments @(
    "social-post\scripts\comment_capability_gate.py"
)
Invoke-Step -Label "6. Chrome actuator test (Node)" -Command "node" -Arguments @(
    "social-post\scripts\comment_chrome_actuator_test.mjs"
)
Invoke-Step -Label "7. Chrome claim bridge test (Node)" -Command "node" -Arguments @(
    "social-post\scripts\comment_chrome_claim_bridge_test.mjs"
)
Invoke-Step -Label "8. Chrome claim integration test (Node)" -Command "node" -Arguments @(
    "social-post\scripts\comment_chrome_claim_integration_test.mjs"
)
Invoke-Step -Label "9. Comment JS architecture gate (Node)" -Command "node" -Arguments @(
    "social-post\scripts\comment_js_architecture_gate.mjs", "--self-test"
)

Write-Host "ALL PRODUCT AND ADAPTER TESTS GREEN"
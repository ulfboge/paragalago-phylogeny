# Resolve Google Docs edit URL from a local .gdoc placeholder and update manuscript/GOOGLE_DOC.md
param(
    [string]$GdocPath = "G:\My Drive\Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago).gdoc",
    [string]$RepoRoot = (Split-Path $PSScriptRoot -Parent)
)

$targetFile = Join-Path $RepoRoot "manuscript\GOOGLE_DOC.md"
if (-not (Test-Path -LiteralPath $GdocPath)) {
    Write-Error "Gdoc not found: $GdocPath"
    exit 1
}

try {
    $json = Get-Content -LiteralPath $GdocPath -Raw -Encoding UTF8 | ConvertFrom-Json
} catch {
    Write-Error @"
Could not read .gdoc placeholder (file may be cloud-only).
Open the manuscript in Google Docs, copy the edit URL, and paste it into:
  $targetFile
"@
    exit 1
}

if (-not $json.doc_id) {
    Write-Error "No doc_id found in .gdoc file."
    exit 1
}

$editUrl = "https://docs.google.com/document/d/$($json.doc_id)/edit"
$viewUrl = "https://docs.google.com/document/d/$($json.doc_id)/view"

$content = Get-Content -LiteralPath $targetFile -Raw -Encoding UTF8
$linkPattern = '\[Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos \(Paragalago\)\]\([^)]+\)'
$replacement = "[Multilocus Species-Tree Reconstruction Reveals Deep Lineage Structure in East African Dwarf Galagos (Paragalago)]($editUrl)"

if ($content -match $linkPattern) {
    $content = [regex]::Replace($content, $linkPattern, $replacement)
} else {
    Write-Warning "Link pattern not found; appending direct URL."
    $content += "`n`n**Direct edit link:** $editUrl`n"
}

$content = $content -replace '(?s)> \*\*Tip:\*\* Once you have the direct link.*', "> **Direct link (auto-resolved):** [$editUrl]($editUrl)"

Set-Content -LiteralPath $targetFile -Value $content -Encoding UTF8 -NoNewline
Write-Host "Updated manuscript link:"
Write-Host "  Edit: $editUrl"
Write-Host "  View: $viewUrl"

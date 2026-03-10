$baseDir = 'g:\bjir\tugas peting\fun offroad batu malang coban talun'

# Find all HTML files
$htmlFiles = Get-ChildItem -Path $baseDir -Filter *.html

$replacements = @{}

for ($i = 2; $i -le 9; $i++) {
    $oldName = "blog-$i.html"
    $filePath = Join-Path $baseDir $oldName
    
    if (Test-Path $filePath) {
        $content = Get-Content $filePath -Raw
        
        # Get h1
        if ($content -match '<h1>(.*?)</h1>') {
            $h1 = $matches[1].Trim()
            
            # Remove invalid Windows chars
            $h1Sanitized = $h1 -replace '[\\/*?:"<>|]', ''
            $newName = "$h1Sanitized.html"
            
            $replacements[$oldName] = $newName
        }
    }
}

$replacements.GetEnumerator() | ForEach-Object {
    Write-Host "Will replace/rename $($_.Name) -> $($_.Value)"
}

# Add blog-1 replacement logic too
$replacements["blog-1.html"] = "5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html"

# 1. Update all files with new links
# Wait, also replace in .py, .xml, .txt
$allFiles = Get-ChildItem -Path $baseDir -Include *.html,*.py,*.xml,*.txt -Recurse

foreach ($file in $allFiles) {
    # Skip directories or script itself
    if ($file.PSIsContainer -or $file.Name -eq "rename.ps1") { continue }
    
    $fileContent = Get-Content $file.FullName -Raw
    $newContent = $fileContent
    $changed = $false
    
    foreach ($kv in $replacements.GetEnumerator()) {
        $old = $kv.Name
        $new = $kv.Value
        
        # For XML encode spaces as %20
        if ($file.Extension -eq '.xml') {
            $new = $new -replace ' ', '%20'
        }
        
        if ($newContent -match [regex]::Escape($old)) {
            $newContent = $newContent -replace [regex]::Escape($old), $new
            $changed = $true
        }
    }
    
    if ($changed) {
        Set-Content -Path $file.FullName -Value $newContent -Encoding UTF8
        Write-Host "Updated references in $($file.Name)"
    }
}

# 2. Rename files
foreach ($kv in $replacements.GetEnumerator()) {
    $old = $kv.Name
    $new = $kv.Value
    
    # Don't try to rename blog-1.html if it's already renamed
    $oldPath = Join-Path $baseDir $old
    $newPath = Join-Path $baseDir $new
    
    if (Test-Path $oldPath) {
        if (-not (Test-Path $newPath)) {
            Rename-Item -Path $oldPath -NewName $new
            Write-Host "Renamed $old -> $new"
        }
    }
}

Write-Host "Done."

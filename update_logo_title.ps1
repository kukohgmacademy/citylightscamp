$directory = "."
$htmlFiles = Get-ChildItem -Path $directory -Filter *.html

foreach ($file in $htmlFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    # Navbar replace
    $content = $content -replace 'Batu <span>Sunrise</span>', 'citylights<span>camp</span>'

    # Footer replace
    $content = [regex]::Replace($content, 'Batu\s*<span style="color: var\(--primary\);">Sunrise</span>', "citylights`r`n                        <span style=""color: var(--primary);"">camp</span>")

    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}

Write-Host "Update title complete for $($htmlFiles.Count) HTML files."

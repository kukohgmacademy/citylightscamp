$directory = "."
$htmlFiles = Get-ChildItem -Path $directory -Filter *.html

foreach ($file in $htmlFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $content = $content.Replace('`r`n', "`r`n")
    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}

Write-Host "Fix complete."

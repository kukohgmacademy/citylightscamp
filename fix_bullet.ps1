$files = Get-ChildItem -Filter "*.html"
foreach ($f in $files) {
    if ($f.Name -eq "template.html") { continue }
    $c = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $c = $c.Replace("â€¢", "•")
    [System.IO.File]::WriteAllText($f.FullName, $c, [System.Text.Encoding]::UTF8)
}
Write-Host "Done"

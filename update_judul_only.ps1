$baseDir = 'g:\bjir\tugas peting\fun offroad batu malang coban talun'
$htmlFiles = Get-ChildItem -Path $baseDir -Filter *.html

foreach ($file in $htmlFiles) {
    if (Test-Path $file.FullName) {
        $content = Get-Content $file.FullName -Raw
        
        # Replace occurrences inside <title> tags using regex matcher
        $content = [regex]::Replace($content, '(?i)<title>(.*?)</title>', {
            param($match)
            $oldTitle = $match.Groups[1].Value
            
            # Replace the brand names within the title
            $newTitle = $oldTitle -replace 'Review Jujur Paket Camping Batu Malang|Camping Batu Malang', 'Citylightscamp'
            
            # If nothing was replaced and it doesn't already have a pipe |
            if ($newTitle -eq $oldTitle -and $newTitle -notmatch '\|') {
               $newTitle = "$newTitle | Citylightscamp"
            }
            # Special case for index
            if ($file.Name -eq 'index.html') {
                $newTitle = "Citylightscamp"
            }
            
            return "<title>$newTitle</title>"
        })

        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Updated title strings in: $($file.Name)"
    }
}
Write-Host "Done"

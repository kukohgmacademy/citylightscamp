$baseDir = 'g:\bjir\tugas peting\fun offroad batu malang coban talun'
for ($i=1; $i -le 9; $i++) {
    $filePath = Join-Path $baseDir ("blog-$i.html")
    if (Test-Path $filePath) {
        $content = Get-Content $filePath -Raw
        
        # Parse out the <h1> content
        if ($content -match '<h1>(.*?)</h1>') {
            $h1 = $matches[1]
            
            # Replace the <title> tag entirely
            $content = $content -replace '(?i)<title>.*?</title>', "<title>$h1</title>"
            
            # Replace og:title
            $content = $content -replace '(?i)<meta property="og:title" content=".*?">', "<meta property=`"og:title`" content=`"$h1`">"
            
            # Replace twitter:title
            $content = $content -replace '(?i)<meta name="twitter:title" content=".*?">', "<meta name=`"twitter:title`" content=`"$h1`">"
            
            # Replace schema headline
            $content = $content -replace '(?i)"headline": ".*?"', "`"headline`": `"$h1`""
            
            Set-Content -Path $filePath -Value $content -Encoding UTF8
            Write-Host "Updated title for blog-$i to: $h1"
        }
    }
}

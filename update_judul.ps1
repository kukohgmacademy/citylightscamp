$baseDir = 'g:\bjir\tugas peting\fun offroad batu malang coban talun'
$htmlFiles = Get-ChildItem -Path $baseDir -Filter *.html

foreach ($file in $htmlFiles) {
    $content = Get-Content $file.FullName -Raw
    
    # Simple regex replace for titles containing the old phrases
    $content = $content -replace "Review Jujur Paket Camping Batu Malang", "Citylightscamp"
    $content = $content -replace "Camping Batu Malang", "Citylightscamp"

    # For files where we only put the H1 without any suffix, let's append " | Citylightscamp" 
    # if it's not already there.
    if ($file.Name -match "^(5 Barang|3 Spot|Amankah|Keseruan|Waktu|Mengenal|Review|Cara|7 Keuntungan)") {
        $content = $content -replace '(?i)<title>(.*?)</title>', '<title>$1 | Citylightscamp</title>'
    }

    # Special handling for index.html title
    if ($file.Name -eq 'index.html') {
        $content = $content -replace '(?i)<title>.*?</title>', '<title>Citylightscamp</title>'
    }

    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
    Write-Host "Updated title strings in: $($file.Name)"
}
Write-Host "Done"

$dict = @{
    "5-Barang-Wajib-Bawa-Saat-Paket-Camping-di-Coban-Talun.html" = "Tips & Trik &bull; 10 Mar 2026"
    "3-Spot-Foto-Paling-Instagramable-di-Area-Camping.html" = "Destinasi &bull; 10 Mar 2026"
    "Amankah-Paket-Camping-Untuk-Anak-anak-dan-Keluarga.html" = "Family Liburan &bull; 10 Mar 2026"
    "Keseruan-BBQ-dan-Api-Unggun-di-Camping-Batu-Malang.html" = "Kuliner & Aktivitas &bull; 10 Mar 2026"
    "Waktu-Terbaik-untuk-Camping-Menikmati-City-Light-Batu-Malang.html" = "Tips & Panduan &bull; 10 Mar 2026"
    "Mengenal-Keunggulan-Sewa-Tenda-Premium-Batu-Malang.html" = "Review Perlengkapan &bull; 10 Mar 2026"
    "Review-Jujur-Jeep-Offroad-Coban-Talun-Batu.html" = "Destinasi &bull; 10 Mar 2026"
    "Cara-Booking-Paket-Camping-Batu-Malang-Paling-Mudah.html" = "Panduan &bull; 10 Mar 2026"
    "7-Keuntungan-Memilih-Paket-Camping-VIP.html" = "Tips & Trik &bull; 10 Mar 2026"
    "Tidur-di-Bawah-Ribuan-Lampu-Intip-Serunya-Pengalaman.html" = "Pengalaman &bull; 11 Mar 2026"
    "Kenapa-Citylightscamp-Adalah-Terapi-Visual-Terbaik.html" = "Review & Opini &bull; 11 Mar 2026"
}

$files = Get-ChildItem -Filter "*.html"
foreach ($file in $files) {
    if ($file.Name -eq "template.html") { continue }
    
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    
    foreach ($key in $dict.Keys) {
        $replacement = $dict[$key]
        # Match <div style="...">...</div> whitespace <h3><a href="KEY"
        $pattern = "<div style=`"color: var\(--primary\); font-size: 0\.9rem; margin-bottom: 10px;`">.*?</div>(\s*<h3>\s*<a href=`"$key`")"
        $replaceString = "<div style=`"color: var(--primary); font-size: 0.9rem; margin-bottom: 10px;`">$replacement</div>`$1"
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, $pattern, $replaceString, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase -bor [System.Text.RegularExpressions.RegexOptions]::Singleline)
    }

    # Fix the post meta inside the article itself
    if ($dict.ContainsKey($file.Name)) {
        $postMeta = $dict[$file.Name].Replace("&bull;", "•")
        $pattern2 = "<p class=`"post-meta`">.*?</p>"
        $replaceString2 = "<p class=`"post-meta`">$postMeta</p>"
        $content = [System.Text.RegularExpressions.Regex]::Replace($content, $pattern2, $replaceString2, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase -bor [System.Text.RegularExpressions.RegexOptions]::Singleline)
    }

    if ($originalContent -ne $content) {
        [System.IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($file.Name)"
    }
}
Write-Host "Done"

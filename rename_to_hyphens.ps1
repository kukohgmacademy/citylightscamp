$base_dir = "g:\bjir\tugas peting\fun offroad batu malang coban talun"
$files = Get-ChildItem -Path $base_dir -Include *.html, *.xml -Recurse

$titles = @(
    "3 Spot Foto Paling Instagramable di Area Camping.html",
    "5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html",
    "7 Keuntungan Memilih Paket Camping VIP.html",
    "Amankah Paket Camping Untuk Anak-anak dan Keluarga.html",
    "Cara Booking Paket Camping Batu Malang Paling Mudah.html",
    "Keseruan BBQ dan Api Unggun di Camping Batu Malang.html",
    "Mengenal Keunggulan Sewa Tenda Premium Batu Malang.html",
    "Review Jujur Jeep Offroad Coban Talun Batu.html",
    "Waktu Terbaik untuk Camping Menikmati City Light Batu Malang.html"
)

# 1. Update references
foreach ($file in $files) {
    if ($file.Extension -notin @(".html", ".xml")) { continue }

    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $new_content = $content
    $changed = $false

    foreach ($title in $titles) {
        $hyphenated = $title -replace " ", "-"
        
        if ($new_content -like "*$title*") {
            $new_content = $new_content.Replace($title, $hyphenated)
            $changed = $true
        }

        $url_encoded = $title -replace " ", "%20"
        if ($new_content -like "*$url_encoded*") {
            $new_content = $new_content.Replace($url_encoded, $hyphenated)
            $changed = $true
        }
    }

    if ($changed) {
        Set-Content -Path $file.FullName -Value $new_content -Encoding UTF8
        Write-Host "Updated references in $($file.Name)"
    }
}

# 2. Rename files
$html_files = Get-ChildItem -Path $base_dir -Filter *.html
foreach ($file in $html_files) {
    if ($file.Name -match " ") {
        $new_name = $file.Name -replace " ", "-"
        Rename-Item -Path $file.FullName -NewName $new_name
        Write-Host "Renamed $($file.Name) to $new_name"
    }
}

Write-Host "Done"

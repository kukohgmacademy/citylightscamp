$directory = "."
$htmlFiles = Get-ChildItem -Path $directory -Filter *.html

foreach ($file in $htmlFiles) {
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    # 1. Update Domain
    $content = $content -replace 'https://campingbatu\.com/', 'https://citylightscamp.web.id/'
    $content = $content -replace 'https://campingbatu\.com', 'https://citylightscamp.web.id'
    $content = $content -replace 'http://campingbatu\.com', 'https://citylightscamp.web.id'
    $content = $content -replace 'campingbatu\.com', 'citylightscamp.web.id'

    # 2. Update Robots for SEO & AEO
    if ($content -notmatch 'max-image-preview:large' -and $content -match '<meta name="robots" content="index, follow">') {
        $content = $content -replace '<meta name="robots" content="index, follow">', '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">`r`n    <meta name="googlebot" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">`r`n    <meta name="bingbot" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">'
    }

    # 3. Enhanced Pagespeed (DNS Prefetch)
    if ($content -notmatch '<link rel="dns-prefetch" href="https://fonts\.googleapis\.com">' -and $content -match '<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>') {
        $content = $content -replace '<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>', '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`r`n    <link rel="dns-prefetch" href="https://fonts.googleapis.com">`r`n    <link rel="dns-prefetch" href="https://fonts.gstatic.com">'
    }

    # 4. Favicon - Add webmanifest
    if ($content -notmatch '<link rel="manifest" href="site\.webmanifest">' -and $content -match '<meta name="theme-color" content="#f26422">') {
        $content = $content -replace '<meta name="theme-color" content="#f26422">', '<link rel="manifest" href="site.webmanifest">`r`n    <meta name="theme-color" content="#f26422">'
    }

    # Add extra Apple Touch icons if missing
    if ($content -match '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon\.png">' -and $content -notmatch '<link rel="apple-touch-icon" sizes="152x152"') {
        $content = $content -replace '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon\.png">', '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">`r`n    <link rel="apple-touch-icon" sizes="152x152" href="apple-touch-icon.png">`r`n    <link rel="apple-touch-icon" sizes="120x120" href="apple-touch-icon.png">'
    }

    # 5. OpenGraph Enhancements
    if ($content -notmatch '<meta property="og:site_name"' -and $content -match '<!-- Twitter Card -->') {
        $content = $content -replace '<!-- Twitter Card -->', '<meta property="og:site_name" content="Citylightscamp">`r`n    <meta property="og:locale" content="id_ID">`r`n    <meta property="og:image:width" content="1200">`r`n    <meta property="og:image:height" content="630">`r`n`r`n    <!-- Twitter Card -->'
    }

    # 6. Twitter Card Enhancements
    if ($content -notmatch '<meta name="twitter:site"' -and $content -match '<!-- Schema Markup \(JSON-LD\) khusus AI Overview -->') {
        $content = $content -replace '<!-- Schema Markup \(JSON-LD\) khusus AI Overview -->', '<meta name="twitter:site" content="@Citylightscamp">`r`n    <meta name="twitter:creator" content="@Citylightscamp">`r`n`r`n    <!-- Schema Markup (JSON-LD) khusus AI Overview -->'
    }

    # 7. Add GEO/AEO Publisher info
    if ($content -notmatch '<meta name="distribution" content="global">' -and $content -match '<meta name="author"') {
        $content = [regex]::Replace($content, '(<meta name="author" content="[^"]+">)', '$1`r`n    <meta name="publisher" content="Citylightscamp">`r`n    <meta name="distribution" content="global">`r`n    <meta name="geo.region" content="ID-JI">`r`n    <meta name="geo.placename" content="Batu">`r`n    <meta name="geo.position" content="-7.8671;112.5239">`r`n    <meta name="ICBM" content="-7.8671, 112.5239">')
    }

    Set-Content -Path $file.FullName -Value $content -Encoding UTF8
}

Write-Host "Update complete for $($htmlFiles.Count) HTML files."

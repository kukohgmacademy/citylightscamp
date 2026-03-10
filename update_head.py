import os
import glob
import re

directory = "g:/bjir/tugas peting/fun offroad batu malang coban talun"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # 1. Update Domain
    content = content.replace("https://campingbatu.com/", "https://citylightscamp.web.id/")
    content = content.replace("https://campingbatu.com", "https://citylightscamp.web.id")
    content = content.replace("http://campingbatu.com", "https://citylightscamp.web.id")
    content = content.replace("campingbatu.com", "citylightscamp.web.id")

    # 2. Update Robots for SEO & AEO
    if "max-image-preview:large" not in content and '<meta name="robots" content="index, follow">' in content:
        content = content.replace(
            '<meta name="robots" content="index, follow">',
            '<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">\n    <meta name="googlebot" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">\n    <meta name="bingbot" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">'
        )

    # 3. Enhanced Pagespeed (DNS Prefetch)
    if '<link rel="dns-prefetch" href="https://fonts.googleapis.com">' not in content and '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>' in content:
        content = content.replace(
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n    <link rel="dns-prefetch" href="https://fonts.googleapis.com">\n    <link rel="dns-prefetch" href="https://fonts.gstatic.com">'
        )
    
    # 4. Favicon - Add webmanifest
    if '<link rel="manifest" href="site.webmanifest">' not in content and '<meta name="theme-color" content="#f26422">' in content:
        content = content.replace(
            '<meta name="theme-color" content="#f26422">',
            '<link rel="manifest" href="site.webmanifest">\n    <meta name="theme-color" content="#f26422">'
        )

    # Add extra Apple Touch icons if missing
    if '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">' in content and '<link rel="apple-touch-icon" sizes="152x152"' not in content:
        content = content.replace(
            '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">',
            '<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">\n    <link rel="apple-touch-icon" sizes="152x152" href="apple-touch-icon.png">\n    <link rel="apple-touch-icon" sizes="120x120" href="apple-touch-icon.png">'
        )

    # 5. OpenGraph Enhancements
    if '<meta property="og:site_name"' not in content and '<!-- Twitter Card -->' in content:
        content = content.replace(
            '<!-- Twitter Card -->',
            '<meta property="og:site_name" content="Citylightscamp">\n    <meta property="og:locale" content="id_ID">\n    <meta property="og:image:width" content="1200">\n    <meta property="og:image:height" content="630">\n\n    <!-- Twitter Card -->'
        )
        
    # 6. Twitter Card Enhancements
    if '<meta name="twitter:site"' not in content and '<!-- Schema Markup (JSON-LD) khusus AI Overview -->' in content:
        content = content.replace(
            '<!-- Schema Markup (JSON-LD) khusus AI Overview -->',
            '<meta name="twitter:site" content="@Citylightscamp">\n    <meta name="twitter:creator" content="@Citylightscamp">\n\n    <!-- Schema Markup (JSON-LD) khusus AI Overview -->'
        )

    # 7. Add GEO/AEO Publisher info
    if '<meta name="distribution" content="global">' not in content and '<meta name="author"' in content:
        content = re.sub(
            r'(<meta name="author" content="[^"]+">)',
            r'\1\n    <meta name="publisher" content="Citylightscamp">\n    <meta name="distribution" content="global">\n    <meta name="geo.region" content="ID-JI">\n    <meta name="geo.placename" content="Batu">\n    <meta name="geo.position" content="-7.8671;112.5239">\n    <meta name="ICBM" content="-7.8671, 112.5239">',
            content
        )

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print(f"Update complete for {len(html_files)} HTML files.")

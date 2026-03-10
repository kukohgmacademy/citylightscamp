import os
import re

base_dir = r"g:\bjir\tugas peting\fun offroad batu malang coban talun"
files_to_update = ["paket.html", "about.html", "fasilitas.html"]

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # 1. html lang
    if '<html lang="id">' in content:
        content = content.replace('<html lang="id">', '<html lang="id-ID">')
        changed = True

    # 2. Add Floating WA Button
    if 'class="floating-wa"' not in content:
        wa_pattern = r'(<!-- Back to top button -->\s*<button id="backToTop".*?</button>)'
        wa_replacement = r'\1\n\n    <!-- Floating WA Button (Pengecualian Struktural) -->\n    <a href="https://wa.me/6281239225692?text=Halo%20Admin%20Camping%20Batu,%20saya%20ingin%20info%20lebih%20lanjut."\n        class="floating-wa" target="_blank" rel="noopener noreferrer" aria-label="Hubungi kami di WhatsApp">\n        <i class="fab fa-whatsapp"></i>\n    </a>'
        new_content = re.sub(wa_pattern, wa_replacement, content, flags=re.DOTALL)
        if new_content != content:
            content = new_content
            changed = True

    # 3. Media print fonts
    if 'media="print"' not in content:
        font_pattern = r'(<link[^>]*href="https://fonts\.googleapis\.com/css2[^>]+>)'
        font_repl = r'\1 media="print" onload="this.media=\'all\'">\n    <noscript>\1</noscript>'
        content = re.sub(font_pattern, font_repl, content)

        fa_pattern = r'(<link[^>]*href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome[^>]+>)'
        fa_repl = r'\1 media="print" onload="this.media=\'all\'">\n    <noscript>\1</noscript>'
        content = re.sub(fa_pattern, fa_repl, content)
        changed = True
        
    # 4. script defer
    if '<script src="assets/js/scripts.js"></script>' in content:
        content = content.replace('<script src="assets/js/scripts.js"></script>', '<script src="assets/js/scripts.js" defer></script>')
        changed = True

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes needed for {filename}")

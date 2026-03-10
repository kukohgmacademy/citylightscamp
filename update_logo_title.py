import os
import glob
import re

directory = "g:/bjir/tugas peting/fun offroad batu malang coban talun"
html_files = glob.glob(os.path.join(directory, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace in Navbar
    content = re.sub(r'Batu <span>Sunrise</span>', r'citylights<span>camp</span>', content)

    # Replace in Footer
    # Since there are multiple lines and spaces, use a regex
    content = re.sub(
        r'Batu\s*<span style="color: var\(--primary\);">Sunrise</span>',
        r'citylights\n                        <span style="color: var(--primary);">camp</span>',
        content
    )

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

print(f"Update complete for {len(html_files)} HTML files.")

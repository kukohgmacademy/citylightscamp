import os
import re

base_dir = r"g:\bjir\tugas peting\fun offroad batu malang coban talun"

for filename in os.listdir(base_dir):
    if filename.endswith(".html") and filename != "fasilitas.html":
        filepath = os.path.join(base_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # We look for <a href="paket.html"*>Paket</a>
        # and we replace it by appending <a href="fasilitas.html">Fasilitas</a> if it's not already there.
        if "fasilitas.html" not in content:
            # Match <a href="paket.html".*?>Paket</a> or <a href="#packages">Paket</a>
            pattern = r'(<a href="paket\.html"[^>]*>Paket</a>|<a href="#packages"[^>]*>Paket</a>)'
            # We want to keep the matched string, then add \n            <a href="fasilitas.html">Fasilitas</a>
            replacement = r'\1\n            <a href="fasilitas.html">Fasilitas</a>'
            
            new_content = re.sub(pattern, replacement, content)
            
            if content != new_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated navbar in {filename}")

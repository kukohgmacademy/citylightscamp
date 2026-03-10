import os
import re
import glob

base_dir = r"g:\bjir\tugas peting\fun offroad batu malang coban talun"

def sanitize_filename(name):
    # Remove invalid Windows characters
    return re.sub(r'[\\/*?:"<>|]', "", name)

# Get all html files
html_files = glob.glob(os.path.join(base_dir, "*.html"))

replacements = {}

# Discover file renames
for i in range(2, 10):
    old_filename = f"blog-{i}.html"
    filepath = os.path.join(base_dir, old_filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Get h1
        h1_match = re.search(r'<h1>(.*?)</h1>', content)
        if h1_match:
            h1 = h1_match.group(1).strip()
            new_filename = sanitize_filename(h1) + ".html"
            replacements[old_filename] = new_filename

print("Renames to execute:", replacements)

# 1. Update all HTML files with new links
# We also have 5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html changed to "5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html" 
# Oh wait, we should check if we need to replace 5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html too!
for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
        
    new_content = content
    # For 5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html we can also do a replace if we find it
    new_content = new_content.replace('5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html', '5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html')
    
    for old_name, new_name in replacements.items():
        new_content = new_content.replace(old_name, new_name)
        new_content = new_content.replace(f"/{old_name}", f"/{new_name}") # in case of absolute URLs
        
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated references in {os.path.basename(file)}")

# 2. Rename files
for old_name, new_name in replacements.items():
    old_path = os.path.join(base_dir, old_name)
    new_path = os.path.join(base_dir, new_name)
    if os.path.exists(old_path) and not os.path.exists(new_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} -> {new_name}")

# Also update python and xml files if necessary
other_files = glob.glob(os.path.join(base_dir, "*.xml")) + glob.glob(os.path.join(base_dir, "*.py")) + glob.glob(os.path.join(base_dir, "*.txt"))
for file in other_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = content
    new_content = new_content.replace('5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html', '5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html')
    for old_name, new_name in replacements.items():
        new_content = new_content.replace(old_name, urllib.parse.quote(new_name) if file.endswith('.xml') else new_name)
    if new_content != content:
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated references in {os.path.basename(file)}")

print("Done.")


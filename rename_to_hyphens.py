import os
import glob
import urllib.parse

base_dir = r"g:\bjir\tugas peting\fun offroad batu malang coban talun"

html_files = glob.glob(os.path.join(base_dir, "*.html"))
xml_files = glob.glob(os.path.join(base_dir, "*.xml"))
all_files = html_files + xml_files

# Create a mapping of current filename to intended hyphenated filename
renames = {}
files_with_spaces_in_links = [
    "3 Spot Foto Paling Instagramable di Area Camping.html",
    "5 Barang Wajib Bawa Saat Paket Camping di Coban Talun.html",
    "7 Keuntungan Memilih Paket Camping VIP.html",
    "Amankah Paket Camping Untuk Anak-anak dan Keluarga.html",
    "Cara Booking Paket Camping Batu Malang Paling Mudah.html",
    "Keseruan BBQ dan Api Unggun di Camping Batu Malang.html",
    "Mengenal Keunggulan Sewa Tenda Premium Batu Malang.html",
    "Review Jujur Jeep Offroad Coban Talun Batu.html",
    "Waktu Terbaik untuk Camping Menikmati City Light Batu Malang.html"
]

all_blog_titles = []
for name in files_with_spaces_in_links:
    hyphenated = name.replace(' ', '-')
    all_blog_titles.append((name, hyphenated))

print("Processing space-to-hyphen substitutions:")

# 1. Update references in all files
for filepath in all_files:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content
    for old_name, new_name in all_blog_titles:
        # Replace normal space names with hyphenated names
        new_content = new_content.replace(old_name, new_name)
        # Also handle %20
        old_url_encoded = old_name.replace(' ', '%20')
        new_content = new_content.replace(old_url_encoded, new_name)
        
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated references in {os.path.basename(filepath)}")

# 2. Rename files on disk
for filepath in html_files:
    filename = os.path.basename(filepath)
    if ' ' in filename:
        new_filename = filename.replace(' ', '-')
        old_path = filepath
        new_path = os.path.join(base_dir, new_filename)
        
        if os.path.exists(old_path) and not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Renamed {filename} -> {new_filename}")

print("Done.")

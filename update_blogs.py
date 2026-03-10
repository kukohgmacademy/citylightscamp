import os
import re

cards = {
    1: """            <div class="card">
                <div class="card-img">
                    <img src="img/b3.webp" alt="Persiapan Camping" loading="lazy" decoding="async" width="800" height="auto">
                </div>
                <div class="card-content">
                    <div style="color: var(--primary); font-size: 0.9rem; margin-bottom: 10px;">Tips & Trik &bull; 25 Feb 2026</div>
                    <h3><a href="blog-1.html" style="color: #fff;">5 Barang Wajib Bawa Saat Paket Camping di Coban Talun</a></h3>
                    <p>Pastikan pengalaman campingmu bebas hambatan dan siap menghadapi lokasi beralam terbuka dengan panduan barang bawaan essensial ini.</p>
                    <a href="blog-1.html" style="margin-top: auto; font-weight: 600;" aria-label="Membaca blog 1">Baca Artikel <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>""",
    2: """            <div class="card">
                <div class="card-img">
                    <img src="img/b1.webp" alt="Spot Foto Batu Malang" loading="lazy" decoding="async" width="800" height="auto">
                </div>
                <div class="card-content">
                    <div style="color: var(--primary); font-size: 0.9rem; margin-bottom: 10px;">Destinasi &bull; 18 Feb 2026</div>
                    <h3><a href="blog-2.html" style="color: #fff;">3 Spot Foto Paling Instagramable di Area Camping</a></h3>
                    <p>Temukan sudut-sudut rahasia Batu Malang yang hanya bisa diakses via rute camping. Foto liburanmu dijamin estetik!</p>
                    <a href="blog-2.html" style="margin-top: auto; font-weight: 600;" aria-label="Membaca blog 2">Baca Artikel <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>""",
    3: """            <div class="card">
                <div class="card-img">
                    <img src="img/b2.webp" alt="Family Camping" loading="lazy" decoding="async" width="800" height="auto">
                </div>
                <div class="card-content">
                    <div style="color: var(--primary); font-size: 0.9rem; margin-bottom: 10px;">Family Liburan &bull; 10 Feb 2026</div>
                    <h3><a href="blog-3.html" style="color: #fff;">Amankah Paket Camping Untuk Anak-anak dan Keluarga?</a></h3>
                    <p>Membedah keamanan rute dan jenis kendaraan yang cocok agar si kecil tetap bisa menikmati derunya ketenangan secara aman.</p>
                    <a href="blog-3.html" style="margin-top: auto; font-weight: 600;" aria-label="Membaca blog 3">Baca Artikel <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>""",
    4: """            <div class="card">
                <div class="card-img">
                    <img src="img/b2.webp" alt="Api Unggun Camping Baru" loading="lazy" decoding="async" width="800" height="auto">
                </div>
                <div class="card-content">
                    <div style="color: var(--primary); font-size: 0.9rem; margin-bottom: 10px;">Kuliner & Aktivitas &bull; 01 Mar 2026</div>
                    <h3><a href="blog-4.html" style="color: #fff;">Keseruan BBQ dan Api Unggun di Camping Batu Malang</a></h3>
                    <p>Malam hari di kawasan Batu terkenal dingin, namun di sanalah letak keistimewaan aktivitas api unggun dan BBQ.</p>
                    <a href="blog-4.html" style="margin-top: auto; font-weight: 600;" aria-label="Membaca blog 4">Baca Artikel <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>""",
    5: """            <div class="card">
                <div class="card-img">
                    <img src="img/b1.webp" alt="Pemandangan City Light" loading="lazy" decoding="async" width="800" height="auto">
                </div>
                <div class="card-content">
                    <div style="color: var(--primary); font-size: 0.9rem; margin-bottom: 10px;">Tips & Panduan &bull; 02 Mar 2026</div>
                    <h3><a href="blog-5.html" style="color: #fff;">Waktu Terbaik untuk Camping Menikmati City Light Batu Malang</a></h3>
                    <p>Memilih waktu yang tepat adalah kunci utama agar pengalaman camping tidak terganggu cuaca buruk atau kabut tebal.</p>
                    <a href="blog-5.html" style="margin-top: auto; font-weight: 600;" aria-label="Membaca blog 5">Baca Artikel <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>""",
    6: """            <div class="card">
                <div class="card-img">
                    <img src="img/b3.webp" alt="Tenda Premium Camping" loading="lazy" decoding="async" width="800" height="auto">
                </div>
                <div class="card-content">
                    <div style="color: var(--primary); font-size: 0.9rem; margin-bottom: 10px;">Review Perlengkapan &bull; 04 Mar 2026</div>
                    <h3><a href="blog-6.html" style="color: #fff;">Mengenal Keunggulan Sewa Tenda Premium Batu Malang</a></h3>
                    <p>Tenda premium tidak hanya menawarkan estetika yang baik, namun juga keandalan saat menghadapi kerasnya iklim di tengah alam terbuka.</p>
                    <a href="blog-6.html" style="margin-top: auto; font-weight: 600;" aria-label="Membaca blog 6">Baca Artikel <i class="fas fa-arrow-right"></i></a>
                </div>
            </div>"""
}

mapping = {
    1: [2, 3, 4],
    2: [1, 3, 4],
    3: [4, 5, 2],
    4: [5, 6, 1],
    5: [6, 1, 2],
    6: [1, 2, 3]
}

template = """    <!-- Related Articles -->
    <section class="related-articles">
        <div class="section-title">
            <h2>Artikel Menarik Lainnya</h2>
            <div class="accent"></div>
        </div>
        <div class="grid">
{}
        </div>
    </section>

    <!-- Footer -->"""

base_dir = r"g:\bjir\tugas peting\fun offroad batu malang coban talun"

for i in range(1, 7):
    filepath = os.path.join(base_dir, f"blog-{i}.html")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    cards_html = "\n".join([cards[c] for c in mapping[i]])
    replacement = template.format(cards_html)
    new_content = re.sub(r'    <!-- Related Articles -->.*?    <!-- Footer -->', replacement, content, flags=re.DOTALL)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated blog-{i}.html")

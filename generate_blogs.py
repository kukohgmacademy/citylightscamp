import os
import re

base_dir = r"g:\bjir\tugas peting\fun offroad batu malang coban talun"

with open(os.path.join(base_dir, "Mengenal Keunggulan Sewa Tenda Premium Batu Malang.html"), "r", encoding="utf-8") as f:
    template = f.read()

blogs_data = [
    {
        "id": 7,
        "title": "Review Jujur Jeep Offroad Coban Talun Batu",
        "date": "Destinasi &bull; 07 Mar 2026",
        "desc": "Rasakan sensasi menantang adrenalin dengan Jeep Offroad melintasi trek menantang Coban Talun.",
        "img": "img/b1.webp",
        "h1": "Review Jujur Jeep Offroad Coban Talun Batu",
        "h2_1": "1. Menyusuri Jalur Ekstrim",
        "p_1": "Jeep Offroad di Coban Talun menawarkan rute yang sangat memacu adrenalin. Dari jalanan berlumpur, berbatu, hingga tanjakan curam yang menantang.",
        "h2_2": "2. Keamanan yang Terjamin",
        "p_2": "Meskipun rutenya ekstrem, Anda dikemudikan oleh driver profesional yang berpengalaman. Semua armada Jeep juga selalu dicek secara berkala.",
        "h2_3": "3. Pemandangan Hutan Pinus",
        "p_3": "Sepanjang perjalanan, mata Anda akan dimanjakan dengan deretan pohon pinus menjulang tinggi serta udara yang sangat segar.",
        "h2_4": "4. Kesimpulan",
        "p_4": "Sangat direkomendasikan bagi Anda yang mencari aktivitas luar ruangan seru selain bersantai di tenda."
    },
    {
        "id": 8,
        "title": "Cara Booking Paket Camping Batu Malang Paling Mudah",
        "date": "Panduan &bull; 10 Mar 2026",
        "desc": "Simak panduan lengkap cara melakukan pemesanan paket camping agar liburanmu terencana dengan sempurna.",
        "img": "img/b2.webp",
        "h1": "Cara Booking Paket Camping Batu Malang Paling Mudah",
        "h2_1": "1. Pilih Paket yang Sesuai",
        "p_1": "Langkah pertama adalah memilih paket yang paling cocok dengan kebutuhan Anda, apakah untuk keluarga, teman, atau pasangan.",
        "h2_2": "2. Hubungi Admin via WhatsApp",
        "p_2": "Untuk respons tercepat, hubungi nomor WhatsApp yang tertera di website. Admin kami siap membantu dan menginformasikan ketersediaan.",
        "h2_3": "3. Lakukan DP (Down Payment)",
        "p_3": "Setelah tanggal disepakati, silakan bayarkan uang muka sebagai tanda jadi. Kami menerima berbagai metode pembayaran digital.",
        "h2_4": "4. Persiapkan Keberangkatan",
        "p_4": "Setelah booking terkonfirmasi, Anda tinggal datang membawa pakaian secukupnya karena semua fasilitas dasar telah kami siapkan."
    },
    {
        "id": 9,
        "title": "7 Keuntungan Memilih Paket Camping VIP",
        "date": "Tips & Trik &bull; 12 Mar 2026",
        "desc": "Jelajahi berbagai fasilitas mewah yang bisa kamu nikmati dengan memilih paket camping VIP di Batu Malang.",
        "img": "img/b3.webp",
        "h1": "7 Keuntungan Memilih Paket Camping VIP",
        "h2_1": "1. Fasilitas Tenda Super Nyaman",
        "p_1": "Tenda VIP menggunakan material double layer premium yang sangat tebal, menjamin kehangatan di tengah udara dingin Batu.",
        "h2_2": "2. Area Api Unggun Eksklusif",
        "p_2": "Anda tidak perlu berbagi spot dengan pengunjung lain. Nikmati momen hangat yang lebih private bersama orang tersayang.",
        "h2_3": "3. Sajian Kuliner BBQ Terabaik",
        "p_3": "Paket VIP dilengkapi dengan sajian makan malam dan BBQ daging premium yang siap menggoyang lidah Anda di bawah bintang.",
        "h2_4": "4. Layanan Pendamping Personal",
        "p_4": "Ada tim khusus yang akan membantu keperluan Anda selama berada di area camping, memastikan pengalaman liburan 100% rileks."
    }
]

for data in blogs_data:
    content = template
    
    # meta tags replacement
    content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} | Blog</title>', content)
    content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="Baca artikel: {data["desc"]}">', content)
    content = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="blog camping batu, {data["title"]}">', content)
    
    # open graph tags
    content = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{data["title"]}">', content)
    content = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{data["desc"]}">', content)
    content = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="https://campingbatu.com/blog-{data["id"]}.html">', content)
    content = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="https://campingbatu.com/blog-{data["id"]}.html">', content)
    
    # page header
    content = re.sub(r'<h1>.*?</h1>', f'<h1>{data["h1"]}</h1>', content)
    content = re.sub(r'<p class="post-meta">.*?</p>', f'<p class="post-meta">{data["date"]}</p>', content)
    
    # Images in figure
    content = re.sub(r'<img src="img/b3.webp" alt="Tenda Premium Camping">', f'<img src="{data["img"]}" alt="{data["title"]}">', content)
    content = re.sub(r'<header class="page-header" style="background-image: url\(\'img/b3.webp\'\);">', f'<header class="page-header" style="background-image: url(\'{data["img"]}\');">', content)
    
    # Article content replacements
    content = re.sub(r'<h2 id="kualitas-material">.*?</h2>', f'<h2 id="section1">{data["h2_1"]}</h2>', content)
    content = re.sub(r'<h2 id="kenyamanan-ruang">.*?</h2>', f'<h2 id="section2">{data["h2_2"]}</h2>', content)
    content = re.sub(r'<h2 id="ventilasi">.*?</h2>', f'<h2 id="section3">{data["h2_3"]}</h2>', content)
    content = re.sub(r'<h2 id="kesimpulan">.*?</h2>', f'<h2 id="section4">{data["h2_4"]}</h2>', content)
    
    # Find all paragraphs in <section class="post-content"> up to <!-- Author Profile -->
    post_content_match = re.search(r'(<section class="post-content">.*?)(<!-- Author Profile -->)', content, re.DOTALL)
    if post_content_match:
        post_content = post_content_match.group(1)
        # replacing paragraphs loosely
        ps = re.findall(r'<p>.*?</p>', post_content, re.DOTALL)
        if len(ps) >= 4:
            content = content.replace(ps[0], f'<p>Halo para pecinta alam! Di artikel ini, kita akan membahas {data["title"]} agar pengalaman campingmu semakin mantap.</p>')
            content = content.replace(ps[1], f'<p>{data["p_1"]}</p>')
            content = content.replace(ps[2], f'<p>{data["p_2"]}</p>')
            content = content.replace(ps[3], f'<p>{data["p_3"]}</p>')
            content = content.replace(ps[4], f'<p>{data["p_4"]}</p>')
            
    # TOC replacement
    content = re.sub(r'<li><a href="#kualitas-material">.*?</a></li>', f'<li><a href="#section1">{data["h2_1"]}</a></li>', content)
    content = re.sub(r'<li><a href="#kenyamanan-ruang">.*?</a></li>', f'<li><a href="#section2">{data["h2_2"]}</a></li>', content)
    content = re.sub(r'<li><a href="#ventilasi">.*?</a></li>', f'<li><a href="#section3">{data["h2_3"]}</a></li>', content)
    content = re.sub(r'<li><a href="#kesimpulan">.*?</a></li>', f'<li><a href="#section4">{data["h2_4"]}</a></li>', content)
    
    filename = os.path.join(base_dir, f"blog-{data['id']}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
        
print("New blogs generated.")


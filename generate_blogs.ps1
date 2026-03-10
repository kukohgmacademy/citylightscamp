$content = Get-Content "blog-6.html" -Raw

# Helper to create blog
function Create-Blog {
    param(
        [string]$id,
        [string]$title,
        [string]$date,
        [string]$desc,
        [string]$img,
        [string]$h1,
        [string]$h2_1, [string]$p_1,
        [string]$h2_2, [string]$p_2,
        [string]$h2_3, [string]$p_3,
        [string]$h2_4, [string]$p_4
    )
    
    $newContent = $content
    $newContent = $newContent -replace 'Keunggulan Sewa Tenda Premium vs Tenda Biasa \| Blog', "$title | Blog"
    $newContent = $newContent -replace 'blog-6.html', "blog-$id.html"
    $newContent = $newContent -replace 'Mengenal Keunggulan Sewa Tenda Premium Batu Malang', $h1
    $newContent = $newContent -replace 'Review Perlengkapan â€¢ 04 Mar 2026', $date
    $newContent = $newContent -replace 'img/b3.webp', $img
    
    # regex replace content section roughly, but we can do exact replacements based on blog-6 content
    $newContent = $newContent -replace '1\. Kualitas Material dan Tahan Cuaca', $h2_1
    $newContent = $newContent -replace '2\. Kenyamanan dan Ruang Bergerak', $h2_2
    $newContent = $newContent -replace '3\. Sistem Ventilasi yang Mencegah Kondensasi', $h2_3
    $newContent = $newContent -replace '4\. Apakah Harganya Sepadan\?', $h2_4
    
    $newContent = $newContent -replace 'Tenda premium menggunakan material kain.*?rentan patah\.', $p_1
    $newContent = $newContent -replace 'Lupakan harus membungkuk.*?kotoran luar\.', $p_2
    $newContent = $newContent -replace 'Pernahkah Anda bangun tidur.*?tetap kering dan sejuk\.', $p_3
    $newContent = $newContent -replace 'Untuk mereka yang baru pertama kali camping.*?selama liburam\.', $p_4
    
    $newContent = $newContent -replace 'Bagi sebagian orang, camping berarti.*?di Batu Malang\.', "Halo para pecinta alam! Di artikel ini, kita akan membahas $title agar pengalaman petualanganmu semakin mantap."
    
    # replace TOC links
    $newContent = $newContent -replace '#kualitas-material', '#section1'
    $newContent = $newContent -replace '#kenyamanan-ruang', '#section2'
    $newContent = $newContent -replace '#ventilasi', '#section3'
    $newContent = $newContent -replace '#kesimpulan', '#section4'
    
    Set-Content -Path "blog-$id.html" -Value $newContent -Encoding UTF8
}

Create-Blog -id "7" `
    -title "Review Jujur Jeep Offroad Coban Talun Batu" `
    -date "Destinasi &bull; 07 Mar 2026" `
    -desc "Rasakan sensasi menantang adrenalin dengan Jeep Offroad melintasi trek menantang Coban Talun." `
    -img "img/b1.webp" `
    -h1 "Review Jujur Jeep Offroad Coban Talun Batu" `
    -h2_1 "1. Menyusuri Jalur Ekstrim" `
    -p_1 "Jeep Offroad di Coban Talun menawarkan rute yang sangat memacu adrenalin. Dari jalanan berlumpur, berbatu, hingga tanjakan curam yang menantang." `
    -h2_2 "2. Keamanan yang Terjamin" `
    -p_2 "Meskipun rutenya ekstrem, Anda dikemudikan oleh driver profesional yang berpengalaman. Semua armada Jeep juga selalu dicek secara berkala." `
    -h2_3 "3. Pemandangan Hutan Pinus" `
    -p_3 "Sepanjang perjalanan, mata Anda akan dimanjakan dengan deretan pohon pinus menjulang tinggi serta udara yang sangat segar." `
    -h2_4 "4. Kesimpulan" `
    -p_4 "Sangat direkomendasikan bagi Anda yang mencari aktivitas luar ruangan seru selain bersantai di tenda."

Create-Blog -id "8" `
    -title "Cara Booking Paket Camping Batu Malang Paling Mudah" `
    -date "Panduan &bull; 10 Mar 2026" `
    -desc "Simak panduan lengkap cara melakukan pemesanan paket camping agar liburanmu terencana dengan sempurna." `
    -img "img/b2.webp" `
    -h1 "Cara Booking Paket Camping Batu Malang Paling Mudah" `
    -h2_1 "1. Pilih Paket yang Sesuai" `
    -p_1 "Langkah pertama adalah memilih paket yang paling cocok dengan kebutuhan Anda, apakah untuk keluarga, teman, atau pasangan." `
    -h2_2 "2. Hubungi Admin via WhatsApp" `
    -p_2 "Untuk respons tercepat, hubungi nomor WhatsApp yang tertera di website. Admin kami siap membantu dan menginformasikan ketersediaan." `
    -h2_3 "3. Lakukan DP (Down Payment)" `
    -p_3 "Setelah tanggal disepakati, silakan bayarkan uang muka sebagai tanda jadi. Kami menerima berbagai metode pembayaran digital." `
    -h2_4 "4. Persiapkan Keberangkatan" `
    -p_4 "Setelah booking terkonfirmasi, Anda tinggal datang membawa pakaian secukupnya karena semua fasilitas dasar telah kami siapkan."

Create-Blog -id "9" `
    -title "7 Keuntungan Memilih Paket Camping VIP" `
    -date "Tips &amp; Trik &bull; 12 Mar 2026" `
    -desc "Jelajahi berbagai fasilitas mewah yang bisa kamu nikmati dengan memilih paket camping VIP di Batu Malang." `
    -img "img/b3.webp" `
    -h1 "7 Keuntungan Memilih Paket Camping VIP" `
    -h2_1 "1. Fasilitas Tenda Super Nyaman" `
    -p_1 "Tenda VIP menggunakan material double layer premium yang sangat tebal, menjamin kehangatan di tengah udara dingin Batu." `
    -h2_2 "2. Area Api Unggun Eksklusif" `
    -p_2 "Anda tidak perlu berbagi spot dengan pengunjung lain. Nikmati momen hangat yang lebih private bersama orang tersayang." `
    -h2_3 "3. Sajian Kuliner BBQ Terabaik" `
    -p_3 "Paket VIP dilengkapi dengan sajian makan malam dan BBQ daging premium yang siap menggoyang lidah Anda di bawah bintang." `
    -h2_4 "4. Layanan Pendamping Personal" `
    -p_4 "Ada tim khusus yang akan membantu keperluan Anda selama berada di area camping, memastikan pengalaman liburan 100% rileks."

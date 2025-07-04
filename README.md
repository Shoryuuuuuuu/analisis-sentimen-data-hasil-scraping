## Analisis Sentimen Ulasan Google Play Store: Dari Pengambilan Data Hingga Evaluasi Model
Di era digital, opini dan ulasan dari pengguna memegang peranan penting dalam menentukan kualitas dan reputasi sebuah aplikasi. Google Play Store, sebagai toko aplikasi Android terbesar di dunia, menjadi sumber data berharga bagi perusahaan atau peneliti yang ingin memahami bagaimana persepsi masyarakat terhadap sebuah aplikasi. Melalui proyek ini, kita akan mempelajari bagaimana membangun sistem analisis sentimen untuk mengolah ribuan ulasan pengguna Google Play Store menjadi informasi terstruktur, sehingga bisa digunakan untuk mengambil keputusan bisnis yang lebih tepat.

## Tahap Pertama: Mengambil Data Ulasan Secara Otomatis
Tahap awal dalam membangun sistem ini adalah pengambilan data atau scraping. Kita tidak bisa melakukan analisis jika tidak memiliki data yang cukup. Untuk itu, kita memanfaatkan sebuah skrip Python sederhana bernama scraper-playstore.py, yang ditulis menggunakan pustaka google_play_scraper. Pustaka ini sangat membantu karena menyediakan fungsi siap pakai untuk mengambil data ulasan, sehingga kita tidak perlu membangun crawler dari nol.

Di dalam skrip ini, kita mendefinisikan ID aplikasi yang akan diambil, misalnya com.gojek.app untuk aplikasi Gojek. Kemudian kita memanggil fungsi reviews() yang akan terhubung ke Google Play Store, mengambil ulasan terbaru dalam jumlah besar (bahkan hingga puluhan ribu jika tersedia). Hasil scraping berupa kumpulan review lengkap dengan nama penulis, isi ulasan, rating bintang, serta tanggal penulisan. Semua data ini kemudian disimpan ke file CSV bernama gojek_reviews.csv. Dengan data ini, kita memiliki bahan baku mentah yang siap diolah lebih lanjut.

## Tahap Kedua: Pembersihan dan Normalisasi Teks
Langkah selanjutnya adalah melakukan pembersihan data atau yang sering disebut preprocessing. Data ulasan dari Play Store umumnya ditulis dalam bahasa percakapan sehari-hari. Sering kali, penulis ulasan menggunakan bahasa slang, kata singkatan, emotikon, atau bahkan typo. Jika kita langsung memberikan teks seperti ini ke algoritma Machine Learning tanpa dibersihkan, hasilnya akan buruk karena model tidak mampu mengenali kata slang sebagai kata baku. Oleh sebab itu, tahap ini menjadi krusial.

Pembersihan teks dilakukan dengan beberapa cara. Pertama, kita mengubah semua huruf menjadi huruf kecil agar kata “Bagus” dan “bagus” diperlakukan sama. Kedua, kita menghapus tanda baca, angka, dan karakter aneh dengan teknik regular expression (regex). Ketiga, kita menghapus spasi ganda agar teks menjadi rapi.

Yang membuat proyek ini lebih menarik adalah adanya kamus slang yang disiapkan di file slangwords.txt. File ini berisi ribuan pasangan kata slang beserta padanan katanya dalam bahasa Indonesia baku. Sebagai contoh, kata “gak” diubah menjadi “tidak”, “btw” diubah menjadi “ngomong”, atau “gue” diubah menjadi “saya”. Proses normalisasi slang ini dilakukan dengan cara membagi setiap kalimat menjadi daftar kata, lalu setiap kata dicek di kamus slang — jika cocok, maka diganti dengan padanan bakunya. Dengan begitu, kita memastikan bahwa teks ulasan sudah homogen, rapi, dan konsisten dalam bahasa yang dapat dipahami oleh model.

## Tahap Ketiga: Memberikan Label Sentimen
Setelah teks ulasan dibersihkan dan dinormalisasi, kita masuk ke tahap pemberian label atau labeling. Karena ulasan di Play Store sudah dilengkapi dengan skor bintang (1 sampai 5), kita bisa memanfaatkan skor ini sebagai dasar untuk menentukan sentimen pengguna. Konvensi yang umum digunakan adalah:
- Skor 4 atau 5 dianggap sebagai sentimen positif, karena menunjukkan kepuasan.
- Skor 3 dianggap netral, karena nilainya berada di tengah.
- Skor 1 atau 2 dianggap negatif, karena menunjukkan kekecewaan atau keluhan.

Label ini ditambahkan ke dataset sebagai kolom baru, sehingga sekarang setiap ulasan tidak hanya punya teks, tetapi juga memiliki kelas sentimen: positif, netral, atau negatif.

##  Tahap Keempat: Mengubah Teks Menjadi Angka
Algoritma Machine Learning tidak bisa bekerja langsung dengan teks, melainkan harus diubah menjadi bentuk numerik. Di tahap ini, kita menggunakan teknik populer yaitu TF-IDF (Term Frequency - Inverse Document Frequency). Dengan teknik ini, setiap kata di dalam teks diubah menjadi vektor angka yang mewakili pentingnya kata tersebut di satu dokumen dibandingkan dengan keseluruhan kumpulan dokumen.

Sebagai contoh, kata “aplikasi” yang muncul di hampir semua review akan memiliki bobot kecil, karena tidak membantu membedakan sentimen. Sebaliknya, kata-kata seperti “lambat”, “bagus”, atau “error” akan memiliki bobot lebih besar jika hanya muncul di sebagian review dan punya hubungan kuat dengan sentimen tertentu.

## Tahap Kelima: Membagi Data dan Melatih Model
Setelah semua teks diubah menjadi representasi angka, langkah berikutnya adalah membagi data menjadi data pelatihan (training set) dan data pengujian (test set). Biasanya, 80% data digunakan untuk melatih model, sementara 20% sisanya digunakan untuk mengevaluasi kinerja model.

Dalam contoh ini, kita mencoba dua model dasar yang sering digunakan untuk teks pendek:
1. Naive Bayes — algoritma klasik yang sederhana tetapi efektif untuk teks.
2. Logistic Regression — model linier yang dapat digunakan untuk klasifikasi biner maupun multikelas.

Kedua model ini dilatih menggunakan data pelatihan, lalu diuji pada data pengujian untuk melihat bagaimana kinerjanya memprediksi sentimen.

## Tahap Keenam: Mengevaluasi Hasil

Evaluasi hasil dilakukan dengan menghitung metrik seperti Precision, Recall, dan F1-Score. Precision menunjukkan seberapa akurat prediksi positif, Recall menunjukkan seberapa banyak ulasan benar yang berhasil ditangkap oleh model, dan F1-Score adalah rata-rata harmonik dari Precision dan Recall. Selain itu, kita juga bisa melihat Confusion Matrix untuk mengetahui berapa banyak prediksi yang benar dan salah untuk setiap kelas (positif, netral, negatif).

Hasil evaluasi ini akan menjadi tolok ukur apakah pipeline yang kita bangun bekerja dengan baik atau masih perlu ditingkatkan, misalnya dengan menambah data, mencoba algoritma yang lebih canggih seperti LSTM atau BERT, atau dengan memperbaiki tahap pembersihan data.

## Mengapa Tahap Ini Sangat Penting?
Semua tahap di atas membentuk pipeline analisis sentimen yang utuh. Dengan pipeline ini, kita tidak hanya bisa memahami tren opini publik, tetapi juga bisa mendeteksi pola keluhan yang berulang, merumuskan strategi peningkatan layanan, dan merespons masalah pelanggan dengan lebih cepat. Hal ini tentu sangat berguna untuk perusahaan yang bergerak di bidang layanan digital, transportasi online, perbankan, maupun sektor e-commerce.

##  Kesimpulan
Dari mengambil data dengan scraper-playstore.py, membersihkan dan menormalkan teks menggunakan kamus slang, memberi label sentimen berdasarkan skor bintang, mengubah teks ke angka melalui TF-IDF, hingga membangun model Machine Learning untuk memprediksi sentimen — seluruh proses ini adalah contoh nyata bagaimana data mentah bisa diolah menjadi informasi berharga.

Pipeline ini fleksibel, bisa diterapkan pada aplikasi lain, dan bisa dikembangkan lebih jauh dengan model NLP modern seperti IndoBERT, yang dapat memahami konteks bahasa Indonesia dengan lebih baik.

Dengan pemahaman mendalam akan proses ini, kita bisa menerjemahkan suara pengguna menjadi keputusan nyata, memperbaiki kualitas layanan, dan meningkatkan kepercayaan publik.


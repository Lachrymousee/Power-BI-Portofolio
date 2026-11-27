# **Laporan Analisis Portofolio Power BI**

## **Project:**

Fleet Utilization & Logistics Operational Performance Dashboard Menggunakan Microsoft Power BI

## **Description:**

End-to-end Business Intelligence and Data Validation Portofolio

Link Video and GitHub:

- <u>Portofolio MS Power BI</u>

- <u>Lachrymousee/Power-BI-Portofolio: End-to-end Business Intelligence and Data Validation using MS Power BI</u>

## **Tools:**

- Microsoft Power BI (Power Query, DAX, Data Modeling) untuk pembersihan data (ETL), pemodelan data, dan visualisasi interaktif.

- Python Library (Pandas, Numpy) untuk pembuatan sample data.

## **I. Business Context & Objective**

Dalam operasional transportasi dan logistik dengan skala multi-cabang, manajemen sering menghadapi kendala visibilitas data terkait tingkat keterpakaian armada/kendaraan ( _fleet utilization_ ), ketepatan waktu pengiriman ( _On-Time Delivery_ ), serta biaya perawatan armada ( _maintenance cost_ ).

Project ini bertujuan membangun sistem pelaporan interaktif menggunakan Microsoft Power BI yang dapat mengkonsolidasikan data operasional mentah menjadi _insight_ strategis guna:

1. Memantau kinerja operasional harian dan bulanan lintas cabang regional secara _real-time_ .

2. Mengevaluasi efisiensi biaya perawatan per kilometer armada berdasarkan tipe kendaraan.

3. Mendeteksi anomali unit armada yang mengalami inefisiensi biaya untuk mendukung keputusan audit dan peremajaan unit.

## **II. Data Architecture & Validation**

Untuk menjamin akurasi, integritas, dan konsistensi pelaporan, seluruh data mentah diproses melalui tahapan _Extract, Transform, Load_ (ETL) pada Power Query sebelum data diproses menjadi bentuk visualisasi. Berikut step-by-step pembersihan data:

- Data Cleansing & Validation
  - **Deduplikasi Primary Key:** Mengidentifikasi dan menghapus catatan duplikat pada tabel armada (‘dim_vehicle’) untuk mencegah perhitungan berulang dengan data yang sama.

  - **Standarisasi Kategori:** Melakukan pembersihan spasi ( _trim_ ) dan penyeragaman huruf kapital pada atribut status operasional kendaraan (‘Active’, ’Maintenance’, ’Inactive’).

  - **Penanganan Nilai Kosong & Anomali:** Mengkonversi nilai kosong ( _null_ ) pada catatan biaya perawatan menjadi ‘0’ serta menyaring keluar anomali pencatatan jarak tempuh bernilai negatif akibat kesalahan input sistem.

  - **Validasi Tipe Data:** Memastikan seluruh kolom tanggal, numerik, dan mata uang memiliki tipe data relasional yang konsisten.

- Data Modeling (Star Schema)

Merancang arsitektur Star Schema dengan memisahkan tabel transaksi operasional (‘fact_operations’ berisi 1.400+ catatan bersih) sebagai pusat skema yang terhubung melalui relasi One-to-Many (‘1:\*’) ke tiga tabel dimensi:

- ‘dim_vehicle’ : profil 50 unit armada

- ‘dim_branch’ : profil 5 cabang regional

- ‘Dim_Date’ : tabel kalender dinamis berbasis M-Language

## **III. Key Metrics & DAX Implementation**

Seluruh _Key Performance Indicator_ (KPI) dibangun menggunakan formula _Data Analysis Expressions_ (DAX) yang terpusat dalam tabel ‘\_Measures’. Formula yang dibuat:

- **Fleet Utilization Rate (%):** Mengukur rasio armada berstatus aktif yang beroperasi aktual terhadap total kapasitas armada aktif yang tersedia.

- **On-Time Delivery (%):** Menghitung persentase pengiriman yang diselesaikan sesuai/lebih cepat dari target waktu operasional
  - (‘actual_hours’ <= ‘target_hours’).

- **Maintenance Cost per KM (IDR):** Mengukur rasio total biaya pemeliharaan terhadap total jarak tempuh armada untuk menstandarisasi evaluasi efisiensi antar tipe kendaraan.

## **IV. Dashboard Overview & Key Analytical Findings**

## **A. Executive Operational Overview**

<!-- Start of picture text -->

SERA Fleet & Logistics Operational Performance (2026) sun<br>Teta Tip (ae) Tet Maintenance Cost (ard) ont ame<br>1,484 Rp. 1,221,513,590 ns<br>Fleet zion Rate On-Time Deven Rate<br>100.0% 33.6%<br>Totaby MonthDistance Name (kM On-Timeby bench Deiveryame Rate Maintenancebye ype Cost er kM<br>a<br>so 200<br>etA gh Oei weth et th wegt oe‘ osi ..s.it © evn Mov ansh S0v-innave Sort<br><!-- End of picture text -->

**Kinerja Keseluruhan:** Selama periode operasional 2026, tercatat total 1.400+ perjalanan dan Total Maintenance Cost sebesar Rp. 1.2 Miliar dengan tingkat utilisasi armada mencapai 100% dan rata-rata ketepatan waktu pengiriman sebesar 33,6%.

**Perbandingan Cabang:** Cabang Semarang (Region Jawa Tengah) mencatatkan performa ketepatan waktu tertinggi sebesar 35,5%, sedangkan cabang Bandung (Region Jawa Barat) berada di posisi terendah sebesar 32,1% sehingga memerlukan evaluasi alokasi rute.

**Tren Jarak Tempuh Bulanan:** Grafik tren menunjukkan pergerakan jarak tempuh operasional yang berada di kisaran 300.000 KM - 390.000 KM per bulan, di mana pengguna dapat memfilter performa spesifik berdasarkan wilayah (‘region’) dan bulan (‘Month Name’) secara dinamis.

**Efisiensi Biaya Berdasarkan Tipe Armada:** Grafik perbandingan tipe kendaraan (Maintenance Cost per KM by Vehicle Type) mengungkap bahwa kategori Blind Van - GranMax memiliki beban biaya pemeliharaan tertinggi sebesar Rp. 411,37 / KM, sedangkan kategori Box Truck - Engkel terbukti paling efisien dengan biaya Rp. 280,03 / KM.

## **B. Fleet Maintenance & Anomaly Audit**

<!-- Start of picture text -->

SERA Fleet & Logistics Operational Performance (2026) regen Mont Name<br>il HORS SUV inno Acve 00 5753500] a8<br>‘ot tancekl and Teta antnance os esse whet ity ainrianaSn |<br>} . cS Seg ie ESS as<br>[on oe oe wos Cee omen ae<br>Fo oC Ne Ces ENNSMIDSS SNES ce<br><!-- End of picture text -->

**Deteksi Anomali Unit :** Melalui analisis Grafik _Scatter Plot_ dan tabel audit berbasis _Conditional Formatting,_ teridentifikasi 3 unit kendaraan dengan rasio biaya perawatan per kilometer tertinggi yang menyimpang jauh dari rata-rata armada:

**1. VH-025 (‘SUV-Innova’):** Biaya perawatan mencapai Rp. 740,46 / KM dengan total jarak tempuh 57.535 KM.

**2. VH-038 (‘Blind Van - GranMax’):** Biaya perawatan mencapai Rp. 597,76 / KM dengan total jarak tempuh 67.094 KM.

**3. VH-040 (‘MPV-Avanza’):** Biaya perawatan mencapai Rp. 590,40 / KM dengan total jarak tempuh 53.159 KM.

## **V. Actionable Recommendations**

Berdasarkan temuan data di atas, rekomendasi langkah operasional yang dapat diambil manajemen meliputi:

**1. Audit Teknis & Evaluasi Peremajaan Unit:** Memprioritaskan inspeksi mekanis menyeluruh terhadap 3 unit dengan _Maintenance Cost per KM_ tertinggi untuk menentukan kelayakan perbaikan lanjutan atau penggantian unit.

**2. Optimasi Penjadwalan Cabang:** Melakukan peninjauan ulang estimasi waktu tempuh ( _target_hours_ ) dan distribusi armada pada cabang dengan _On-Time Delivery Rate_ di bawah rata-rata regional.

**3. Otomatisasi Validasi Input:** Menerapkan aturan validasi langsung pada sistem operasional untuk mencegah masuknya nilai jarak tempuh negatif maupun inkonsistensi penulisan status unit sejak awal pencatatan.

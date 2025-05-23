# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan fiktif yang menghadapi masalah serius terkait jumlah mahasiswa yang tidak menyelesaikan studi alias dropout. Tingginya angka dropout berdampak buruk pada reputasi institusi, efisiensi operasional, dan efektivitas pendidikan.

Variabel-variabel yang terdapat pada dataset yaitu :
Nama Kolom	dan Deskripsi
* Marital_status : Status pernikahan mahasiswa (1: single, 2: married, 3: widower, 4: divorced, 5: facto union, 6: legally separated)
* Application_mode : Jalur pendaftaran mahasiswa ke perguruan tinggi (contoh: 1st phase, transfer, over 23 years old, dll)
* Application_order :	Urutan pilihan program studi (0 = pilihan pertama, 9 = pilihan terakhir)
* Course : Program studi mahasiswa (contoh: Informatics Engineering, Social Service, Tourism, dll)
* Daytime_evening_attendance : Waktu kehadiran kuliah (1: siang, 0: malam)
* Previous_qualification : Jenis kualifikasi terakhir sebelum mendaftar (contoh: secondary, bachelor's, master's, dll)
* Previous_qualification_grade : Nilai dari kualifikasi sebelumnya (0–200)
* Nacionality : Kewarganegaraan mahasiswa (contoh: 1 - Portuguese, 41 - Brazilian, 105 - Russian, dll)
* Mothers_qualification : Tingkat pendidikan terakhir ibu
* Fathers_qualification : Tingkat pendidikan terakhir ayah
* Mothers_occupation : Pekerjaan ibu mahasiswa
* Fathers_occupation : Pekerjaan ayah mahasiswa
* Admission_grade : Nilai ujian masuk perguruan tinggi (0–200)
* Displaced : Apakah mahasiswa berasal dari luar daerah (1: ya, 0: tidak)
* Educational_special_needs : Apakah mahasiswa memiliki kebutuhan khusus (1: ya, 0: tidak)
* Debtor : Apakah mahasiswa memiliki tunggakan biaya kuliah (1: ya, 0: tidak)
* Tuition_fees_up_to_date : Apakah pembayaran biaya kuliah lancar (1: ya, 0: tidak)
* Gender : Jenis kelamin (1: laki-laki, 0: perempuan)
* Scholarship_holder : Apakah mahasiswa penerima beasiswa (1: ya, 0: tidak)
* Age_at_enrollment : Usia mahasiswa saat pendaftaran
* International : Apakah mahasiswa merupakan mahasiswa internasional (1: ya, 0: tidak)
* Curricular_units_1st_sem_credited : Jumlah mata kuliah yang diakui (credit transfer) di semester 1
* Curricular_units_1st_sem_enrolled : Jumlah mata kuliah yang diambil di semester 1
* Curricular_units_1st_sem_evaluations : Jumlah evaluasi/ujian yang diikuti di semester 1
* Curricular_units_1st_sem_approved	: Jumlah mata kuliah yang lulus di semester 1
* Curricular_units_1st_sem_grade : Rata-rata nilai semester 1
* Curricular_units_1st_sem_without_evaluations : Jumlah mata kuliah yang tidak dievaluasi di semester 1
* Curricular_units_2nd_sem_credited : Jumlah mata kuliah yang diakui (credit transfer) di semester 2
* Curricular_units_2nd_sem_enrolled	: Jumlah mata kuliah yang diambil di semester 2
* Curricular_units_2nd_sem_evaluations : Jumlah evaluasi/ujian yang diikuti di semester 2
* Curricular_units_2nd_sem_approved	: Jumlah mata kuliah yang lulus di semester 2
* Curricular_units_2nd_sem_grade : Rata-rata nilai semester 2
* Curricular_units_2nd_sem_without_evaluations : Jumlah mata kuliah yang tidak dievaluasi di semester 2
* Unemployment_rate	: Tingkat pengangguran nasional pada tahun pendaftaran
* Inflation_rate : Tingkat inflasi pada tahun pendaftaran
* GDP	: Produk Domestik Bruto pada tahun pendaftaran
* Status : Target (label) klasifikasi: Graduate, Dropout, atau Enrolled

### Permasalahan Bisnis
- Tingginya tingkat mahasiswa yang dropout sebelum menyelesaikan studi
- Apa saja faktor-faktor yang dapat memperngaruhi keputusan siswa untuk melakukan dropout dari kampus?

### Cakupan Proyek
- Melakukan eksplorasi dan analisis terhadap data akademik dan administratif mahasiswa 
- Membuat business dashboard untuk monitoring performa
- Membangun model machine learning untuk prediksi dropout



### Persiapan

Sumber data: Dataset performa mahasiswa yang mencakup data akademik, sosial, dan administratif dari Jaya Jaya Institut. Dataset terdiri dari 4424 baris dan 37 kolom, yang sebagian besar kolomnya bertipe numerik (int64, float64), namun ada juga kolom bertipe kategorikal (object) termasuk dengan fitur Status.

[Jaya Jaya Institut Link Dataset](https://github.com/dicodingacademy/dicoding_dataset/raw/refs/heads/main/students_performance/data.csv).

* Setup environment:
    ```
    conda create --name proyek-institusi-pendidikan
    ```
* Install requirements: 
    ```
    pip install -r requirements.txt
    ```
* Setup metabase:
    ```
    docker pull metabase/metabase:v0.46.4
    docker run -p 3000:3000 --name metabase metabase/metabase
    ```
    Akses metabase pada http://localhost:3000/setup dan lakukan setup.

* Setup database (supabase):

    * Buat akun dan login https://supabase.com/dashboard/sign-in.
    * Buat new project
    * Copy URI pada database setting
    * Kirim dataset menggunakan sqlalchemy 
    ```python
    from sqlalchemy import create_engine
 
    URL = "DATABASE_URL"
    
    engine = create_engine(URL)
    df.to_sql('dataset', engine)
    ```

## Business Dashboard
Dashboard dibuat menggunakan **Metabase** untuk memvisualisasikan performa akademik dan tren dropout mahasiswa. Visualisasi disusun ke dalam beberapa bagian utama:

- **Ringkasan**: Menampilkan metrik utama berupa total mahasiswa, jumlah mahasiswa lulus, dan jumlah dropout dalam bentuk scorecard.
- **Distribusi Status Mahasiswa**: Pie chart untuk melihat proporsi Graduate, Dropout, dan Enrolled.
- **Faktor**: Menyediakan visualisasi hubungan antara status mahasiswa dengan beasiswa, usia saat masuk kuliah, status pembayaran kuliah, gender, status perkawinan, tunggakan mahasiswa dan waktu kehadiran kuliah terhadap peluang terjadinya dropout.
- **Filter Interaktif**: Terdapat filter untuk Status, yang dapat memfilter data sesuai kebutuhan pengguna.

* Link dashboard Metabase:
  
[Dashboard Metabase](http://localhost:3000/public/dashboard/922ce83f-9337-444b-9b92-a572e6ba481e)


## Menjalankan Sistem Machine Learning
Prototype sistem prediksi dropout dibangun menggunakan Streamlit dan dapat dijalankan secara lokal maupun online.

### Cara Menjalankan Lokal:
Pastikan Anda telah mengikuti tahapan pada bagian *Setup Environment*. Jika sudah, jalankan perintah berikut di terminal atau command prompt:
```
streamlit run app.py
```
* Link Dashboard Streamlit
Klik [Streamlit Predict Dashboard](https://data-science-2.streamlit.app/) untuk membuka prototype yang sudah dijalankan pada streamlit community.


## Conclusion

Tingkat dropout mahasiswa di Jaya Jaya Institut dipengaruhi oleh berbagai aspek, termasuk faktor demografi, latar belakang pendidikan, kondisi ekonomi, lingkungan keluarga, serta pencapaian akademik. Mahasiswa yang mendaftar pada usia lebih muda, status single, memiliki nilai masuk yang rendah, dan tidak memperoleh beasiswa cenderung memiliki risiko dropout yang lebih tinggi. Berdasarkan hasil analisis dan pemodelan machine learning yang dilakukan, terdapat pola-pola yang jelas mengenai mahasiswa berisiko tinggi untuk tidak menyelesaikan studinya. Mahasiswa dengan nilai rendah, matkul yang tidak diselesaikan, serta mahasiswa yang tidak memperoleh beasiswa cenderung tidak melanjutkan kuliah.

Analisis korelasi dan pentingnya fitur dalam model prediktif menunjukkan bahwa beberapa faktor yang paling berpengaruh terhadap keputusan siswa untuk dropout antara lain latar belakang akademik (seperti nilai dan jumlah unit yang diambil) dan kondisi ekonomi (scholarship ataupun displaced) . Misalnya, siswa yang menghadapi kesulitan akademik dalam semester pertama atau kedua cenderung memiliki risiko lebih tinggi untuk dropout.

Model Random Forest yang dibangun dalam proyek ini dapat menjadi pilihan yang cukup optimal dengan hasil evaluasi mencapai akurasi 77% dan f1-score sebesar 81% pada kelas dropout. Evaluasi dilakukan menggunakan validasi silang dan optimasi hyperparameter melalui GridSearchCV. Model ini dapat mengidentifikasi sejumlah fitur penting seperti nilai semester, jumlah matkul lulus, serta status pembayaran dan beasiswa sebagai indikator terjadinya dropout.

Implementasi sistem prediksi berbasis Streamlit serta dashboard visual di Metabase yang dilakukan diharapkan dapat digunakan sebagai alat yang efisien dalam mendeteksi mahasiswa yang memiliki kemungkinan dropout. Harapannya dengan diterapkan solusi ini, pihak institusi dapat mengidentifikasi mahasiswa berisiko sejak dini dan mengambil langkah intervensi yang tepat.


### Rekomendasi Action Items
- Menerapkan program mentoring untuk mahasiswa dengan nilai semester 1 & 2 yang rendah atau jumlah matkul lulus minimum.
- Memprioritaskan pemantauan pada mahasiswa dengan status pembayaran tertunggak dan bukan penerima beasiswa.
- Mengarahkan hasil model ke tim konseling untuk dilakukan tindakan lebih lanjut.
- Mengembangkan sistem agar dapat terhubung langsung dengan data real-time akademik kampus.
- Menjadwalkan retraining model setiap semester untuk menjaga akurasi terhadap dinamika mahasiswa.

Username: root@mail.com Password: root123

# Tirta - AI yang Selalu Memberikan Solusi

**Tirta** berasal dari kata dalam bahasa Sanskerta yang berarti "air" atau "sumber kehidupan". Nama ini dipilih karena **Tirta AI** berfungsi layaknya air yang mengalir: selalu tersedia, mudah diakses, dan memberikan solusi yang mengalir secara alami. Seperti air yang memberikan kehidupan dan memenuhi berbagai kebutuhan, Tirta hadir untuk membantu pengguna dengan memberikan jawaban dan penjelasan yang dibutuhkan kapan saja, dengan cara yang sederhana dan mudah dipahami.

## Deskripsi

Tirta adalah aplikasi AI berbasis **Retrieval-Augmented Generation (RAG)** yang menggunakan model **Qwen-Plus** untuk memberikan penjelasan dan solusi terkait berbagai topik dengan cara yang mudah dipahami. Seperti air yang mengalir, Tirta hadir untuk memberikan informasi yang mengalir dan membantu kapan saja dibutuhkan.

### Fitur:
- **Penjelasan Topik**: Menggunakan AI untuk menjelaskan topik-topik dengan cara yang sederhana.
- **Pencarian Pengetahuan**: Menggunakan pengetahuan yang ada untuk memberikan jawaban yang lebih tepat.
- **Interface Sederhana**: Antarmuka yang ramah pengguna menggunakan Streamlit.

## Teknologi yang Digunakan
- **DashScope**: SDK untuk mengakses model AI dan API-nya.
- **Streamlit**: Framework untuk membuat aplikasi web interaktif.
- **Qwen-Plus**: Model AI yang digunakan untuk menghasilkan teks dan jawaban berbasis pencarian.

## Persyaratan
- Python 3.x
- DashScope
- Streamlit
- Pandas (jika dibutuhkan untuk manipulasi data)

## Instalasi

Untuk menjalankan aplikasi ini, pastikan kamu memiliki Python 3.x dan dependensi yang diperlukan. Ikuti langkah-langkah berikut:

1. **Clone repositori ini**:

   ```bash
   git clone https://github.com/narendrasatyaa/ai-with-qwen-plus.git
   cd ai-with-qwen-plus


2. **Install dependencies**:

   Pastikan kamu memiliki file `requirements.txt` yang benar di repositori ini dan jalankan:

   ```bash
   pip install -r requirements.txt
   ```

   Jika belum ada file `requirements.txt`, buat file tersebut dengan isi:

   ```txt
   dashscope
   streamlit
   pandas
   ```

3. **Jalankan aplikasi**:

   Setelah dependensi terinstal, jalankan aplikasi Streamlit dengan perintah berikut:

   ```bash
   streamlit run ai_app.py
   ```

4. **Akses aplikasi**:

   Setelah menjalankan aplikasi, buka browser dan akses aplikasi di `http://localhost:8501`.

## Penggunaan

Tirtaai memungkinkan pengguna untuk bertanya tentang berbagai topik. Setelah aplikasi berjalan, cukup masukkan prompt atau pertanyaan yang ingin kamu jawab dan Tirta akan memberikan penjelasan yang relevan.

## Kontribusi

Jika kamu ingin berkontribusi pada pengembangan Tirta, silakan ikuti langkah-langkah berikut:

1. Fork repositori ini.
2. Buat cabang (branch) baru untuk fitur atau perbaikan yang akan kamu buat.
3. Lakukan commit perubahan dan push ke repositori forked.
4. Buat pull request ke repositori utama.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).



### Penjelasan:
- **Makna Nama Tirta**: Menjelaskan bahwa nama **Tirta** diambil dari kata dalam bahasa Sanskerta yang berarti "air" atau "sumber kehidupan". Ini menggambarkan peran AI yang hadir untuk memberikan solusi dan informasi seperti air yang mengalir, yang selalu ada dan mudah diakses.
- **Relevansi Nama dengan Proyek**: Penjelasan ini juga menghubungkan filosofi nama dengan tujuan dari aplikasi AI, yaitu memberikan solusi yang selalu ada dan mudah diakses.

Dengan menambahkan penjelasan seperti ini, orang-orang yang melihat repositori kamu akan lebih memahami arti di balik nama tersebut dan bagaimana nama itu mencerminkan tujuan aplikasi.


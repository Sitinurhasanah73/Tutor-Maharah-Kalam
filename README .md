# 🕌 Tahaddas Ma'ana (تَحَدَّثْ مَعَنَا)
**Proyek Chatbot Pembelajaran Bahasa Arab Berbasis AI**

Repositori ini dibuat untuk memenuhi tugas Ujian Akhir Semester (UAS) mata kuliah terkait pemanfaatan AI dalam pembelajaran pada Program Studi Pendidikan Bahasa Arab.

## 👤 Identitas Mahasiswa
*   **Nama:** Siti Nurhasanah
*   **NIM:** [1232030176]
*   **Program Studi:** Pendidikan Bahasa Arab
*   **Semester:** 6

---

## 🎯 Fokus Pembelajaran (Maharah & Level)
*   **Maharah:** Kalam (Berbicara)
*   **Persona Tutor:** Ustadzah Noor & Ustadzah Hasanah (Muhadatsah Bot)
*   **Level Target:** Menengah (Siswa MTs Kelas VIII)

**Alasan Pemilihan:**
Maharah Kalam seringkali menjadi tantangan terbesar bagi siswa karena adanya rasa takut salah dalam mengucapkan tata bahasa (*Nahwu/Sharaf*). Chatbot ini dirancang dengan pendekatan *gentle correction* agar siswa MTs Kelas VIII dapat berlatih merangkai kalimat dan membangun kepercayaan diri dalam simulasi percakapan sehari-hari tanpa merasa dihakimi.

---

## 🤖 Layanan API & Teknologi
Aplikasi ini dibangun menggunakan bahasa pemrograman Python (versi 3.8+) dan mengintegrasikan layanan Kecerdasan Buatan berikut:
*   **API Model:** Google Gemini API (`gemini-2.5-flash`) via Google GenAI SDK.
*   **Antarmuka Pengguna (UI):** Streamlit (Web Framework) sebagai peningkatan visual interaktif.

---

## ✨ Fitur-Fitur Tersedia
Aplikasi ini telah memenuhi spesifikasi teknis dan fitur minimum yang diwajibkan:
1.  **Antarmuka Percakapan Interaktif:** Dibangun secara visual menggunakan Streamlit dengan tampilan obrolan (*chat interface*) yang elegan dan responsif.
2.  **Riwayat Percakapan (Conversation History):** Menggunakan `st.session_state` sehingga alur percakapan dalam satu sesi terus terekam dan berkesinambungan.
3.  **Tiga Mode Pembelajaran:**
    *   **Mode 1:** الساعة (Materi Jam & Bilangan Bertingkat / *'Adad Tartibi*).
    *   **Mode 2:** يومياتنا (Aktivitas Sehari-hari & *Jumlah Ismiyyah*).
    *   **Mode 3:** الْهِوَايَةُ (Hobi & Waktu Luang).
4.  **Pesan Pembuka (Greeting):** Chatbot secara otomatis menyapa pengguna menggunakan bahasa Arab berharakat dan bahasa Indonesia pada awal sesi.
5.  **Perintah Keluar / Reset Sesi:** Terdapat tombol khusus "🗑️ Hapus Obrolan" untuk mengakhiri dan mengatur ulang sesi percakapan dari awal.

---

## 🛠️ Cara Instalasi dan Menjalankan Aplikasi

**1. Persiapan Repositori**
Pastikan Anda telah mengkloning repositori ini ke komputer lokal Anda:
```bash
git clone [https://github.com/username/nama-proyek.git](https://github.com/username/nama-proyek.git)
cd nama-proyek
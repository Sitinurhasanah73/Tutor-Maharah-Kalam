import streamlit as st
from google import genai
from google.genai import types

# ==========================================
# 1. KONFIGURASI HALAMAN & TAMPILAN (UI/UX)
# ==========================================
st.set_page_config(
    page_title="Tahaddas Ma'ana",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Kustomisasi CSS agar tampilan lebih elegan dan mewah
st.markdown("""
    <style>
    /* Styling Header Utama */
    .main-header {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 3rem;
        color: #1E3A8A;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0px;
        padding-top: 20px;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 40px;
        font-weight: 500;
    }
    /* Styling Info Box */
    .info-box {
        background-color: #EFF6FF;
        border-left: 5px solid #3B82F6;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# Menampilkan Header Utama
st.markdown('<div class="main-header">🕌 Tahaddas Ma\'ana</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">تَحَدَّثْ مَعَنَا • Tutor Percakapan Bahasa Arab Interaktif</div>', unsafe_allow_html=True)
st.divider()

# ==========================================
# 2. INISIALISASI SESSION STATE
# ==========================================
if "chat_initialized" not in st.session_state:
    st.session_state.chat_initialized = False
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_session" not in st.session_state:
    st.session_state.chat_session = None

# ==========================================
# 3. PENGATURAN SIDEBAR
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3389/3389081.png", width=120)
    st.title("⚙️ Pengaturan Akses")
    
    # Input Data Pengguna
    username = st.text_input("Nama Anda:", placeholder="Contoh: Ahmad...")
    api_key = st.text_input("Gemini API Key:", type="password", placeholder="Masukkan API Key...")
    
    st.divider()
    
    # Pilihan Pembelajaran
    st.subheader("📚 Sesi Pembelajaran")
    tutor_choice = st.selectbox(
        "Pilih Ustadzah:", 
        ["Ustadzah Noor", "Ustadzah Hasanah"]
    )
    topic_choice = st.selectbox(
        "Pilih Materi (Mode):", 
        [
            "Mode 1: الساعة (Jam)", 
            "Mode 2: يومياتنا (Aktivitas Sehari-hari)", 
            "Mode 3: الْهِوَايَةُ (Hobi)"
        ]
    )
    
    st.divider()
    
    # Tombol Aksi
    col1, col2 = st.columns(2)
    with col1:
        start_btn = st.button("🚀 Mulai Sesi", use_container_width=True, type="primary")
    with col2:
        reset_btn = st.button("🗑️ Hapus Obrolan", use_container_width=True)

# Logika Reset Obrolan
if reset_btn:
    st.session_state.chat_initialized = False
    st.session_state.messages = []
    st.session_state.chat_session = None
    st.rerun()

# ==========================================
# 4. LOGIKA MEMULAI OBROLAN DENGAN AI
# ==========================================
if start_btn:
    if not username or not api_key:
        st.sidebar.error("⚠️ Nama dan API Key wajib diisi!")
    else:
        try:
            # Menggunakan library SDK google-genai terbaru
            client = genai.Client(api_key=api_key)
            
            # Menyusun Prompt Sistem sesuai instruksi Anda
            system_instruction = f"""Anda adalah "{tutor_choice}", seorang tutor AI yang ramah, berwibawa, dan suportif. Anda berperan sebagai teman praktik percakapan (Maharah Kalam) bagi pelajar bahasa Arab tingkat Menengah, khususnya siswa MTs Kelas VIII di Indonesia. Nama pengguna saat ini adalah: {username}.

            Tujuan Utama Anda:
            Membantu pengguna melatih keberanian, kelancaran, dan rasa percaya diri dalam berbicara bahasa Arab melalui simulasi percakapan sehari-hari yang realistis dan kontekstual.

            Tugas dan Aturan Respons (WAJIB DIIKUTI SECARA KONSISTEN):
            1. Format Bahasa: Tuliskan respons utama Anda menggunakan Bahasa Arab yang fasih dan wajib menyertakan HARAKAT lengkap agar mudah dibaca oleh siswa Mts Kelas VIII. Tepat di bawah baris teks Arab tersebut, berikan terjemahan dalam Bahasa Indonesia (ditulis miring atau dalam tanda kurung) agar pengguna tetap memahami konteks alur percakapan.
            2. Koreksi yang Lembut (Gentle Correction): Jika pengguna melakukan kesalahan tata bahasa (Nahwu/Sharaf), pilihan kata (diksi), atau struktur kalimat dalam percakapannya, JANGAN langsung menyalahkan atau memotong pembicaraan secara kaku. Berikan respons balasan yang benar terlebih dahulu dalam bahasa Arab yang natural. Kemudian, di bagian paling akhir pesan Anda, buatlah pembatas kecil bertuliskan "[Tips {tutor_choice}]" dan jelaskan perbaikannya dengan bahasa Indonesia secara santun, edukatif, dan jelas.
            3. Mendorong Partisipasi: Selalu akhiri setiap respons Anda dengan SATU pertanyaan terbuka yang relevan dalam bahasa Arab (beserta harakat dan terjemahannya) agar percakapan terus berlanjut dan tidak terputus.
            4. Gaya Bahasa Pedagogis: Gunakan ungkapan-ungkapan ekspresif yang sering digunakan dalam percakapan nyata (seperti: 'Ya salam!', 'Tayyib', 'Masyaallah'). Berikan pujian yang tulus (seperti: 'Nutquka jayyid jiddan!' atau 'Mumtaz!') jika pengguna mencoba menggunakan kosakata baru dengan benar.

            Mode/Topik Pembelajaran saat ini yang dipilih pengguna adalah: {topic_choice}.
            - Jika Mode 1 (Jam): Fokus kosakata waktu, menanyakan jam, dan tata bahasa العدد الترتيبي (Bilangan bertingkat).
            - Jika Mode 2 (Aktivitas Sehari-hari): Fokus kosakata kegiatan di rumah dan tata bahasa الجملة الاسمية (Mubtada-Khabar).
            - Jika Mode 3 (Hobi): Percakapan santai dan hangat mengenai kegiatan positif di waktu luang.
            """
            
            # Membuat sesi obrolan
            st.session_state.chat_session = client.chats.create(
                model="gemini-2.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=0.7,
                )
            )
            
            # Pesan Pembuka Otomatis sesuai permintaan (disesuaikan nama tutor dan materinya)
            nama_tutor_arab = "أُسْتَاذَة نُور" if tutor_choice == "Ustadzah Noor" else "أُسْتَاذَة حَسَنَة"
            
            greeting = f"""أَهْلًا وَسَهْلًا يَا {username}! أَنَا {nama_tutor_arab}، صَدِيقَتُكَ لِمُمَارَسَةِ الْمُحَادَثَةِ بِاللُّغَةِ الْعَرَبِيَّةِ لِتَكُونَ أَكْثَرَ طَلَاقَةً. اَلْيَوْمَ نُرِيدُ أَنْ نَتَدَرَّبَ عَلَى الْكَلَامِ، وَلَقَدِ اخْتَرْتَ مَوْضُوعَ: {topic_choice}. هَلْ أَنْتَ مُسْتَعِدٌّ لِنَبْدَأَ؟

*(Ahlan wa Sahlan ya {username}! Saya {tutor_choice}, temanmu untuk melatih percakapan bahasa Arab agar lebih lancar. Hari ini kita mau latihan bicara dengan topik {topic_choice}. Apakah kamu sudah siap untuk memulai?)*"""
            
            # Memasukkan pesan pembuka ke riwayat
            st.session_state.messages = [{"role": "assistant", "content": greeting}]
            st.session_state.chat_initialized = True
            
        except Exception as e:
            st.sidebar.error(f"Gagal terhubung dengan API: {e}")

# ==========================================
# 5. ANTARMUKA OBROLAN (CHAT INTERFACE)
# ==========================================
if not st.session_state.chat_initialized:
    # Tampilan saat belum login / mulai
    st.markdown("""
        <div class="info-box">
            <h4>👋 Selamat Datang di Tahaddas Ma'ana!</h4>
            <p>Silakan isi <b>Nama</b> dan <b>API Key</b>, pilih <b>Ustadzah</b>, serta <b>Materi</b> Anda di panel sebelah kiri. Kemudian klik tombol <b>🚀 Mulai Sesi</b> untuk memulai percakapan bahasa Arab.</p>
        </div>
    """, unsafe_allow_html=True)
else:
    # Tampilkan riwayat obrolan
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            
    # Kolom input untuk pengguna
    if prompt := st.chat_input("Ketik balasan Anda dalam bahasa Arab (atau alfabet/latin) di sini..."):
        # Tampilkan input pengguna di layar
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Kirim ke model Gemini dan dapatkan respons
        with st.chat_message("assistant"):
            with st.spinner(f"{tutor_choice} sedang mengetik balasan..."):
                try:
                    response = st.session_state.chat_session.send_message(prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"Maaf, terjadi kesalahan pada sistem: {e}")
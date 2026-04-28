import streamlit as st

st.title("Sistem Pakar Pemilihan Jurusan Kuliah")
st.write("Jawablah pertanyaan berikut sesuai dengan minat dan kemampuan Anda:")

st.subheader("Karakteristik & Minat Anda:")
berhitung = st.checkbox("Saya suka berhitung dan logika matematika")
menulis = st.checkbox("Saya suka menulis atau membaca")
teknologi = st.checkbox("Saya sangat tertarik dengan teknologi dan gadget")
gambar = st.checkbox("Saya memiliki hobi menggambar atau mendesain")
interaksi = st.checkbox("Saya senang berinteraksi dan bicara dengan orang lain")

if st.button("Cek Rekomendasi Jurusan"):
    rekomendasi = []
    
    if berhitung and teknologi:
        rekomendasi.append("Teknik Informatika / Sistem Informasi")
    
    if menulis and interaksi:
        rekomendasi.append("Ilmu Komunikasi / Hubungan Internasional")
        
    if berhitung and interaksi:
        rekomendasi.append("Akuntansi / Manajemen Bisnis")
        
    if gambar and teknologi:
        rekomendasi.append("Desain Komunikasi Visual (DKV)")
        
    if menulis and gambar:
        rekomendasi.append("Arsitektur / Desain Interior")

    st.divider()
    if rekomendasi:
        st.success("Berdasarkan minat Anda, jurusan yang cocok adalah:")
        for r in rekomendasi:
            st.write(f"- **{r}**")
    else:
        st.warning("Maaf, sistem belum menemukan jurusan yang pas. Coba pilih kombinasi minat yang lain.")
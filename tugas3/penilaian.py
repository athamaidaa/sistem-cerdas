import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sistem Penilaian Mahasiswa", layout="wide")

if 'data_mahasiswa' not in st.session_state:
    st.session_state.data_mahasiswa = pd.DataFrame(columns=['Nama', 'Nilai', 'Keterangan'])

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("Login Sistem Akademik")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "123":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Username atau password salah")
else:
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False}))
    st.title("Sistem Penilaian Mahasiswa (Rule-Based)")

    with st.expander("Tambah/Edit Nilai Mahasiswa"):
        nama = st.text_input("Nama Mahasiswa")
        nilai = st.number_input("Masukkan Nilai (0-100)", min_value=0, max_value=100, step=1)
        
        if st.button("Simpan Data"):
            if nama:

                if nilai >= 75:
                    keterangan = "LULUS"
                else:
                    keterangan = "TIDAK LULUS"
                
                new_data = pd.DataFrame([[nama, nilai, keterangan]], columns=['Nama', 'Nilai', 'Keterangan'])
                st.session_state.data_mahasiswa = pd.concat([st.session_state.data_mahasiswa, new_data], ignore_index=True)
                st.success(f"Data {nama} berhasil disimpan!")
            else:
                st.warning("Nama tidak boleh kosong")

    st.subheader("Daftar Nilai Mahasiswa")
    if not st.session_state.data_mahasiswa.empty:
        st.table(st.session_state.data_mahasiswa)
        
        if st.button("Hapus Semua Data"):
            st.session_state.data_mahasiswa = pd.DataFrame(columns=['Nama', 'Nilai', 'Keterangan'])
            st.rerun()
    else:
        st.info("Belum ada data mahasiswa.")
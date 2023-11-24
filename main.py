import streamlit as st 
from streamlit_option_menu import option_menu

with st.sidebar:
    st.title("Aplikasi Kalkulator Sederhana")
    selected = option_menu("Pilih Operasi  Aritmatika", 
            ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"], 
            default_index=0)

if selected == "Penjumlahan":
    st.title("Penjumlahan")
    Angka1 = st.number_input("Masukkan Nilai Pertama")
    Angka2 = st.number_input("Masukkan Nilai Kedua")

    hitung = st.button("Hitung")

    if hitung:
        Hasil = Angka1 + Angka2
        st.success(f"Jadi {Angka1} + {Angka2} Adalah {Hasil}")


if selected == "Pengurangan":
    st.title("Pengurangan")
    Angka1 = st.number_input("Masukkan Nilai Pertama")
    Angka2 = st.number_input("Masukkan Nilai Kedua")

    hitung = st.button("Hitung")

    if hitung:
        Hasil = Angka1 - Angka2
        st.success(f"Jadi {Angka1} - {Angka2} Adalah {Hasil}")
        
        
if selected == "Perkalian":
    st.title("Perkalian")
    Angka1 = st.number_input("Masukkan Nilai Pertama")
    Angka2 = st.number_input("Masukkan Nilai Kedua")

    hitung = st.button("Hitung")

    if hitung:
        Hasil = Angka1 * Angka2
        st.success(f"Jadi {Angka1} * {Angka2} Adalah {Hasil}")
        
        
if selected == "Pembagian":
    st.title("Pembagian")
    Angka1 = st.number_input("Masukkan Nilai Pertama")
    Angka2 = st.number_input("Masukkan Nilai Kedua")

    hitung = st.button("Hitung")

    if hitung:
        Hasil = Angka1 / Angka2
        st.success(f"Jadi {Angka1} / {Angka2} Adalah {Hasil}")
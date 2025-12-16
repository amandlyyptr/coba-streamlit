import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Coba Deploy Streamlit",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Coba Deploy Streamlit")
st.write("Kalau halaman ini muncul online, berarti deploy BERHASIL 🎉")

st.header("📊 Contoh Data Acak")

# bikin data dummy
df = pd.DataFrame({
    "X": np.arange(1, 11),
    "Y": np.random.randint(10, 100, 10)
})

st.dataframe(df)

st.header("📈 Grafik Sederhana")
st.line_chart(df)

st.success("Streamlit berhasil dijalankan!")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# FULL WIDTH
st.set_page_config(page_title="Dashboard Hotspot", layout="wide")

st.title("Dashboard Monitoring Hotspot")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip()

    # =========================
    # 🔹 METRIC (ATAS)
    # =========================
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Login", int(df['login'].sum()))
    col2.metric("Total Logout", int(df['logout'].abs().sum()))
    col3.metric("User Aktif Tertinggi", int(df['active'].max()))

    st.markdown("---")

    # =========================
    # 🔹 GRAFIK BESAR
    # =========================
    df_sampled = df.iloc[::6, :].copy()

    waktu = df_sampled['time']
    x = np.arange(len(waktu))
    lebar = 0.25

    fig, ax = plt.subplots(figsize=(20, 8))  # 🔥 BESAR

    ax.bar(x - lebar, df_sampled['active'], lebar, label='User Aktif')
    ax.bar(x, df_sampled['login'], lebar, label='Login')
    ax.bar(x + lebar, df_sampled['logout'], lebar, label='Logout')

    ax.set_title('Aktivitas Hotspot (Interval 30 Menit)', fontsize=18)
    ax.set_xlabel('Waktu', fontsize=12)
    ax.set_ylabel('Jumlah User', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(waktu, rotation=45)

    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    st.pyplot(fig, use_container_width=True)  # 🔥 FULL WIDTH

    st.markdown("---")

    # =========================
    # 🔹 DATA (OPTIONAL)
    # =========================
    with st.expander("📂 Lihat Data"):
        st.dataframe(df)

else:
    st.info("Upload file CSV untuk melihat dashboard")
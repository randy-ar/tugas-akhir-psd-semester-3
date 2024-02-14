import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor

# st.header(Path(__file__).resolve())
st.title("Prediksi Jumlah Kebutuhan Peminjaman Sepeda Menggunakan Methode Regresi")

df = pd.read_csv(str(Path(__file__).resolve().parent)+"/hour.csv") # Membaca data set hour.csv
# Menganti nama kolom
df = df.rename(columns={'weathersit':'weather',
                       'yr':'year',
                       'mnth':'month',
                       'hr':'hour',
                       'hum':'humidity',
                       'cnt':'count'})
df = df.drop(columns = ['instant' , 'dteday' , 'year']) # hapus kolom yang tidak diperlukan
# Membuat list kolom
cols = ['season' , 'month' , 'hour' , 'holiday' , 'weekday' , 'workingday' , 'weather']
# Mengganti Dtype kolom menjadi Dtype Category
for col in cols:
    df[col] = df[col].astype('category')



st.markdown("### 1. Pengaruh Penggunaaan Sepeda Selama Hari Kerja dan Hari Libur")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='count', hue='weekday', ax=ax)
ax.set(title='Jumlah sepeda selama weekdays dan weekends')
st.pyplot(fig)
st.markdown(f"<p style='font-size:11px;'>Dari grafik ini kita dapat lihat jika penggunaan sepeda dominan ada dihari kerja, tepatnya pada jam berangkat kerja dan pulang kerja. Informasi ini dapat digunakan untuk memprediksi kenaikan kebutuhan peminjaman sepeda pada jam berangkat kerja dan pulang kerja.</p>")

st.markdown("### 2. Pengaruh Penggunaaan Sepeda Terdaftar Selama Hari Kerja dan Hari Libur")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur pada pengguna yang tidak terdaftar
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='casual', hue='weekday', ax=ax)
ax.set(title='Jumlah sepeda selama weekdays dan weekends pada pengguna yang tidak terdaftar')
st.pyplot(fig)
st.markdown(f"<p style='font-size:11px;'>Dari grafik ini kita dapat lihat jika penggunaan sepeda yang tidak terdaftar dominan ada dihari libur. Informasi ini dapat digunakan untuk memprediksi kenaikan kebutuhan peminjaman pengguna yang tidak terdaftar pada hari libur dan penurunan kebutuhan peminjaman sepeda pada pengguna yang tidak terdaftar.</p>")

st.markdown("### 3. Pengaruh Penggunaaan Sepeda Tidak Terdaftar Selama Hari Kerja dan Hari Libur")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur pada pengguna yang terdaftar
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='registered', hue='weekday', ax=ax)
ax.set(title='Jumlah sepeda selama weekdays dan weekends pada pengguna yang tidak terdaftar')
st.pyplot(fig)
st.markdown(f"<p style='font-size:11px;'>Dari grafik ini kita dapat lihat jika penggunaan sepeda yang terdaftar dominan ada dihari kerja. Informasi ini dapat digunakan untuk memprediksi kenaikan dan penurunan kebutuhan peminjaman sepeda pada pengguna yang terdaftar.</p>")

st.markdown("### 4. Pengaruh Penggunaaan Sepeda Pada Setiap Kondisi Cuaca")
# Melihat pengaruh penggunaaan sepeda pada setiap cuaca
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='count', hue='weather', ax=ax)
ax.set(title='Jumlah sepeda pada setiap cuaca')
st.markdown(f"<p style='font-size:11px;'>Dari grafik ini kita dapat lihat jika tren penggunaan sepeda menurun cukup banyak pada musim dingin. Informasi ini dapat digunakan untuk memprediksi penurunan tren peminjaman sepeda pada musim dingin.</p>")


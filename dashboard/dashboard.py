import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor

# st.header(Path(__file__).resolve())
st.header("Prediksi Jumlah Kebutuhan Peminjaman Sepeda Menggunakan Methode Regresi")

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

st.subheader("Pengaruh Penggunaaan Sepeda Selama Hari Kerja dan Hari Libur")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='count', hue='weekday', ax=ax)
ax.set(title='Jumlah sepeda selama weekdays dan weekends')

st.pyplot(fig)
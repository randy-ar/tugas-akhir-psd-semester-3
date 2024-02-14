import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor
from statsmodels.graphics.gofplots import qqplot
from sklearn.model_selection import train_test_split

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



st.markdown("### 1. Pengaruh Hari Kerja dan Hari Libur Penggunaaan Sepeda")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='count', hue='weekday', ax=ax)
ax.set(title='Jumlah sepeda selama weekdays dan weekends')
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika penggunaan sepeda dominan ada dihari kerja, tepatnya pada jam berangkat kerja dan pulang kerja. Informasi ini dapat digunakan untuk memprediksi kenaikan kebutuhan peminjaman sepeda pada jam berangkat kerja dan pulang kerja.</p>", unsafe_allow_html = True)

st.markdown("### 2. Pengaruh Hari Kerja dan Hari Libur Pada Penggunaaan Sepeda Terdaftar")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur pada pengguna yang tidak terdaftar
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='casual', hue='weekday', ax=ax)
ax.set(title='Jumlah sepeda selama weekdays dan weekends pada pengguna yang tidak terdaftar')
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika penggunaan sepeda yang tidak terdaftar dominan ada dihari libur. Informasi ini dapat digunakan untuk memprediksi kenaikan kebutuhan peminjaman pengguna yang tidak terdaftar pada hari libur dan penurunan kebutuhan peminjaman sepeda pada pengguna yang tidak terdaftar.</p>", unsafe_allow_html = True)

st.markdown("### 3. Pengaruh Hari Kerja dan Hari Libur Pada Penggunaaan Sepeda Tidak Terdaftar")
# Melihat pengaruh penggunaaan sepeda selama hari kerja dan hari libur pada pengguna yang terdaftar
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='registered', hue='weekday', ax=ax)
ax.set(title='Jumlah sepeda selama weekdays dan weekends pada pengguna yang tidak terdaftar')
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika penggunaan sepeda yang terdaftar dominan ada dihari kerja. Informasi ini dapat digunakan untuk memprediksi kenaikan dan penurunan kebutuhan peminjaman sepeda pada pengguna yang terdaftar.</p>", unsafe_allow_html = True)

st.markdown("### 4. Pengaruh Setiap Kondisi Cuaca Pada  Penggunaaan Sepeda")
# Melihat pengaruh penggunaaan sepeda pada setiap cuaca
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=df, x='hour', y='count', hue='weather', ax=ax)
ax.set(title='Jumlah sepeda pada setiap cuaca')
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika tren penggunaan sepeda menurun cukup banyak pada musim dingin. Informasi ini dapat digunakan untuk memprediksi penurunan tren peminjaman sepeda pada musim dingin.</p>", unsafe_allow_html = True)


st.markdown("### 5. Tren Penggunaaan Sepeda Setiap Bulan")
# Melihat pengaruh penggunaaan sepeda pada setiap bulan
fig, ax = plt.subplots(figsize=(20,5))
sns.barplot(data=df, x='month', y='count', ax=ax)
ax.set(title='Jumlah sepeda pada setiap bulan')
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat jika tren penggunaan sepeda menurun pada awal dan akhir tahun. Informasi ini dapat digunakan untuk memprediksi penurunan tren peminjaman sepeda pada awal dan akhir tahun.</p>", unsafe_allow_html = True)


st.markdown("### 6. Tren Penggunaaan Sepeda Setiap Hari")
# Melihat pengaruh penggunaaan sepeda pada setiap hari
fig, ax = plt.subplots(figsize=(20,5))
sns.barplot(data=df, x='weekday', y='count', ax=ax)
ax.set(title='Jumlah sepeda pada setiap hari')
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Dari grafik ini kita dapat lihat tidak ada perbedaan signifikan pada tren penggunaan sepeda pada tiap hari</p>", unsafe_allow_html = True)

st.markdown("### 7. Relasi Antara Temperatur dan Kelembapan Pada Jumlah Peminjaman Sepeda")
# Melihat relasi antara temperatur dan kelembapan pada jumlah peminjaman sepeda
fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(20,5))
sns.regplot(x=df['temp'], y=df['count'], ax=ax1 ,color='red')
ax1.set(title="Relasi antara temperatur dan pengguna")
sns.regplot(x=df['humidity'], y=df['count'], ax=ax2)
ax2.set(title="Relasi antara kelembapan dan pengguna")
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Grafik ini menunjukan tidak ada relasi yang sangat kuat pada temperatur dan kelembapan pada jumlah peminjaman sepeda, terbukti titik sangat jauh dari garis linear regresi.</p>", unsafe_allow_html = True)


st.markdown("### Distribusi Peminjaman Sepeda")
# Melihat distribusi user
fig, (ax1,ax2) = plt.subplots(ncols=2, figsize=(20,5))
sns.histplot(df['count'], ax=ax1 , color ='red', kde=True)
ax1.set(title='Distribusi user')
qqplot(df['count'], ax=ax2, line='s')
ax2.set(title='Kuantil teoritis')
st.pyplot(fig)
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Grafik ini menunjukan distribusi user dan kuantil teoritis. Terlihat jika data cukup linear dengan garis linear, menujukan pegaruh yang cukup kuat antar variable pada jumlah peminjaman sepeda.</p>", unsafe_allow_html = True)


# One Hot Encoding
# one hot encoding untuk kolom season
pd.get_dummies(df['season'], prefix='season', drop_first=True)
# one hot encoding untuk kolom lain, season, month, hour, holiday, weekday, workingday, weather

df_oh = df

def one_hot_encoding(data, column):
    data = pd.concat([data, pd.get_dummies(data[column], prefix=column, drop_first=True)], axis=1)
    data = data.drop([column], axis=1)
    return data

cols = ['season','month','hour','holiday','weekday','workingday','weather']

for col in cols:
    df_oh = one_hot_encoding(df_oh, col)
# Membuang kolom yang tidak diperlukan
X = df_oh.drop(columns=['atemp', 'windspeed', 'casual', 'registered', 'count'], axis=1)
y = df_oh['count']

# Memecah data untuk data train dan data test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
loaded_model = joblib.load(str(Path(__file__).resolve().parent)+"/my_random_forest.joblib")
# Membuat prediksi dari model
y_pred = loaded_model.predict(X_test)
# Melihat error yang dihasilkan prediksi
error = y_test - y_pred

st.markdown("### Hasil Prediksi Menggunakan Algoritma Random Forest Regressor")
# Menampilkan Hasil error regresi
fig, ax = plt.subplots()
ax.scatter(y_test, error ,color = 'red')
ax.axhline(lw=3, color='black')
ax.set_xlabel('Observed')
ax.set_ylabel('Error')
st.markdown(f"<p style='font-size:12px; font-color:#868686;'>Grafik ini adalah hasil regresi dari prediksi model latih menggunakan algoritma Random Forest Regressor. Jika dilihat dari data titik terhadap garis regresi cukup berdekatan yang mengindikasi jika prediksi model cukup akurat.</p>", unsafe_allow_html = True)
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv(str(Path(__file__).resolve().parent)+"/data_hour.csv") # Membaca data set hour.csv
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

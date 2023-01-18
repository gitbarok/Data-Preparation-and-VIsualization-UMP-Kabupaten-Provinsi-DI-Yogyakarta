import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/processed/DI-Yogyakarta Minimum Wage.csv')

st.title('Visualisasi Sederhana UMP Kabupaten di Provinsi DI Yogyakarta Tahun 2013-2022')
st.dataframe(df)

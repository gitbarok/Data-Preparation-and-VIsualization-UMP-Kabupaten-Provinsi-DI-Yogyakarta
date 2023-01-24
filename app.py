import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import json

#Load Data
df = pd.read_csv('data/processed/DI-Yogyakarta Minimum Wage.csv')
with open('data/processed/yogyakarta.geojson') as f:
    district = json.load(f)



#Streamlit App
st.title('Visualisasi Sederhana UMP Kabupaten di Provinsi DI Yogyakarta')
tahun = list(df['tahun'].unique())
choice = st.selectbox('Pilih Tahun!', options=tahun)
df_choice = df[df['tahun']==choice]

st.header(f":money_with_wings: Upah Minimum Kabupaten di Provinsi DI Yogyakarta Tahun {choice}")
#Geographic Map
fig = go.Figure(
    go.Choroplethmapbox(
        geojson=district,
        locations=df_choice.kabupaten,
        featureidkey="properties.region",
        colorscale="Bluered",
        z=df_choice.upah_minimum,
        marker_opacity=0.5,   
        marker_line_width=0,
        colorbar={"orientation": "h", "tickformat":",.0f", "tickprefix":"Rp "},
    )
)


fig.update_geos(fitbounds='locations', visible=False)
fig.update_layout(
    mapbox_center = {'lat':-7.871236995632798, 'lon':110.42614574441643},
    mapbox_style="carto-positron",
    mapbox_zoom=9,
    width=700,
    height=600,
    
)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
st.plotly_chart(fig)

fig = px.line(
    df, x='tahun', y='upah_minimum', color='kabupaten', markers=True, title=f'Riwayat Kenaikan Upah Minimum Provinsi DI-Yogyakarta (UMP) Tahun <br> 2012-2022'
)
st.plotly_chart(fig)

fig = px.line(
    df, x='tahun', y='different_amount_yearly', color='kabupaten', markers=True, title=f'Riwayat Jumlah Perbedaan Kenaikan Upah Minimum Provinsi DI-Yogyakarta (UMP) Tahun <br> 2012-2022'
)
st.plotly_chart(fig)


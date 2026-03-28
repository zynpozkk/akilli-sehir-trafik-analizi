import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np

def display_city_map(lat, lon, average_density):
    # Noktaları kara içine hapsetmek için çok küçük bir sapma (0.007) kullanıyoruz
    np.random.seed(int(lat * 100)) 
    data = pd.DataFrame({
        'lat': lat + np.random.uniform(-0.007, 0.007, 15),
        'lon': lon + np.random.uniform(-0.007, 0.007, 15),
        'density': np.random.randint(30, 100, 15)
    })

    def get_color(d):
        if 30 <= d < 60: return [255, 255, 0, 180]   # SARI
        if 60 <= d < 80: return [0, 255, 0, 180]     # YEŞİL
        if d >= 80: return [255, 0, 0, 180]          # KIRMIZI
        return [180, 180, 180, 120]

    data['color'] = data['density'].apply(get_color)

    view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=12.5, pitch=0)
    
    layer = pdk.Layer(
        "ScatterplotLayer",
        data,
        get_position='[lon, lat]',
        get_color='color',
        get_radius=150, # Noktalar sokak içinde kalsın diye küçültüldü
        pickable=True
    )

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="road" # Yol haritası altlığı zorunlu kılındı
    ))
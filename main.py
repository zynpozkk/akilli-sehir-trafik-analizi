import streamlit as st
import matplotlib.pyplot as plt
import time
from services.city_factory import CityFactory
from services.traffic_service import TrafficService
from services.analysis_strategy import DensityAnalysis
from utils.map_tool import display_city_map

def run():
    st.set_page_config(page_title="Trafik Analizi", layout="centered")
    st.title("🏙️ Akıllı Şehir Canlı Yoğunluk Paneli")
    
    city_name = st.sidebar.selectbox("Şehir Seçin", ["Ankara", "İstanbul", "İzmir"])
    auto_refresh = st.sidebar.checkbox("Otomatik Yenileme", value=True)
    
    city = CityFactory.get_city(city_name)
    placeholder = st.empty()

    while True:
        service = TrafficService(DensityAnalysis())
        report = service.get_city_report(city.name, city.lat, city.lon)
        
        with placeholder.container():
            # ÜSTTE: HARİTA
            st.subheader(f"📍 {city.name} Yoğunluk Haritası")
            display_city_map(city.lat, city.lon, report.average_density)
            
            st.markdown("---")
            
            # ALTA: METRİK VE SÜTUN GRAFİĞİ
            st.subheader("📊 Trafik Analiz Raporu")
            st.metric("Anlık Ortalama Yoğunluk", f"%{report.average_density:.2f}")

            fig, ax = plt.subplots(figsize=(10, 4))
            colors = ['red' if x >= 80 else 'green' if x >= 60 else 'yellow' for x in report.density_df["density"]]
            ax.bar(report.density_df["hour"], report.density_df["density"], color=colors)
            st.pyplot(fig)

        if not auto_refresh: break
        time.sleep(30)
        st.rerun()

if __name__ == "__main__":
    run()
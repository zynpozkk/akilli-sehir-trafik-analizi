import requests
import pandas as pd
import numpy as np
from models.traffic_data import TrafficReport

class TrafficService:
    def __init__(self, strategy):
        self.strategy = strategy

    def get_city_report(self, city_name, lat, lon):
        # f-string ile her şehre özel koordinatlar API'ye gönderilir
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=relative_humidity_2m"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            values = data['hourly']['relative_humidity_2m'][:24]
            raw_df = pd.DataFrame({"hour": list(range(24)), "density": values})
        except Exception:
            # Hata durumunda şehre özel farklı veriler üretilir
            np.random.seed(int(lat))
            raw_df = pd.DataFrame({"hour": np.arange(24), "density": np.random.randint(30, 100, 24)})
            
        return TrafficReport(city_name, self.strategy.analyze(raw_df), raw_df["density"].mean())
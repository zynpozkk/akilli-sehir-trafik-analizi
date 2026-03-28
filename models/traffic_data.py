from dataclasses import dataclass
import pandas as pd

@dataclass
class TrafficReport:
    city_name: str
    density_df: pd.DataFrame
    average_density: float
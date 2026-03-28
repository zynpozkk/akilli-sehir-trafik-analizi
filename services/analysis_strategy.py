from abc import ABC, abstractmethod
import pandas as pd

class TrafficAnalysisStrategy(ABC):
    @abstractmethod
    def analyze(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        pass

class DensityAnalysis(TrafficAnalysisStrategy):
    def analyze(self, raw_data: pd.DataFrame) -> pd.DataFrame:
        raw_data["density"] = raw_data["density"].fillna(0)
        return raw_data.groupby("hour")["density"].mean().reset_index()
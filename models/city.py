from dataclasses import dataclass

@dataclass
class City:
    name: str
    lat: float
    lon: float
    zoom_level: int
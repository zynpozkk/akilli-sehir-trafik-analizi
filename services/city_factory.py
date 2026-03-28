from models.city import City

class CityFactory:
    @staticmethod
    def get_city(city_name: str) -> City:
        cities = {
            "Ankara": City("Ankara", 39.9208, 32.8541, 12),
            "İstanbul": City("İstanbul", 41.0700, 28.9850, 11), 
            "İzmir": City("İzmir", 38.4650, 27.2050, 11)      
        }
        return cities.get(city_name)
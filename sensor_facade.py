from sensor_repository import SensorRepository

class SensorFacade:
    def __init__(self):
        self.repository = SensorRepository()

    def get_all_data(self):
        """Obtiene todos los datos de sensores."""
        return self.repository.read_all()

    def get_data_by_zone(self, zone):
        """Devuelve los datos filtrados por zona (ignorando mayúsculas/minúsculas)."""
        data = self.get_all_data()
        return [entry for entry in data if entry.get('zone', '').lower() == zone.lower()]

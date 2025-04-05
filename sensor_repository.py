import json
import os

class SensorRepository:
    def __init__(self, data_file='sensor_data.json'):
        self.data_file = data_file

    def read_all(self):
        """Lee y devuelve todos los datos del archivo JSON."""
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
        return data

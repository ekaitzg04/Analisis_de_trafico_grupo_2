import unittest
import json
from app import app


class SensorAPITestCase(unittest.TestCase):
    def setUp(self):
        # Configuramos el cliente de pruebas de Flask
        self.client = app.test_client()

    def test_get_all_sensors(self):
        # Prueba que al llamar al endpoint sin zona se devuelvan todos los datos
        response = self.client.get('/obtener_datos_sensores')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        # Comprobamos que se devuelve una lista
        self.assertIsInstance(data, list)
        # Se asume que el JSON tiene al menos un registro
        self.assertGreater(len(data), 0)

    def test_get_sensor_data_by_zone_salburua(self):
        # Prueba para obtener datos de la zona "salburua"
        response = self.client.get('/obtener_datos_sensores/salburua')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIsInstance(data, list)
        # Validamos que todos los registros correspondan a la zona "salburua"
        for entry in data:
            self.assertEqual(entry.get('zone').lower(), 'salburua')

    def test_get_sensor_data_by_zone_arriaga(self):
        # Prueba para obtener datos de la zona "arriaga"
        response = self.client.get('/obtener_datos_sensores/arriaga')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIsInstance(data, list)
        for entry in data:
            self.assertEqual(entry.get('zone').lower(), 'arriaga')

    def test_get_sensor_data_by_zone_zaramaga(self):
        # Prueba para obtener datos de la zona "zaramaga"
        response = self.client.get('/obtener_datos_sensores/zaramaga')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIsInstance(data, list)
        for entry in data:
            self.assertEqual(entry.get('zone').lower(), 'zaramaga')


if __name__ == '__main__':
    unittest.main()

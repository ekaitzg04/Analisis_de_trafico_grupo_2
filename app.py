from flask import Flask, jsonify
from sensor_facade import SensorFacade

app = Flask(__name__)
facade = SensorFacade()

# Endpoint para obtener todos los datos de sensores
@app.route('/obtener_datos_sensores', methods=['GET'])
def obtener_todos_datos():
    data = facade.get_all_data()
    return jsonify(data)

# Endpoint para obtener datos de sensores por zona
@app.route('/obtener_datos_sensores/<zone>', methods=['GET'])
def obtener_datos_por_zona(zone):
    data = facade.get_data_by_zone(zone)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

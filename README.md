# Proyecto: API RESTful para Datos de Sensores

Este proyecto expone una API RESTful para acceder a datos simulados de sensores, almacenados en un archivo JSON. Se implementa el patrón **Facade** para abstraer el acceso a los datos y simplificar la interacción con la API.

---

## 📁 Estructura del Proyecto

```
.
├── app.py                 # Aplicación Flask que expone la API
├── sensor_facade.py       # Implementación de la fachada (Facade)
├── sensor_repository.py   # Repositorio que accede al archivo JSON
├── sensor_data.json       # Archivo JSON con datos simulados de sensores
└── requirements.txt       # Dependencias del proyecto
```

---

## 📂 Descripción de los Archivos

### `sensor_data.json`
Contiene datos simulados de sensores para las zonas:
- Salburua
- Arriaga
- Zaramaga

### `sensor_repository.py`
Módulo encargado de acceder al archivo JSON y devolver los datos.

### `sensor_facade.py`
Implementa la fachada que encapsula el acceso al repositorio de datos. Expone métodos para:
- Obtener todos los datos
- Filtrar datos por zona

### `app.py`
Aplicación principal en Flask. Expone los siguientes endpoints:

- `GET /obtener_datos_sensores`
  - Devuelve todos los datos de sensores

- `GET /obtener_datos_sensores/<zona>`
  - Devuelve los datos filtrados por la zona especificada

### `requirements.txt`
Contiene las dependencias necesarias para ejecutar el proyecto:
```
Flask==2.2.3
Werkzeug==2.2.3
```

---

## 🚀 Ejecución del Proyecto

1. **Clonar o copiar el proyecto**  
   Copia todos los archivos en un mismo directorio.

2. **Instalar las dependencias**
   Asegúrate de tener Python instalado y ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```
   La aplicación estará disponible en:
   ```
   http://localhost:5000
   ```

---

## 📈 Uso de la API

Puedes probar los endpoints usando tu navegador, `curl` o herramientas como **Postman**.

- Obtener todos los datos:
  ```
  GET http://localhost:5000/obtener_datos_sensores
  ```

- Obtener datos de una zona específica (por ejemplo, "salburua"):
  ```
  GET http://localhost:5000/obtener_datos_sensores/salburua
  ```

---

## 🚛 Tecnologías Usadas
- Python
- Flask
- JSON
- Patrón de diseño **Facade**

---

## 📄 Branching y Flujo de Trabajo

Este proyecto sigue *GitHub Flow*:

- Rama principal: main
- Ramas por funcionalidad: feature/nombre-funcionalidad

Ejemplo:

```
git checkout -b feature/api-zona
```

---

## 👥 Autores

- Garai Martínez de Santos
- Ekaitz García 
- Pablo Ruiz de Azúa


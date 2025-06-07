import os
import requests
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Lista de ciudades a consultar
cities = ["Madrid", "Barcelona", "Valencia"]

# Lista para almacenar los datos
weather_data = []

# Obtener la fecha y hora actual
now = datetime.now()
fecha_actual = now.strftime("%Y-%m-%d %H:%M:%S")

# Iterar por las ciudades y obtener datos
for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_data.append({
            "ciudad": city,
            "temperatura": data["main"]["temp"],
            "humedad": data["main"]["humidity"],
            "clima": data["weather"][0]["description"],
            "fecha": fecha_actual
        })
    else:
        print(f"Error al obtener datos de {city}: {response.status_code}")

# Convertir la lista a DataFrame
df = pd.DataFrame(weather_data)

# Mostrar el DataFrame
print("\nDatos recolectados:\n")
print(df)

# Crear ruta tipo data lake
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

output_dir = Path(f"data/raw/{year}/{month}/{day}")
output_dir.mkdir(parents=True, exist_ok=True)

# Guardar como CSV
output_path = output_dir / "weather.csv"
df.to_csv(output_path, index=False)

print(f"\n Archivo guardado en: {output_path}")

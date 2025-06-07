import os
import requests
from dotenv import load_dotenv

# Cargar variables del entorno
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Ciudad de prueba
city = "Madrid"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=es"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Clima actual en {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
else:
    print("Error al obtener datos:", response.status_code)

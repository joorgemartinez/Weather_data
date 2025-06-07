# 🌦️ Weather Data Pipeline

Este es un proyecto personal de ingeniería de datos que implementa un pipeline para recolectar datos meteorológicos desde una API pública, transformarlos y almacenarlos en un data lake local con una estructura organizada. Es ideal para incluir en un portafolio como Data Engineer Junior.

## 📌 Objetivos del proyecto

- Conectar con una API REST pública (OpenWeatherMap) para obtener datos del clima en tiempo real.
- Procesar y estructurar los datos usando pandas.
- Almacenar los datos en formato Parquet o CSV de manera eficiente.
- Organizar los archivos en carpetas estilo data lake: /data/raw/YYYY/MM/DD/.
- Automatizar pasos iniciales del flujo de trabajo de datos.
- Documentar el proceso para replicabilidad y presentación profesional.

## 🔧 Tecnologías utilizadas

- Python 3.10+
- requests
- pandas
- python-dotenv
- pyarrow
- Git + GitHub

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/weather-data-pipeline.git
cd weather-data-pipeline
```

2. Crear un entorno virtual e instalar dependencias

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip3 install -r requirements.txt 
```

3. Configurar la clave de la API

Crear un archivo .env en la raíz del proyecto con el siguiente contenido:

```bash
OPENWEATHER_API_KEY=tu_clave_aquí
```
Puedes obtener tu clave gratuita registrándote en: https://home.openweathermap.org/api_keys

4. Ejecutar el pipeline

```bash
python3 pipeline.py
```

## 📁 Estructura del proyecto

```bash
weather-data-pipeline/
├── data/                  # Almacena los datos crudos por fecha
│   └── raw/YYYY/MM/DD/    # Estructura estilo data lake
├── notebooks/             # Notebooks opcionales para exploración
├── pipeline.py            # Script principal del pipeline
├── requirements.txt       # Librerías necesarias
├── .env                   # Variables de entorno (no subir al repo)
└── README.md              # Documentación del proyecto
```

## 📈 Estado del desarrollo

 - Conexión con la API de OpenWeatherMap
 - Transformación a DataFrame limpio
 - Almacenamiento en data lake local (CSV)
 - Organización por fecha
 - Automatización del flujo
 - Visualización opcional

## 🔒 Seguridad

- El archivo .env está incluido en .gitignore y no debe subirse a GitHub.
- No compartas tu clave API en público.

## ✍️ Autor

[Jorge Martínez](https://github.com/joorgemartinez)

Proyecto personal para el portafolio de ingeniería de datos.
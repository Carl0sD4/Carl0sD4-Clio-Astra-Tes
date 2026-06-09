# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponemos el puerto 8080 (estándar de Cloud Run)
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]

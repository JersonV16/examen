# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido de la aplicación al contenedor
COPY . .

# Expone el puerto 5000 para que Flask sea accesible
EXPOSE 5000

# Comando para ejecutar la aplicación Flask
CMD ["python", "application.py"]


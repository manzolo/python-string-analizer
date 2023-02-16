FROM python:3.9-slim-buster

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt contenente le dipendenze dell'applicazione
COPY requirements.txt .

# Installa le dipendenze dell'applicazione
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'applicazione nella directory di lavoro del container
COPY . .

# Imposta la variabile d'ambiente FLASK_APP per l'applicazione Flask
ENV FLASK_APP=main.py
ENV SERVER_PORT=8080
# Esegui l'applicazione quando il container è avviato
CMD ["python", "main.py"]
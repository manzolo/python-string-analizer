FROM python:3.9-slim-buster

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt contenente le dipendenze dell'applicazione
COPY . .

# Installa le dipendenze dell'applicazione
RUN pip install -e .

ENV APP_ENV=prod
ENV SERVER_PORT=8000

# Esegui l'applicazione quando il container è avviato
CMD ["flask", "run"]



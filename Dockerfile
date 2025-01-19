# Basis-Image mit Python 
FROM python:3.11-slim 
 
# Arbeitsverzeichnis erstellen 
WORKDIR /app 
 
# Anforderungen kopieren 
COPY requirements.txt requirements.txt 
 
# Installiere die AbhÑngigkeiten 
RUN pip install --no-cache-dir -r requirements.txt 
 
# Anwendungscode kopieren 
COPY . . 
 
# Flask-Umgebung fÅr die Produktion konfigurieren 
ENV FLASK_APP=run.py 
ENV FLASK_ENV=production 
ENV PYTHONUNBUFFERED=1 
 
# Port 5000 fÅr Flask-Server îffnen 
EXPOSE 5000 
 
# Container starten 
CMD ["python", "run.py"] 

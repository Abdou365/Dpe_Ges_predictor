# Utiliser une image officielle de Python comme image de base
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements.txt et main.py dans le répertoire de travail
COPY requirements.txt ./

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le reste des fichiers dans le répertoire de travail
COPY . .

# Exposer le port sur lequel l'application sera disponible
EXPOSE 8000

# Démarrer l'application FastAPI en utilisant Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

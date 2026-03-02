# Image de base : système d'exploitation minimal avec Python
FROM python:3.11-slim

# Définition du répertoire de travail dans le conteneur
WORKDIR /app

# Copie du fichier de dépendances
COPY requirements.txt .

# Installation des librairies Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie de tout votre code source
COPY . .

# Commande par défaut lors du démarrage du conteneur
CMD ["python", "premier_pipeline.py"]
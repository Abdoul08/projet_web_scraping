#Utilisez une image de base Python
FROM python:3.9
# Définissez le répertoire de travail dans le conteneur
WORKDIR /app



# Copiez les fichiers requis dans le conteneur
COPY requirements.txt .


# Installez les dépendances de l'application
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exposez le port sur lequel votre application Flask s'exécute
EXPOSE 5000

# Commande pour démarrer votre application Flask
CMD ["python3.9", "backend.py"]

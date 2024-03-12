# Application de Classification des offres d'appel via le web scraping 

## Comment l'exécuter ?

**Cloner le projet**

git clone https://github.com/Abdoul08/projet_web_scraping.git

**Se placer dans le repertoire racine et lancer les commandes suivantes**

` docker build -t backend-flask .   `

` docker run -d -p 5000:5000 backend-flask `

` docker build -t front -f Dockerfile-web .` 

` docker run -d -p 8501:8501 front `

Lien vers le docker hub des images : https://hub.docker.com/repositories/abdoul08





# Codislife Foundation — Backend

Backend Django du programme éducatif Codislife Foundation : plateforme de formation en ligne et de suivi professionnel pour jeunes africains.
![CI](https://github.com/tcho98/codislife-backend/actions/workflows/ci.yml/badge.svg)

## À propos

Codislife Foundation est le programme éducatif du mouvement Codislife, né en 2023. Sa mission : donner aux jeunes africains les moyens d'acquérir une culture numérique concrète, à travers des formations pratiques couplées à un suivi professionnel réel.

Ce dépôt contient le backend de la plateforme : API, gestion des formations, suivi des apprenants.

## Stack technique

- **Langage / Framework** : Python 3.14, Django
- **Base de données** : PostgreSQL 17
- **Reverse proxy** : Traefik v3.6
- **Conteneurisation** : Docker, Docker Compose
- **CI** : GitHub Actions

## Prérequis

- [Docker](https://docs.docker.com/get-docker/) et Docker Compose (inclus avec Docker Desktop ou Docker Engine récent)

Aucune installation locale de Python, Django ou PostgreSQL n'est nécessaire — tout tourne en conteneurs.

## Démarrage rapide

1. Cloner le dépôt :
```bash
   git clone https://github.com/tcho98/codislife-backend.git
   cd codislife-backend
```

2. Créer un fichier `.env` à la racine (non versionné, voir `.gitignore`) :
    POSTGRES_DB=codislife
    POSTGRES_USER=codislife
    POSTGRES_PASSWORD=change_moi
3. Lancer les conteneurs :
```bash
   docker compose up --build
```

4. Dans un second terminal, appliquer les migrations :
```bash
   docker compose exec web python manage.py migrate
```

5. Le site est accessible sur [http://localhost](http://localhost)

## Lancer les tests

```bash
docker compose exec web python manage.py test
```

## Structure du projet

codislife-backend/
├── config/ # Réglages Django (settings, urls racine)
├── Dockerfile # Image de l'application
├── compose.yaml # Orchestration des services (web, db, traefik)
├── requirements.txt # Dépendances Python
└── .github/workflows/ # Pipeline CI

## Roadmap

Le développement suit un phasage en 3 étapes, détaillé dans le cahier des charges du projet :

- **Phase 1 (en cours)** : catalogue de formations, contenu pédagogique, suivi professionnel de base
- **Phase 2** : paiement, certification, suivi enrichi
- **Phase 3** : programme d'alternance, communauté, lien entreprises partenaires

## Licence

À définir.
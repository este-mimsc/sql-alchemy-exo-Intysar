[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/KT4lxLyy)
# Démarrage Flask SQLAlchemy (GitHub Classroom)

Ce dépôt est un **gabarit de départ** pour un devoir GitHub Classroom du Module
5 Flask : Bases de données et ORM avec SQLAlchemy. Les étudiantes et étudiants
connecteront SQLAlchemy à une application Flask, construiront des modèles et
les relieront à des routes pour des opérations CRUD basiques.

## Objectifs d'apprentissage

- Configurer SQLAlchemy dans une application Flask (schéma factory recommandé).
- Définir des modèles et relations (`User`, `Post`).
- Réaliser des opérations CRUD avec les sessions SQLAlchemy.
- Intégrer les modèles à des routes Flask qui renvoient du JSON.
- (Optionnel) Utiliser Flask-Migrate pour gérer les évolutions du schéma.

## Ce que vous devez faire

Travaillez dans `app.py` et `models.py` pour terminer le devoir. Les tests
décrivent le comportement attendu. En résumé :

1. **Modèles (`models.py`)**
   - Ajouter les colonnes requises à `User` et `Post`.
   - Mettre en place une relation un-à-plusieurs : un `User` possède plusieurs
     `Post`.
   - Rendre `username` unique et obligatoire ; `Post.user_id` doit référencer
     `users.id`.

2. **Routes (`app.py`)**
   - Implémenter `GET /users` pour lister les utilisateurs (tableau JSON).
   - Implémenter `POST /users` pour créer un utilisateur à partir du JSON
     fourni.
   - Implémenter `GET /posts` pour lister les posts avec les informations de
     l'auteur.
   - Implémenter `POST /posts` pour créer un post lié à un utilisateur existant.
   - Retourner des codes de statut adaptés (voir les tests pour les attentes).

3. **(Optionnel) Migrations**
   - Utiliser `flask db init/migrate/upgrade` si vous souhaitez vous exercer aux
     migrations.

## Structure du projet

```
.
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── tests/
│   ├── conftest.py
│   ├── test_app_structure.py
│   ├── test_models.py
│   └── test_routes.py
└── .github/workflows/autograding.yml
```

## Démarrage en local

1. Créez un environnement virtuel et installez les dépendances :

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Lancez l'application Flask :

   ```bash
   flask --app app run
   ```

   Ou exécutez `python app.py`.

3. Lancez les tests :

   ```bash
   pytest
   ```

## Auto-évaluation avec GitHub Actions

GitHub Actions (voir `.github/workflows/autograding.yml`) installe les
dépendances et exécute `pytest`. Utilisez-le comme guide dans GitHub Classroom :
push vos modifications pour déclencher le workflow et consulter les retours.

## Conseils

- Utilisez le shell Flask pour des essais rapides : `flask --app app shell`.
- En test local, la base par défaut est `sqlite:///blog.db`.
- Pendant les tests, la base tourne en mémoire (`sqlite:///:memory:`) pour
  conserver l'isolation et la rapidité.

# Projet 10 DA-Python
***Créez une API sécurisée RESTful en utilisant Django REST;***

**SoftDesk API est une REST API securisée qui permet de remonter et suivre des problèmes techniques ( issues tracking system) pour les trois plateformes : Site web ( front-end & back-end), applications Android, applications iOs.**

**Les fonctionnalités:**

- L'authentification avec JWT tokens ( access et refresh tokens)
- Créer un projet ayant plusieurs collaborateurs en ajoutant des contributors, chaque projet peut contenir plusieus problèmes ( issues). Est accessible par l'author ou contributeurs.
- Créer une ou plusieurs problèmes d'un projet. Seule l'author a droit de modifier ou supprimer.
- Créer un ou plusieurs commentaires d'une problème. Seul l'author a droit de modifier ou supprimer.


## Initialisation du projet

### Windows :
    git clone https://github.com/Maiphuongthao/MaiPhuongThao_10_062023.git

    cd MaiPhuongThao_10_062023
    python -m venv env 
    env\scripts\activate

    pip install -r requirements.txt


### MacOS et Linux :
    git clone https://github.com/Maiphuongthao/MaiPhuongThao_10_062023.git

    cd MaiPhuongThao_10_062023
    python3 -m venv env 
    source env/bin/activate

    pip install -r requirements.txt



## Exécution du programme

Pour lancer le serveur:

    cd SoftDesk
    python3 manage.py runserver
    
   
Entrez l'adresse suivante dans le navigateur avec point de termination :

    http:/127.0.0.1:8000/


Ou avec la plateforme [Postman](https://www.postman.com/)


Les points de terminations:

| #   | *Point de terminaison d'API*                                              | *Méthode HTTP* | *URL*       |
|-----|---------------------------------------------------------------------------|----------------|-------------------------------------------|
| 1   | Inscription de l'utilisateur                                              | POST           | /signup/                                  |
| 2   | Connexion de l'utilisateur                                                | POST           | /login/                                   |
| 3   | Récupérer la liste de tous les projets rattachés à l'utilisateur connecté | GET            | /projects/                                |
| 4   | Créer un projet                                                           | POST           | /projects/                                |
| 5   | Récupérer les détails d'un projet via son id                              | GET            | /projects/{id}/                           |
| 6   | Mettre à jour un projet                                                   | PUT            | /projects/{id}/                           |
| 7   | Supprimer un projet et ses problèmes                                      | DELETE         | /projects/{id}/                           |
| 8   | Ajouter un utilisateur (collaborateur) à un projet                        | POST           | /projects/{id}/users/                     |
| 9   | Récupérer la liste de tous les utilisateurs attachés à un projet          | GET            | /projects/{id}/users/                     |
| 10  | Supprimer un utilisateur d'un projet                                      | DELETE         | /projects/{id}/users/{id}/                |
| 11  | Récupérer la liste des problèmes liés à un projet                         | GET            | /projects/{id}/issues/                    |
| 12  | Créer un problème dans un projet                                          | POST           | /projects/{id}/issues/                    |
| 13  | Mettre à jour un problème dans un projet                                  | PUT            | /projects/{id}/issues/{id}/               |
| 14  | Supprimer un problème d'un projet                                         | DELETE         | /projects/{id}/issues/{id}/               |
| 15  | Créer des commentaires sur un problème                                    | POST           | /projects/{id}/issues/{id}/comments/      |
| 16  | Récupérer la liste de tous les commentaires liés à un problème            | GET            | /projects/{id}/issues/{id}/comments/      |
| 17  | Modifier un commentaire                                                   | PUT            | /projects/{id}/issues/{id}/comments/{id}/ |
| 18  | Supprimer un commentaire                                                  | DELETE         | /projects/{id}/issues/{id}/comments/{id}/ |
| 19  | Récupérer un commentaire via son id                                       | GET            | /projects/{id}/issues/{id}/comments/{id}/ |


Afin de tester les différentes donctionalités su site: il y a 3 utilisateurs qui sont crées:

|   *Identifiant*   | *Mot de passe* |
|-------------------|----------------|
| admin@admin.com   | Password124    |
| test1@test.com    | Password124    |
| test2@test.com    | Password124    |



# Documentation

# 01 - user creation :

- **URL** : `POST /api/user`
- **Description** : Crée un nouvel utilisateur.

#### Paramètres Requis (dans le corps de la requête JSON) :

- `username` (string) : Nom d'utilisateur unique.
- `email` (string) : Adresse email unique.
- `password` (string) : Mot de passe.
- `pseudo` (string, optionnel) : Pseudonyme.

#### Réponse en cas de succès (`201 Created`) :

#### json
{
  "message": "Ok",
  "data": {
    "id": 8,
    "username": "bkay",
    "pseudo": "BK.",
    "email": "bkayy@example.com",
    "created_at": "2024-11-06T12:10:06.043998Z"
  }
}

#### Codes de Retour :

- **201 Created** : Utilisateur créé avec succès.
- **400 Bad Request** : Erreur de validation (ex. : email déjà pris).

# 02 - authentication :

- **URL** : `POST /api/auth/`
- **Description** : Authentifie un utilisateur et génère des tokens d'accès et de rafraîchissement pour l'accès sécurisé.

#### Paramètres Requis (dans le corps de la requête JSON) :
- `username` (string) : Nom d'utilisateur.
- `password` (string) : Mot de passe de l'utilisateur.

#### Réponse en cas de succès (`200 OK`) :
## json
{
  "refresh": "<token_refresh>",
  "access": "<token_access>"
}

- **refresh** : Token permettant de rafraîchir l’accès.
- **access** : Token d'accès qui sera utilisé pour accéder aux autres endpoints sécurisés.

#### Codes de Retour :
- **200 OK** : Authentification réussie, tokens générés.
- **401 Unauthorized** : Identifiants invalides.

# 03 - user deletion :

- **URL** : `DELETE /api/user/<id>`
- **Description** : Supprime un utilisateur spécifique en utilisant son ID.

#### Authentification :
- **Requis** : l’utilisateur doit être authentifié pour effectuer cette opération.

#### Réponse en cas de succès (`204 No Content`) :
- Aucune donnée dans le corps de la réponse. La suppression est confirmée par un code de statut 204.

#### Codes de Retour :
- **204 No Content** : Suppression réussie.
- **404 Not Found** : Utilisateur non trouvé (ex. : l'ID spécifié n'existe pas).
- **401 Unauthorized** : L’utilisateur n’est pas authentifié pour effectuer cette action.

# 04 - user update :

- **URL** : `PUT /api/user/<id>`
- **Description** : Met à jour les informations d'un utilisateur spécifique.

#### Paramètres Requis (dans le corps de la requête JSON) :

- `username` (string) : Nouveau nom d'utilisateur unique.
- `pseudo` (string, optionnel) : Nouveau pseudonyme de l'utilisateur.
- `email` (string) : Nouvelle adresse email unique de l'utilisateur.
- `password` (string, optionnel) : Nouveau mot de passe de l'utilisateur.

#### Réponse en cas de succès (`200 OK`) :

## json
{
  "message": "Ok",
  "data": {
    "username": "nouhailB",
    "pseudo": "new_pseudo",
    "email": "nouhab@example.com"
  }
}

#### Codes de Retour :

- **200 OK** : Mise à jour réussie des informations de l'utilisateur.
- **404 Not Found** : Utilisateur non trouvé (ex. : l'ID spécifié n'existe pas).
- **400 Bad Request** : Erreur de validation (ex. : email déjà pris).
- **401 Unauthorized** : L’utilisateur n’est pas authentifié pour effectuer cette action.

### 05 - user list

- **URL** : `GET /api/users`
- **Description** : Récupère la liste des utilisateurs enregistrés, avec pagination et possibilité de filtrer par pseudonyme.

#### Paramètres de Requête (optionnels) :

- `pseudo` (string) : Filtre par pseudonyme (partie du pseudonyme).
- `page` (integer) : Numéro de la page des résultats à afficher.
- `perPage` (integer) : Nombre d’utilisateurs par page (par défaut, 10).

#### Réponse en cas de succès (`200 OK`) :

## json
{
  "message": "OK",
  "data": [
    {
      "id": 3,
      "username": "testuser3",
      "pseudo": "Test User 3",
      "email": "testuser3@example.com",
      "created_at": "2024-10-17T17:03:31.841387Z"
    },
    {
      "id": 4,
      "username": "basmakasmi",
      "pseudo": "Basma K.",
      "email": "basma.kkasmi@example.com",
      "created_at": "2024-11-03T14:02:56.501649Z"
    },
    ...
  ],
  "pager": {
    "current": 1,
    "total": 3
  }
}


- **data** : Liste des utilisateurs avec leurs informations de base.
- **pager** : Informations sur la pagination :
  - `current` : Numéro de la page actuelle.
  - `total` : Nombre total de pages disponibles.

#### Codes de Retour :

- **200 OK** : Liste des utilisateurs récupérée avec succès.
- **400 Bad Request** : Erreur de requête (ex. : paramètres invalides). 

### 06 - users by id

- **URL** : `GET /api/user/<id>`
- **Description** : Récupère les détails d'un utilisateur spécifique par son ID.

#### Paramètres Requis :

- **Authorization** : `Bearer <token_access>` (nécessaire pour l'authentification et l'accès aux informations sécurisées).

#### Réponse en cas de succès (`200 OK`) :

## json
{
  "message": "OK",
  "data": {
    "id": 7,
    "username": "nouhailB",
    "pseudo": "new_pseudo",
    "email": "nouhab@example.com",
    "created_at": "2024-11-06T11:34:01.965923Z"
  }
}

- **data** : Informations sur l'utilisateur demandé :
  - `id` : Identifiant unique de l'utilisateur.
  - `username` : Nom d'utilisateur.
  - `pseudo` : Pseudonyme.
  - `email` : Adresse email.
  - `created_at` : Date et heure de création de l'utilisateur.

#### Codes de Retour :

- **200 OK** : Détails de l'utilisateur récupérés avec succès.
- **401 Unauthorized** : Le token d'authentification est manquant ou invalide.
- **404 Not Found** : Aucun utilisateur n'a été trouvé avec cet ID.

###  07 - video creation

- **URL** : `POST /api/videos/create/`
- **Description** : Crée une nouvelle vidéo et enregistre les fichiers multimédias associés.

#### Paramètres Requis (dans le corps de la requête `form-data`) :

- `name` (string) : Nom ou titre de la vidéo.
- `source` (file) : Fichier vidéo principal à télécharger.

#### Réponse en cas de succès (`201 Created`) :

## json
{
  "message": "Video created successfully",
  "data": {
    "id": 7,
    "name": "video BK tangier 2022",
    "source": "http://127.0.0.1:8080/public/videos/C5027570-8D7D-4B9A-885F-C620C63665F1_2_0_a_fjUtacV.mov",
    "created_at": "2024-11-06T13:24:59.764245Z"
  }
}


- **data** : Informations sur la vidéo créée :
  - `id` : Identifiant unique de la vidéo.
  - `name` : Nom ou titre de la vidéo.
  - `source` : Lien vers le fichier vidéo téléchargé.
  - `created_at` : Date et heure de création de la vidéo.

#### Codes de Retour :

- **201 Created** : Vidéo créée avec succès.
- **400 Bad Request** : Erreur de validation (ex. : fichier manquant ou nom de vidéo invalide).

### 08 - video list

- **URL** : `GET /api/videos/`
- **Description** : Récupère une liste de toutes les vidéos.

#### Paramètres de Requête (optionnels) :

- Aucun paramètre n'est requis, mais il peut y avoir des filtres ou des paramètres de pagination en fonction des besoins (exemple : `page`, `name`, etc.).

#### Réponse en cas de succès (`200 OK`) :

## json
{
  "message": "OK",
  "data": [
    {
      "id": 1,
      "name": "BKAY 2022",
      "source": "/public/videos/C5027570-8D7D-4B9A-885F-C620C63665F1_2_0_a.mov",
      "created_at": "2024-11-06T11:55:23.464586Z"
    },
    {
      "id": 3,
      "name": "tangier vid 2022",
      "source": "/public/videos/C5027570-8D7D-4B9A-885F-C620C63665F1_2_0_a_x91A7eT.mov",
      "created_at": "2024-11-06T12:10:37.937494Z"
    },
    {
      "id": 4,
      "name": "video BK tangier",
      "source": "/encoded_mp4_encoded_file.mp4",
      "created_at": "2024-11-06T12:12:15.293194Z"
    }
  ]
}

#### Structure de la Réponse :

- **message** : Confirmation de la réussite de l'opération (`OK`).
- **data** : Liste des vidéos disponibles :
  - `id` : Identifiant unique de la vidéo.
  - `name` : Nom ou titre de la vidéo.
  - `source` : Chemin d'accès au fichier vidéo.
  - `created_at` : Date et heure de création de la vidéo.

#### Codes de Retour :

- **200 OK** : Liste de vidéos récupérée avec succès.
- **404 Not Found** : Si aucun élément correspondant aux critères de filtrage n'est trouvé (si applicable).

### 09 - video list by user

- **URL** : `GET /api/user/{id}/videos`
- **Description** : Récupère la liste des vidéos associées à un utilisateur spécifique.

#### Paramètres de l'URL :

- `{id}` (int) : Identifiant unique de l'utilisateur pour lequel on veut récupérer les vidéos.

#### Réponse en cas de succès (`200 OK`) :

## json
{
  "message": "OK",
  "data": [
    {
      "id": 1,
      "name": "Ma Vidéo Test",
      "source": "/public/videos/C5027570-8D7D-4B9A-885F-C620C63665F1_2_0_a.mov",
      "created_at": "2024-11-06T11:55:23.464586Z"
    },
    {
      "id": 2,
      "name": "Ma Vidéo Test",
      "source": "/public/videos/C5027570-8D7D-4B9A-885F-C620C63665F1_2_0_a_kxoJkLs.mov",
      "created_at": "2024-11-06T12:04:23.588092Z"
    }
  ],
  "pager": {
    "current": 1,
    "total": 1
  }
}

#### Structure de la Réponse :

- **message** : Confirmation de la réussite de l'opération (`OK`).
- **data** : Liste des vidéos associées à l'utilisateur spécifié :
  - `id` : Identifiant unique de la vidéo.
  - `name` : Nom ou titre de la vidéo.
  - `source` : Chemin d'accès au fichier vidéo.
  - `created_at` : Date et heure de création de la vidéo.
- **pager** : Informations de pagination pour la liste des vidéos.
  - `current` : Numéro de la page courante.
  - `total` : Nombre total de pages.

#### Codes de Retour :

- **200 OK** : Liste des vidéos récupérée avec succès.
- **404 Not Found** : Si l'utilisateur spécifié par `{id}` n'existe pas ou n'a pas de vidéos associées.

### 10 - encoding video by id

- **URL** : `PATCH /api/video/{id}/encode`
- **Description** : Permet de mettre à jour l'encodage d'une vidéo spécifique en modifiant son format et son fichier source.

#### Paramètres de l'URL :

- `{id}` (int) : Identifiant unique de la vidéo à encoder.

#### Paramètres Requis (dans le corps de la requête JSON) :

- `format` (string) : Le format de la vidéo souhaité (ex. : "mp4").
- `file` (string) : Le nom du fichier de la vidéo encodée.

#### Exemple de Requête :

## json
{
  "format": "mp4",
  "file": "encoded_file.mp4"
}

#### Réponse en cas de succès (`200 OK`) :

## json
{
  "message": "OK",
  "data": {
    "id": 7,
    "name": "video BK tangier 2022",
    "source": "/encoded_mp4_encoded_file.mp4",
    "created_at": "2024-11-06T13:24:59.764245Z"
  }
}

#### Structure de la Réponse :

- **message** : Confirmation de la réussite de l'opération (`OK`).
- **data** : Informations sur la vidéo mise à jour :
  - `id` : Identifiant unique de la vidéo.
  - `name` : Nom ou titre de la vidéo.
  - `source` : Chemin d'accès au nouveau fichier vidéo encodé.
  - `created_at` : Date et heure de création initiale de la vidéo.

#### Codes de Retour :

- **200 OK** : Vidéo encodée avec succès.
- **400 Bad Request** : Données invalides fournies pour le format ou le fichier.
- **404 Not Found** : Si la vidéo spécifiée par `{id}` n'existe pas.

### 11 - video update

- **URL** : `PUT /api/video/{id}`
- **Description** : Met à jour les informations d'une vidéo spécifique.

#### Paramètres de l'URL :

- `{id}` (int) : Identifiant unique de la vidéo à mettre à jour.

#### Paramètres Requis (dans le corps de la requête JSON) :

- `name` (string) : Nouveau nom de la vidéo.
- `user` (int) : Identifiant de l'utilisateur propriétaire de la vidéo.

#### Exemple de Requête :

## json
{
  "name": "BKAY 2022",
  "user": 8
}

#### Réponse en cas de succès (`200 OK`) :

## json
{
  "message": "OK",
  "data": {
    "id": 1,
    "name": "BKAY 2022",
    "source": "/public/videos/C5027570-8D7D-4B9A-885F-C620C63665F1_2_0_a.mov",
    "created_at": "2024-11-06T11:55:23.464586Z"
  }
}

#### Structure de la Réponse :

- **message** : Confirmation de la réussite de l'opération (`OK`).
- **data** : Informations mises à jour de la vidéo :
  - `id` : Identifiant unique de la vidéo.
  - `name` : Nouveau nom de la vidéo.
  - `source` : Chemin actuel de la source de la vidéo.
  - `created_at` : Date et heure de création initiale de la vidéo.

#### Codes de Retour :

- **200 OK** : Vidéo mise à jour avec succès.
- **400 Bad Request** : Données invalides fournies.
- **404 Not Found** : Si la vidéo spécifiée par `{id}` n'existe pas.

### 12 - video deletion

- **URL** : `DELETE /api/video/{id}/delete`
- **Description** : Supprime une vidéo spécifique.

#### Paramètres de l'URL :

- `{id}` (int) : Identifiant unique de la vidéo à supprimer.

#### Exemple de Requête :

Cette requête n'a pas de corps. Elle nécessite uniquement l'ID de la vidéo dans l'URL.

#### Réponse en cas de succès (`204 No Content`) :

Aucun contenu dans la réponse, confirmant que la suppression a été effectuée.

#### Codes de Retour :

- **204 No Content** : Vidéo supprimée avec succès.
- **404 Not Found** : La vidéo spécifiée par `{id}` n'existe pas.

### 13 - comment creation

- **URL** : `POST /api/video/{id}/comment`
- **Description** : Crée un commentaire pour une vidéo spécifique.

#### Paramètres de l'URL :

- `{id}` (int) : Identifiant unique de la vidéo pour laquelle le commentaire est ajouté.

#### Paramètres Requis (dans le corps de la requête JSON) :

- `body` (string) : Le contenu du commentaire.

#### Exemple de Requête :

## json
{
  "body": "This is a great video!"
}

#### Réponse en cas de succès (`201 Created`) :

## json
{
  "message": "OK",
  "data": {
    "id": 2,
    "video": 4,
    "user": 8,
    "body": "This is a great video!",
    "created_at": "2024-11-06T14:00:31.835536Z"
  }
}

#### Codes de Retour :

- **201 Created** : Commentaire créé avec succès.
- **400 Bad Request** : Erreur de validation (ex. : contenu du commentaire manquant).
- **404 Not Found** : La vidéo spécifiée par `{id}` n'existe pas.

### 14 - comment list

- **URL** : `GET /api/video/{id}/comments`
- **Description** : Récupère la liste des commentaires associés à une vidéo spécifique.

#### Paramètres de l'URL :

- `{id}` (int) : Identifiant unique de la vidéo pour laquelle les commentaires sont récupérés.

#### Réponse en cas de succès (`200 OK`) :

## json
{
  "message": "OK",
  "data": [
    {
      "id": 1,
      "video": 4,
      "user": 8,
      "body": "This is a great video!",
      "created_at": "2024-11-06T14:00:20.099608Z"
    },
    {
      "id": 2,
      "video": 4,
      "user": 8,
      "body": "This is a great video!",
      "created_at": "2024-11-06T14:00:31.835536Z"
    }
  ],
  "pager": {
    "current": 1,
    "total": 1
  }
}

#### Codes de Retour :

- **200 OK** : La liste des commentaires a été récupérée avec succès.
- **404 Not Found** : La vidéo spécifiée par `{id}` n'existe pas.
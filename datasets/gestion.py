"""
Module gestion.py
------------------
Ce module contient toute la logique "métier" de gestion des datasets :
    - la structure de données (liste de dictionnaires)
    - le tuple des domaines autorisés
    - les fonctions CRUD (Créer, Lire, Modifier, Supprimer)
    - les fonctions de saisie sécurisée (gestion des erreurs de saisie)
"""

# ---------------------------------------------------------------------------
# Partie 4 - TUPLES
# Un tuple est utilisé ici car la liste des domaines autorisés ne doit
# jamais être modifiée pendant l'exécution du programme (immuable).
# ---------------------------------------------------------------------------
DOMAINES_AUTORISES = ("Santé", "Finance", "Agriculture", "Transport", "Education")

# ---------------------------------------------------------------------------
# Partie 5 - LISTES
# DATASETS est la liste principale de l'application : chacun de ses éléments
# est un dictionnaire (Partie 3) représentant un dataset.
# ---------------------------------------------------------------------------
DATASETS = []

# Compteur interne servant à générer un identifiant unique pour chaque
# dataset ajouté (fonctionnalité bonus, cf. Partie 12).
_prochain_id = 1


# ---------------------------------------------------------------------------
# Partie 1 + Partie 8 - SAISIES SECURISEES (gestion des erreurs de saisie)
# ---------------------------------------------------------------------------
def demander_entier(message):
    """
    Demande un nombre entier à l'utilisateur.
    Si l'utilisateur saisit du texte au lieu d'un nombre, une exception
    ValueError est levée par int(). On l'intercepte et on redemande la
    saisie tant qu'elle n'est pas valide (Partie 8).
    """
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier valide.")


def demander_flottant(message):
    """Identique à demander_entier mais pour un nombre décimal (ex: taille en Mo)."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Erreur : veuillez saisir un nombre valide (ex: 12.5).")


def demander_booleen(message):
    """Demande une réponse type true/false et la convertit en booléen Python."""
    while True:
        reponse = input(message).strip().lower()
        if reponse in ("true", "vrai", "oui", "o", "1"):
            return True
        if reponse in ("false", "faux", "non", "n", "0"):
            return False
        print("Erreur : répondez par true ou false.")


def demander_domaine(message):
    """
    Demande un domaine et vérifie qu'il appartient bien au tuple
    DOMAINES_AUTORISES (Partie 4, question 8).
    """
    while True:
        domaine = input(message).strip().capitalize()
        if domaine in DOMAINES_AUTORISES:
            return domaine
        print(f"Erreur : le domaine doit être parmi {DOMAINES_AUTORISES}")


def demander_format(message):
    """Vérifie que le format saisi est bien 'csv' ou 'json'."""
    while True:
        format_fichier = input(message).strip().lower()
        if format_fichier in ("csv", "json"):
            return format_fichier
        print("Erreur : le format doit être 'csv' ou 'json'.")


# ---------------------------------------------------------------------------
# Partie 1 + Partie 3 + Partie 9 - AJOUT D'UN DATASET
# ---------------------------------------------------------------------------
def ajouter_dataset():
    """
    Demande à l'utilisateur les métadonnées d'un dataset (nom, domaine,
    lignes, colonnes, taille, format, public), construit un dictionnaire
    et l'ajoute à la liste DATASETS.
    """
    global _prochain_id

    print("\n--- Ajout d'un nouveau dataset ---")
    nom = input("Nom du dataset : ").strip()
    domaine = demander_domaine("Domaine (Santé, Finance, Agriculture, Transport, Education) : ")
    lignes = demander_entier("Nombre de lignes : ")
    colonnes = demander_entier("Nombre de colonnes : ")
    taille = demander_flottant("Taille en Mo : ")
    format_fichier = demander_format("Format (csv/json) : ")
    public = demander_booleen("Public (true/false) : ")

    # Construction du dictionnaire représentant le dataset (Partie 3)
    dataset = {
        "id": _prochain_id,
        "nom": nom,
        "domaine": domaine,
        "lignes": lignes,
        "colonnes": colonnes,
        "taille": taille,
        "format": format_fichier,
        "public": public,
    }

    DATASETS.append(dataset)  # Partie 5 : ajout dans la liste
    _prochain_id += 1

    print(f"\nDataset '{nom}' ajouté avec succès (id={dataset['id']}).")
    afficher_resume(dataset)
    return dataset


def afficher_resume(dataset):
    """Partie 1, question 4 : affiche un résumé formaté d'un dataset unique."""
    print("\n========== Résumé du dataset ==========")
    print(f"ID        : {dataset['id']}")
    print(f"Nom       : {dataset['nom']}")
    print(f"Domaine   : {dataset['domaine']}")
    print(f"Lignes    : {dataset['lignes']}")
    print(f"Colonnes  : {dataset['colonnes']}")
    print(f"Taille    : {dataset['taille']} Mo")
    print(f"Format    : {dataset['format'].upper()}")
    print(f"Public    : {'Oui' if dataset['public'] else 'Non'}")
    print("========================================")


# ---------------------------------------------------------------------------
# Partie 5 + Partie 9 - RECHERCHE
# ---------------------------------------------------------------------------
def rechercher_dataset(terme):
    """
    Recherche tous les datasets dont le nom contient le terme recherché.
    Recherche insensible à la casse et partielle (ex: "tita" trouve "Titanic").
    Retourne une liste de résultats, potentiellement vide.
    """
    terme = terme.strip().lower()
    # Compréhension de liste utilisée pour filtrer (préfigure la Partie 6)
    return [d for d in DATASETS if terme in d["nom"].lower()]


def trouver_par_id(id_dataset):
    """Retourne le dataset correspondant à l'id donné, ou None si absent."""
    for d in DATASETS:
        if d["id"] == id_dataset:
            return d
    return None


# ---------------------------------------------------------------------------
# Partie 5 + Partie 9 - MODIFICATION
# ---------------------------------------------------------------------------
def modifier_dataset(id_dataset):
    """
    Modifie un champ d'un dataset existant, identifié par son id.
    Lève une KeyError si le dataset n'existe pas (gérée en Partie 8).
    """
    dataset = trouver_par_id(id_dataset)
    if dataset is None:
        raise KeyError(f"Aucun dataset avec l'id {id_dataset}.")

    print("\nChamps modifiables : nom, domaine, lignes, colonnes, taille, format, public")
    champ = input("Champ à modifier : ").strip().lower()

    if champ == "nom":
        dataset["nom"] = input("Nouveau nom : ").strip()
    elif champ == "domaine":
        dataset["domaine"] = demander_domaine("Nouveau domaine : ")
    elif champ == "lignes":
        dataset["lignes"] = demander_entier("Nouveau nombre de lignes : ")
    elif champ == "colonnes":
        dataset["colonnes"] = demander_entier("Nouveau nombre de colonnes : ")
    elif champ == "taille":
        dataset["taille"] = demander_flottant("Nouvelle taille (Mo) : ")
    elif champ == "format":
        dataset["format"] = demander_format("Nouveau format (csv/json) : ")
    elif champ == "public":
        dataset["public"] = demander_booleen("Public (true/false) : ")
    else:
        print("Champ inconnu, aucune modification effectuée.")
        return None

    print("Dataset modifié avec succès.")
    afficher_resume(dataset)
    return dataset


# ---------------------------------------------------------------------------
# Partie 5 + Partie 9 - SUPPRESSION
# ---------------------------------------------------------------------------
def supprimer_dataset(id_dataset):
    """
    Supprime un dataset de la liste à partir de son id.
    Lève une KeyError si le dataset n'existe pas (Partie 8).
    """
    dataset = trouver_par_id(id_dataset)
    if dataset is None:
        raise KeyError(f"Aucun dataset avec l'id {id_dataset}.")
    DATASETS.remove(dataset)
    print(f"Dataset '{dataset['nom']}' (id={id_dataset}) supprimé.")
    return dataset


# ---------------------------------------------------------------------------
# Partie 5 + Partie 9 - TRI
# ---------------------------------------------------------------------------
def trier_dataset(critere="nom", decroissant=False):
    """
    Retourne une copie triée de DATASETS selon le critère demandé.
    On ne modifie pas la liste d'origine, seulement l'ordre d'affichage.
    """
    criteres_valides = ("nom", "lignes", "colonnes", "taille", "domaine")
    if critere not in criteres_valides:
        raise ValueError(f"Critère de tri invalide : '{critere}'. Choisissez parmi {criteres_valides}.")

    return sorted(DATASETS, key=lambda d: d[critere], reverse=decroissant)


# ---------------------------------------------------------------------------
# Bonus - synchronisation du compteur d'id après un rechargement de fichier
# ---------------------------------------------------------------------------
def recharger_id_max():
    """
    Après un chargement depuis un fichier CSV/JSON, met à jour le compteur
    _prochain_id pour qu'il continue après le plus grand id déjà utilisé
    (évite de créer deux fois le même id).
    """
    global _prochain_id
    _prochain_id = (max(d["id"] for d in DATASETS) + 1) if DATASETS else 1

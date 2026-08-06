"""
Module csv_manager.py
-----------------------
Sauvegarde et chargement des datasets au format CSV (Partie 7).
"""

import csv
import os

# Chemin du fichier CSV, situé dans le dossier data/ à la racine du projet
CHEMIN_CSV = os.path.join(os.path.dirname(__file__), "..", "data", "datasets.csv")

# Colonnes du fichier CSV, dans l'ordre
ENTETES = ["id", "nom", "domaine", "lignes", "colonnes", "taille", "format", "public"]


def sauvegarder_csv(datasets):
    """Écrit la liste des datasets dans le fichier datasets.csv."""
    os.makedirs(os.path.dirname(CHEMIN_CSV), exist_ok=True)
    with open(CHEMIN_CSV, mode="w", newline="", encoding="utf-8") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=ENTETES)
        writer.writeheader()
        for dataset in datasets:
            writer.writerow(dataset)


def charger_csv():
    """
    Lit le fichier datasets.csv et retourne une liste de dictionnaires.

    - Lève FileNotFoundError si le fichier n'existe pas (Partie 8, cas
      "le fichier n'existe pas") : l'appelant décide comment réagir.
    - Retourne une liste vide si le fichier ne contient que l'en-tête ou
      est totalement vide (Partie 8, cas "le fichier est vide").
    """
    if not os.path.exists(CHEMIN_CSV):
        raise FileNotFoundError(CHEMIN_CSV)

    datasets = []
    with open(CHEMIN_CSV, mode="r", newline="", encoding="utf-8") as fichier:
        reader = csv.DictReader(fichier)
        for ligne in reader:
            # Le CSV ne contient que du texte : on reconvertit chaque
            # champ vers son type Python d'origine (int, float, bool).
            datasets.append({
                "id": int(ligne["id"]),
                "nom": ligne["nom"],
                "domaine": ligne["domaine"],
                "lignes": int(ligne["lignes"]),
                "colonnes": int(ligne["colonnes"]),
                "taille": float(ligne["taille"]),
                "format": ligne["format"],
                "public": ligne["public"] == "True",
            })
    return datasets

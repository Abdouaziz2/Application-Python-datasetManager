"""
Module json_manager.py
------------------------
Sauvegarde et chargement des datasets au format JSON.
Ce format est plus naturel pour des structures de type liste de
dictionnaires : il ne nécessite aucune conversion de type au chargement.
"""

import json
import os

CHEMIN_JSON = os.path.join(os.path.dirname(__file__), "..", "data", "datasets.json")


def sauvegarder_json(datasets):
    """Écrit la liste des datasets dans le fichier datasets.json (indenté et lisible)."""
    os.makedirs(os.path.dirname(CHEMIN_JSON), exist_ok=True)
    with open(CHEMIN_JSON, mode="w", encoding="utf-8") as fichier:
        json.dump(datasets, fichier, indent=4, ensure_ascii=False)


def charger_json():
    """
    Lit le fichier datasets.json et retourne une liste de dictionnaires.

    - Lève FileNotFoundError si le fichier n'existe pas.
    - Retourne une liste vide si le fichier est vide.
    - Si le contenu est corrompu (JSON mal formé), un message est affiché
      et une liste vide est retournée plutôt que de faire planter le
      programme (Partie 8).
    """
    if not os.path.exists(CHEMIN_JSON):
        raise FileNotFoundError(CHEMIN_JSON)

    with open(CHEMIN_JSON, mode="r", encoding="utf-8") as fichier:
        contenu = fichier.read().strip()
        if not contenu:
            return []  # fichier vide

        try:
            return json.loads(contenu)
        except json.JSONDecodeError:
            print("Attention : le fichier JSON est corrompu, il sera ignoré.")
            return []

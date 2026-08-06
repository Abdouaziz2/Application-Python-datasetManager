"""
Module affichage.py
--------------------
Fonctions dédiées à l'affichage des datasets dans la console
(mise en forme sous forme de tableau).
"""

from datasets.gestion import DATASETS


def afficher_datasets(liste=None):
    """
    Affiche une liste de datasets sous forme de tableau aligné.
    Si aucune liste n'est passée en paramètre, affiche la liste complète
    DATASETS (Partie 2, option "Afficher les datasets").
    """
    liste_a_afficher = liste if liste is not None else DATASETS

    if not liste_a_afficher:
        print("\nAucun dataset à afficher.")
        return

    # En-tête du tableau (les nombres entre {} définissent la largeur des colonnes)
    entete = "{:<4} {:<20} {:<12} {:>10} {:>10} {:>10} {:<6} {:<6}".format(
        "ID", "Nom", "Domaine", "Lignes", "Colonnes", "Taille", "Format", "Public"
    )
    print("\n" + entete)
    print("-" * len(entete))

    for d in liste_a_afficher:
        print("{:<4} {:<20} {:<12} {:>10} {:>10} {:>10} {:<6} {:<6}".format(
            d["id"], d["nom"], d["domaine"], d["lignes"], d["colonnes"],
            d["taille"], d["format"].upper(), "Oui" if d["public"] else "Non"
        ))

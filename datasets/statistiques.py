"""
Module statistiques.py
-----------------------
Calcule des statistiques globales sur l'ensemble des datasets, en
s'appuyant volontairement sur des compréhensions de listes et de
dictionnaires (Partie 6 du sujet).
"""

from datasets.gestion import DATASETS, DOMAINES_AUTORISES


def calculer_statistiques():
    """
    Calcule et retourne un dictionnaire de statistiques globales.
    Retourne None si aucun dataset n'est enregistré (évite une division
    par zéro lors du calcul de la moyenne).
    """
    if not DATASETS:
        return None

    nb_datasets = len(DATASETS)

    # --- Compréhensions de liste avec somme -------------------------------
    total_lignes = sum(d["lignes"] for d in DATASETS)
    total_colonnes = sum(d["colonnes"] for d in DATASETS)
    moyenne_colonnes = total_colonnes / nb_datasets

    # --- Compréhensions de liste avec filtre -------------------------------
    # On compte les datasets publics / privés grâce à une condition dans
    # la compréhension.
    nb_publics = len([d for d in DATASETS if d["public"]])
    nb_prives = nb_datasets - nb_publics

    nb_csv = len([d for d in DATASETS if d["format"] == "csv"])
    nb_json = len([d for d in DATASETS if d["format"] == "json"])

    # --- Compréhension de dictionnaire --------------------------------------
    # Construit {domaine: nombre_de_datasets} pour chaque domaine autorisé.
    repartition_domaines = {
        domaine: len([d for d in DATASETS if d["domaine"] == domaine])
        for domaine in DOMAINES_AUTORISES
    }

    return {
        "nb_datasets": nb_datasets,
        "total_lignes": total_lignes,
        "moyenne_colonnes": round(moyenne_colonnes, 2),
        "nb_publics": nb_publics,
        "nb_prives": nb_prives,
        "nb_csv": nb_csv,
        "nb_json": nb_json,
        "repartition_domaines": repartition_domaines,
    }


def afficher_statistiques():
    """Affiche les statistiques calculées de façon lisible dans la console."""
    stats = calculer_statistiques()

    if stats is None:
        print("\nAucun dataset enregistré, impossible de calculer des statistiques.")
        return

    print("\n============ STATISTIQUES ============")
    print(f"Nombre de datasets       : {stats['nb_datasets']}")
    # Formatage avec des espaces comme séparateur de milliers (ex: 2 540 000)
    print(f"Nombre total de lignes   : {stats['total_lignes']:,}".replace(",", " "))
    print(f"Nombre moyen de colonnes : {stats['moyenne_colonnes']}")
    print(f"Datasets publics         : {stats['nb_publics']}")
    print(f"Datasets privés          : {stats['nb_prives']}")
    print(f"Format CSV               : {stats['nb_csv']}")
    print(f"Format JSON              : {stats['nb_json']}")
    print("Répartition par domaine :")
    for domaine, nb in stats["repartition_domaines"].items():
        print(f"   - {domaine} : {nb}")
    print("========================================")

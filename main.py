# ==========================================================
# DATASET MANAGER
# Orange Digital Center - Projet Python
#
# Auteur : Baye Abdoul Aziz Seck
#
# Version corrigée et complétée :
# - Ajouter
# - Afficher
# - Rechercher
# - Modifier
# - Supprimer
# - Trier
# - Statistiques : PARTIE 7
# - Quitter
# ==========================================================

import os

# ==========================================================
# DONNÉES GLOBALES
# ==========================================================

domain_autorise = (
    "Sante",
    "Finance",
    "Agriculture",
    "Transport",
    "Education",
)

# Liste contenant tous les datasets
list_datasets = []


# ==========================================================
# FONCTIONS UTILITAIRES
# ==========================================================

def nettoyer_ecran():
    """Nettoie l'écran selon le système d'exploitation."""
    os.system("cls" if os.name == "nt" else "clear")


def afficher_dataset(dataset):
    """Affiche les informations d'un dataset."""
    print(f"Nom du dataset      : {dataset['nom']}")
    print(f"Domaine             : {dataset['domaine']}")
    print(f"Nombre de lignes    : {dataset['lignes']}")
    print(f"Nombre de colonnes  : {dataset['colonnes']}")
    print(f"Taille (Mo)         : {dataset['taille']}")
    print(f"Format              : {dataset['format']}")
    print(f"Public              : {dataset['public']}")
    print("-" * 35)


def demander_entier_positif(message):
    """Demande un entier positif ou nul à l'utilisateur."""
    while True:
        valeur = input(message)
        try:
            nombre = int(valeur)
            if nombre >= 0:
                return nombre
            print("Erreur : veuillez saisir un nombre positif ou nul.")
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier.")


def demander_entier_positif_modification(message, ancienne_valeur):
    """
    Demande un entier positif ou nul.
    Si l'utilisateur laisse vide, l'ancienne valeur est conservée.
    """
    while True:
        valeur = input(message)

        if valeur.strip() == "":
            return ancienne_valeur

        try:
            nombre = int(valeur)
            if nombre >= 0:
                return nombre
            print("Erreur : veuillez saisir un nombre positif ou nul.")
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier.")


def demander_domaine(message):
    """Demande un domaine autorisé."""
    while True:
        domaine = input(message).strip()

        for d in domain_autorise:
            if domaine.lower() == d.lower():
                return d

        print("Domaine invalide.")
        print("Domaines autorisés :")
        for d in domain_autorise:
            print("-", d)


def demander_domaine_modification(message, ancien_domaine):
    """
    Demande un domaine autorisé.
    Si l'utilisateur laisse vide, l'ancien domaine est conservé.
    """
    while True:
        domaine = input(message).strip()

        if domaine == "":
            return ancien_domaine

        for d in domain_autorise:
            if domaine.lower() == d.lower():
                return d

        print("Domaine invalide.")
        print("Domaines autorisés :")
        for d in domain_autorise:
            print("-", d)


def demander_format(message):
    """Demande un format : CSV ou JSON."""
    while True:
        format_dataset = input(message).strip().upper()

        if format_dataset in ("CSV", "JSON"):
            return format_dataset

        print("Format invalide. Veuillez choisir CSV ou JSON.")


def demander_format_modification(message, ancien_format):
    """
    Demande un format : CSV ou JSON.
    Si l'utilisateur laisse vide, l'ancien format est conservé.
    """
    while True:
        format_dataset = input(message).strip().upper()

        if format_dataset == "":
            return ancien_format

        if format_dataset in ("CSV", "JSON"):
            return format_dataset

        print("Format invalide. Veuillez choisir CSV ou JSON.")


def demander_public(message):
    """Demande si le dataset est public : Oui ou Non."""
    while True:
        public = input(message).strip().lower()

        if public == "oui":
            return "Oui"

        if public == "non":
            return "Non"

        print("Réponse invalide. Veuillez répondre Oui ou Non.")


def demander_public_modification(message, ancien_public):
    """
    Demande si le dataset est public : Oui ou Non.
    Si l'utilisateur laisse vide, l'ancienne valeur est conservée.
    """
    while True:
        public = input(message).strip().lower()

        if public == "":
            return ancien_public

        if public == "oui":
            return "Oui"

        if public == "non":
            return "Non"

        print("Réponse invalide. Veuillez répondre Oui ou Non.")


# ==========================================================
# MENU PRINCIPAL
# ==========================================================

while True:

    nettoyer_ecran()

    print("===================================")
    print("        DATASET MANAGER - P7")
    print("===================================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. Modifier un dataset")
    print("5. Supprimer un dataset")
    print("6. Trier les datasets (par nom)")
    print("7. Afficher les statistiques")
    print("8. Quitter")
    print("===================================")

    try:
        choix = int(input("Entrez votre choix : "))
    except ValueError:
        nettoyer_ecran()
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 8.")
        input("\nAppuyez sur Entrée pour revenir au menu...")
        continue

    nettoyer_ecran()

    match choix:

        # ==================================================
        # CASE 1 : AJOUTER UN DATASET
        # ==================================================
        case 1:
            print("===================================")
            print("      AJOUTER UN DATASET")
            print("===================================")

            datasets = {}

            while True:
                nom = input("Nom du dataset : ").strip()
                if nom != "":
                    break
                print("Le nom du dataset ne peut pas être vide.")

            datasets["nom"] = nom
            datasets["domaine"] = demander_domaine("Domaine : ")
            datasets["lignes"] = demander_entier_positif("Nombre de lignes : ")
            datasets["colonnes"] = demander_entier_positif("Nombre de colonnes : ")
            datasets["taille"] = demander_entier_positif("Taille (Mo) : ")
            datasets["format"] = demander_format("Format (CSV/JSON) : ")
            datasets["public"] = demander_public("Public (Oui/Non) : ")

            list_datasets.append(datasets)

            print("\nLe dataset a été enregistré avec succès.")
            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 2 : AFFICHER LES DATASETS
        # ==================================================
        case 2:
            print("===================================")
            print("   INFORMATIONS DES DATASETS")
            print("===================================")

            if not list_datasets:
                print("Aucun dataset enregistré pour le moment.")
            else:
                for dataset in list_datasets:
                    afficher_dataset(dataset)

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 3 : RECHERCHER UN DATASET
        # ==================================================
        case 3:
            print("===================================")
            print("    RECHERCHER UN DATASET")
            print("===================================")

            if not list_datasets:
                print("Aucun dataset enregistré pour le moment.")
            else:
                recherche = input("Entrez le nom du dataset : ").strip()
                trouve = False

                for dataset in list_datasets:
                    if recherche.lower() == dataset["nom"].lower():
                        print("\nDataset trouvé.\n")
                        afficher_dataset(dataset)
                        trouve = True
                        break

                if not trouve:
                    print("\nDataset introuvable.")

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 4 : MODIFIER UN DATASET
        # ==================================================
        case 4:
            print("===================================")
            print("     MODIFIER UN DATASET")
            print("===================================")

            if not list_datasets:
                print("Aucun dataset enregistré pour le moment.")
            else:
                nom_a_modifier = input("Entrez le nom du dataset à modifier : ").strip()
                trouve = False

                for dataset in list_datasets:
                    if nom_a_modifier.lower() == dataset["nom"].lower():
                        trouve = True

                        print(f"\nDataset '{dataset['nom']}' trouvé.")
                        print("Laissez vide si vous ne souhaitez pas modifier une valeur.\n")

                        nouveau_nom = input(f"Nouveau nom ({dataset['nom']}) : ").strip()
                        if nouveau_nom != "":
                            dataset["nom"] = nouveau_nom

                        dataset["domaine"] = demander_domaine_modification(
                            f"Nouveau domaine ({dataset['domaine']}) : ",
                            dataset["domaine"]
                        )

                        dataset["lignes"] = demander_entier_positif_modification(
                            f"Nombre de lignes ({dataset['lignes']}) : ",
                            dataset["lignes"]
                        )

                        dataset["colonnes"] = demander_entier_positif_modification(
                            f"Nombre de colonnes ({dataset['colonnes']}) : ",
                            dataset["colonnes"]
                        )

                        dataset["taille"] = demander_entier_positif_modification(
                            f"Taille en Mo ({dataset['taille']}) : ",
                            dataset["taille"]
                        )

                        dataset["format"] = demander_format_modification(
                            f"Format ({dataset['format']}) : ",
                            dataset["format"]
                        )

                        dataset["public"] = demander_public_modification(
                            f"Public ({dataset['public']}) : ",
                            dataset["public"]
                        )

                        print("\nDataset modifié avec succès !")
                        break

                if not trouve:
                    print("\nDataset introuvable.")

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 5 : SUPPRIMER UN DATASET
        # ==================================================
        case 5:
            print("===================================")
            print("     SUPPRIMER UN DATASET")
            print("===================================")

            if not list_datasets:
                print("Aucun dataset enregistré pour le moment.")
            else:
                nom_a_supprimer = input("Entrez le nom du dataset à supprimer : ").strip()
                trouve = False

                for index, dataset in enumerate(list_datasets):
                    if nom_a_supprimer.lower() == dataset["nom"].lower():
                        trouve = True

                        print("\nDataset trouvé :")
                        afficher_dataset(dataset)

                        confirmation = input("Confirmer la suppression ? (Oui/Non) : ").strip().lower()

                        if confirmation == "oui":
                            list_datasets.pop(index)
                            print("Dataset supprimé avec succès.")
                        else:
                            print("Suppression annulée.")

                        break

                if not trouve:
                    print("\nDataset introuvable.")

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 6 : TRIER LES DATASETS PAR NOM
        # ==================================================
        case 6:
            print("===================================")
            print("   TRIER LES DATASETS PAR NOM")
            print("===================================")

            if not list_datasets:
                print("Aucun dataset enregistré pour le moment.")
            else:
                list_datasets.sort(key=lambda dataset: dataset["nom"].lower())

                print("Datasets triés par nom :\n")

                for dataset in list_datasets:
                    afficher_dataset(dataset)

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 7 : AFFICHER LES STATISTIQUES
        # PARTIE 7
        # ==================================================
        case 7:
            print("===================================")
            print("      STATISTIQUES DES DATASETS")
            print("===================================")

            if not list_datasets:
                print("Aucun dataset enregistré pour le moment.")
            else:
                total_datasets = len(list_datasets)

                total_lignes = 0
                total_colonnes = 0
                total_taille = 0

                nb_publics = 0

                domaines = {}
                formats = {}

                for dataset in list_datasets:
                    total_lignes += dataset["lignes"]
                    total_colonnes += dataset["colonnes"]
                    total_taille += dataset["taille"]

                    if dataset["public"] == "Oui":
                        nb_publics += 1

                    domaines[dataset["domaine"]] = domaines.get(dataset["domaine"], 0) + 1
                    formats[dataset["format"]] = formats.get(dataset["format"], 0) + 1

                moyenne_lignes = total_lignes / total_datasets
                moyenne_colonnes = total_colonnes / total_datasets
                moyenne_taille = total_taille / total_datasets

                plus_grand = max(list_datasets, key=lambda dataset: dataset["taille"])
                plus_petit = min(list_datasets, key=lambda dataset: dataset["taille"])

                print(f"Nombre total de datasets : {total_datasets}")
                print(f"Total des lignes         : {total_lignes}")
                print(f"Total des colonnes       : {total_colonnes}")
                print(f"Total des tailles (Mo)   : {total_taille}")
                print(f"Moyenne des lignes       : {moyenne_lignes:.2f}")
                print(f"Moyenne des colonnes     : {moyenne_colonnes:.2f}")
                print(f"Moyenne des tailles (Mo) : {moyenne_taille:.2f}")
                print(f"Datasets publics         : {nb_publics}")
                print(f"Datasets non publics     : {total_datasets - nb_publics}")

                print("\nRépartition par domaine :")
                for domaine, nombre in domaines.items():
                    print(f"- {domaine} : {nombre}")

                print("\nRépartition par format :")
                for format_dataset, nombre in formats.items():
                    print(f"- {format_dataset} : {nombre}")

                print("\nDataset le plus grand :")
                afficher_dataset(plus_grand)

                print("Dataset le plus petit :")
                afficher_dataset(plus_petit)

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 8 : QUITTER
        # ==================================================
        case 8:
            print("Merci d'avoir utilisé Dataset Manager. Au revoir !")
            break

        # ==================================================
        # CHOIX NON VALIDE
        # ==================================================
        case _:
            print("Choix invalide. Veuillez choisir une option entre 1 et 8.")
            input("\nAppuyez sur Entrée pour revenir au menu...")
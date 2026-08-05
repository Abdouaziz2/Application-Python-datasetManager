# ==========================================================
# DATASET MANAGER
# Orange Digital Center - Projet Python
#
# Auteur : Baye Abdoul Aziz Seck
#
# Ce fichier évoluera progressivement de la Partie 1
# jusqu'à la Partie 11.
# Les anciennes méthodes seront conservées sous forme
# de commentaires afin de suivre l'évolution du projet.
# ==========================================================

import os

# ==========================================================
# - PARTIE 1
# Types de base, variables, entrées et sorties
# ==========================================================
#
# Dans cette première partie, les informations étaient
# stockées dans plusieurs variables.
#
# nomData = input("Nom : ")
# domaine = input("Domaine : ")
# nombreLigne = int(input("Nombre de lignes : "))
# nombre_colonne = int(input("Nombre de colonnes : "))
# taille = int(input("Taille : "))
# format_dataset = input("Format : ")
# public = input("Public : ")
#
# Cette méthode fonctionne mais devient difficile à gérer
# lorsque plusieurs datasets sont manipulés.
#
# ==========================================================


# ==========================================================
# - PARTIE 2
# Structures de contrôle
# ==========================================================
#
# Cette partie a permis d'ajouter :
#
# • une boucle while
# • un menu interactif
# • une instruction match...case
# • break pour quitter le programme
# • os.system("cls") pour nettoyer l'écran
#
# Le stockage reposait encore sur plusieurs variables.
#
# ==========================================================


# ==========================================================
# PARTIE 3 : DICTIONNAIRES
# ==========================================================
#
# Les informations d'un dataset sont maintenant regroupées
# dans un dictionnaire.
#
# Cette méthode est plus simple à maintenir et facilitera
# l'ajout de plusieurs datasets dans les prochaines parties.
#
# ==========================================================

domain_autorise = ("Sante",
                   "Finance",
                   "Agriculture",
                   "Transport",
                   "Education",
                   )
list_datasets = []

# ==========================================================
# MENU PRINCIPAL
# ==========================================================

while True:

    # Nettoyage de l'écran
    os.system("cls" if os.name == "nt" else "clear")

    # Affichage du menu
    print("===================================")
    print("        DATASET MANAGER")
    print("===================================")
    print("1. Ajouter un dataset")
    print("2. Afficher le dataset")
    print("3. Rechercher un dataset")
    print("4. Quitter")
    print("===================================")

    # Choix de l'utilisateur
    choix = int(input("Entrez votre choix : "))

    # Nettoyage de l'écran
    os.system("cls" if os.name == "nt" else "clear")

    # Analyse du choix
    match choix:
        # ==================================================
        # CASE 1 : AJOUTER UN DATASET
        # ==================================================
        #
        # Cette partie permet de saisir les informations
        # d'un dataset et de les enregistrer dans le
        # dictionnaire "datasets".
        #
        # Ancienne méthode (Partie 1) :
        #
        # nomData = input(...)
        # domaine = input(...)
        # ...
        #
        # Nouvelle méthode (Partie 3) :
        # Toutes les informations sont regroupées dans
        # un seul dictionnaire.
        #
        # ==================================================

        case 1:

            print("===================================")
            print("      AJOUTER UN DATASET")
            print("===================================")

            # Pour la Partie 5 (Gérer plusieurs datasets), on crée un nouveau dictionnaire à chaque fois
            datasets = {}

            # Saisie des informations
            datasets["nom"] = input("Nom du dataset : ")

            # Vérification du domaine autorisé
            while True:
                domaine = input("Domaine : ")

                if domaine in domain_autorise:
                    datasets["domaine"] = domaine
                    print("Domaine enregistré avec succès.")
                    break
                else:
                    print("Domaine invalide.")
                    print("Domaines autorisés :")
                    for item in domain_autorise:
                        print("-", item)

            datasets["lignes"] = int(input("Nombre de lignes : "))
            datasets["colonnes"] = int(input("Nombre de colonnes : "))
            datasets["taille"] = int(input("Taille (Mo) : "))
            datasets["format"] = input("Format (CSV/JSON) : ")
            datasets["public"] = input("Public (Oui/Non) : ")

            print("\nLe dataset a été enregistré avec succès.")
            list_datasets.append(datasets)

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # TODO - Partie 4
        # Vérifier que le domaine appartient au tuple des domaines autorisés.

        # TODO - Partie 5
        # Ajouter ce dictionnaire dans une liste afin de gérer plusieurs datasets.

        # ==================================================
        # CASE 2 : AFFICHER LE DATASET
        # ==================================================
        #
        # Cette partie affiche les informations contenues
        # dans le dictionnaire.
        #
        # Toutes les données sont récupérées grâce à leur clé.
        #
        # Exemple :
        # datasets["nom"]
        #
        # ==================================================

        case 2:
            print("===================================")
            print("   INFORMATIONS DES DATASETS")
            print("===================================")

            # Correction pour la Partie 5 : On parcourt la liste des datasets
            for dataset in list_datasets:
                print(f"Nom du dataset      : {dataset['nom']}")
                print(f"Domaine             : {dataset['domaine']}")
                print(f"Nombre de lignes    : {dataset['lignes']}")
                print(f"Nombre de colonnes  : {dataset['colonnes']}")
                print(f"Taille (Mo)         : {dataset['taille']}")
                print(f"Format              : {dataset['format']}")
                print(f"Public              : {dataset['public']}")
                print("-" * 35)

            # L'attente est sortie de la boucle pour ne pas bloquer à chaque dataset
            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 3 : RECHERCHER UN DATASET
        # ==================================================
        #
        # Pour cette première version, la recherche est
        # effectuée uniquement sur le nom du dataset.
        #
        # Si le nom saisi correspond au nom enregistré,
        # les informations sont affichées.
        #
        # ==================================================

        case 3:

            print("===================================")
            print("    RECHERCHER UN DATASET")
            print("===================================")

            recherche = input("Entrez le nom du dataset : ")
            trouve = False

            # Correction pour chercher à travers TOUTE la liste multi-datasets
            for dataset in list_datasets:
                if recherche.lower() == dataset["nom"].lower():
                    print("\nDataset trouvé.\n")
                    print(f"Nom du dataset      : {dataset['nom']}")
                    print(f"Domaine             : {dataset['domaine']}")
                    print(f"Nombre de lignes    : {dataset['lignes']}")
                    print(f"Nombre de colonnes  : {dataset['colonnes']}")
                    print(f"Taille (Mo)         : {dataset['taille']}")
                    print(f"Format              : {dataset['format']}")
                    print(f"Public              : {dataset['public']}")
                    trouve = True
                    break

            if not trouve:
                print("\nDataset introuvable.")

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 4 : QUITTER
        # ==================================================
        case 4:
            print("Fermeture du Dataset Manager. Au revoir !")
            break

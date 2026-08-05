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

# ==========================================================
# PARTIE 5 : LISTES (Questions 9 et 10)
# ==========================================================
# 9) Chaque ajout est enregistré dans cette liste.
list_datasets = []

# ==========================================================
# MENU PRINCIPAL
# ==========================================================

while True:

    # Nettoyage de l'écran
    os.system("cls" if os.name == "nt" else "clear")

    # Affichage du menu mis à jour avec les fonctionnalités demandées
    print("===================================")
    print("        DATASET MANAGER - P5")
    print("===================================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. Modifier un dataset")
    print("5. Supprimer un dataset")
    print("6. Trier les datasets (par nom)")
    print("7. Quitter")
    print("===================================")

    # Choix de l'utilisateur
    choix = int(input("Entrez votre choix : "))

    # Nettoyage de l'écran
    os.system("cls" if os.name == "nt" else "clear")

    # Analyse du choix
    match choix:
        # ==================================================
        # CASE 1 : AJOUTER UN DATASET (Fonctionnalité : Ajouter)
        # ==================================================
        case 1:
            print("===================================")
            print("      AJOUTER UN DATASET")
            print("===================================")

            # On initialise un nouveau dictionnaire indépendant pour ce dataset
            datasets = {}

            datasets["nom"] = input("Nom du dataset : ")

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

            # Ajout persistant dans la liste globale
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
                    print(f"Nom du dataset      : {dataset['nom']}")
                    print(f"Domaine             : {dataset['domaine']}")
                    print(f"Nombre de lignes    : {dataset['lignes']}")
                    print(f"Nombre de colonnes  : {dataset['colonnes']}")
                    print(f"Taille (Mo)         : {dataset['taille']}")
                    print(f"Format              : {dataset['format']}")
                    print(f"Public              : {dataset['public']}")
                    print("-" * 35)

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 3 : RECHERCHER UN DATASET (Fonctionnalité : Rechercher)
        # ==================================================
        case 3:
            print("===================================")
            print("    RECHERCHER UN DATASET")
            print("===================================")

            recherche = input("Entrez le nom du dataset : ")
            trouve = False

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
        # CASE 4 : MODIFIER UN DATASET (Fonctionnalité : Modifier)
        # ==================================================
        case 4:
            print("===================================")
            print("     MODIFIER UN DATASET")
            print("===================================")

            nom_a_modifier = input("Entrez le nom du dataset à modifier : ")
            trouve = False

            for dataset in list_datasets:
                if nom_a_modifier.lower() == dataset["nom"].lower():
                    trouve = True
                    print(f"\nDataset '{dataset['nom']}' trouvé. Entrez les nouvelles valeurs.")

                    # Modification des valeurs du dictionnaire ciblé
                    dataset["nom"] = input(f"Nouveau nom ({dataset['nom']}) : ") or dataset["nom"]

                    while True:
                        nouveau_dom = input(f"Nouveau domaine ({dataset['domaine']}) : ") or dataset["domaine"]
                        if nouveau_dom in domain_autorise:
                            dataset["domaine"] = nouveau_dom
                            break
                        print("Domaine invalide.")

                    saisie_lignes = input(f"Nombre de lignes ({dataset['lignes']}) : ")
                    if saisie_lignes: dataset["lignes"] = int(saisie_lignes)

                    saisie_col = input(f"Nombre de colonnes ({dataset['colonnes']}) : ")
                    if saisie_col: dataset["colonnes"] = int(saisie_col)

                    saisie_taille = input(f"Taille ({dataset['taille']} Mo) : ")
                    if saisie_taille: dataset["taille"] = int(saisie_taille)

                    dataset["format"] = input(f"Format ({dataset['format']}) : ") or dataset["format"]
                    dataset["public"] = input(f"Public ({dataset['public']}) : ") or dataset["public"]

                    print("\nDataset modifié avec succès !")
                    break

            if not trouve:
                print("\nDataset introuvable.")

            input("\nAppuyez sur Entrée pour revenir au menu...")

        # ==================================================
        # CASE 5 : SUPPRIMER UN DATASET (Fonctionnalité : Supprimer)
        # ==================================================
        case 5:
            print("===================================")
            print("     SUPPRIMER UN DATASET")
            print("===================================")


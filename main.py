import os
# ==========================================
# DATASET MANAGER - Partie 2
# Menu interactif
# ==========================================

# La boucle permet de maintenir le programme actif
# jusqu'à ce que l'utilisateur choisisse de quitter.
while True:

    # Affichage du menu
    print("\n========================")
    print("     DATASET MANAGER")
    print("========================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. Quitter")
    print("========================")

    # Demande du choix de l'utilisateur
    choix = int(input("Entrez votre choix : "))
    os.system("cls")

    # Analyse du choix
    match choix:

        # Ajouter un dataset
        case 1:

            print("\n=== Ajouter un dataset ===")

            nomData = input("Entrez le nom du dataset : ")
            domaine = input("Entrez le domaine : ")
            nombreLigne = int(input("Entrez le nombre de lignes : "))
            nombre_colonne = int(input("Entrez le nombre de colonnes : "))
            taille = int(input("Entrez le taille : "))
            format_dataset = input("Entrez le format du dataset (CSV/JSON) : ")
            public = input("Le dataset est-il public ? (Oui/Non) : ")

            print("\nDataset enregistré avec succès !")

        # Afficher le dataset
        case 2:

            print("\n===== INFORMATIONS DU DATASET =====")
            print(f"Nom du dataset      : {nomData}")
            print(f"Domaine             : {domaine}")
            print(f"Nombre de lignes    : {nombreLigne}")
            print(f"Nombre de colonnes  : {nombre_colonne}")
            print(f"Taille               : {taille}")
            print(f"Format              : {format_dataset}")
            print(f"Public              : {public}")

            input("\nAppuyez sur Entrée pour revenir au menu...")

            os.system("cls")


        # Rechercher
        case 3:

            print("\n'Rechercher un dataset' !")

            input("\nAppuyez sur Entrée pour revenir au menu...")

            os.system("cls")

        # Quitter
        case 4:

            print("\nMerci d'avoir utilisé DatasetManager.")
            print("À bientôt !")

            break

        # Cas où le choix est invalide
        case _:

            print("\nChoix invalide ! Veuillez choisir un nombre entre 1 et 4.")

            input("\nAppuyez sur Entrée pour revenir au menu...")

            os.system("cls")
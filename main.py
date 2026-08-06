# ==========================================================
# DATASET MANAGER
# Orange Digital Center - Projet Python
#
# Auteur : Baye Abdoul Aziz Seck
#
# Version progressive SANS fonctions personnalisées.
#
# Notions utilisées :
# - types de base
# - variables
# - entrées / sorties
# - structures de contrôle
# - dictionnaires
# - tuples
# - listes
# - compréhensions
# - fichiers CSV
# - exceptions
#
# La Partie 9 seulement introduira les fonctions.
# ==========================================================

import os

# ==========================================================
# PARTIE 4 : TUPLES
# ==========================================================
# Domaines autorisés.
# Le tuple n'est pas modifiable.

domain_autorise = (
    "Santé",
    "Finance",
    "Agriculture",
    "Transport",
    "Education",
)

# ==========================================================
# PARTIE 5 : LISTES
# ==========================================================
# Chaque dataset est un dictionnaire.
# Tous les datasets sont enregistrés dans cette liste.

list_datasets = []

# Nom du fichier CSV utilisé pour la sauvegarde.
fichier_sauvegarde = "datasets.csv"

# Séparateur visuel pour l'affichage.
separateur = "-" * 35

# LES FONCTIONS PARTIE 9:
#a-  Fonction netoyer pour les menu ..

def netoyer_ecran():
    os.system("cls" if os.name == "nt" else "clear")
#a-  Fonction pour Afficher le menu ..

def Afficher_menu():
    print("===================================")
    print("        DATASET MANAGER - P8")
    print("===================================")
    print("1. Ajouter un dataset")
    print("2. Afficher les datasets")
    print("3. Rechercher un dataset")
    print("4. Modifier un dataset")
    print("5. Supprimer un dataset")
    print("6. Trier les datasets (par nom)")
    print("7. Afficher les statistiques")
    print("8. Sauvegarder dans datasets.csv")
    print("9. Charger depuis datasets.csv")
    print("10. Quitter")
    print("===================================")
# FONCTION POUR AFFICHER UN DATASET
def Afficher_dataset():
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
            print(separateur)

#FONCTION POUR AJOUTER DATASET
def ajouter_dataset():
    print("===================================")
    print("      AJOUTER UN DATASET")
    print("===================================")

    # PARTIE 3 : DICTIONNAIRE
    # Un dataset est stocké sous forme de dictionnaire.
    datasets = {}

    # Saisie du nom du dataset.
    while True:
        nom = input("Nom du dataset : ").strip()

        if nom == "":
            print("Le nom du dataset ne peut pas être vide.")

        elif ";" in nom:
            print("Le nom ne doit pas contenir de ';' car il sera sauvegardé en CSV.")

        else:
            break

    datasets["nom"] = nom

    # Saisie du domaine avec vérification par rapport au tuple.
    while True:
        domaine_saisi = input("Domaine : ").strip()
        domaine_valide = False

        for domaine in domain_autorise:
            # On accepte aussi la saisie sans accent.
            # Exemple : "Sante" pour "Santé".
            if domaine_saisi.lower().replace("é", "e") == domaine.lower().replace("é", "e"):
                datasets["domaine"] = domaine
                domaine_valide = True
                break

        if domaine_valide:
            break

        print("Domaine invalide.")
        print("Domaines autorisés :")
        for domaine in domain_autorise:
            print("-", domaine)

    # Saisie du nombre de lignes.
    while True:
        saisie = input("Nombre de lignes : ").strip()

        if saisie.isdigit():
            datasets["lignes"] = int(saisie)
            break

        print("Erreur : veuillez saisir un nombre entier positif ou nul.")

    # Saisie du nombre de colonnes.
    while True:
        saisie = input("Nombre de colonnes : ").strip()

        if saisie.isdigit():
            datasets["colonnes"] = int(saisie)
            break

        print("Erreur : veuillez saisir un nombre entier positif ou nul.")

    # Saisie de la taille en Mo.
    while True:
        saisie = input("Taille (Mo) : ").strip()

        if saisie.isdigit():
            datasets["taille"] = int(saisie)
            break

        print("Erreur : veuillez saisir un nombre entier positif ou nul.")

    # Saisie du format.
    while True:
        format_saisi = input("Format (CSV/JSON) : ").strip().upper()

        if format_saisi in ("CSV", "JSON"):
            datasets["format"] = format_saisi
            break

        print("Format invalide. Veuillez choisir CSV ou JSON.")

    # Saisie du champ public.
    # Le sujet demande true ou false.
    while True:
        public_saisi = input("Public (true/false) : ").strip().lower()

        if public_saisi in ("true", "vrai", "oui", "1"):
            datasets["public"] = True
            break

        if public_saisi in ("false", "faux", "non", "0"):
            datasets["public"] = False
            break

        print("Public invalide. Utilisez true ou false.")

    # PARTIE 5 : LISTES
    # On ajoute le dictionnaire dans la liste des datasets.
    list_datasets.append(datasets)
    print("\nLe dataset a été enregistré avec succès.")

# FONCTIONS POUR SUPPRIMER un data set
def Supprimer_dataset():
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
                print(f"Nom du dataset      : {dataset['nom']}")
                print(f"Domaine             : {dataset['domaine']}")
                print(f"Nombre de lignes    : {dataset['lignes']}")
                print(f"Nombre de colonnes  : {dataset['colonnes']}")
                print(f"Taille (Mo)         : {dataset['taille']}")
                print(f"Format              : {dataset['format']}")
                print(f"Public              : {dataset['public']}")
                print(separateur)
                confirmation = input("Confirmer la suppression ? (Oui/Non) : ").strip().lower()
                if confirmation in ("oui", "true", "1", "vrai"):
                    list_datasets.pop(index)
                    print("Dataset supprimé avec succès.")
                else:
                    print("Suppression annulée.")
                break
        if not trouve:
            print("\nDataset introuvable.")

#FONCTIONS POUR RECHERCHER UN DATASET
def rechercher_dataset():
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
                print(f"Nom du dataset      : {dataset['nom']}")
                print(f"Domaine             : {dataset['domaine']}")
                print(f"Nombre de lignes    : {dataset['lignes']}")
                print(f"Nombre de colonnes  : {dataset['colonnes']}")
                print(f"Taille (Mo)         : {dataset['taille']}")
                print(f"Format              : {dataset['format']}")
                print(f"Public              : {dataset['public']}")
                print(separateur)
                trouve = True
                break

        if not trouve:
            print("\nDataset introuvable.")

#FONCTIONS POUR TRIERZ UN DATASET
def trier_dataset():
    print("===================================")
    print("   TRIER LES DATASETS PAR NOM")
    print("===================================")

    if not list_datasets:
        print("Aucun dataset enregistré pour le moment.")
    else:
        # Tri manuel sans fonction personnalisée ni lambda.
        # On utilise une méthode simple de tri à bulles.
        n = len(list_datasets)
        for i in range(n):
            for j in range(0, n - i - 1):
                nom1 = list_datasets[j]["nom"].lower()
                nom2 = list_datasets[j + 1]["nom"].lower()
                if nom1 > nom2:
                    list_datasets[j], list_datasets[j + 1] = list_datasets[j + 1], list_datasets[j]
        print("Datasets triés par nom avec succès.\n")
        for dataset in list_datasets:
            print(f"Nom du dataset      : {dataset['nom']}")
            print(f"Domaine             : {dataset['domaine']}")
            print(f"Nombre de lignes    : {dataset['lignes']}")
            print(f"Nombre de colonnes  : {dataset['colonnes']}")
            print(f"Taille (Mo)         : {dataset['taille']}")
            print(f"Format              : {dataset['format']}")
            print(f"Public              : {dataset['public']}")
            print(separateur)


#FONCTIONS POUR MODIFIER  LE DATASET
def modifier_dataset():
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

                # Modification du nom.
                nouveau_nom = input(f"Nouveau nom ({dataset['nom']}) : ").strip()

                if nouveau_nom != "":
                    if ";" in nouveau_nom:
                        print("Le nom ne doit pas contenir de ';'. Nom non modifié.")
                    else:
                        dataset["nom"] = nouveau_nom
                # Modification du domaine.
                while True:
                    nouveau_domaine = input(f"Nouveau domaine ({dataset['domaine']}) : ").strip()

                    if nouveau_domaine == "":
                        break

                    domaine_valide = False

                    for domaine in domain_autorise:
                        if nouveau_domaine.lower().replace("é", "e") == domaine.lower().replace("é", "e"):
                            dataset["domaine"] = domaine
                            domaine_valide = True
                            break

                    if domaine_valide:
                        break

                    print("Domaine invalide.")
                    print("Domaines autorisés :")
                    for domaine in domain_autorise:
                        print("-", domaine)

                # Modification du nombre de lignes.
                while True:
                    saisie = input(f"Nombre de lignes ({dataset['lignes']}) : ").strip()

                    if saisie == "":
                        break

                    if saisie.isdigit():
                        dataset["lignes"] = int(saisie)
                        break

                    print("Erreur : veuillez saisir un nombre entier positif ou nul.")

                # Modification du nombre de colonnes.
                while True:
                    saisie = input(f"Nombre de colonnes ({dataset['colonnes']}) : ").strip()

                    if saisie == "":
                        break

                    if saisie.isdigit():
                        dataset["colonnes"] = int(saisie)
                        break

                    print("Erreur : veuillez saisir un nombre entier positif ou nul.")

                # Modification de la taille.
                while True:
                    saisie = input(f"Taille en Mo ({dataset['taille']}) : ").strip()

                    if saisie == "":
                        break

                    if saisie.isdigit():
                        dataset["taille"] = int(saisie)
                        break

                    print("Erreur : veuillez saisir un nombre entier positif ou nul.")

                # Modification du format.
                while True:
                    saisie = input(f"Format ({dataset['format']}) : ").strip().upper()

                    if saisie == "":
                        break

                    if saisie in ("CSV", "JSON"):
                        dataset["format"] = saisie
                        break

                    print("Format invalide. Veuillez choisir CSV ou JSON.")

                # Modification du champ public.
                while True:
                    saisie = input(f"Public ({dataset['public']}) : ").strip().lower()

                    if saisie == "":
                        break

                    if saisie in ("true", "vrai", "oui", "1"):
                        dataset["public"] = True
                        break

                    if saisie in ("false", "faux", "non", "0"):
                        dataset["public"] = False
                        break

                    print("Public invalide. Utilisez true ou false.")

                print("\nDataset modifié avec succès !")
                break

        if not trouve:
            print("\nDataset introuvable.")

#FONCTION POUR SAUVEGARDER
def sauvegarder():
    print("===================================")
    print("     SAUVEGARDER DANS datasets.csv")
    print("===================================")

    if not list_datasets:
        print("Aucun dataset à sauvegarder.")
    else:
        try:
            with open(fichier_sauvegarde, "w", encoding="utf-8") as fichier:
                fichier.write("nom;domaine;lignes;colonnes;taille;format;public\n")

                for dataset in list_datasets:
                    ligne = (
                        f"{dataset['nom']};{dataset['domaine']};{dataset['lignes']};"
                        f"{dataset['colonnes']};{dataset['taille']};{dataset['format']};"
                        f"{dataset['public']}\n"
                    )
                    fichier.write(ligne)

            print("Sauvegarde effectuée avec succès dans datasets.csv.")

        except PermissionError:
            print("Erreur : impossible d'écrire dans le fichier (accès refusé).")

        except OSError:
            print("Erreur : une erreur est survenue lors de l'écriture du fichier.")

#FONCTIONS POUR RECHARGER UN DATASET
def recharger():
    print("===================================")
    print("    CHARGER DEPUIS datasets.csv")
    print("===================================")

    try:
        if not os.path.exists(fichier_sauvegarde):
            print("Erreur : le fichier datasets.csv n'existe pas.")

        else:
            with open(fichier_sauvegarde, "r", encoding="utf-8") as fichier:
                lignes_fichier = fichier.readlines()

            if len(lignes_fichier) <= 1:
                print("Erreur : le fichier datasets.csv est vide.")

            else:
                list_datasets.clear()

                for index, ligne in enumerate(lignes_fichier):
                    if index == 0:
                        continue

                    ligne = ligne.strip()

                    if ligne == "":
                        continue

                    valeurs = ligne.split(";")

                    if len(valeurs) == 7 and valeurs[2].isdigit() and valeurs[3].isdigit() and valeurs[4].isdigit():
                        dataset = {}
                        dataset["nom"] = valeurs[0]
                        dataset["domaine"] = valeurs[1]
                        dataset["lignes"] = int(valeurs[2])
                        dataset["colonnes"] = int(valeurs[3])
                        dataset["taille"] = int(valeurs[4])
                        dataset["format"] = valeurs[5].upper()
                        dataset["public"] = valeurs[6] == "True"

                        list_datasets.append(dataset)

                print("Chargement effectué avec succès depuis datasets.csv.")

    except FileNotFoundError:
        print("Erreur : le fichier datasets.csv est introuvable.")

    except OSError:
        print("Erreur : une erreur est survenue lors de la lecture du fichier.")
#FONCTION POUR AFFICHER LE STATISTIQUE
def statistiques():
    print("===================================")
    print("        STATISTIQUES")
    print("===================================")

    if not list_datasets:
        print("Aucun dataset enregistré pour le moment.")
    else:
        nombre_datasets = len(list_datasets)

        # Compréhension de liste : lignes de chaque dataset.
        liste_lignes = [dataset["lignes"] for dataset in list_datasets]
        total_lignes = sum(liste_lignes)

        # Compréhension de liste : colonnes de chaque dataset.
        liste_colonnes = [dataset["colonnes"] for dataset in list_datasets]
        moyenne_colonnes = sum(liste_colonnes) / nombre_datasets

        # Compréhension de liste : datasets publics / privés.
        datasets_publics = [dataset for dataset in list_datasets if dataset["public"] is True]
        datasets_prives = [dataset for dataset in list_datasets if dataset["public"] is False]

        # Compréhension de liste : datasets par format.
        datasets_csv = [dataset for dataset in list_datasets if dataset["format"] == "CSV"]
        datasets_json = [dataset for dataset in list_datasets if dataset["format"] == "JSON"]

        # Compréhension de dictionnaire : répartition par domaine.
        repartition_domaines = {
            domaine: len([dataset for dataset in list_datasets if dataset["domaine"] == domaine])
            for domaine in domain_autorise
        }
        print(f"Nombre de datasets        : {nombre_datasets}")
        print(f"Nombre total de lignes    : {total_lignes}")
        print(f"Nombre moyen de colonnes  : {moyenne_colonnes:.0f}")
        print(f"Datasets publics          : {len(datasets_publics)}")
        print(f"Datasets privés           : {len(datasets_prives)}")
        print(f"Datasets au format CSV    : {len(datasets_csv)}")
        print(f"Datasets au format JSON   : {len(datasets_json)}")
        print("\nRépartition par domaine :")

        for domaine, total in repartition_domaines.items():
            print(f"  {domaine} : {total}")

# ==========================================================
# PARTIE 7 : FICHIERS
# ==========================================================
# Chargement automatique des données au démarrage du programme.
# Si le fichier datasets.csv existe, on lit son contenu.
#
# Format attendu :
# nom;domaine;lignes;colonnes;taille;format;public
#
# Exemple :
# Titanic;Transport;891;12;48;CSV;True
#
# PARTIE 8 : EXCEPTIONS
# Le chargement au démarrage est protégé : fichier absent,
# fichier vide ou erreur de lecture ne doivent pas empêcher
# le programme de démarrer.

try:
    if os.path.exists(fichier_sauvegarde):
        with open(fichier_sauvegarde, "r", encoding="utf-8") as fichier:
            lignes_fichier = fichier.readlines()

        # On charge seulement s'il y a au moins l'en-tête et une ligne de données.
        if len(lignes_fichier) > 1:
            for index, ligne in enumerate(lignes_fichier):

                # La première ligne est l'en-tête.
                if index == 0:
                    continue

                ligne = ligne.strip()

                # Ignorer les lignes vides.
                if ligne == "":
                    continue

                valeurs = ligne.split(";")

                # On vérifie qu'il y a bien 7 colonnes.
                if len(valeurs) == 7:

                    # On vérifie que les nombres sont corrects.
                    if valeurs[2].isdigit() and valeurs[3].isdigit() and valeurs[4].isdigit():

                        dataset = {}
                        dataset["nom"] = valeurs[0]
                        dataset["domaine"] = valeurs[1]
                        dataset["lignes"] = int(valeurs[2])
                        dataset["colonnes"] = int(valeurs[3])
                        dataset["taille"] = int(valeurs[4])
                        dataset["format"] = valeurs[5].upper()

                        if valeurs[6] == "True":
                            dataset["public"] = True
                        else:
                            dataset["public"] = False

                        list_datasets.append(dataset)

except OSError:
    # Le fichier existe peut-être mais n'a pas pu être lu (droits, etc.).
    # On démarre simplement avec une liste vide.
    list_datasets = []


# ==========================================================
# MENU PRINCIPAL
# ==========================================================

while True:

    # Nettoyage de l'écran.
    netoyer_ecran()
    # print("===================================")
    # print("        DATASET MANAGER - P8")
    # print("===================================")
    # print("1. Ajouter un dataset")
    # print("2. Afficher les datasets")
    # print("3. Rechercher un dataset")
    # print("4. Modifier un dataset")
    # print("5. Supprimer un dataset")
    # print("6. Trier les datasets (par nom)")
    # print("7. Afficher les statistiques")
    # print("8. Sauvegarder dans datasets.csv")
    # print("9. Charger depuis datasets.csv")
    # print("10. Quitter")
    # print("===================================")
    Afficher_menu()

    choix_saisie = input("Entrez votre choix : ").strip()

    # Vérification du choix sans utiliser les exceptions.
    if not choix_saisie.isdigit():
        os.system("cls" if os.name == "nt" else "clear")
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 10.")
        input("\nAppuyez sur Entrée pour revenir au menu...")
        continue

    choix = int(choix_saisie)

    # Nettoyage de l'écran après le choix.
    netoyer_ecran()
    match choix:

        # ==================================================
        # CASE 1 : AJOUTER UN DATASET
        # ==================================================
        case 1:
            ajouter_dataset()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        # ==================================================
        # CASE 2 : AFFICHER LES DATASETS
        # ==================================================
        case 2:
            print("===================================")
            print("   INFORMATIONS DES DATASETS")
            print("===================================")
            Afficher_dataset()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        # ==================================================
        # CASE 3 : RECHERCHER UN DATASET
        # ==================================================
        case 3:
            rechercher_dataset()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        # ==================================================
        # CASE 4 : MODIFIER UN DATASET
        # ==================================================
        case 4:
            modifier_dataset()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        # ==================================================
        # CASE 5 : SUPPRIMER UN DATASET
        # ==================================================
        case 5:
            Supprimer_dataset()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        # ==================================================
        # CASE 6 : TRIER LES DATASETS PAR NOM
        # ==================================================
        case 6:
            trier_dataset()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        # ==================================================
        # CASE 7 : AFFICHER LES STATISTIQUES
        # PARTIE 6 : COMPRÉHENSIONS (listes et dictionnaire)
        # ==================================================
        case 7:
            statistiques()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        # ==================================================
        # CASE 8 : SAUVEGARDER DANS datasets.csv
        # PARTIE 7 : FICHIERS / PARTIE 8 : EXCEPTIONS
        # ==================================================
        case 8:
            fichier_sauvegarde()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        # ==================================================
        # CASE 9 : CHARGER DEPUIS datasets.csv
        # PARTIE 7 : FICHIERS / PARTIE 8 : EXCEPTIONS
        # ==================================================
        case 9:
            recharger()
            input("\nAppuyez sur Entrée pour revenir au menu...")
        # ==================================================
        # CASE 10 : QUITTER
        # ==================================================
        case 10:
            print("Merci d'avoir utilisé DatasetManager. À bientôt !")
            break

        # ==================================================
        # CASE PAR DÉFAUT : CHOIX HORS LIMITES (11, 0, ...)
        # ==================================================
        case _:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 10.")
            input("\nAppuyez sur Entrée pour revenir au menu...")
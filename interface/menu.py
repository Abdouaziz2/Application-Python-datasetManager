"""
Module menu.py
---------------
Gère l'affichage du menu interactif (Partie 2) et la boucle principale
de l'application, qui orchestre tous les autres modules.
"""
import os
from datasets import gestion, statistiques
from interface import affichage
from stockage import csv_manager, json_manager

def nettoyer_ecran():
    os.system("cls" if os.name == "nt" else "clear")
def afficher_menu():
    """Partie 2 : affiche le menu interactif de l'application."""
    print("\n================================")
    print("   GESTIONNAIRE DE DATASETS")
    print("================================")
    print("1.  Ajouter un dataset")
    print("2.  Afficher les datasets")
    print("3.  Rechercher un dataset")
    print("4.  Modifier un dataset")
    print("5.  Supprimer un dataset")
    print("6.  Trier les datasets")
    print("7.  Afficher les statistiques")
    print("8.  Sauvegarder (CSV et JSON)")
    print("9.  Recharger depuis un fichier")
    print("10. Quitter")
    print("================================")


def lancer_application():
    """
    Boucle principale de l'application (Partie 2 + Partie 9).
    Reste active tant que l'utilisateur ne choisit pas "Quitter".

    Toutes les exceptions d'utilisation (saisie invalide, fichier absent,
    dataset introuvable, fichier vide...) sont interceptées ici afin que
    le programme ne s'arrête jamais brutalement (Partie 8).
    """
    # Chargement automatique des données existantes au démarrage
    charger_donnees_existantes()

    actif = True
    while actif:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        try:
            if choix == "1":
                gestion.ajouter_dataset()

            elif choix == "2":
                affichage.afficher_datasets()

            elif choix == "3":
                terme = input("Nom (ou partie du nom) à rechercher : ")
                resultats = gestion.rechercher_dataset(terme)
                if resultats:
                    affichage.afficher_datasets(resultats)
                else:
                    # Partie 8 : cas du dataset recherché qui n'existe pas
                    print("Aucun dataset ne correspond à cette recherche.")

            elif choix == "4":
                id_dataset = gestion.demander_entier("ID du dataset à modifier : ")
                gestion.modifier_dataset(id_dataset)

            elif choix == "5":
                id_dataset = gestion.demander_entier("ID du dataset à supprimer : ")
                confirmation = input("Confirmer la suppression ? (o/n) : ").strip().lower()
                if confirmation == "o":
                    gestion.supprimer_dataset(id_dataset)
                else:
                    print("Suppression annulée.")

            elif choix == "6":
                critere = input("Trier par (nom/lignes/colonnes/taille/domaine) : ").strip().lower()
                ordre_decroissant = input("Ordre décroissant ? (o/n) : ").strip().lower() == "o"
                resultats = gestion.trier_dataset(critere, ordre_decroissant)
                affichage.afficher_datasets(resultats)

            elif choix == "7":
                statistiques.afficher_statistiques()

            elif choix == "8":
                csv_manager.sauvegarder_csv(gestion.DATASETS)
                json_manager.sauvegarder_json(gestion.DATASETS)
                print("Sauvegarde terminée (datasets.csv + datasets.json).")

            elif choix == "9":
                charger_donnees_existantes(forcer=True)

            elif choix == "10":
                # Sauvegarde automatique avant de quitter (fonctionnalité bonus)
                csv_manager.sauvegarder_csv(gestion.DATASETS)
                json_manager.sauvegarder_json(gestion.DATASETS)
                print("Données sauvegardées. Au revoir !")
                actif = False

            else:
                print("Choix invalide, veuillez réessayer.")

        # -------------------------------------------------------------
        # Partie 8 : gestion centralisée des exceptions d'utilisation
        # -------------------------------------------------------------
        except KeyError as e:
            # Levée par modifier_dataset()/supprimer_dataset() si l'id n'existe pas
            print(f"Erreur : {e}")
        except ValueError as e:
            # Levée par trier_dataset() si le critère est invalide
            print(f"Erreur : {e}")
        except FileNotFoundError as e:
            # Levée par les modules de stockage si le fichier n'existe pas
            print(f"Erreur : fichier introuvable ({e}).")
        except Exception as e:
            # Filet de sécurité : toute erreur imprévue ne doit jamais
            # faire planter le programme.
            print(f"Une erreur inattendue est survenue : {e}")


def charger_donnees_existantes(forcer=False):
    """
    Tente de recharger automatiquement les données déjà sauvegardées :
    d'abord depuis datasets.csv, sinon depuis datasets.json.
    Gère le cas où les fichiers n'existent pas ou sont vides (Partie 8).

    Le paramètre `forcer` sert uniquement à afficher un message explicite
    quand l'utilisateur déclenche lui-même un rechargement (option 9 du menu).
    """
    try:
        donnees = csv_manager.charger_csv()
        if donnees:
            gestion.DATASETS.clear()
            gestion.DATASETS.extend(donnees)
            gestion.recharger_id_max()
            print(f"{len(donnees)} dataset(s) rechargé(s) depuis datasets.csv.")
            return
    except FileNotFoundError:
        pass  # Pas grave : on essaiera le JSON ensuite
    except Exception as e:
        print(f"Erreur lors du chargement du CSV : {e}")

    try:
        donnees = json_manager.charger_json()
        if donnees:
            gestion.DATASETS.clear()
            gestion.DATASETS.extend(donnees)
            gestion.recharger_id_max()
            print(f"{len(donnees)} dataset(s) rechargé(s) depuis datasets.json.")
            return
    except FileNotFoundError:
        if forcer:
            print("Aucun fichier de données trouvé (ni CSV, ni JSON).")
    except Exception as e:
        print(f"Erreur lors du chargement du JSON : {e}")

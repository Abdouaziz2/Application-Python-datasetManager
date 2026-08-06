"""
main.py
--------
Point d'entrée de l'application "Dataset Manager".

Cette application console permet aux Data Scientists de gérer un
catalogue de datasets (nom, domaine, taille, format, etc.) avant de
commencer leurs traitements avec Pandas.

Fonctionnalités :
    - ajout / affichage / recherche / modification / suppression / tri
    - statistiques globales sur le catalogue
    - sauvegarde et rechargement automatique (CSV + JSON)
    - gestion des erreurs de saisie et de fichiers

Lancement : python main.py
"""
from interface.menu import afficher_menu, nettoyer_ecran
from interface.menu import lancer_application

if __name__ == "__main__":
    print("Bienvenue dans Dataset Manager !")
    lancer_application()

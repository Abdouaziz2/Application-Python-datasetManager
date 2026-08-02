# Saisie des donnee du datasets
nomData= input("Entrez le nom du dataset : ")
domaine = input("Entrez le domaine: ")
nombreLigne = int(input("Entrez le nombre de la ligne: "))
nombre_colonne = int(input("Entrez le nombre de la colonne: "))
format_dataset = input("Entrez le format_dataset : ")
public = bool(input("Est ce public ? Oui /Non: "))
 #Affichage un resume formate

print("Voici les donnee du dataset\n")
print(f"Nom du Dataset {nomData}")
print(f"Domaine{domaine}")
print(f"Nombre de ligne,{nombreLigne}")
print(f"Colonne {nombre_colonne}")
print(f"Format dataset{format_dataset}")
print(f"Public {public}")

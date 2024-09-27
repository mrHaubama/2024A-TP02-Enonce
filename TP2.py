"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv

dictionnaire_bibli={}
with open("collection_bibliotheque.csv", newline='') as csvfile:
    biblio = csv.reader(csvfile, delimiter= ",") # cr/e une liste d/limit/ par , dans une ligne
    for row in biblio:
        key= (row[-1]) #ajoute dernier element de la ligne
        livre=(tuple(row[0:-1])) 
        dictionnaire_bibli.update({key:livre})
        
print( f' La collection de la bibliotheque contient ces livres: \n {dictionnaire_bibli}')       

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici

Ajout_dictionnaire_bibli={}
with open("nouvelle_collection.csv", newline='') as csvfile:
    ajout_biblio = csv.reader(csvfile, delimiter= ",") # cr/e une liste d/limit/ par , dans une ligne
    for ajout_row in ajout_biblio:
        ajout_key= (ajout_row[-1]) #ajoute dernier element de la ligne
        ajout_livre=(tuple(ajout_row[0:-1])) 
        Ajout_dictionnaire_bibli.update({ajout_key: ajout_livre})

 

for ajout_livre, ajout_key in Ajout_dictionnaire_bibli.items():
    if ajout_key not in dictionnaire_bibli:
        dictionnaire_bibli[ajout_key] = ajout_livre

        print (f'le livre {ajout_livre} --- {ajout_key[0]} par {ajout_key[1]} --- a ete ajoute avec succes')
    else:
        print (f'Le livre {ajout_livre} --- {ajout_key[0]} par {ajout_key[1]} --- est deja present dans la bibliotheque ')

print (f'Dictionnaire mise a jour\nNouvelle bibliotheque:\n{dictionnaire_bibli}\n')


########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici

for key, livre in list(dictionnaire_bibli.items()):  
    if len(livre) == 3: 
        titre, auteur, date = livre
        if auteur == "William Shakespeare" and key.startswith("S"):
            nouvelle_cote = "WS" + key[1:]  # Remplacer the "S" with "WS"
            dictionnaire_bibli[nouvelle_cote] = dictionnaire_bibli.pop(key)

print(f'\nBibliothèque avec modifications de cote : {dictionnaire_bibli}\n')


########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici







########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici







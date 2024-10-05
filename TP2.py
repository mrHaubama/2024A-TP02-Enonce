"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : L01
Numéro d'équipe : YY
Noms et matricules : Mikkelsen Bazelais(2372411), Nom2 (Matricule2)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
########################################################################################################## 

# TODO : Écrire votre code ici
import csv


ordre_rangement= [ "titre","auteur", "date_publication"]
bibliotheque ={}
with open("collection_bibliotheque.csv", newline='') as csvfile:
    biblio = csv.reader(csvfile, delimiter= ",") # crée une liste délimité par , dans une ligne
    for row in biblio:
        key= (row[-1]) #ajoute dernier élement de la ligne
        livre=(tuple(row[0:-1]))
        if  len(key) == 4:
            sous_dict= {}
            for i in range(len(ordre_rangement)):
                sous_dict.update({ordre_rangement[i]:livre[i]})
            
            bibliotheque.update({key:sous_dict})
     
    print( f' La collection de la bibliotheque contient ces livres: \n {bibliotheque}')     

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# TODO : Écrire votre code ici


with open("nouvelle_collection.csv", newline='') as csvfile:
    ajout_biblio = csv.reader(csvfile, delimiter= ",") # cr/e une liste d/limit/ par , dans une ligne
    for ajout_row in ajout_biblio:
        ajout_key= (ajout_row[-1]) #ajoute dernier element de la ligne
        ajout_livre=(tuple(ajout_row[0:-1]))
        if len(ajout_key) == 4: 
            if ajout_key not in bibliotheque:                
                sous_dict= {}
                for i in range(len(ordre_rangement)):
                    sous_dict.update({ordre_rangement[i]:ajout_livre[i]})
                    
                bibliotheque.update({ajout_key:sous_dict})
                print (f'le livre {ajout_key} --- {sous_dict.get("titre")} par {sous_dict.get("auteur")} --- a ete ajoute avec succes')
            else:
                print (f'Le livre {ajout_key} --- {ajout_livre[0]} par {ajout_livre[1]} --- est deja present dans la bibliotheque ')


print (f'Dictionnaire mise a jour\nNouvelle bibliotheque:\n{bibliotheque}\n')

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

# TODO : Écrire votre code ici



for key, livre in list(bibliotheque.items()): 
      
    if livre["auteur"] == "William Shakespeare" and key.startswith("S"):
        nouvelle_cote = "WS" + key[1:]  # Remplacer the "S" with "WS"
        bibliotheque[nouvelle_cote] = bibliotheque.pop(key)
        print(key ,bibliotheque[nouvelle_cote])
print(f'\nBibliothèque avec modifications de cote : {bibliotheque}\n')


########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

# TODO : Écrire votre code ici
dict_emprunt={}

with open("emprunts.csv", newline='') as csvfile:
    livre_emprunter = csv.reader(csvfile, delimiter= ",") # crée une liste délimité par , dans une ligne
    for row in livre_emprunter:
        key = row[0]
        date = row[-1]
        dict_emprunt.update ({key: row[-1]})

for k in bibliotheque:
    if k in dict_emprunt:
        temp= bibliotheque.get(k) 
        temp.update({"emprunt":"emprunté","date_emprunt":dict_emprunt.get(k)})
    if k not in dict_emprunt:
        temp= bibliotheque.get(k)
        temp.update({"emprunt":"disponible"})
    bibliotheque[k]= temp 
    
          



print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')







########################################################################################################## 
#PARTIE 5 : Livres en retard
########################################################################################################## 

# TODO : Écrire votre code ici

import datetime
        
livre_perdu= []
for k, donnee_livre in bibliotheque.items():
    if donnee_livre.get("emprunt") == "emprunté":
        date = donnee_livre["date_emprunt"].split("-")
        year, month, day = date
        date_emprunt = datetime.date(int(year), int(month), int(day))
        
        date_remise = date_emprunt + datetime.timedelta(days=30) 
        date_livre_perdu= date_emprunt + datetime.timedelta(days = 365)
        
        today= datetime.date.today()
        if today >= date_livre_perdu:
            
            donnee_livre.update({"livres_perdus":True})
            bibliotheque.update({k:donnee_livre})
            print(f"le livre {k} --- {donnee_livre["titre"]} par {donnee_livre["auteur"]} --- a été perdu")
        elif today > date_remise:
            retard = today- date_remise 
            frais_retard= retard.days *2 if 50 > retard.days  else 100 
            donnee_livre.update({"frais_retard":frais_retard})
            bibliotheque.update({k:donnee_livre})
            print(f"le livre {k} --- {donnee_livre["titre"]} par {donnee_livre["auteur"]} --- a {donnee_livre["frais_retard"]}$ de frais de retard")

print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')

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
    biblio = csv.reader(csvfile, delimiter= ",") # crée une liste délimité par , dans une ligne
    for row in biblio:
        key= (row[-1]) #ajoute dernier élement de la ligne
        livre=(tuple(row[0:-1]))
        if  len(key) == 4:
            print(key)
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
        if len(ajout_key) == 4: 
            if ajout_key not in dictionnaire_bibli:
            # Ajout_dictionnaire_bibli.update({ajout_key: ajout_livre})
                dictionnaire_bibli.update({ajout_key: ajout_livre})
                print (f'le livre {ajout_key} --- {ajout_livre[0]} par {ajout_livre[1]} --- a ete ajoute avec succes')
            else:
                print (f'Le livre {ajout_key} --- {ajout_livre[0]} par {ajout_livre[1]} --- est deja present dans la bibliotheque ')

# for ajout_livre, ajout_key in Ajout_dictionnaire_bibli.items():
#     if ajout_key not in dictionnaire_bibli:
#         dictionnaire_bibli[ajout_key] = ajout_livre

#         print (f'le livre {ajout_livre} --- {ajout_key[0]} par {ajout_key[1]} --- a ete ajoute avec succes')
#     else:
#         print (f'Le livre {ajout_livre} --- {ajout_key[0]} par {ajout_key[1]} --- est deja present dans la bibliotheque ')

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
dict_emprunt={}

with open("emprunts.csv", newline='') as csvfile:
    livre_emprunter = csv.reader(csvfile, delimiter= ",") # crée une liste délimité par , dans une ligne
    for row in livre_emprunter:
        key = row[0]
        date = row[-1]
        dict_emprunt.update ({key: row[-1]})
print(dict_emprunt)
for element in dictionnaire_bibli:
    print("ceci, est lelemet, ",element)
    if element in dict_emprunt:
        temp = dictionnaire_bibli.get(element)
        temp = temp + ("emprunté", dict_emprunt.get(element))
        dictionnaire_bibli.update({element:temp})
    if element not in dict_emprunt:
        temp = dictionnaire_bibli.get(element)
        temp = temp + ("disponible",)
        dictionnaire_bibli.update({element:temp})

 
    
          


print(f' \n Bibliotheque avec ajout des emprunts : {dictionnaire_bibli} \n')








########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

# TODO : Écrire votre code ici

import datetime

for element in dictionnaire_bibli:
    donnee_livre= dictionnaire_bibli.get(element)
    if donnee_livre[-2] == "emprunté":
        date = donnee_livre[-1].split("-")
        year, month, day = date
        date_emprunt = datetime.date(int(year), int(month), int(day))
        
        date_remise = date_emprunt + datetime.timedelta(days=30) 
        date_livre_perdu= date_emprunt + datetime.timedelta(days = 365)
        
        today= datetime.date.today()
        if today >= date_livre_perdu:
            print("ce livre a ete perdu", date_livre_perdu)
            temp = dictionnaire_bibli.get(element)
            temp = temp + ("livre est perdu",)
            dictionnaire_bibli.update({element:temp})
            print(temp)
        elif today > date_remise:
            retard = today- date_remise 
            frais_retard= retard.days *2 if 50 > retard.days  else 100 
            print(date_remise, retard.days, frais_retard,"$", today)
            temp = dictionnaire_bibli.get(element)
            temp = temp + (str(frais_retard)+"$",)
            dictionnaire_bibli.update({element:temp})
            print(f"le livre {element} --- {temp[0]} par {temp[1]} --- a {temp[-1]} de frais de retard")
        

#print(f' \n Bibliotheque avec ajout des retards et frais : {dictionnaire_bibli} \n')

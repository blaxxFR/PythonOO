# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 23:29:46 2022

@author: Nathan AMSELLEM & Valentin THEDON
Présentation de l'analyse de données en python
"""

from Utilisateur import Utilisateur
from Clients import Client
from Salaries import Salarie
from Types_Salaries import Comptable, Commercial
from Types_Salaries import *
from Entreprise import Entreprise

tabemp = []
tabcli = []


Client1 = Client("Martin","Bernard", 1, "martin.bernard1@gmail.com", "MB290867")
tabcli.append(Client1)

Salarie1 = Salarie("Dubois","Renaud", 1, "MB231289", 2000)
tabemp.append(Salarie1)

Salarie2 = Comptable("Dupont","Michel", 2, "HDO73JD", 3000)
tabemp.append(Salarie2)

Salarie3 = Commercial("Amsellem","Nathan", 3, "26DHKS78", 500, 50)
tabemp.append(Salarie3)

Salarie4 = Commercial("Thedon","Valentin", 4, "3JSPDJX3", 40000, 500)
tabemp.append(Salarie4)

#Affichage des statuts des personnes créées
for obj in tabcli:
    obj.toString()
for obj in tabemp:
    obj.toString()


#On créée l'entreprise qui recevra les Employés et les clients présents dans les 2 listes précédemment affichées
ETUENTREPRISE = Entreprise()

for i in tabemp:
    ETUENTREPRISE.Employes.push(i)
for j in tabcli:
    ETUENTREPRISE.Clients.push(j)

#On affiche la rémuneration totale de l'entreprise vers ses salariés
print("L'entreprise rémunère au total", ETUENTREPRISE.totalRemuneration()  ,"$ par mois")
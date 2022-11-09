# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 23:29:46 2022

@author: Nathan AMSELLEM & Valentin THEDON
Présentation de l'analyse de données en python
"""

########################################################################################################
####################################### OUTILS : PANDAS & SEABORN ######################################
########################################################################################################

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Création de la classe Poutre encastrée libre en traitant des dataframes DF
class DF_Cantilever_beams :
    #Initialise les entrées (modélisation physique) du problèmes ainsi que les sorties (fréquences en Hz)
    #à partir des deux csv
    #Utilisation de la bibliothèque Pandas pour manier les dataframes ainsi générés
    def __init__(self, path_freq, path_inputs) :

        self.freq = pd.read_csv(open(path_freq, "r"),
                            delimiter=",")
        self.inputs = pd.read_csv(open(path_inputs, "r"),
                            delimiter=",")

    #renvoie un dataframe isolant les entrées du matériau souhaité qui est passé en paramètre de la fonction
    def isolate_material_inputs(self, mat):
        Material = self.inputs.loc[self.inputs.loc[:, 'Mat'] == mat]
        return Material
    #renvoie un dataframe isolant les sorties du matériau souhaité qui est passé en paramètre de la fonction
    def isolate_material_frequencies (self, mat):
        indexs = self.isolate_material_inputs(mat).index
        freq_alu = self.freq.iloc[indexs]
        return freq_alu
    #Utilisation de la bibliothèque Seaborn afin d'afficher une matrice de correlation
    #La matrice de correlation nous permet de voir quelles données sont correllées entre elles
    #C'est a dire de voir quelles variables sont dépendantes d'autres :
    #           on peut s'en servir pour limiter la duplication des données
    def plot_correlation_matrix(self):
        corr = self.inputs.corr()
        sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns)
        plt.show()
        print(corr)
    #A partir de l'interprétation que l'on aura eu de la matrice de corrélation on envoie un certain tableau de labels
    #Ces labels permettent de supprimer des colonnes qui dupliquent l'information a interpréter
    def reduce_inputs(self, labels_to_drop):
        self.inputs = self.inputs.drop(columns=labels_to_drop)

#Chargement des chemins vers les sorties/entrées du problème
path_freq = "test.csv"
path_inputs = "dict.csv"

#Initialisation de Beams qui prendra comme attribut 2 dataframes freq et inputs provenant
#des tableaux respectivements passés en paramètres
Beams = DF_Cantilever_beams(path_freq, path_inputs)
print(Beams.freq.head())

#On crée 2 nouveaux dataframes qui représentent les sorties et entrées d'un matériau en alu
Alu_Beams = Beams.isolate_material_inputs('Aluminium')
Alu_Freq = Beams.isolate_material_frequencies('Aluminium')
print(Alu_Beams)
print(Alu_Freq)

#On affiche la matrice de correlation
Beams.plot_correlation_matrix()

# d'apres la matrice de correlation, certaines entrées sont étroitement liées
# on va donc supprimer certaines de ces valeurs pour conserver :
# surface S la masse volumique rho, la longueur de la poutre L_tot
corr = ['NbElts', 'rho', 'h', 'b', 'I', 'L']

#On supprime les labels contenus dans corr
Beams.reduce_inputs(corr)
print('entrées réduites =', Beams.inputs)


########################################################################################################
######################################### OUTILS : NUMPY / LISTES ######################################
########################################################################################################


#Utilisation de la bibliothèque csv permettant de charger les 2 fichiers csv
import csv
#Utilisation de la bibliothèque numpy pour montrer la puissance du slicing sur des types array en python
import numpy as np


#Création de la classe Poutre encastrée libre en traitant des listes : types natifs à python afin de voir
#les possibilités qui sont offertes par de tels types
class list_Cantilever_beams :
    def __init__(self, path_freq, path_inputs) :
        # Initialise les entrées (modélisation physique) du problèmes ainsi que les sorties (fréquences en Hz)
        # à partir des deux csv
        # Utilisation de la bibliothèque csv afin de les convertir en liste
        self.list_freq = list(csv.reader(open(path_freq, "r"),
                                    delimiter=","))
        self.list_inputs = list(csv.reader(open(path_inputs, "r"),
                                      delimiter=","))

        # On isole les labels de données d'entrées et de sorties (freq)
        # Slicing horizontal pour des listes 2d : natif à python
        # "...[0]..." : selectionner la premiere ligne
        # "...[:]" : selectionner toutes les colonnes
        self.labels_inputs = self.list_inputs[0][:]
        self.labels_freq = self.list_freq[0][:]

        #On isole les données numériques qui seront traitées par la suite à partir du slicing des lables effectuté
        self.list_freq.remove(self.labels_freq)
        self.list_inputs.remove(self.labels_inputs)

    #Retourne l'attibut list_freq en array de la bibliothèque numpy
    def freq_to_array(self):
        arr_freq = np.array(self.list_freq)
        return arr_freq

    #Retourne l'attibut list_inputs en array de la bibliothèque numpy
    def inputs_to_array(self):
        arr_inputs = np.array(self.list_inputs)
        return arr_inputs

#Initialisation de Beams qui prendra comme attribut 2 listes : list_freq et list_inputs provenant
#des csv respectivements passés en paramètres
list_Beams = list_Cantilever_beams(path_freq, path_inputs)


#Conversion des listes de fréquences vers des numpy array
arr_freq = list_Beams.freq_to_array()


#slicing offert par la librairie numpy :
#   "...[: ..." : sélectionne toutes les lignes...
#   "... 0]..." : ... de la premiere colonne
arr_freq1 = arr_freq[:, 0]
print(arr_freq1)
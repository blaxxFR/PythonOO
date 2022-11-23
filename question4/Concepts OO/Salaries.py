from Utilisateur import Utilisateur

class Salarie (Utilisateur):
    def __init__(self, nom, prenom, id, mdp, salaire):
        mail = nom + prenom + "@locahub.com" # On créée le mail de l'employé de l'entreprise avec l'adresse de l'entreprise
        super().__init__(nom, prenom, mail, mdp) # Classe Salarié : possède les attributs de la classe utilisateur
                                                 # dont elle dérive
        self.id_Salarie = id # Possède en plus : un attribut id_Salarie
        self.salaire = salaire #Possède en plus : un attributs salaire

    #De la même manière, toString (méthode abstraite dans Utilisaeur) doit obligatoirement être redéfnie pour un Salarié
    def toString(self):
        print("Bonjour " + self.prenom +" "+ self.nom +" ! Vous êtes un Salarié")
    # Le salarié possèdera une méthode rémunération qui renverra la rémunération mensuelle d'un salarié
    # Elle fera office de simple getter pour le salarié (pour l'instant) dans la mesure ou l'on retourne seulement
    # l'attribut salaire
    def remuneration (self) :
        return self.salaire


#Avec cet import on va pouvoir créer une classe qui derive de ABC
from abc import ABC, abstractmethod

class Utilisateur(ABC): # Hérite de ABC(Abstract Base Class)
    def __init__(self, nom,prenom,mail,mdp):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.password = mdp

    @abstractmethod  # Decorateur pour definir une méthode abstraite
    def toString(self):
        pass    # Rien ne se passe à l'interieur de cette methode

    # L'implémentation d'un overloading à la manière d'un code JAVA/C++ ne sera pas possible en python
    # Nous devrons donc passer les arguments en None
    # En faisant cela nous avons l'option d'appeler la fonction avec ou sans le paramètre spécifié
    def Login(self, mail = None, mdp = None):
        if(mail == None or mdp == None): # Si rien n'est envoyé au niveau du mail ou du mot de passe
            print("Veuillez entrer vos identifiants") # Alors nous demanderons à l'utilisateur de spécifier ces arguments
        elif (mail == self.mail and mdp == self.password):
            print("Vous êtes connecté")
        elif (mail != self.mail or mdp != self.password):
            print("les identifiants sont incorrects")



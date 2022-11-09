from Utilisateur import Utilisateur

class Client(Utilisateur):
    def __init__(self, nom, prenom, id, mail, mdp):
        super().__init__(nom, prenom, mail, mdp)    # Classe client : possède les attributs de la classe utilisateur
                                                    # dont elle dérive
        self.id_Client = id # Possède en plus : un attribut id_Client

    # Si une classe hérite d'une classe ABC, on doit implémenter les méthodes abstraites, autrement, on aura une erreur
    def toString(self): #évidemment la fonction se doit d'avoir la même définition (nom, arguments) que celle dont elle dérive
        print("Bonjour " + self.prenom + " " + self.nom +" ! Vous êtes un Client")

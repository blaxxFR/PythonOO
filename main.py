from abc import ABC, abstractmethod

class Utilisateur(ABC):
    def __init__(self, nom,prenom,mail,mdp):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.password = mdp

    def affiche(self):
        pass


class Client(Utilisateur):
    def __init__(self, nom, prenom, id, mail, mdp):
        super().__init__(nom, prenom, mail, mdp)
        self.id_Client = id

    def affiche(self):
        print("Bonjour " + self.prenom + " " + self.nom +" ! Vous êtes un Client")


class Salarie (Utilisateur):
    def __init__(self, nom, prenom, id, mdp, salaire):
        mail = nom + prenom + "@locahub.com"
        super().__init__(nom, prenom, mail, mdp)
        self.id_Salarie = id
        self.salaire = salaire

    def affiche(self):
        print("Bonjour " + self.prenom +" "+ self.nom +" ! Vous êtes un Salarié")
    def remuneration (self) :
        return self.salaire


class Comptable(Salarie):
    def __init__(self, nom, prenom, id, mdp, salaireFixe):
        super().__init__(nom, prenom, id, mdp, salaireFixe)


class Commercial(Salarie):
    def __init__(self, nom, prenom, id, mdp, salaireFixe, prime):
        super().__init__(nom, prenom, id, mdp, salaireFixe)
        self.prime = prime

    def remuneration(self):
        remuneration = self.salaire + self.prime
        return remuneration




tab = []
Client1 = Client("Martin","Bernard", 1, "martin.bernard1@gmail.com", "MB290867")
tab.append(Client1)

Salarie1 = Salarie("Dubois","Renaud", 1, "MB231289")
tab.append(Salarie1)

for obj in tab:
    obj.affiche()





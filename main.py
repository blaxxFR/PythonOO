from abc import ABC, abstractmethod

class Utilisateur(ABC):
    def __init__(self, nom,prenom,mail,mdp):
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.password = mdp

    def toString(self):
        pass


class Client(Utilisateur):
    def __init__(self, nom, prenom, id, mail, mdp):
        super().__init__(nom, prenom, mail, mdp)
        self.id_Client = id

    def toString(self):
        print("Bonjour " + self.prenom + " " + self.nom +" ! Vous êtes un Client")


class Salarie (Utilisateur):
    def __init__(self, nom, prenom, id, mdp, salaire):
        mail = nom + prenom + "@locahub.com"
        super().__init__(nom, prenom, mail, mdp)
        self.id_Salarie = id
        self.salaire = salaire

    def toString(self):
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


from typing import TypeVar, Generic

T = TypeVar('T')

class Liste_Gestion(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items

    def length(self) -> int :
        return len(self.items)
class Entreprise():
    def __init__(self):
        # Create an empty list with items of type T
        self.Clients = Liste_Gestion()
        self.Employes = Liste_Gestion()
    def totalRemuneration(self):
        total = 0.0;
        x = range(0, self.Employes.length())
        for i in x:
            total += self.Employes.items[i].remuneration()
        return total


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

for obj in tabemp:
    obj.toString()

ETUENTREPRISE = Entreprise()

for i in tabemp:
    ETUENTREPRISE.Employes.push(i)
for j in tabcli:
    ETUENTREPRISE.Clients.push(j)

print("L'entreprise rémunère au total", ETUENTREPRISE.totalRemuneration()  ,"$ par mois")

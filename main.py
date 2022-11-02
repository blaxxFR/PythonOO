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


class Client(Utilisateur):
    def __init__(self, nom, prenom, id, mail, mdp):
        super().__init__(nom, prenom, mail, mdp)    # Classe client : possède les attributs de la classe utilisateur
                                                    # dont elle dérive
        self.id_Client = id # Possède en plus : un attribut id_Client

    # Si une classe hérite d'une classe ABC, on doit implémenter les méthodes abstraites, autrement, on aura une erreur
    def toString(self): #évidemment la fonction se doit d'avoir la même définition (nom, arguments) que celle dont elle dérive
        print("Bonjour " + self.prenom + " " + self.nom +" ! Vous êtes un Client")


class Salarie (Utilisateur):
    def __init__(self, nom, prenom, id, mdp, salaire):
        mail = nom + prenom + "@locahub.com" # On créée le mail de l'employé de l'entreprise avec l'adresse de l'entreprise
        super().__init__(nom, prenom, mail, mdp) # Classe Salarié : possède les attributs de la classe utilisateur
                                                 # dont elle dérive
        self.id_Salarie = id # Possède en plus : un attribut id_Salarie
        self.salaire = salaire #Possède en plus : un attributs salaire

    #De la même manière, toString (méthode abstraite) doit être redéfni pour un Salarié
    def toString(self):
        print("Bonjour " + self.prenom +" "+ self.nom +" ! Vous êtes un Salarié")
    # Le salarié possèdera une méthode rémunération qui renverra la rémunération mensuelle d'un salarié
    # Elle fera office de simple getter pour le salarié (pour l'instant) dans la mesure ou l'on retourne seulement
    # l'attribut salaire
    def remuneration (self) :
        return self.salaire


class Comptable(Salarie):
    def __init__(self, nom, prenom, id, mdp, salaireFixe):
        super().__init__(nom, prenom, id, mdp, salaireFixe)
    # la manière dont est définie la méthode rémunération dans le salarié convient pour le comptable,
    # on ne redéfinira donc pas cette fonction
class Commercial(Salarie):
    def __init__(self, nom, prenom, id, mdp, salaireFixe, prime):
        super().__init__(nom, prenom, id, mdp, salaireFixe) # Classe Commercial : possède les attributs de la
                                                            # classe Salarié
        self.prime = prime #Ainsi qu'une prime qui lui sera propre

    # En revanche, un commercial aura des primes qui rentreront en compte dans la rémunération de ce type de poste
    # Il s'agira donc de redéfinir la fonction rémunération
    def remuneration(self):
        remuneration = self.salaire + self.prime
        return remuneration


# Dans cette partie on va se servir du typing afin de montrer le principe de généricité
from typing import TypeVar, Generic
#T sera le type de variable d'entrées
T = TypeVar('T')
#Une classe liste_gestion est définie : elle sera instancié dans la gestion de l'entreprise qui suivra
class Liste_Gestion(Generic[T]): #On défini Liste_Gestion qui fera dériver des types génériques T
    # A travers cette classe on pourra donc gérer des listes d'un Type T unique à instancier
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
        # Grace a la classe Liste Gestion on va pouvoir gérer de la manière dont on le souhaite à la fois des clients et
        # et des employés a l'intereur d'une même classe Liste_Gestion
        self.Clients = Liste_Gestion()
        self.Employes = Liste_Gestion()
    # la fonction total_Remuneration renverra la rémunération totale émise par l'entreprise à ses salariés
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
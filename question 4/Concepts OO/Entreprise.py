from Liste import Liste_Gestion

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

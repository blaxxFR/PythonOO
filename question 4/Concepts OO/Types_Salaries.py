from Salaries import Salarie

class Comptable(Salarie):
    def __init__(self, nom, prenom, id, mdp, salaireFixe):
        super().__init__(nom, prenom, id, mdp, salaireFixe)
    # la manière dont est définie la méthode rémunération dans le salarié convient pour le comptable,
    # on ne redéfinira donc pas cette fonction
class Commercial(Salarie):
    def __init__(self, nom, prenom, id, mdp, salaireFixe, primeMensuelle):
        super().__init__(nom, prenom, id, mdp, salaireFixe) # Classe Commercial : possède les attributs de la
                                                            # classe Salarié
        self.primeMensuelle = primeMensuelle #Ainsi qu'une prime qui lui sera propre

    # En revanche, un commercial aura des primes qui rentreront en compte dans la rémunération de ce type de poste
    # Il s'agira donc de redéfinir la fonction rémunération
    def remuneration(self):
        remuneration = self.salaire + self.primeMensuelle
        return remuneration


# Dans ce module on va se servir du typing afin de montrer le principe de généricité
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

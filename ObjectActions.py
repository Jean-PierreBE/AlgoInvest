class ObjetAction:
    def __init__(self, name, poids, profit, indice):
        self.name = name
        self.indice = indice
        self.poids = poids
        self.profit = profit
  #Fonction pour la comparaison entre deux ObjetSac
  #On compare le rapport calculé pour les trier
    def __lt__(self, other):
        return self.profit < other.profit
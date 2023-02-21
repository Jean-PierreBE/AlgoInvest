class Actions:
    def __init__(self, name, price, profit, gain, indice):
        self.name = name
        self.price = price
        self.profit = profit
        self.gain = gain
        self.indice = indice
    '''tri suivant la colonne profit'''
    def __lt__(self, other):
        return self.profit < other.profit

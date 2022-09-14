import random

class Dado:
    #Metodo constructor de la clase
    def __init__(self):
        self.valor

    def girar(self):
        self.valor=random.randint(1,6)

    def getValor(self):
        return self.valor

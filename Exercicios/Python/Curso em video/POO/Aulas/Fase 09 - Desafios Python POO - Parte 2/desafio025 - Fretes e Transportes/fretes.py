'''
--------Superclasse--------
Transporte {abstract}
---------------------------
+ distancia
+ frete
---------------------------
+ calc_frete() {abstract}
---------------------------

---------Subclasses--------
Moto - fator = 0.5     | Distância - livre
Caminhão - fator = 1.2 | Distância - 50Km mínimo
Drone - fator = 9.5    | Distância - 10Km máximo
---------------------------
'''
from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass
    
class Moto(Transporte):
    
    fator = 0.5
    
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"
    
class Caminhao(Transporte):

    fator = 1.2

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 50:
            return "Distância mínima de 50Km para caminhão"
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"
    
class Drone(Transporte):

    fator = 9.5

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            return "Distância máxima de 10Km para drone"
        self.frete = self.distancia * self.fator
        return f"R${self.frete:.2f}"

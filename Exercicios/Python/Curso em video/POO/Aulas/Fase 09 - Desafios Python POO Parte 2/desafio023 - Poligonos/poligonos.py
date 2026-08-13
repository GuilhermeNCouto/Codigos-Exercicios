'''
                            +----------------------------+
                            |    Poligono {abstrato}     |
                            +----------------------------+
                            | + qtd_lados: int           |
                            +----------------------------+
                            | + area()   {abstrato}      |
                            | + perimetro()   {abstrato} |
                            +----------------------------+
                                            ^
                                            |
                                            |
                  --------------------------------------------------
                  |                                                |
    +-----------------------------+                  +-----------------------------+
    |         Quadrado            |                  |          Circulo            |
    +-----------------------------+                  +-----------------------------+
    | + lado                      |                  | + raio                      |
    +-----------------------------+                  +-----------------------------+
    | + area()                    |                  | + area()                    |
    | + perimetro()               |                  | + perimetro()               |
    +-----------------------------+                  +-----------------------------+
    
'''

from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
    
class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4
    

class Triangulo(Poligono):
    def __init__(self, base, altura):
        super().__init__(3)
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base * 3 #Assumindo que é um triângulo equilátero para simplificação

    
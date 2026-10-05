from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        pass


class Gato(Animal): 
    def emitir_som(self):
        print(f"{self.nome} -> MIAU! MIAU!")


class Cachorro(Animal):  
    def emitir_som(self):
        print(f"{self.nome} -> AU! AU! AU!")

class Spitz(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} -> au!au!au!au!au!au!")

class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} -> WOOOFF WOOFFF!")

class Pato(Animal):
    def emitir_som(self):
        print(f"{self.nome} -> QUACK! QUACK!")


class Galinha(Animal):
    def emitir_som(self):
        print(f"{self.nome} -> CÓ! CÓ! CÓ!")

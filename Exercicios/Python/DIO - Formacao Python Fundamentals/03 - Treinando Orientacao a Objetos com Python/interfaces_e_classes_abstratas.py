# Interfaces definem o que uma classe deve fazer, mas não como ela deve fazer.
# O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito),
# e suas respectivas assinaturas. Em Python utilizamos classes abstratas para criar contratos.
# Classes abstratas não podem ser instanciadas diretamente, servindo apenas como base para outras classes.


from abc import ABC, abstractmethod

class ControleRemoto(ABC): # Classe abstrata
    @abstractmethod
    def ligar(self): # Método abstrato
        pass

    @abstractmethod
    def desligar(self): # Método abstrato
        pass

    def trocar_pilha(self): # Método concreto da classe abstrata
        print("Pilhas trocadas")

    @property
    @abstractmethod
    def marca(self): # Outro método concreto da classe abstrata
        pass

class ControleTV(ControleRemoto): # Classe concreta que implementa a interface
    def ligar(self): # Método concreto do filho
        print("TV ligada")

    def desligar(self): # Método concreto do filho 
        print("TV desligada")
    
    @property
    def marca(self): # Implementação do método abstrato
        return "Samsung"


class ControleArCondicionado(ControleRemoto): # Outra classe concreta que implementa a interface
    def ligar(self): # Método concreto do filho
        print("Ar condicionado ligado")

    def desligar(self): # Método concreto do filho
        print("Ar condicionado desligado")

    @property
    def marca(self): # Implementação do método abstrato
        return "LG"


controle = ControleTV()
print(f"Marca do controle: {controle.marca}")
controle.ligar()
controle.desligar()
controle.trocar_pilha()

controle_ar = ControleArCondicionado()
print(f"Marca do controle: {controle_ar.marca}")
controle_ar.ligar()
controle_ar.desligar()
controle_ar.trocar_pilha()


'''
Objeto na Memória (Instância de ControleTV)
+------------------------------------------+
| Atributos: nome, marca                   |
| ---------------------------------------- |
| Métodos que ele pode usar:               |
| [Filho] ligar()                          |
| [Pai]   trocar_pilha()  <-- via herança  |
| [Pai]   marca()         <-- via super()  |
+------------------------------------------+

'''
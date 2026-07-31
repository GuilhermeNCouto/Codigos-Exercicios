'''
Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
Crie também um método que permita ao funcionário se apresentar.
'''

from rich import print

class Funcionario:
    
    #atributos de classe
    empresa = 'Guigas.bet'
    

    def __init__(self, nome, setor, cargo, empresa='Guigas.bet'):
        #atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá, meu nome é [blue]{self.nome}[/], trabalho no setor de {self.setor} e atuo como {self.cargo} na {self.__class__.empresa}."


func1 = Funcionario("João", "Vendas", "Atendente")
print(func1.apresentacao())

Funcionario.empresa = 'Church'

func2 = Funcionario("Maria", "RH", "Recrutadora")
print(func2.apresentacao())

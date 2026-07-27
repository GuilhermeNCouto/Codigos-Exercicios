'''
Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo.
Crie também um método que permita ao funcionário se apresentar.
'''
from rich import print

class Funcionario:

    def __init__(self, nome, setor, cargo, empresa='Guigas.bet'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        self.empresa = empresa

    def apresentacao(self):
        print(f":handshake: Olá, meu nome é [blue]{self.nome}[/], trabalho no setor de {self.setor} e atuo como {self.cargo} na {self.empresa}.")


func1 = Funcionario("João", "Vendas", "Atendente")
func1.apresentacao()
func2 = Funcionario("Maria", "RH", "Recrutadora")
func2.apresentacao()

'''
Diagrama:

Diario
----------------
- __segredos[]
- __senha
----------------
+ escrever(msg)
+ ler(senha)
'''
from rich import print

class Diario():
    
    def __init__(self, senha = "mudar"):
        self.__segredos = []
        self.__senha = senha
        
    @property
    def senha(self):
        raise PermissionError("Ninguém pode ver a senha.")
    
    @senha.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha
        
    def escrever(self, msg):
        self.__segredos.append(msg)
        
    def ler(self, senha=None):
        if self.__senha == senha:
            print("[green]Diário LIBERADO![/]")
            for msg in self.__segredos:
                print(f" - {msg}")
        else:
            raise PermissionError("Senha inválida.")
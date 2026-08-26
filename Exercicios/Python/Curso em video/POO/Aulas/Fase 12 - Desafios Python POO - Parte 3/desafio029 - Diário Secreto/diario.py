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
        # Inicializa o atributo privado como None para o setter saber que é a criação inicial
        self.__senha = None
        self.senha = senha.strip()
        
    @property
    def senha(self):
        raise PermissionError("Ninguém pode ver a senha.")
    
    @senha.setter
    def senha(self, nova_senha):
        nova_senha_limpa = str(nova_senha).strip()

        # 1. Se for a primeira definição (durante o __init__), define direto
        if self.__senha is None:
            self.__senha = nova_senha_limpa
            return

        # 2. Se já existe uma senha, exige a anterior para autorizar a troca
        senha_atual = input("Digite a senha anterior para autorizar a alteração: ").strip()

        if senha_atual != self.__senha:
            raise PermissionError("Senha anterior incorreta. Acesso negado.")

        self.__senha = nova_senha_limpa
        print("[green]✅ Senha do diário alterada com sucesso![/]")
        
    def escrever(self, msg):
        if not isinstance(msg, str) or not msg.strip():
            raise ValueError("O segredo não pode ser vazio.")
        
        self.__segredos.append(msg.strip())
        
        
    def ler(self, senha=None):
        if self.__senha == senha:
            print("[green]Diário LIBERADO![/]")
            for msg in self.__segredos:
                print(f" - {msg}")
        else:
            raise PermissionError("Senha inválida. Você não pode ler o diário.")
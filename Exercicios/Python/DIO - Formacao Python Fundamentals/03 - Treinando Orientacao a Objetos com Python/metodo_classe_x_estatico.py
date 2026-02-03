class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2026 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

class Estudante(Pessoa):
    # Imagine que Estudante tem algo a mais, como a escola
    escola = "DIO"

#p = Pessoa("Guilherme", 24) # Exemplo de uso do construtor
#print(p.nome, p.idade) # Saída: Guilherme 24

p2 = Pessoa.criar_apartir_data_nascimento(2002, 10, 11, "Guilherme") # Exemplo de uso do método de classe
print(p2.nome, p2.idade) # Saída: Guilherme 24


# Chamando o método que você criou, mas através da classe FILHA
aluno = Estudante.criar_apartir_data_nascimento(2005, 5, 20, "Thiago")

print(type(aluno)) # Saída: <class '__main__.Estudante'>
print(aluno.escola, aluno.nome, aluno.idade) # Saída: DIO Thiago 21

# Exemplo de uso do método estático
print(Pessoa.e_maior_idade(18)) # Saída: True
print(Pessoa.e_maior_idade(16)) # Saída: False
print(Estudante.e_maior_idade(20)) # Saída: True
print(Estudante.e_maior_idade(15)) # Saída: False
print(aluno.e_maior_idade(25)) # Saída: True
print(p2.e_maior_idade(15)) # Saída: False
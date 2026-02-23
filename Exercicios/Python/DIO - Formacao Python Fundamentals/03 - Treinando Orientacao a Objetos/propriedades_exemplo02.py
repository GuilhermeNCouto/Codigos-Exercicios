class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    
    @property
    def idade(self):
        return 2026 - self._ano_nascimento
    
    

# --- Testando a classe Pessoa ---

pessoa = Pessoa("Guilherme", 2002)
print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade} anos") # Saída: Nome: Guilherme Idade: 24 anos: Guilherme Idade (método): 24 anos
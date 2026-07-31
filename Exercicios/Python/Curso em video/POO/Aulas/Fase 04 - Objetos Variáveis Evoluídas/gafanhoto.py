# Declaração de classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.

    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome = "Desconhecido", idade = 0): # Método construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade

    def __str__(self): # Dunder - Método especial
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."

    # Métodos de instância
    def aniversario(self): # Método comum
        self.idade += 1

    def __getstate__(self): # Dunder - Método especial
        return f"Estado: nome = {self.nome}, idade = {self.idade}"
    
# Declaração de objetos
g1 = Gafanhoto("Guilherme", 23)
print(g1) # Chama o método __str__() implicitamente

# g2 = Gafanhoto("Letícia", 24)
# g2.aniversario()
# print(g2) # Chama o método __str__() implicitamente

g3 = Gafanhoto()

#print(g1) # Chama o método __str__() implicitamente
print(g1.__dict__)  # É um atributo - Mostra os atributos do objeto g1
print(g1.__getstate__())  # É um método - Mostra o estado do objeto g1
print(g1.__class__)  # É um atributo - Mostra a classe do objeto g1

'''
Neste desafio, temos a classe Pessoa com seus atributos que armazenam o nome e a idade de uma pessoa.
Implemente um método para retornar uma representação formatada dos dados da pessoa,crie uma instância
da pessoa e, por fim, chame o método para retornar as informações formatadas e imprimir o resultado.
O objetivo é utilizarmos formas para criar e manipular objetos com POO, usando atributos e métodos
para encapsular dados e comportamentos.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/classes.html

https://docs.python.org/pt-br/3/library/stdtypes.html#methods

Entrada
- Nome da pessoa (string)
- Idade da pessoa (inteiro)

Saída
Uma string formatada com o nome e a idade da pessoa, no seguinte formato: Nome: {nome}, Idade: {idade}
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

#TODO: Crie um método para retornar as informações formatas com Nome e Idade:    
    def apresentar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

# Entrada do usuário
nome = input()
idade = int(input())

# TODO: Crie uma instância da pessoa:
p = Pessoa(nome, idade)

#TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
p.apresentar()

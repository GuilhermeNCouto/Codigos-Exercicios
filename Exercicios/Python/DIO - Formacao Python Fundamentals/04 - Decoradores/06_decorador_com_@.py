'''
Decoradores em Python são uma forma de modificar o comportamento de uma função sem alterar seu código.
'''

def meu_decorador(funcao): # Decorador simples
    
    def envelope(): # Função interna que envolve a função original
        print("Faz algo antes da execução da função.")
        funcao()# Chama a função original
        print("Faz algo depois da execução da função.")
    
    return envelope # Retorna a função interna

@meu_decorador # Usando o decorador com a sintaxe @
def ola_mundo():
    print("Olá, mundo!")


ola_mundo()  # Chama a função decorada
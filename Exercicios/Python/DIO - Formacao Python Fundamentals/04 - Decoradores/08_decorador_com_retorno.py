'''
O decorador pode decidir se retorna o valor da função decorada ou não. Para que o valor seja retornado,
a função envelope deve retornar o valor da função decorada.
'''

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes da execução da função.")
        resultado = funcao(*args, **kwargs) # Chama a função original e armazena o resultado
        print("Faz algo depois da execução da função.")
        return resultado # Retorna o valor da função decorada
    
    return envelope # Retorna a função interna

@meu_decorador # Usando o decorador com a sintaxe @
def ola(nome):
    print(f"Olá, {nome}!")
    return nome.upper()  # Retorna o nome em maiúsculas


ola1 = ola("Alice")  # Chama a função decorada
print(ola1)         # Imprime o valor retornado pela função decorada
ola2 = ola("Bob")    # Chama a função decorada novamente
print(ola2)         # Imprime o valor retornado pela função decorada

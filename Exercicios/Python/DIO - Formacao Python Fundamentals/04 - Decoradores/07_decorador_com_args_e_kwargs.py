'''
Podemos usar *args e **kwargs na função interna, com isso ela aceitará um número arbitrário de argumentos
posicionais e de palavras-chave.
'''

'''
Decoradores em Python são uma forma de modificar o comportamento de uma função sem alterar seu código.
'''

def meu_decorador(funcao): # Decorador simples
    
    def envelope(*args, **kwargs): # Função interna que envolve a função original
        print("Faz algo antes da execução da função.")
        funcao(*args, **kwargs)# Chama a função original
        print("Faz algo depois da execução da função.")
    
    return envelope # Retorna a função interna

@meu_decorador # Usando o decorador com a sintaxe @
def ola(nome):
    print(f"Olá, {nome}!")


ola("Alice")  # Chama a função decorada
ola("Bob")    # Chama a função decorada novamente
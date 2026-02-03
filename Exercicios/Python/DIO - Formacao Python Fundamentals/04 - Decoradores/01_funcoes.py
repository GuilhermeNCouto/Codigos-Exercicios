'''
Funções em Python são objetos de primeira classe. Isso significa que as funções podem ser passadas
e usadas como argumentos.
'''

def dizer_oi(nome):
    return f'Oi {nome}!'

def incentivar_aprender(nome):
    return f'Vamos aprender Python, {nome}!'

def mensagem_personalizada(funcao, nome):
    return funcao(nome)


print(mensagem_personalizada(dizer_oi, 'Maria'))
print(mensagem_personalizada(incentivar_aprender, 'João'))

'''
Python também permite que você use funções internas como retorno de outras funções.
'''

def calcular(operacao):
    # Funções internas compactas (possuem acesso ao escopo do pai)
    def soma(a, b): return a + b
    def sub(a, b):  return a - b
    def mult(a, b): return a * b
    def div(a, b):  return a / b if b != 0 else "Erro: Divisão por zero!"

    # O dicionário agora funciona apenas como um "mapa" para retornar as funções internas
    ops = {
        '+': soma, 
        '-': sub, 
        '*': mult, 
        '/': div
    }

    # Função interna para o caso de erro
    def erro_operacao(*args): 
        return f"Operação '{operacao}' inválida!"

    ops = {'+': soma, '-': sub, '*': mult, '/': div}

    match operacao:
        case '+' | '-' | '*' | '/':
            return ops[operacao]
        case _:
            return erro_operacao
    


resultado = calcular('+')(5, 3)
print(resultado)  # Saída: 8

resultado = calcular('-')
print(resultado(5, 3))  # Saída: 2

print(calcular('*')(5, 3))  # Saída: 15

resultado = calcular('/')(6, 3)
print(resultado)  # Saída: 2.0

resultado = calcular('/')(5, 0)
print(resultado)  # Saída: Erro: Divisão por zero!

resultado = calcular('%')(5, 3)
print(resultado)  # Saída: Operação 'modulo' inválida!

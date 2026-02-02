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
        'soma': soma, 
        'subtracao': sub, 
        'multiplicacao': mult, 
        'divisao': div
    }

    return ops.get(operacao, lambda *_: f"Operação '{operacao}' não encontrada")
    
resultado = calcular('soma')(5, 3)
print(resultado)  # Saída: 8
resultado = calcular('subtracao')(5, 3)
print(resultado)  # Saída: 2
resultado = calcular('multiplicacao')(5, 3)
print(resultado)  # Saída: 15
resultado = calcular('divisao')(6, 3)
print(resultado)  # Saída: 2.0
resultado = calcular('divisao')(5, 0)
print(resultado)  # Saída: Erro: Divisão por zero!
resultado = calcular('modulo')(5, 3)
print(resultado)  # Saída: Operação 'modulo' inválida!
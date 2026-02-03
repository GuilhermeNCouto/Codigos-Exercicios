'''
O desafio consiste em implementar uma classe Calculadora que utilize os princípios da Programação
Orientada a Objetos (POO). A classe deve conter um método para realizar a operação de soma entre
dois números inteiros, encapsulando assim a lógica matemática da adição.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/classes.html

Entrada
A entrada será composta por dois números inteiros fornecidos pelo usuário.

Saída
A saída esperada é o resultado da soma dos dois números inteiros fornecidos como entrada.
'''

# TODO: Crie uma classe e método para realizar a soma:
class Calculadora:
    def soma(self, num1, num2):
        return num1 + num2

num1 = int(input())
num2 = int(input())

# Criando uma instância da calculadora
calc = Calculadora()

resultado = calc.soma(num1, num2)
print(resultado)
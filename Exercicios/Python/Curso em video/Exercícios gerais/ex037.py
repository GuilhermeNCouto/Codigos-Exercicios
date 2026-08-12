numero = int(input('Digite um número: '))
conversao = int(input('''\nBase de conversão
[1] - Binário
[2] - Octal
[3] - Hexadecimal
Escolha: '''))

while conversao not in (1, 2, 3):
    conversao = int(input('inválido! Digite novamente: '))

if conversao == 1:
    print(f'{numero} em binário é {bin(numero)[2:]}')
elif conversao == 2:
    print(f'{numero} em octal é {oct(numero)[2:]}')
else:
    print(f'{numero} em hexadecimal é {hex(numero)[2:]}')

from random import randint
from time import sleep
print('VAMOS JOGAR JOKENPÔ!!!\n'
      '     PEDRA - 1\n'
      '     PAPEL - 2\n'
      '   TESOURA - 3\n'
      '======================')
opcoes = ['PEDRA', 'PAPEL', 'TESOURA']
continuar = True
pJogador = 0
pComp = 0

while continuar:
    jogador = int(input('\nEscolha: '))
    while jogador not in (1, 2, 3):
        print('Invalido!')
        jogador = int(input('Escolha entre 1 e 3: '))
    computador = randint(1, 3)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!\n')
    print(f'Jogador| {opcoes[jogador-1]} x {opcoes[computador-1]} |Computador')
    while jogador == computador:
        print('Empate!')
        jogador = int(input('\nEscolha: '))
        while jogador not in (1, 2, 3):
            print('Invalido!')
            jogador = int(input('Escolha entre 1 e 3: '))
        computador = randint(1, 3)
        print(f'Jogador| {opcoes[jogador - 1]} x {opcoes[computador - 1]} |Computador')
    if jogador == 1 and computador == 2 or jogador == 2 and computador == 3 or jogador == 3 and computador == 1:
        print('Eu ganhei!')
        pComp += 1
    else:
        print('Você ganhou!')
        pJogador += 1

    print(f'\njogador| {pJogador} x {pComp} |Computador\n')

    continuar = int(input('Digite 1 para continuar ou 0 para sair: '))

print(f'\nPlacar final: Jogador| {pJogador} x {pComp} |Computador')
if pJogador == pComp:
    print('Ficamos empatados', end='')
elif pJogador > pComp:
    print('Você venceu, ', end='')
else:
    print('Eu venci, ', end='')
print(' Obrigado por jogar!')

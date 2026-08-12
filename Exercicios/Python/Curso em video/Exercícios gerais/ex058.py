from random import randint
num = randint(0, 5)
palpites = 1
chute = int(input('Pensei em um número que está entre 0 e 5. Advinhe: '))
while chute != num:
    chute = int(input('Você errou! Tente novamente: '))
    palpites += 1
print(f'Parabéns, você acertou após {palpites} tentativa(s)!')

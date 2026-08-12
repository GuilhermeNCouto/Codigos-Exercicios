print('''Abaixo podemos ver os números ímpares,
múltiplos de 3 e que se encontram entre 1 e 500''')

soma = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        print(c, end=' ')
        soma += c

print(f'\nA soma entre eles é {soma}!')

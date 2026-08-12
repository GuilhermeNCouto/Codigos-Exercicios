print('Você deverá digitar 6 números inteiros.\n')
aux = 0
soma = 0
for c in range(1, 7):
    aux = int(input(f'{c}º número: '))
    if aux % 2 == 0:
        soma += aux

print(f'\nA soma dos pares é {soma}.')

maior = 0
menor = 0
for c in range(1, 6):
    aux = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = aux
        menor = aux
    elif aux > maior:
        maior = aux
    elif aux < menor:
        menor = aux

print(f'O maior peso foi {maior}kg e\no menor foi {menor}kg')

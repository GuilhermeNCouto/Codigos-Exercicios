from datetime import date
maior = 0
menor = 0

for c in range(1, 8):
    aux = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    if date.today().year - aux < 18:
        menor += 1
    else:
        maior += 1

print(f'\nAdultos: {maior}\nMenores: {menor}')

print('Digite um número para saber se ele é primo.')

n = int(input('Número: '))
primo = True

for c in range(2, int(n/2)):
    if n % c == 0:
        primo = False

print(f'Primo? {primo}')

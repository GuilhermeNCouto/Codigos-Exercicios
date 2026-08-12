p1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
for c in range(p1, (p1 + (10-1) * r) + r, r):
    print(f'{c}', end=' ')

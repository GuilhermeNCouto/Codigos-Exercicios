from time import sleep
input("Digite ENTER para iniciar a contagem do show de fogos! ")

for c in range(10, -1, -1):
    sleep(1)
    print(f'{c}...')


print('Os fogos estouraram!')

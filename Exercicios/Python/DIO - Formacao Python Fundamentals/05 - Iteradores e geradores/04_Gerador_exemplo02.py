def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2
    
    

for i in meu_gerador(numeros=[6, 7, 8, 9, 10]):
    print(i)
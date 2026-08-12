ladoA = float(input('Lado A (cm): '))
ladoB = float(input('Lado B (cm): '))
ladoC = float(input('Lado C (cm): '))

if ladoA + ladoB < ladoC or ladoA + ladoC < ladoB or ladoC + ladoB < ladoA:
    print('As retas não podem formar um triângulo.')
else:
    print('As retas podem formar um triângulo.')
    print('Será um triângulo ', end='')
    if ladoA == ladoB == ladoC:
        print('equilátero.')
    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        print('isóceles.')
    else:
        print('escaleno.')

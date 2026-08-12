peso = float(input('Peso (kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura*altura)
print(f'O seu IMC é de {imc:.1f}, ', end='')
if imc > 40:
    print('você está em Obesidade Mórbida.')
elif imc >= 30:
    print('Você está Obeso.')
elif imc >= 25:
    print('Você está em Sobrepeso.')
elif imc >= 18.5:
    print('Você está no Peso Ideal.')
else:
    print('Você está abaixo do peso.')

print('Se cuide!')

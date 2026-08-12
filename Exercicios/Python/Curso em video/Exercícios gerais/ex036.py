valor = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Anos para pagar: '))
prestacao = valor / (anos*12)
print(f'O valor da prestação ficaria em R${prestacao:.2f},')
if prestacao > (salario * 0.3):
    print('seu empréstimo foi negado.')
else:
    print('seu empréstimo foi aprovado!')

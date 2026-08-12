valor = float(input('Valor do produto: R$ '))
pagamento = int(input('\n À vista \ \t\t\t   Dinheiro (10%-) - 1 \n'
                      ' À vista \ \t\t\t\t  cartão (5%-) - 2\n'
                      'Parcelar \ \t\t\t      2x no cartão - 3\n'
                      'Parcelar \ 3x ou mais no cartão (20%+) - 4\n'
                      '\nForma de pagamento: '))

if pagamento == 1:
    print(f'Nessa forma de pagamento você receberá\num desconto de 10%, o valor a pagar é de R$ {valor*0.9:.2f}!')
elif pagamento == 2:
    print(f'Nessa forma de pagamento você receberá\num desconto de 5%, o valor a pagar é de R$ {valor * 0.95:.2f}!')
elif pagamento == 3:
    print('Nessa forma de pagamento o valor a pagar não é alterado.')
else:
    print(f'Nessa forma de pagamento há um júros de 20%,\n o valor a pagar é de R$ {valor * 1.2:.2f}.')
    parcelas = int(input('Número de parcélas: '))
    while parcelas < 3:
        print('Você precisa escolher a partir de 3 parcélas.')
        parcelas = int(input('Número de parcélas: '))
    print(f'O valor de cada parcéla será de R$ {(valor*1.2)/parcelas:.2f}.')

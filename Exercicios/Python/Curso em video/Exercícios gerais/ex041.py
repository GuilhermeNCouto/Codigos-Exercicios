from datetime import date
idade = date.today().year - int(input('Ano de nascimento: '))
print('Sua categoria é ', end='')
if idade > 25:
    print('MASTER')
elif idade >= 19:
    print('SÊNIOR')
elif idade >= 14:
    print('JUNIOR')
elif idade >= 9:
    print('INFANTIL')
else:
    print('MIRIM')

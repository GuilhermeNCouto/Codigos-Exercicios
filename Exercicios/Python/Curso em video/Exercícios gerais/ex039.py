from datetime import date
nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc
if idade < 18:
    print(f'Você deverá se alistas em {nasc + 18}.')
elif idade == 18:
    print('Chegou a hora de se alistar!')
else:
    alistou = str.upper(input(f'O seu alistamento era em {nasc + 18}. Você se alistou? (S/N): '))
    if alistou == 'S':
        print('Parabéns por cumprir seu dever!')
    else:
        print(f'O seu alistamento está atrasado em {idade - 18} ano(s).')

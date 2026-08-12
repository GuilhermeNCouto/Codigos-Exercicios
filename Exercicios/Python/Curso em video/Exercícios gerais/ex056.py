MulherMenor20 = 0
somaIdade = 0
nomeVelho = ''
idadeVelho = 0

for c in range(1, 5):
    nome = input(f'Nome da {c}ª pessoa: ')
    idade = int(input(f'Idade da {c}ª pessoa: '))
    sexo = input(f'Sexo da {c}ª pessoa (F/M): ')
    somaIdade += idade
    if sexo in 'Mm' and idade > idadeVelho:
        nomeVelho = nome
        idadeVelho = idade
    elif sexo in 'Ff' and idade < 20:
        MulherMenor20 += 1

print(f'Média de idade: {somaIdade/4}')
print(f'Nome do homem mais velho: {nomeVelho}' if idadeVelho != 0 else 'Não houve homens.')
print(f'Mulheres com menos de 20 anos: {MulherMenor20}')



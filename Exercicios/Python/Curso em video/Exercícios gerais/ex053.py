frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}, ', end='')
print('Temos um palíndromo!' if inverso == junto else 'Não temos um palíndromo.')

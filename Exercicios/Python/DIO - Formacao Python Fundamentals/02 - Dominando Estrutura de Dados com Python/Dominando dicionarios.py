def contar_caracteres(string):
    # Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
    # Itere através de cada caractere na string string.
    for char in string:
        # Verifica se o caractere já está no dicionário
        if char in contador:
            # Se estiver, incrementa o valor
            contador[char] += 1
        else:
            # Caso contrário, adiciona com valor inicial 1
            contador[char] = 1
    # Para cada caractere, verifique se ele já está presente no dicionário contador:
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
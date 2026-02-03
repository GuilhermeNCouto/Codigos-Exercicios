def conta_vogais(texto):
    # 1. Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = 'aeiouAEIOU'
    
    # 2. Inicialize um contador para contar as vogais:
    contador = 0
    
    # 3. Itere pelos caracteres da string
    for char in texto:
        # 4. Verifique se o caractere é uma vogal e incremente o contador:
        if char in vogais:
            contador += 1
    
    # 5. Retorne o contador:
    return contador

# Solicitamos ao usuário que insira uma string
texto = input()

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")

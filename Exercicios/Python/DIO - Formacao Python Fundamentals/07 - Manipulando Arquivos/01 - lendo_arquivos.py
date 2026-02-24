arquivo = open("/workspaces/Codigos-Exercicios/Exercicios/Python/DIO - Formacao Python Fundamentals/07 - Manipulando Arquivos/lorem.txt", "r")

#print(arquivo.read(), end="\n\n") # Imprime todo o conteúdo do arquivo como uma única string
#print(arquivo.readline(), end="\n\n") # Imprime a primeira linha do arquivo
#print(arquivo.readlines(), end="\n\n") # Imprime todas as linhas do arquivo como uma lista


# Imprime o conteúdo do arquivo linha por linha
while len(linha := arquivo.readline()): # O len verifica se a linha lida tem conteúdo, ou seja, se não é uma string vazia (indicando o final do arquivo)
    print(linha, end="")



# Fecha o arquivo
arquivo.close()

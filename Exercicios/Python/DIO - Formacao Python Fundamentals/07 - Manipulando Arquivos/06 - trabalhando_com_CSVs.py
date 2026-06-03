import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

'''
try:
    with open(ROOT_PATH / 'usuarios.csv', 'w', newline='', encoding='utf-8', ) as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['id','Nome'])
        escritor.writerow(['1','Guilherme'])
        escritor.writerow(['2','Letícia'])

except IOError as exc:
    print(f"Erro ao criar o arquivo: {exc}") # Imprime uma mensagem de erro personalizada
'''

try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for index, row in enumerate(leitor):
            if index == 0:
                continue
            print(f'ID: {row[0]} \nNome: {row[1]}')

except IOError as exc:
    print(f"Erro ao criar o arquivo: {exc}") # Imprime uma mensagem de erro personalizada


# try:
#     with open(ROOT_PATH / 'usuarios.csv', 'r', newline='', encoding='utf-8') as arquivo_csv:
#         leitor = csv.DictReader(arquivo_csv)
#         for row in leitor:
#             print(row['id'], row['Nome'])
# except IOError as exc:
#     print(f"Erro ao criar o arquivo: {exc}") # Imprime uma mensagem de erro personalizada

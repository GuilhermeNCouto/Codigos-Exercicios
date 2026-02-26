import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent # Obtém o caminho do diretório onde o arquivo está localizado

#os.mkdir(ROOT_PATH / "Novo_diretorio") # Altera o diretório de trabalho para o diretório do arquivo

#arquivo = open(ROOT_PATH / "Novo_diretorio" / "novo_arquivo.txt", "w") # Cria um novo arquivo e escreve algo nele
#arquivo.close()

#os.rename(ROOT_PATH / "Novo_diretorio" / "novo_arquivo.txt", ROOT_PATH / "Novo_diretorio" / "arquivo_renomeado.txt") # Renomeia o arquivo

#os.remove(ROOT_PATH / "Novo_diretorio" / "arquivo_renomeado.txt") # Remove o arquivo

#shutil.move(ROOT_PATH / "novo_arquivo.txt", ROOT_PATH / "Novo_diretorio" / "novo_arquivo_movido.txt") # Move o diretório para outro local
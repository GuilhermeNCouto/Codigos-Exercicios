import time

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

# Criando massa de dados (1 a 100000)
dados = list(range(1, 100001))
meu_iteravel = MeuIterador(dados)

tempo_total_inicio = time.perf_counter()

print(f"{'Valor':<10} | {'Tempo Iteração (s)':<20}")
print("-" * 35)

for i in meu_iteravel:
    # Início do tempo da iteração individual
    it_inicio = time.perf_counter()
    
    # Exibição do resultado
    print(f"{i:<10}", end=" | ")
    
    it_fim = time.perf_counter()
    print(f"{it_fim - it_inicio:.8f}")

tempo_total_fim = time.perf_counter()
tempo_total_execucao = tempo_total_fim - tempo_total_inicio

print("-" * 35)
print(f"TEMPO TOTAL DE EXECUÇÃO: {tempo_total_execucao:.6f} segundos")
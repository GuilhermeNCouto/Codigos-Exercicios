import time

# Versão com Gerador
def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

# Criando massa de dados (1 a 100000)
dados = list(range(1, 100001))
gerador_instancia = meu_gerador(dados)

print(f"{'Gerador':<10} | {'Tempo Iteração (s)':<20}")
print("-" * 35)

# Início da contagem total
tempo_total_inicio = time.perf_counter()

for i in gerador_instancia:
    # Início do tempo da iteração individual
    it_inicio = time.perf_counter()
    
    # Exibição do resultado
    print(f"{i:<10}", end=" | ")
    
    it_fim = time.perf_counter()
    print(f"{it_fim - it_inicio:.8f}")

# Fim da contagem total
tempo_total_fim = time.perf_counter()
tempo_total_execucao = tempo_total_fim - tempo_total_inicio

print("-" * 35)
print(f"TEMPO TOTAL (GERADOR): {tempo_total_execucao:.6f} segundos")

'''
    Característica      Gerador (yield)                     Iterador (Classe)
 Esforço de Código      Mínimo (algumas linhas)             Médio (precisa de estrutura de classe)
           Memória      Excelente (um item por vez)         Excelente (um item por vez)
      Reutilização      Uma única vez (esgota o gerador)    Pode ser reiniciado se você programar
              Foco      Ação (O que fazer com o dado)       Estado (O que o objeto sabe/guarda)
'''
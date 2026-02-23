import datetime

# Referência para os exemplos
base_time = datetime.datetime(2026, 1, 1, 12, 0, 0)
print(f"Tempo base: {base_time}")

# A) Deslocamento Multi-parâmetro
# O timedelta ajusta automaticamente overflow de dias, meses e anos.
offset = datetime.timedelta(days=1, hours=12, minutes=30, seconds=15)
result = base_time + offset
print(f"Offset positivo: {result}")

# B) Subtração e Períodos Passados
# Útil para janelas de observação em logs (Lookback Windows)
lookback = datetime.datetime.now() - datetime.timedelta(days=30)
print(f"Janela de 30 dias atrás: {lookback}")

# C) Diferença entre Datetimes (Resulta em um objeto Timedelta)
t1 = datetime.datetime(2026, 2, 10, 14, 0, 0)
t2 = datetime.datetime(2026, 2, 11, 16, 45, 30)
delta = t2 - t1

print(f"Diferença bruta: {delta}")
print(f"Dias de diferença: {delta.days}")
print(f"Segundos totais da diferença: {delta.total_seconds()}")

# D) Operações Escalares com Timedelta
# Você pode multiplicar ou dividir durações
sessao_padrao = datetime.timedelta(minutes=45)
ciclo_triplo = sessao_padrao * 3
print(f"Duração triplicada: {ciclo_triplo}")

# E) Comparação de Intervalos
# Verificar se um intervalo é maior que outro
if delta > datetime.timedelta(hours=24):
    print("O intervalo excede 24 horas.")
    
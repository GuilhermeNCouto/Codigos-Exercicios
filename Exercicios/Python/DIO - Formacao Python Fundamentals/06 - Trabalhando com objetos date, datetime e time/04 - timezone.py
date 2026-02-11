import datetime
import zoneinfo

# ==========================================
# 4. TIMEZONE (Localização e Conversão)
# ==========================================

# A) Criando um objeto 'Aware' (Consciente do fuso)
# Boa prática: Sempre use UTC para armazenar e SP para exibir
fuso_sp = zoneinfo.ZoneInfo('America/Sao_Paulo')
fuso_utc = zoneinfo.ZoneInfo('UTC')

agora_sp = datetime.datetime.now(fuso_sp)
agora_utc = datetime.datetime.now(fuso_utc)

print(f"Agora em São Paulo: {agora_sp.strftime('%H:%M:%S')}")
print(f"Agora em UTC (Padrão Nuvem): {agora_utc.strftime('%H:%M:%S')}")


# B) Convertendo entre fusos (O método astimezone)
# Se você recebeu um dado de Tokyo e quer saber que horas eram aqui:
fuso_tokyo = zoneinfo.ZoneInfo('Asia/Tokyo')
chegada_tokyo = datetime.datetime.now(fuso_tokyo)

# Converte o objeto de Tokyo para o fuso de SP mantendo o mesmo instante no tempo
chegada_em_sp = chegada_tokyo.astimezone(fuso_sp)

print(f"\nHora em Tokyo: {chegada_tokyo.strftime('%H:%M:%S')}")
print(f"Mesmo instante em SP: {chegada_em_sp.strftime('%H:%M:%S')}")


# C) Transformando um objeto 'Naive' em 'Aware'
# Às vezes o dado vem sem fuso do banco, e você "carimba" o fuso nele
d_naive = datetime.datetime(2024, 6, 1, 15, 0) # Sem fuso
d_aware = d_naive.replace(tzinfo=fuso_sp)      # Forçando o fuso de SP

print(f"\nObjeto 'carimbado' com fuso: {d_aware}")

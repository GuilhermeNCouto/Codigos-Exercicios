import datetime

# ==========================================
# 1. DATETIME COMUM (Criação de Objetos)
# ==========================================
# Criando um objeto date (ano, mês, dia)
d1 = datetime.date(2026, 2, 9) 
print(f"D1 (Objeto Date): {d1}") 

# Criando um objeto datetime (ano, mês, dia, hora, minuto, segundo)
d2 = datetime.datetime(2024, 6, 1, 12, 30, 45)
print(f"D2 (Objeto Datetime): {d2}")

# Data e hora atual do sistema
d3 = datetime.datetime.now()
print(f"D3 (Now - sem fuso): {d3}")
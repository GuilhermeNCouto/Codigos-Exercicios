from datetime import datetime, timedelta, date, time
from zoneinfo import ZoneInfo

print("Bem-vindo ao Lava Jato!")
while (tipo_carro := input("Digite o tipo do carro (P, M ou G): ").upper()) not in ['P', 'M', 'G']:
    print("Entrada inválida! Escolha apenas P, M ou G: ")

tempos = {'P': 30, 'M': 45, 'G': 60}
data_atual = datetime.now(ZoneInfo("America/Sao_Paulo"))

print(f"O carro chegou em {data_atual.strftime('%d/%m/%Y %H:%M:%S')}.\nFicará pronto em {(data_atual + timedelta(hours=tempos[tipo_carro])).strftime('%d/%m/%Y %H:%M:%S')}.")

print("Obrigado por escolher o Lava Jato!")

print("testes: ")

print(date.today() + timedelta(days=1)) # Data atual mmais 1 dia
time = datetime.now(ZoneInfo("America/Sao_Paulo")) + timedelta(hours=2) # Data e hora atual mais 2 horas
print(time.time()) # Imprime apenas a hora
print(datetime.now().date()) # Imprime apenas a data atual
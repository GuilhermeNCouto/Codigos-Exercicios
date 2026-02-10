import datetime # Importa a biblioteca datetime
import zoneinfo # Importa a biblioteca zoneinfo para fuso horário (Python 3.9+)


# Criando um objeto date
d1 = datetime.date(2026, 2, 9) #ano, mês, dia
print(d1) 


# Criando um objeto datetime
d2 = datetime.datetime(2024, 6, 1, 12, 30, 45) #ano, mês, dia, hora, minuto, segundo
print(d2) 
# Adicionando uma semana
d2 = d2 + datetime.timedelta(weeks=1)
print(d2)


d3 = datetime.datetime.now() # Data e hora atual
# Formatando a data e hora
print(d3.strftime("%d/%m/%Y %H:%M:%S")) 


# Convertendo string para datetime
d4_str = "01/06/2024 14:45:30"
d4 = datetime.datetime.strptime(d4_str, "%d/%m/%Y %H:%M:%S")
print(d4) 


# Trabalhando com fuso horário
d5 = datetime.datetime.now(zoneinfo.ZoneInfo('America/Sao_Paulo')) # Data e hora atual com fuso horário de São Paulo
d5 = datetime.datetime.strftime(d5, "%d/%m/%Y %H:%M:%S") # Formatando a data e hora com fuso horário
print(d5)


# Criando um datetime com fuso horário sem ZoneInfo
d6 = datetime.datetime(2002, 10, 11, 1, 13, 22, tzinfo=zoneinfo.ZoneInfo('America/Sao_Paulo')) # Criando um datetime com fuso horário
print(d6)

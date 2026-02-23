import datetime

# ==========================================
# 3. STRFTIME E STRPTIME (Conversão e Normalização)
# ==========================================

# --- PARTE 1: STRFTIME (Objeto -> Texto) ---
# Útil para exibição (Frontend) e Logs
agora = datetime.datetime.now()
mascara_ptbr = "%d/%m/%Y %H:%M:%S"
mascara_enus = "%m/%d/%Y %I:%M:%S %p"
print(f"Objeto puro (ISO): {agora.weekday()}")
print(f"Formato PT-BR:     {agora.strftime(mascara_ptbr)}")
print(f"Formato EN-US:     {agora.strftime(mascara_enus)}")
print(f"Formato Banco SQL: {agora.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Apenas Horário:    {agora.strftime('%H:%M:%S')}")
print(f"Apenas Data:      {agora.strftime('%d/%m/%Y')}")


# --- PARTE 2: STRPTIME (Texto -> Objeto) ---
# Útil para captura de dados (Ingestão)
data_entrada_str = "01/06/2024 14:45:30"

# O parse exige que a máscara coincida exatamente com a string de entrada
data_objeto = datetime.datetime.strptime(data_entrada_str, "%d/%m/%Y %H:%M:%S")

print(f"\nString capturada: {data_entrada_str}")
print(f"Objeto gerado:    {data_objeto}")


# --- PARTE 3: O FLUXO COMPLETO (Parse -> Processamento -> Format) ---
# Exemplo: Receber data, somar tempo e formatar para relatório
vencimento_str = "20/10/2025"
# 1. Parse
vencimento_obj = datetime.datetime.strptime(vencimento_str, "%d/%m/%Y")
# 2. Processamento (Timedelta)
vencimento_final = vencimento_obj + datetime.timedelta(days=30)
# 3. Format (Saída amigável)
print(f"\nFatura original: {vencimento_str}")
print(f"Novo vencimento: {vencimento_final.strftime('%A, %d de %B de %Y')}")
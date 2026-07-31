class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada para {self.titular} com saldo inicial de R$ {self.saldo:,.2f}.\n")

    def __str__(self):
        return f"Conta {self.id} - {self.titular}"

    def realizar_extrato(self):
        linha = "=" * 40
        titulo = 'EXTRATO'.center(40)
        print(f"\n{linha}\n{titulo}\n{linha}\n{'ID':<15} | {str(self.id):>20}\n{'Titular':<15} | {self.titular:>20}\n{'Saldo':<15} | {f'R$ {self.saldo:,.2f}':>20}\n{linha}\n")

    def depositar(self, valor):
        self.saldo += valor
        linha = "-" * 40
        titulo = 'Depósito realizado'.center(40)
        print(f"{linha}\n{titulo}\n{linha}\n{'Valor Depositado':<20} | {f'R$ {valor:,.2f}':>18}\n{'Novo Saldo':<20} | {f'R$ {self.saldo:,.2f}':>18}\n{linha}\n")

    def sacar(self, valor):
        if valor > self.saldo:
            linha = "-" * 40
            titulo = '❌ Erro no Saque'.center(40)
            print(f"{linha}\n{titulo}\n{linha}\n{'Saldo Disponível':<20} | {f'R$ {self.saldo:,.2f}':>18}\n{'Valor Solicitado':<20} | {f'R$ {valor:,.2f}':>18}\n{linha}\n")
        else:
            self.saldo -= valor
            linha = "-" * 40
            titulo = 'Saque realizado'.center(40)
            print(f"{linha}\n{titulo}\n{linha}\n{'Valor Sacado':<20} | {f'R$ {valor:,.2f}':>18}\n{'Novo Saldo':<20} | {f'R$ {self.saldo:,.2f}':>18}\n{linha}\n")





conta1 = ContaBancaria(1, "Letícia", 1000)
conta1.depositar(50000)
conta1.sacar(2000)
conta1.realizar_extrato()

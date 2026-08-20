from rich import print
from rich.table import Table

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos.
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id # Público (+)
        self._titular = nome # Protegido (#)
        self.__saldo = saldo # Privado (-)
        print(f"Conta {self.id} criada para [yellow]{self._titular}[/] com saldo inicial de [green]R${self.__saldo:,.2f}[/].\n")

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    def realizar_extrato(self):
        tabela = Table(title="[bold blue]:receipt: EXTRATO[/]")
        tabela.add_column("Campo", style="cyan", no_wrap=True)
        tabela.add_column("Detalhes", style="magenta", justify="right")

        tabela.add_row("ID", str(self.id))
        tabela.add_row("Titular", self._titular)
        tabela.add_row("Saldo", f"R${self.__saldo:,.2f}")

        print(tabela)
        print()

    def depositar(self, valor):
        if valor <= 0:
            tabela = Table(title="[bold red]❌ Erro no Depósito[/]")
            tabela.add_column("Mensagem", justify="center", style="red")
            tabela.add_row("Informe um saldo válido para depósito.")
            print(tabela)
            print()
            return
            
        valor = abs(valor)
        self.__saldo += valor
        
        tabela = Table(title="[bold green]✅ Depósito Realizado[/]")
        tabela.add_column("Descrição", style="cyan")
        tabela.add_column("Valor", style="green", justify="right")
        
        tabela.add_row("Valor Depositado", f"R${valor:,.2f}")
        tabela.add_row("Novo Saldo", f"R${self.__saldo:,.2f}")
        
        print(tabela)
        print()

    def sacar(self, valor):
        if valor > self.__saldo or valor <= 0:
            tabela = Table(title="[bold red]❌ Erro no Saque[/]")
            tabela.add_column("Descrição", style="cyan")
            tabela.add_column("Valor", style="red", justify="right")
            
            tabela.add_row("Saldo Atual", f"R${self.__saldo:,.2f}")
            tabela.add_row("Valor Solicitado", f"R${valor:,.2f}")
            
            print(tabela)
            print()
            return
            
        self.__saldo -= valor
        
        tabela = Table(title="[bold green]✅ Saque realizado[/]")
        tabela.add_column("Descrição", style="cyan")
        tabela.add_column("Valor", style="green", justify="right")
        
        tabela.add_row("Valor Sacado", f"R${valor:,.2f}")
        tabela.add_row("Novo Saldo", f"R${self.__saldo:,.2f}")
        
        print(tabela)
        print()
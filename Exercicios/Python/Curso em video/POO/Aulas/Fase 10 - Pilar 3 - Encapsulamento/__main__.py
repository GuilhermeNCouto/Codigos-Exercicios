from conta_bancaria import ContaBancaria

def main ():
    
    conta = ContaBancaria(101, "Guilherme", 1500.00)
    
    conta.realizar_extrato()
    conta.depositar(0)
    conta.depositar(500)
    conta.sacar(2500)  # Vai dar erro de saldo
    conta.sacar(300)
    conta.realizar_extrato()
    
    print(conta)
    
if __name__ == "__main__":
    main()
    
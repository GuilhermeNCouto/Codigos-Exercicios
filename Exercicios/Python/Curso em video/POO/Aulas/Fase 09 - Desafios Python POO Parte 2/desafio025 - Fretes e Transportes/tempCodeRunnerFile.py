def main():
    dist = 20
    entrega = Caminhao(dist)
    
    print(f"Frete de [yellow]{type(entrega).__name__}[/] em [blue]{dist}Km[/]: R$[green]{entrega.calc_frete():.2f}[/]")

if __name__ == '__main__':
    main()
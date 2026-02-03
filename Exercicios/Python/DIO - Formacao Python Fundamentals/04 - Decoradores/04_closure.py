'''
Uma closure ocorre quando uma função interna lembra o ambiente em que foi criada, mesmo depois que a
função externa tenha terminado sua execução
'''

def multiplicador(fator):
    def aplicar(numero):
        return numero * fator  # Ela 'lembra' do fator do pai!
    return aplicar

dobrar = multiplicador(2)
triplicar = multiplicador(3)

print(dobrar(10))    # 20
print(triplicar(10)) # 30

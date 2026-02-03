import requests

'''
Exemplo de gerador que busca produtos de uma API paginada
e retorna um produto por vez.
'''

def fetch_products(api_url, max_pages=100): # Limita o número máximo de páginas a serem buscadas
    page = 1 # Página inicial
    while page <= max_pages: # Limita o número máximo de páginas
        response = requests.get(f"{api_url}?page={page}") # Faz a requisição para a API
        data = response.json() # Converte a resposta para JSON
        for product in data['products']: # Itera sobre os produtos na página
            yield product # Retorna um produto por vez
        if 'next_page' not in data: # Verifica se há uma próxima página
            break # Sai do loop se não houver próxima página
        page += 1 # Incrementa o número da página


#uso do gerador
for product in fetch_products("https://api.example.com/products"): # Substitua pela URL real da API
    print(product['name']) # Imprime o nome do produto
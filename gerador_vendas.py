import random
import datetime


# Função para gerar datas aleatórias no intervalo de 100 dias
def generate_random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_seconds = random.randint(0, 86400)  # Número de segundos em um dia
    random_date = start_date + datetime.timedelta(
        days=random_days, seconds=random_seconds
    )
    return random_date


# Configurar datas de início e fim
start_date = datetime.datetime(2024, 1, 1)
end_date = datetime.datetime(2024, 5, 23)

# Lista de produtos
products = [
    {"id": 1, "nome": "jabuticaba", "preco": 5.0, "categoria": "frutas"},
    {"id": 10, "nome": "teste", "preco": 10.0, "categoria": "legumes"},
    {"id": 6, "nome": "leite", "preco": 5.6, "categoria": "laticínios"},
    {"id": 3, "nome": "manga", "preco": 3.5, "categoria": "frutas"},
    {"id": 4, "nome": "tomate", "preco": 2.8, "categoria": "legumes"},
]

# Lista de vendedores
sellers = ["ANDERSON", "João Silva", "Maria Oliveira"]

# Lista de compradores (CPF fictícios)
buyers = ["Comprador", "12345678901", "76543210122", "10923456788"]

# Gerar registros de vendas
vendas = []
for _ in range(100):
    product = random.choice(products)
    seller = random.choice(sellers)
    buyer = random.choice(buyers)
    quantity = random.randint(1, 5)
    total_price = product["preco"] * quantity
    date = generate_random_date(start_date, end_date).strftime("%d/%m/%Y %H:%M:%S")

    venda = f"{product['id']}|{product['nome']}|{product['preco']}|{product['categoria']}|{seller}|{buyer}|{quantity}|{total_price}|{date}"
    vendas.append(venda)

# Imprimir as vendas geradas
for venda in vendas:
    print(venda)

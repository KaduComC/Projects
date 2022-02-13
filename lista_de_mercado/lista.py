import os

# sistema = os.environ
# print(sistema)
# print(sistema['USERNAME'])
# print(os.getcwd())

nome_lista = 'lista.txt'

while True:
    quantidade = int(input('quantidade '))
    lista_mercado = dict()

    

    for item in range(quantidade):
        nome_item = input(f'Nome: ')
        quantidade_item = int(input(f'quantidade do item: '))
        lista_mercado[nome_item] = quantidade_item

'''
    A função reduce() do Python é usada para reduzir uma sequência a um único valor. 
    Faz a soma dos valores em uma lista ou lista de objetos.
'''

from functools import reduce

# lista
numbers = [1, 2, 3, 4, 5]

# Usa reduce() para calcular a soma dos elementos da lista
total = reduce(lambda x, y : x + y, numbers)

# Imprime o total
print(total)

#-------------------------------------------------------------------

from functools import reduce

# lista de objetos
preco_produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Usa reduce() para calcular a soma dos preços dos produtos
total_precos = reduce(lambda x, y : x + y, [produto['preco'] for produto in preco_produtos])

# Imprime o total dos preços
print(f'Preço total: {total_precos:.2f}')
print(f'Preço total: {round(total_precos, 2)}')

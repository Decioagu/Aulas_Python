'''
O módulo pprint do Python fornece uma maneira de imprimir representações de estruturas 
de dados de forma organizada e legível. Isso pode ser útil para depuração, logging e para tornar 
a saída de programas mais compreensível.
'''

import pprint
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
    {'nome': 'p4', 'preco': 50, },
    {'nome': 'p5', 'preco': 5, },
]

print(*produtos, sep='\n') # imprimir lista descompactada 
print()
print(produtos, sep='\n') # imprimir
print()
pprint.pprint(produtos) # imprimir lista organizada

# -------------------------------------------------------------------------
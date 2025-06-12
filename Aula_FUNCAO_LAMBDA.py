"""
    Introdução à função lambda (função anônima de uma linha)
    A função lambda é uma função como qualquer
    outra em Python. Porém, são funções anônimas
    que contém apenas uma linha. Ou seja, tudo
    deve ser contido dentro de uma única
    expressão.
"""

# função 
def dobro(x):
    return x * 2
print(dobro(5))

dobro_com_lambda = lambda x: x * 2 # função lambda
print(dobro_com_lambda(5))

print('==============================================')


soma = lambda n1, n2: n1 + n2 # função lambda
print(soma(10,5))


print('==============================================')

lista = [(1, 9), (2, 3), (3, 8)]
# ordenado = sorted(iterable, key=None, reverse=False)
ordenado = sorted(lista, key=lambda x: x[1]) # ordena a lista de tuplas pelo segundo elemento
print(ordenado)

print('==============================================')

palavras = ["carro", "avião", "barco"]
ordenadas = sorted(palavras, key=lambda x: x[0])
print(ordenadas)  

'''
x[0] → primeira letra

x[1] → segunda letra

x[2] → terceira letra
'''
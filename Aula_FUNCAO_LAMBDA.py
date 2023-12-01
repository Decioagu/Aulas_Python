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
print()

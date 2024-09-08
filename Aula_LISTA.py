'''
Em Python, uma lista é uma estrutura de dados que permite armazenar uma coleção de itens 
em uma única variável. Os itens da lista podem ser de qualquer tipo, incluindo números, 
strings, objetos ou até mesmo outras listas.

Alguns métodos de lista comuns incluem:

append(): Adiciona um elemento ao final da lista.
count(): Conta o número de ocorrências de um elemento na lista.
extend(): Adiciona os elementos de uma lista a outra lista.
index(): Retorna o índice de um elemento na lista.
insert(): Insere um elemento em uma posição específica na lista.
pop(): Remove um elemento do final da lista.
remove(): Remove a primeira ocorrência de um elemento na lista.
reverse(): Inverte a ordem dos elementos na lista.
sort(): Ordena os elementos na lista.
clear(): Remove todos os itens na lista.
len(): Retorna o número de itens na lista.
'''
# --------------------------------------------------------------
# Criar Lista
print('CRIAR LISTA')
listaA = list()
print(listaA)
listaB = []
print(listaB)
listaC = list(range(0,11,2))
print(listaC)
print()

# --------------------------------------------------------------
# visualizar elementos da lista
lista = [1,2,3]
print(lista)
print(type(lista))
print(type(lista[0]))
print(type(lista[1]))
print((lista[0]+lista[2])) # resposta 4
print()
l= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(l[:4])
print(l[::2])
print(l[::4])
print(l[::-1])

# --------------------------------------------------------------
# desempacotar lista
lista = ['a','b','c','d']
lista0, lista1, lista2, lista3 = lista # desempacotar
print(f'{lista0=}, {lista2=}') # elementos desempacotado
lista = ['a','b','c','d']
lista0, *resto = lista # desempacotar
print(f'{lista0=}, {resto=}')
lista = ['a','b','c','d']
_, _, lista2, *_ = lista # desempacotar
print(f'{lista2=}')
lista = ['a','b','c','d','e','f']
_, lista1, *resto, lista5 = lista # desempacotar
print(f'{resto}')

# --------------------------------------------------------------
# Alterar valor da lista
print('ALTERAR VALOR DE UMA LISTA')
lista = [1,2,3,4,5]
print(lista)
lista[0] = 0
print(lista)
lista[4] = 0
print(lista)
# --------------------------------------------------------------

# Atualizar elementos na lista em uma lista
lista = ['X', 'a', 'Z']
lista[1] = 'Y' # <====== indicação da posição do elemento por índice
print(lista)

# --------------------------------------------------------------
# adicionar elementos na lista
lista = [1,2,3,4,5]
print('ACRESCENTAR ELEMENTOS NO FINAL DE UMA LISTA')
lista.append(6) # adiciona na ultima posição
print(lista)
print('INSERIR ELEMENTOS EM UMA LISTA NA POSIÇÃO DESEJADA "lista.insert(POSIÇÃO, VALOR)"')
lista.insert(3, "x") # (posição, elemento)
print(lista)

# --------------------------------------------------------------
# ELIMINAR ELEMENTOS EM UMA LISTA PELA POSIÇÃO
lista = [1,2,3,4,5]
del lista[2] # deletar por índice (posição em lista)
print(lista)

# --------------------------------------------------------------
# APAGAR, EXCLUIR, DELETAR UMA LISTA
del lista # (apaga, deletar, excluir) a lista

# --------------------------------------------------------------
# LIMPAR TODO CONTEÚDO DE UMS LISTA
lista = [1,2,3,4,5]
print(lista)
lista.clear() # limpa todo o conteúdo de uma lista
print(lista)

# --------------------------------------------------------------
# ELIMINAR ELEMENTOS EM UMA LISTA PELA POSIÇÃO
lista = ['a','b','c','d','e','f']
lista.pop(4) # eliminar por índice
print(lista)
lista.pop() # elimina ultimo elemento => exemplo "f"
print(lista)
lista.pop(-2)
print(lista)
print()
lista = [1,'A',2,3,'D',5]
print(lista)
print('ELIMINAR ELEMENTOS EM UMA LISTA POLO NOME')
lista.remove('D') #  eliminar por nome
print(lista)

# --------------------------------------------------------------
# retornar (armazena) em "b" elemento apagado em "a"
x = ['a','b','c']
b = x.pop()
print(f'{x=}')
print(f'{b=}')

# --------------------------------------------------------------
# ORGANIZAR UMA LISA
lista = [3,7,1,4,2,6,3,5]
print(lista)
print('========================')
lista.sort() # ordem crescente
print(lista)
lista.sort(reverse=True) # ordem decrescente
print(lista)
print('========================')
print(sorted(lista)) # ordem crescente
print(sorted(lista, reverse=True)) # ordem decrescente
print('========================')

# ===================================================================
# COPIAR UMA LISTA
A = [0,1,2,3,4,5]
B = A # não é copia aponta para o mesmo ponto de memorio
C = A[:] # copia rasa (copia parcial) - NÃO copia (lista ou dicionario) interno
del A[0] # deletar por índice (posição em lista)
print(f'Lista A: {A}')
print(f'Lista B: {B}')
print(f'Lista C: {C}')
print()
D = C.copy()
C.remove(5)
C.pop(0)
print(f'Lista C: {C}')
print(f'Lista D: {D}')
print()
lista = [10, 8, 6, 4, 2]
nova_lista = lista[1:3]
print(nova_lista)

print('========================')

# COPIAR UMA LISTA 2
'''
    copy(): cria uma cópia superficial de um objeto.
    deepcopy(): cria uma cópia profunda de um objeto.
'''
import copy # biblioteca copy
d0 = [0, 1, [1,2,3]]

d1 = d0 # aponta para o mesmo dicionario (NÃO é copia real)
d2 = d0[:] # copia rasa (copia parcial) - NÃO copia (lista ou dicionario) interno
# copy.copy(NOME) = NOME.copy() | NOME.copy() não necessita de biblioteca |
d3 = copy.copy(d0) # copia rasa (copia parcial) - NÃO copia (lista ou dicionario) interno
d4 = copy.deepcopy(d2) # deepcopy (cópia profunda) - copia totalmente nova
d0[0] = 1
d1[0] = 2
d1[2][0] = 6
d2[0] = 3
d2[2][0] = 7
d2[0] = 4
d3[2][0] = 8
d3[0] = 5
d4[2][2] = 9
d4[0] = 6
print('d0 = ',d0)
print('d1 = ',d1)
print('d2 = ',d2)
print('d3 = ',d3)
print('d4 = ',d4)
# ===================================================================

# reposicionar elementos da lista
lista = [1,2,3]
print(lista)
lista[0], lista[1], lista[2] = lista[2], lista[1], lista[0] # reposicionar elementos
print(lista)
lista = [1,2,3,4,5]
print(lista)
lista[2], lista[4] = lista[4], lista[2]
print(lista)

# ------------------------------------------------------
# exercício de manipulação
lista = [1,2,3,4,5]
x = [lista] # copiar lista em uma lista "x"
print(x)
lista.pop(1) # eliminar por índice
print(x)
x.append(lista[:]) # adicionar lista na lista "x"
print(x)
lista.insert(1, 'Z') # adicionar letra 'a' na lista
print(x)
x.append(lista.copy()) # copiar lista em uma lista "x"
print(x)
lista.remove('Z') # eliminar 'Z' da lista
print(x)
# ---------------------------------------------------------------------
'''
    range() é uma função em Python é usada para criar uma sequência de números
    range(inicio, fim, passo)
'''

print(list(range(10)))
print(list(range(-10, 10, 2)))

# este exemplo imprime os números de 0 a 9, de um em um
for numero in range(10):
    print(numero)
print()
print('========================')

# este exemplo imprime os números de 1 a 10, de um em um
for numero in range(1,11):
    print(numero)
print()
print('========================')

# começa valendo 1 e salta de 2 em 2 até atingir ou passar 20
for numero in range(1,21,2):
    print(numero)
print()
print('========================')

# imprimindo os números de 1 a 10 em ordem decrescente
for numero in range (10,0,-1):
    print(numero)
print()
print('========================')

# inserir 'x' cinco vez na lista
# "compreensão de lista" ou "list comprehension"
lista = ['x' for numero in range(5)]
print(lista)
print()
print('========================')

# dobra valores da range na lista
# ("compreensão de lista" ou "list comprehension")
lista = [numero * 2 for numero in range(1, 11)]
print(lista)
print()

# ---------------------------------------------------------------------
'''
    enumerate() é uma função para iterar uma sequência e retornar o índice e o valor de cada item
    enumerate(iterável, inicio_da_contagem)
'''

# exibe em tupla (índice, elemento)
lista = ['a','b','c','d','e']
for letra in enumerate(lista):
    print(letra)
print()
print('========================')

# exibe índice com elemento começando por 1
lista = ['a','b','c','d','e']
for index, letra  in enumerate(lista, start=1):
    print(f'{index=} = {letra=}')
print()

# ---------------------------------------------------------------------
# (FILTRO) exibir somente valores igual e maior que 2, igual e menor que 5
# "compreensão de lista" ou "list comprehension"
lista = [n for n in range(10) if 2<= n <= 5]
print(lista)

# ---------------------------------------------------------------------
# (FILTRO) eliminar itens repetidos (NÃO garante a ordem dos elementos)
lista = [30, 10, 20, 40, 40, 10, 40, 20, 60, 20, 90]
print(lista)
lista = set(lista) # conjunto
print(lista)
lista = list(lista) # lista
print(lista)
print()

# ---------------------------------------------------------------------
# (FILTRO) eliminar repetições em lista (garante a ordem dos elementos)
lista1 = [30, 10, 20, 40, 40, 10, 40, 20, 60, 20, 90]
lista2 = []
for p1 in lista1:
    if p1 not in lista2:
        lista2.append(p1)
print(lista2)
print()

# ---------------------------------------------------------------------
# (FILTRO) faz nova lista com itens que se repete (NÃO garante a ordem dos elementos)
lista1 = [30, 10, 20, 40, 40, 10, 40, 20, 60, 20, 90]
lista2 = set()
contador = 0
for numero1 in lista1: 
    for numero2 in lista1:
        if numero1 == numero2:
            contador += 1 

        if contador == 2:  # contador = 0 (número apareceu 2 vezes na lista)
            lista2.add(numero1) # armazene o número
            contador = 0 # zerar contador
    contador = 0 # zerar contador apos o "for" (numero2)
print(list(lista2))
print()

# ---------------------------------------------------------------------
# (FILTRO) faz nova lista com itens que NÃO se repete
lista1 = [30, 10, 20, 40, 40, 10, 40, 20, 60, 20, 90]
lista2 = []
contador = 0
for numero1 in lista1: 
    for numero2 in lista1:
        if numero1 == numero2:
            contador += 1

    if contador == 1: # contador = 1 (número apareceu somente 1 vezes na lista)
        lista2.append(numero1) # armazene o número
        contador = 0 # zerar contador
    contador = 0 # zerar contador apos o "for" (numero2) 
print(lista2)
print()

# ---------------------------------------------------------------------
# Mapeamento de dados em list comprehension
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
print(lista)
print()

# ---------------------------------------------------------------------

# Ordenação de dicionário em lista:
'''
    A sorted() função em Python é uma função interna que classifica os elementos de um iterável 
    em uma ordem específica (crescente ou decrescente) e os retorna como uma lista.

    A sorted()função recebe três parâmetros:

    iterable: O iterável a ser classificado.
    key: Uma função opcional que recebe um elemento do iterável como entrada e retorna um valor 
         a ser usado para classificação. O valor padrão é Nenhum, o que significa que os elementos 
         são classificados por sua ordem natural.
    reverse: Um valor booleano que indica se os elementos devem ser classificados em ordem decrescente (True) 
             ou crescente (False). O valor padrão é falso.
             
            Exemplo: 
            list1 = [3, 4, 5, 1, 2]
            print(sorted(list1))
            print(sorted(list1, reverse=True))

'''
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome']) # ordenar por nome
l2 = sorted(lista, key=lambda item: item['sobrenome']) # ordenar por sobrenome

exibir(l1)
exibir(l2)
print()
# --------------------------------------------------------------
# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
    {'nome': 'p4', 'preco': 50, },
    {'nome': 'p5', 'preco': 5, },
]
# atualizar preço acima de valor 20
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} if produto['preco'] > 20 else {**produto} # regra
    for produto in produtos # percorrer iterável criando nova lista conforme regra
    if produto['preco'] >= 30 # filtro para valores igual ou maior que 30 (valores ainda NÃO atualizados em "novos_produtos")
]
# print(novos_produtos)
print(*novos_produtos, sep='\n') # desempacotar lista
print()

# --------------------------------------------------------------
'''
    O itemgetter() é uma ferramenta útil para classificar itens de um objeto.
'''
from operator import itemgetter # biblioteca

names = ["abc", "bac", "cda"]
ordem = sorted(names, key=itemgetter(0)) # ordena lista conforme letra desejada (ONDE key=itemgetter(posição letra) ) 
print(ordem)

# --------------------------------------------------------------
# UNIR DUAS LISTAS
lista1 = ["a", "b", "c"]
lista2 = ["d", "e", "f"]

nova_lista = lista1 + lista2

print(nova_lista)
print()
print('========================')


# UNIR DUAS LISTAS
lista1 = ["a", "b", "c"]
lista2 = ["d", "e", "f"]

lista1.extend(lista2)

print(lista1)
print()
print('========================')

# UNIR DUAS LISTAS
lista1 = ["a", "b", "c"]
lista2 = ["d", "e", "f"]

for item in lista2:
    lista1.append(item)

print(lista1)

# --------------------------------------------------------------
# zipper
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    res = [(l1[i], l2[i]) for i in range(intervalo)] # "compreensão de lista" ou "list comprehension"
    print(res)
    
zipper(l1, l2)

print()
print('========================')

'''
    Em Python, a função zip() é uma função integrada que permite combinar duas ou mais sequências 
    (listas, tuplas, etc.) em um objeto zip. A partir desse objeto zip, é possível criar iteráveis 
    de tuplas contendo elementos correspondentes de cada sequência original.
'''
# zip utilizando menor lista #
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
lista3 = []

zip_object = zip(lista1, lista2) # retorna um objeto Map
# zip_object = list(zip(lista1, lista2))

for item in zip_object:
    lista3.append(item)

print(lista3)
# print(zip_object)

print()
print('========================')

# zip utilizando maior lista #
from itertools import zip_longest
lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']

# O argumento "fillvalue=" é usado para preencher valores ausentes em uma matriz.
zip_object = zip_longest(lista1, lista2, fillvalue='Sem Nome') 

print(list(zip_object))

# --------------------------------------------------------------

# Combinação ou coleção de objetos em listas
from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = ['João', 'Joana', 'Luiz', 'Letícia']

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]



print_iter(combinations(pessoas, 2)) # (iterável, tamanho do grupo) - sem repetição por ordem
print()
print('========================')

print_iter(permutations(pessoas, 2)) # (iterável, tamanho do grupo) - com repetição por ordem
print()
print('========================')

print_iter(product(*camisetas)) # "PRODUTO CARTESIANO"

'''
    Em matemática, o "PRODUTO CARTESIANO" de dois conjuntos, X e Y, 
    é o conjunto de todos os pares ordenados, 
    cujo primeiro termo pertence a X; e o segundo, a Y.

    X * Y = {(x, y) | x ∈ X, y ∈ Y}
    Por exemplo, se X = {1, 2, 3} e Y = {a, b, c}, então:
    X * Y = {(1, a), (1, b), (1, c), (2, a), (2, b), (2, c), (3, a), (3, b), (3, c)}.
'''

# --------------------------------------------------------------
'''
    OBS: necessário ordenar lista antes de agrupar para não haver grupos como mesmo (elementos selecionado)   
'''
# Agrupar valores
from itertools import groupby
grupo = ['c', 'a', 'b', 'a', 'b', 'a', 'a', 'c']

novo_grupo = groupby(sorted(grupo)) # agrupamento ordenado
# novo_grupo = groupby(grupo) # agrupamento NÃO ordenado

for chave, agrupamento in novo_grupo:
    print(chave)
    print(list(agrupamento))

print('==============================================')


# Agrupar valores
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

ordenar_alunos = sorted(alunos, key=lambda a : a['nota']) # ordenar por 'nota' (antes de agrupar)
alunos_agrupados = groupby(ordenar_alunos, key=lambda a : a['nota']) # agrupar por 'nota'

# visualizar agrupamento
for chave, grupos in alunos_agrupados:
    print(chave)
    print(list(grupos))
    # for aluno in grupos:
    #      print(aluno)

# --------------------------------------------------------

# FILTRO 
'''
    A função filter() do Python é usada para filtrar elementos de uma sequência 
    com base em uma condição. A função recebe dois argumentos: uma função e uma 
    sequência. A função é aplicada a cada elemento da sequência e se ela retornar 
    True, o elemento é incluído no resultado.
'''

def filtro(numeros_pares):
  return numeros_pares % 2 == 0

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nova_lista_de_numeros_pares = filter(filtro, lista_de_numeros)

# Converte o iterador para uma lista
nova_lista_de_numeros_pares = list(nova_lista_de_numeros_pares)

# Imprime a lista de números pares
print(nova_lista_de_numeros_pares)

print('==============================================')

# filter é um filtro funcional
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# filter(função, iterável)
novos_produtos = filter(
    lambda produto: produto['preco'] > 100, # <==== chave
    produtos # <==== lista
)

print_iter(produtos)
print_iter(novos_produtos)

print('==============================================')

# # dados iniciais
cursos = [
    {
        "id" : 1,
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    {
        "id" : 2,
        "titulo": "Algoritmos e logica de programação",
        "aulas": 87,
        "horas": 67
    },
    {   
        "id" : 3,
        "titulo": "Programação linguagem Python",
        "aulas": 33,
        "horas": 47
    }
]

busca_id = 2
# filtro
filtrar_id = filter(lambda meu_id: meu_id['id'] == busca_id, cursos)
curso = dict(*filtrar_id)
print(curso)

# --------------------------------------------------------

# eliminar ultimo digito de um objeto dentro de uma lista

matricula = ['07/08/000.327/2023.']

# ELIMINAR ELEMENTO =============================
matricula_string = str(*matricula)
variavel_auxiliar = ''
matricula.clear()
for n, i in enumerate(matricula_string):

    if n == len(matricula_string)-1:
        break
    else:
        variavel_auxiliar += i
matricula.append(variavel_auxiliar)
variavel_auxiliar = ''
# ELIMINAR ELEMENTO =============================
print(matricula)

# --------------------------------------------------------

# eliminar espaço de um objeto dentro de uma lista

matricula = ['15 / 171 . 341 - 1']
# ELIMINAR ESPAÇO =============================
matricula_string = str(*matricula)
variavel_auxiliar = ''
matricula.clear()
for i in matricula_string:
    if i == ' ':
        ...
    else:
        variavel_auxiliar += i
matricula.append(variavel_auxiliar)
variavel_auxiliar = ''
# ELIMINAR ESPAÇO =============================
print(matricula)
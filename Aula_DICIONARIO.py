'''
Os métodos de dicionário em Python são funções que podem ser usadas para manipular dicionários. Eles são métodos porque operam em um objeto de dicionário específico, em oposição a funções, que operam em valores.

Alguns métodos de dicionário comuns incluem:

get(): Retorna o valor associado a uma chave especificada.
setdefault(): Define o valor associado a uma chave especificada, se a chave não existir.
pop(): Remove uma chave e seu valor associado do dicionário.
update(): Atualiza o dicionário com os valores de outro dicionário.
keys(): Retorna uma lista de todas as chaves do dicionário.
values(): Retorna uma lista de todos os valores do dicionário.
items(): Retorna uma lista de tuplas de chave-valor do dicionário.
clear(): Remove todos os itens do dicionário.
len(): Retorna o número de itens no dicionário.
copy - retorna uma cópia rasa (shallow copy)
copy.deepcopy() - retorna uma cópia profunda
popitem - Apaga o último item adicionado
'''

# criar dicionario
print('Criara dicionario')
a = dict(one=1, two=2, three=3)
print(a)
b = {'one': 1, 'two': 2, 'three': 3}
print(b)
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(c)
d = dict([('two', 2), ('one', 1), ('three', 3)])
print(d)
e = dict({'three': 3, 'one': 1, 'two': 2})
print(e)
f = dict({'one': 1, 'three': 3}, two=2)
print(f)
print(a == b == c == d == e == f)

# ---------------------------------------------------------------------------

# visualizar dicionario
print()
d = {'one': 1, 'two': 2, 'three': 3}
print(d)
print(list(d))
print(len(d))

# ---------------------------------------------------------------------------

# inserir dados em dicionário
print()
dados = {}
dados['Nome'] = 'Décio'
dados['Idade'] = 40
print(dados)
print(dados['Nome'])
print(dados['Idade'])
del dados['Idade'] # deletar "Idade" no dicionario
print(dados)

# ---------------------------------------------------------------------------

# ALTERAR "valor" e "chave" de dicionario
print()
dicionario = {"Nome": "Décio", "Sobre_Nome": "Aguiar"}
print(dicionario)
dicionario["Sobre_Nome"] = "Santana" # alterar valor
print(dicionario)
dicionario["Primeiro_Nome"] = dicionario.pop("Nome") # alterar chave
print(dicionario)
dicionario.update({
    "Sobre_Nome": "Santana de Aguiar",
    "Sexo": "Masculino"
})
print(dicionario)
dicionario.update(idade=41)
print(dicionario)

# ---------------------------------------------------------------------------

# acessar elementos do dicionario individualmente
print()
dados = dict(Nome='Décio', Idade=40, Sexo="M")
print(dados)
print(dados.keys())
print(dados.values())
print(dados.items())
print(dados['Sexo']) # se "Sexo" não existir dá erro no programa
print(dados.get('Nome', 'Não existe'))
print(dados.get('Cor')) # retorna valor padrão "None" caso não exista
print(dados.get('Cor', 'Não existe'))
print(dados.setdefault('Nome'))
print(dados.setdefault('Cor')) # retorna "None" caso não exista

print('==============================================')

# # acesso dicionario em lista por "for"
print()
dados = dict(Nome='Décio', Idade=40, Sexo="M")
for c in dados:
    print(f'{c=}')
for k in dados.keys(): # chave
    print(f'Chave = {k}')
for v in dados.values(): # valor
    print(f'Valor = {v}')
for k, v in dados.items(): # chave e valor
    print(f'{k} = {v}')

print('==============================================')

# acesso dicionario em lista
print()
dados1 = {'Nome':'Décio', 'Idade':40}
dados2 = dict(Nome='Luana', Idade=37)
dados3 = dict([('Nome', 'Ana'), ('Idade', 3)])
lista = [dados1, dados2, dados3]
print(lista)
print(lista[0])
print(lista[1]['Idade'])
print(f'{dados3["Nome"]}')
for x in lista:
    print(x['Nome'], end= '/')

# ---------------------------------------------------------------------------

# combinar duas ou mais sequências em uma única sequência de tuplas.
print()
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y) # empacota "(1, 4), (2, 5), (3, 6)"
print(list(zipped))
x2, y2 = zip(*zip(x, y))# desempacota "x2 = (1, 2, 3)", "y2 = (4, 5, 6)"
print(x2)
print(y2)
print(x == list(x2) and y == list(y2))

# ---------------------------------------------------------------------------
# COPIAR 
import copy
d0 = {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
d1 = d0 # aponta para o mesmo dicionario (não é copia real)
d2 = d1.copy() # copia rasa - 'l1' ainda é apontada (copia parcial)
d3 = copy.deepcopy(d1) # copia profunda - 'l1' é copia (copia total)

d1['c1'] = 111
d2['c1'] = 3333
d2['l1'][1] = 555555
d3['l1'][1] = 9999999

print(d0)
print(d1)
print(d2)
print(d3)

#----------------------------------------------------------------------------
# VER VALOR DICIONARIO POR CHAVE, VALOR OU AMBOS
teste = dict(C=2, A=4, D=1, B=3) # criar dicionario
print(f'{teste=}')
print(f'VALOR = {sorted(teste.values())}') # ver valor
print(f'CHAVE = {sorted(teste.keys())}') # ver cave
print(f'CHAVE = VALOR {sorted(teste.items())}') # ver chave e valor
for t in sorted(teste, reverse=True):
    print(f'{t} = {teste[t]}')

# ---------------------------------------------------------------------------
# ORDENAR DICIONARIO POR CHAVE
students = [{'letra': 'B', 'numero': 2}, {'letra': 'C', 'numero': 1}, {'letra': 'A', 'numero': 3}]
ordem = sorted(students, key=lambda a : a['numero'])
print(ordem)

# ORDENAR DICIONARIO POR CHAVE
students = [{'letra': 'B', 'numero': 2}, {'letra': 'C', 'numero': 1}, {'letra': 'A', 'numero': 3}]
ordem = sorted(students, key=lambda a : a['letra'])
print(ordem)

print('===========================================')

'''
    O itemgetter() é uma ferramenta útil para classificar itens de um objeto.
'''
# ORDENAR DICIONARIO POR CHAVE
from operator import itemgetter
students = [{'letra': 'B', 'numero': 2}, {'letra': 'C', 'numero': 1}, {'letra': 'A', 'numero': 3}]
ordem = sorted(students, key=itemgetter('numero')) # ordenar por numero 
print(ordem)

# ORDENAR DICIONARIO POR CHAVE
from operator import itemgetter
students = [{'letra': 'B', 'numero': 2}, {'letra': 'C', 'numero': 1}, {'letra': 'A', 'numero': 3}]
ordem = sorted(students, key=itemgetter('letra')) # ordenar por letra
print(ordem)

print('===========================================')

from operator import itemgetter # biblioteca
D = dict(C=2, A=4, D=1, B=3) # dicionario
L = [] # lista vazia
print(f'{D=}')
print(f'{L=}')


# ORDENAR POR CHAVE
L = sorted(D.items(), key=itemgetter(0)) # organiza dicionario em tupla dentro da lista por chave "key=itemgetter(0)"
print(f'Ordenado por Chave | {L=}')
for k, v in L:
    print(k, '=', v)


# ORDENAR POR VALOR
L = sorted(D.items(), key=itemgetter(1)) # organiza dicionario em tupla dentro da lista por valoe "key=itemgetter(1)"
print(f'Ordenado por Valor | {L=}')
for k, v in L:
    print(k, '=', v)

print('===========================================')

ordem = list(D.values()) # extrair dicionario "D" VALOR
ordem.sort() # ordenar
print(f'valor => {ordem=}')
ordem = list(D.keys()) # extrair dicionario "D" CHAVE
ordem.sort() # ordenar
print(f'chave => {ordem=}')
ordem = list(D.items()) # extrair dicionario "D" CHAVE & VALOR
ordem.sort() # ordenar
print(f'itens => {ordem=}')

#-------------------------------------------------------------------------------------------------------------

'''
    Cadastre em uma lista, dados de pessoas em dicionario
'''

from operator import itemgetter
dicionario = {}
lista = []
opcao = ''
while opcao != 'N':
    nome = input('Nome: ').strip().upper()
    while True:
        idade = input('Idade: ').strip()
        if idade.isnumeric() == True:
            dicionario[nome] = int(idade)
            break
        else:
            print('Caracter invalido!')
            print('Digite apenas valores numéricos.')
            print()

    while True:
        opcao = input(f'Quer continuar? [S/N] ').upper()
        if opcao == 'S':
            print()
            break
        else:
            if opcao == 'N':
                print()
                lista.append(dicionario.copy())
                break
            else:
                print(f'Opção invalida!')
                print(f'Digite "S" para CONTINUAR ou "N" para SAIR.')
print(lista)
lista = sorted(dicionario.items(), key=itemgetter(0))
print(lista)
for k, v in enumerate(lista):
    print(f'{k+1}º Nome: {v[0]}, Idade: {v[1]}')
lista = sorted(dicionario.items(), key=itemgetter(1))
print(lista)
for k, v in enumerate(lista):
    print(f'{k+1}º Idade: {v[1]}, Nome: {v[0]}')

# ------------------------------------------------------------------------
'''
    # Valor será reescrito em maiúsculo 
'''

# Dictionary Comprehension e Set Comprehension
produto = {'nome': 'Caneta Azul', 'preco': 2.5, 'categoria': 'Escritório'}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor # (FILTRO) retorna Treu ou False (isinstance(object, class))
    for chave, valor in produto.items()
    if chave != 'categoria' # (FILTRO) exclui categoria se existir 
}
print(dc)

# --------------------------------------------------------

# Operadores de união
dict1 = {"name": "Alice", "age": 25}
dict2 = {"occupation": "Software Engineer", "city": "New York"}

# Combina os dois dicionários em um único dicionário
combined_dict = dict1 | dict2

print(combined_dict)

# --------------------------------------------------------

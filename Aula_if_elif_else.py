
'''
    As estruturas condicionais permitem que o código seja executado de forma diferente, 
    dependendo do valor de uma expressão.
'''
x = "1"
if x == 1:
    print("Opção 1")
elif x == "1":
    if int(x) > 1:
        print("Opção 2")
    elif int(x) < 1:
        print("Opção 3")
    else:
        print("Opção 4")
if int(x) == 1:
    print("Opção 5")
else:
    print("Opção 6")


# ----------------------------------------------------------------------------
'''
    O operador ternário em Python é um operador condicional que pode ser usado para avaliar dois valores em uma única linha
    VERDADE if CONDIÇÃO else FALSO
    Exemplo: print('Sim' if 3 == 2 else 'Não')
    Resposta: Não
'''
x = 1
# 1ª escrita
if x == 1:
    print(f'{x} = 1')
else:
    print(f'{x} ≠ 1')

# 2ª escrita
if x == 1: print(f'{x} = 1')
else: print(f'{x} ≠ 1')

# 3ª escrita onde (expressão_verdade if condição else expressão_falso)
print(f'{x} = 1' if x == 1 else f'{x} ≠ 1')

# ----------------------------------------------------------------------------

"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None):
    if z == 0:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x=} {y=}', x + y)

soma(7, 9, 0)
soma(y=9, x=7)
# ----------------------------------------------------------------------------

"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 11 == 11
variavel = 'Verdade' if condicao else 'Falso'
print(f'\n{variavel}\n')
# ----------------------------------------------------------------------------

the_list = []
for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)
print(the_list)

# OU

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
print(the_list)


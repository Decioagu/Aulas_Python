# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
# Teste essa expressão em https://regex101.com/r/XDyL7q/1 (aula 11)

import re

texto = 'Este é um teste de expressões teste regulares. (Teste)'

# retorna se uma texto inicia com palavra pesquisada
print(re.match(r'Este', texto)) # OBS: r'string' = interpretada como uma string literal.

# retorna 1ª string pesquisada na expressões regulares
print(re.search(r'teste', texto)) # OBS: r'string' = interpretada como uma string literal.

# usada para pesquisar todas as ocorrências de uma expressões regulares
print(re.findall(r'teste', texto)) # OBS: r'string' = interpretada como uma string literal.

# realizar substituições baseadas em expressões regulares, manipulação de texto
# substitui todas as ocorrências de "teste" por "ABCD"
print(re.sub(r'teste', 'ABCD', texto)) # OBS: r'string' = interpretada como uma string literal.

'''
"re.compile()" compilar uma expressão regular em um objeto, 
que pode ser usado para realizar operações de correspondência como:
# re.match(); # re.search(); # re.findall(); # re.sub();
'''
complete = re.compile(r'teste')
print(complete.search(texto))
print(complete.findall(texto))
print(complete.sub('DEF', texto))

'''
re.match(r'palavra', texto, flaags=0)
re.search('palavra', texto, flags=0)
re.findall('palavra', texto, flags=0)
re.sub(r'palavra', 'substituto', texto, flags=0)

Onde:
# pattern é a expressão regular a ser pesquisada.
# string é a string na qual a expressão regular será pesquisada.
# flags é um valor opcional que pode ser usado para modificar o comportamento da pesquisa.

Valores possíveis para flags são:
# flags=re.A ou re.ASCII: correspondência somente código ASCII;
# flags=U ou re.UNICODE: faz com que a correspondência seja feita em Unicode.
# flags=re.I ou re.IGNORECASE:  ignorar maiúsculas e minúsculas;
# flags=re.L ou re.LOCALE: faz com que a correspondência dependa da localidade;
# flags=re.M ou re.MULTILINE: faz com que a correspondência seja feita em várias linhas;
# flags=re.S ou re.DOTALL: faz com que o ponto "." corresponda a qualquer caractere, incluindo quebras de linha.;
# flags=re.X ou re.VERBOSE: (permite que você separe visualmente seções lógicas e adicione comentários)
'''
print('===================================================================')

# finalizar frase apos linha em branco
import re

texto = """
Esta é uma linha com texto.
Esta é outra linha com texto.

Esta é uma linha vazia.
Esta é uma linha com texto.
"""

frase = ''

for linha in texto:
    frase += linha
    linhas_vazias = re.findall(r'\n\n', frase)
    if linhas_vazias:
        break

print(frase)

#-----------------------------------------------------------------------------

# Meta caracteres: \ | . ^ $ [] * + ? {} () \w \W \d \D \s \S \b \D
# OBS: r'string' = interpretada como uma string literal.
# \ = carácter de escapa para string
# | = OU
# . = substitui qualquer caractere (com exceção da quebra de linha)
# $ = corresponde ao termino de uma string
# ^ = corresponde ao início de uma string
# OBS: "^" pode ser usada como negação dentro de um conjunto exemplo: [^a-z] -> Negação

# []    = conjunto de caracteres
# [a-z] = conjunto de caracteres letras minusculas
# [A-Z] = conjunto de caracteres letras maiúscula
# [0-9] = conjunto de numerais

# * = 0 ou 'n'= o caractere escolhido pode se repetir 0 ou 'n' vezes
# + = 1 ou 'n'= o caractere escolhido pode se repetir 1 ou 'n' vezes
# ? = 0 ou 1  = o caractere escolhido pode se repetir 0 ou 1 na palavra

# {10} = caractere escolhido repete somente 10 vezes
# {min, max} = caractere escolhido pode se repetir mínimo ou máximo
# {5,10} = caractere escolhido repete 5 até 10 vezes
# {10,} = caractere escolhido pode se repetir 10 ou 'n' vezes
# {,10} = caractere escolhido pode se repetir 0 ou 10

# () = captura palavra desejada ou sequencia de caracteres especifico no grupo
# (?:"expressão regular") = não captura de parênteses em um grupo
# (?P<tag>)"expressão regular"(?P=tag) = grupo nomeado

# \w = [a-zA-ZÀ-ú_] corresponde a um caractere alfanumérico
# \W = not [a-zA-ZÀ-ú_] corresponde a um caractere "NÃO" alfanumérico
# \d = [0-9] corresponde a um caractere numeral
# \D = [^0-9] corresponde a um caractere "NÃO" numeral
# \s = [\n\r\f\t] corresponde a um caractere de espaço em branco
# \S = [^\n\r\f\t] corresponde a um caractere que "NÃO TENHA" espaço em branco
# \b = '\bfles\b' define "inicio" ou "fim" de um conjunto de caractere desejado 
# \B = "NÃO" define inicio ou fim de um conjunto de caractere desejado

'''
Exemplo: 

Para verificar se uma string contém uma "data":
data = ' Hoje é dia 25/01/2024.'
print (re.findall(r"\d{2}.\d{2}.\d{4}", data))

Para encontrar todos os "e-mails" em uma string:
email = 'Seu e-mail é: decioagu@gmail.com'
print (re.findall(r"[a-zA-Z0-9._+-]+\@[a-zA-Z0-9-]+\.[a-zA-Z]+", email))

Para encontrar todas as "tags HTML" em uma string:
html = ' <p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> '
print (re.findall(r"<[^>]+>", html))

Para verificar se uma string contém uma "cpf":
cpf = 'Meu cpf é: 147.852.963-12'
print(re.findall(r'\d+.\d+.\d+.\d+', cpf))
'''

#-----------------------------------------------------------------------------

# Demostração:

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Vem, Veem, Veeem, Veeemm, Veeemmm, Veeeemmmm"!
'''
# | OU
print(re.findall(r'João|joão|Maria', texto))

# . Qualquer caractere (com exceção da quebra de linha)
print(re.findall(r'João|Maria|adu.....s', texto)) 

# [] conjunto de caracteres
print(re.findall(r'[Jj]oão|[Mm]aria', texto))

# [a-z] "ranger" conjunto de caracteres com letras minusculas 
print(re.findall(r'[a-z]aria', texto))

# [a-zA-Z0-9] conjunto de caracteres com letras minusculas, maiúscula, numeral 
print(re.findall(r'[a-zA-Z0-9]aria|[a-zA-Z0-9]oão', texto))

# flags=re.I ou re.IGNORECASE=  ignorar maiúsculas e minúsculas;
print(re.findall(r'jOãO|mAriA', texto, flags=re.IGNORECASE))

# OBS: aplica-se ao carácter à esquerda
# []= conjunto de caracteres
# + = 1 ou 'n'= o caractere escolhido pode se repetir 1 ou 'n' vezes
# flags=re.I ou re.IGNORECASE=  ignorar maiúsculas e minúsculas;
print(re.findall(r'j[o]+ão+', texto, flags=re.I))

# OBS: aplica-se ao carácter à esquerda
# {1,} = caractere escolhido pode se repetir 1 ou 'n' vezes
# flags=re.I ou re.IGNORECASE=  ignorar maiúsculas e minúsculas;
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))

# OBS: aplica-se ao carácter à esquerda
# {3} = caractere escolhido repete somente 3 vezes
# {1,2} = caractere escolhido repete 1 até 2 vezes
# flags=re.I ou re.IGNORECASE=  ignorar maiúsculas e minúsculas;
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
# OBS: print [Veeem, Veeemm, Veeemm] "resultado não desejado"

print('===================================================================')
# Execício 1 Substituir palavras em texto

import re

texto1 = 'João ama ser amado, jooÃoo ama.'
print(re.findall(r'ama[od]{0,2}', texto1, flags=re.I))

# OBS: aplica-se ao carácter à esquerda
# {1,} = caractere escolhido pode se repetir 1 ou 'n' vezes
# flags=re.I ou re.IGNORECASE=  ignorar maiúsculas e minúsculas;
# substitui todas as ocorrências de "jo{1,}ão{1,}" por "Felipe"
print(re.sub(r'jo{1,}ão{1,}', 'Felipe', texto1, flags=re.I))
print('===================================================================')

# Execício 2 de seleção HTML:

# []= conjunto de caracteres
# {min, max} = caractere escolhido pode se repetir mínimo ou máximo
# \ = carácter de escapa para string
# . = substitui qualquer caractere (com exceção da quebra de linha)
# * = 0 ou 'n'= o caractere escolhido pode se repetir 0 ou 'n' vezes
# + = 1 ou 'n'= o caractere escolhido pode se repetir 1 ou 'n' vezes
# ? = 0 ou 1  = o caractere escolhido pode se repetir 0 ou 1 na palavra

import re

texto2 = ' <p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> '

print(re.findall(r'<[pdiv]{1,3}>.', texto2))
# ['<p>F', '<p>E', '<p>Q', '<div><']

print(re.findall(r'<[pdiv]{1,3}>.+', texto2))
# ['<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> ']

print(re.findall(r'<[pdiv]{1,3}>.*', texto2))
# ['<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> ']

print(re.findall(r'<[pdiv]{1,3}>.?', texto2))
# ['<p>F', '<p>E', '<p>Q', '<div><']

print(re.findall(r'<[pdiv]{1,3}>.+?', texto2))
# ['<p>F', '<p>E', '<p>Q', '<div><']

print(re.findall(r'<[pdiv]{1,3}>.*?', texto2))
# ['<p>', '<p>', '<p>', '<div>']

print(re.findall(r'<[pdiv]{1,3}>.+<\/[pdiv]{1,3}>', texto2))
# ['<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div>']

print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto2))
# ['<p>Frase 1</p>', '<p>Eita</p>', '<p>Qualquer frase</p>']

print('===================================================================')

# Execício 3 nome:

# | = OU
# . = substitui qualquer caractere (com exceção da quebra de linha)
# () = captura palavra desejada ou sequencia de caracteres especifico
# flags=re.I ou re.IGNORECASE=  ignorar maiúsculas e minúsculas;

import re

texto3 = 'Décio décio Decio decio DéCiO dÉcIo DeCiO dEcIo'

print(re.findall(r'(decio)', texto3))
# ['decio']

print(re.findall(r'(decio)', texto3, flags=re.I))
# ['Decio', 'decio', 'DeCiO', 'dEcIo']

print(re.findall(r'(Décio)', texto3))
# ['Décio']

print(re.findall(r'(Décio)', texto3, flags=re.I))
# ['Decio', 'decio', 'DeCiO', 'dEcIo']

# # | = OU
print(re.findall(r'(décio|decio)', texto3, flags=re.I))
# ['Décio', 'décio', 'Decio', 'decio', 'DéCiO', 'dÉcIo', 'DeCiO', 'dEcIo']

# . = substitui qualquer caractere (com exceção da quebra de linha)
print(re.findall(r'(d.cio)', texto3, flags=re.I))
# ['Décio', 'décio', 'Decio', 'decio', 'DéCiO', 'dÉcIo', 'DeCiO', 'dEcIo']

print('===================================================================')

# Execício 4 de seleção HTML:

# {min, max} = caractere escolhido pode se repetir mínimo ou máximo
# . = substitui qualquer caractere (com exceção da quebra de linha)
# + = 1 ou 'n'= o caractere escolhido pode se repetir 1 ou 'n' vezes
# ? = 0 ou 1  = o caractere escolhido pode se repetir 0 ou 1 na palavra
# \ = carácter de escapa para string
# []    = conjunto de caracteres
# () = captura palavra desejada ou sequencia de caracteres especifico

# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
'''
Grupo retrovisor:
\1 \2 \3 corresponde acesso ao grupo
# 1()     \1
# 1() 2()  \1 \2
# 1(2()) 3()   \1 \2 \3
# (?P<tag>) (?P=tag) grupo nomeado 
'''
# (?:"expressão regular") = não captura de parênteses em um grupo

import re

texto4 = ' <p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div></div> '
# () = captura palavra desejada ou sequencia de caracteres especifico
print(re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto4)) 

# [('p', 'Frase 1'), ('p', 'Eita'), ('p', 'Qualquer frase')]
print(re.findall(r'<([dpiv]{1,3})>(.+?)<\/\2>', texto4))
# []

tags1 =  re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\3>)', texto4)
print(tags1)

for tag in tags1:
    um, dois, tres = tag
    print(um) # (um, dois, tres) valores diferentes
    # <p>Frase 1</p>
    # <p>Eita</p>
    # <p>Qualquer frase</p>

# OBS: o sinal "?:" no \3 grupo ignora print
tags2 =  re.findall(r'(<([dpiv]{1,3})>(?:.+?)<\/\2>)', texto4)
print(tags2) 

tags3 = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto4)
print(tags3)
print('===================================================================')

# Execício 5 encontrar palavra que inicia com:

# ^ = corresponde ao início de uma string
# flags=re.I ou re.IGNORECASE=  ignorar maiúsculas e minúsculas;

import re

text = "The quick brown fox jumps over the lazy dog"

match = re.search(r"^the", text, flags=re.I)

print(re.findall(r"^the", text, flags=re.I))
# ['The']

if match:
    print(match.group())
    # The

print('===================================================================')

# Execício 6 eliminar palavra que inicia com:
# ^ = corresponde ao início de uma string

import re

texto = "Meu nome é Décio Santana de Aguiar"

novo_texto = re.sub(r"Meu nome é", r"", texto)

print(novo_texto)
#  Décio Santana de Aguiar
print('===================================================================')

# Execício 7 CPF:

# () = captura palavra desejada ou sequencia de caracteres especifico
# \d = [0-9] corresponde a um caractere numeral
# ? = 0 ou 1  = o caractere escolhido pode se repetir 0 ou 1 na palavra
# (?:"expressão regular") = não captura de parênteses em um grupo
# ^ = corresponde ao início de uma string
# + = 1 ou 'n'= o caractere escolhido pode se repetir 1 ou 'n' vezes
# {10} = caractere escolhido repete somente 10 vezes
# [a-z] = conjunto de caracteres letras minusculas
# [0-9] = conjunto de numerais
# \w = [a-zA-ZÀ-ú_] corresponde a um caractere alfanumérico
# \W = not [a-zA-ZÀ-ú_] corresponde a um caractere "NÃO" alfanumérico
# \d = [0-9] corresponde a um caractere numeral
# \D = [^0-9] corresponde a um caractere "NÃO" numeral
# \s = [\n\r\f\t] corresponde a um caractere de espaço em branco

import re

cpf = 'a 147.852.963-12 a'

print(re.findall(r'((?:\d{3}.){2}\d{3}-\d{2})', cpf))
print(re.findall(r'[^a-z\s]+', cpf))
# ['147.852.963-12']

print(re.findall(r'[^a-z]+', cpf))
# [' 147.852.963-12 ']

print(re.findall(r'[^\w]+', cpf))
print(re.findall(r'[\W]+', cpf))
# [' ', '.', '.', '-', ' ']

print(re.findall(r'[^0-9]+', cpf))
print(re.findall(r'[^\d]+', cpf))
print(re.findall(r'[\D]+', cpf))
# ['a ', '.', '.', '-', ' a']

print('===================================================================')
# Execício 8 CPF:

# () = captura palavra desejada ou sequencia de caracteres especifico
# \d = [0-9] corresponde a um caractere numeral
# ? = 0 ou 1  = o caractere escolhido pode se repetir 0 ou 1 na palavra
# (?:"expressão regular") = não captura de parênteses em um grupo
# ^ = corresponde ao início de uma string
# . = substitui qualquer caractere (com exceção da quebra de linha)
# + = 1 ou 'n'= o caractere escolhido pode se repetir 1 ou 'n' vezes
# {10} = caractere escolhido repete somente 10 vezes
# [a-z] = conjunto de caracteres letras minusculas
# [0-9] = conjunto de numerais
# \w = [a-zA-ZÀ-ú_] corresponde a um caractere alfanumérico
# \W = not [a-zA-ZÀ-ú_] corresponde a um caractere "NÃO" alfanumérico
# \d = [0-9] corresponde a um caractere numeral
# \D = [^0-9] corresponde a um caractere "NÃO" numeral
# \s = [\n\r\f\t] corresponde a um caractere de espaço em branco

import re

cpf = '''
104.509.587-81 a098.877.632-72a
a098.877.632-72a
642.567.232-09
042767232-08
642.567.23209
72356478173
'''
print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
print(re.findall(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}', cpf))
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf)) # "?:" NÃO IMPRIME GRUPO SELECIONADO
print(re.findall(r'[0-9]{3}[0-9]{3}[0-9]{3}[0-9]{2}', cpf))
print(re.findall(r'[0-9\.]+...', cpf))
print(re.findall(r'[0-9\.]+-..', cpf))
print(re.findall(r'[0-9\.]+-.[19]', cpf))
print(re.findall(r'[^a-z]+', cpf))
print(re.findall(r'[^0-9]+', cpf))
print(re.findall(r'[0-9].+-+[0-9]+', cpf))
print(re.findall(r'\d+.+-+\d+', cpf))
print(re.findall(r'\d+.*-?\d+', cpf))
print(re.findall(r'\d+.\d+.\d+.\d+', cpf))
print('===================================================================')

# Execício 9 CPF:

# $ = corresponde ao termino de uma string
# ^ = corresponde ao início de uma string
# []    = conjunto de caracteres
# {10} = caractere escolhido repete somente 10 vezes
# () = captura palavra desejada ou sequencia de caracteres especifico no grupo
# . = substitui qualquer caractere (com exceção da quebra de linha)
# \ = carácter de escapa para string
# + = 1 ou 'n'= o caractere escolhido pode se repetir 1 ou 'n' vezes
# (?:"expressão regular") = não captura de parênteses em um grupo


import re

cpf1 = '147.852.963-12'
cpf2 = 'a147.852.963-12'
cpf3 = '147.852.963-12a'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf1))
# ['147.852.963-12']
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf2))
# []
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf3))
# []
print(re.findall(r'[0-9]+', cpf1))
# ['147', '852', '963', '12']
print(re.findall(r'[^0-9]+', cpf1)) # (?:) = não captura
# ['.', '.', '-']
print(re.findall(r'[^0-9]+', cpf2)) # (?:) = não captura
# ['a', '.', '.', '-']
print(re.findall(r'[^0-9]+', cpf3)) # (?:) = não captura
# ['.', '.', '-', 'a']
print(re.findall(r'[0-9$]+', cpf1))
# ['147', '852', '963', '12']
print(re.findall(r'[0-9.$]+', cpf2))
# ['147.852.963', '12']
print(re.findall(r'[0-9-$]+', cpf3))
# ['147', '852', '963-12']

print('===================================================================')

# Execício 10 uso de borda de palavras:

# \b = '\bfles\b' define "inicio" ou "fim" de um conjunto de caractere desejado
# \B = "NÃO" define inicio ou fim de um conjunto de caractere desejado

import re

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'\b\d{2}.*\d{4}\b', texto, flags=re.I))
# ['10 de janeiro de 1970']
print(re.findall(r'sua\b.*faz\b', texto, flags=re.I))
# ['sua esposa, ainda faz']
print(re.findall(r'nunc\B', texto, flags=re.I))
# ['nunc']
print(re.findall(r'nunc\b', texto, flags=re.I))
# []
print(re.findall(r'nunca\B', texto, flags=re.I))
# []
print(re.findall(r'nunca\b', texto, flags=re.I))
# ['nunca']

#-----------------------------------------------------------------------------
# Execício flags "re.MULTILINE":

# flags=re.M ou re.MULTILINE: faz com que a correspondência seja feita em várias linhas
# {10} = caractere escolhido repete somente 10 vezes
# \d = [0-9] corresponde a um caractere numeral
# ^ = corresponde ao início de uma string
# $ = corresponde ao termino de uma string

import re

texto = '''
131.768.460-53
055.123.060-50
955.123.060-90
'''

print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))

print('===================================================================')
# Execício flags "re.MULTILINE":

# flags=re.I ou re.IGNORECASE:  ignorar maiúsculas e minúsculas;
# flags=re.S ou re.DOTALL: faz com que o ponto "." corresponda a qualquer caractere, incluindo quebras de linha.;
# ^ = corresponde ao início de uma string
# $ = corresponde ao termino de uma string
# . = substitui qualquer caractere (com exceção da quebra de linha)
# * = 0 ou 'n'= o caractere escolhido pode se repetir 0 ou 'n' vezes
# | = OU

import re

texto2 = '''O João gosta de folia 
E adora ser amado'''
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))

#-----------------------------------------------------------------------------

# Exercício lookahead (olhe para frente) e lookbehind (olhar para trás):
'''
Lookahead e lookbehind são funcionalidades avançadas de expressões regulares em Python 
que permitem verificar se um padrão existe "antes" (lookbehind) ou "depois" (lookahead) 
da posição atual na string, sem consumir nenhum caractere, apenas checa a sub_expressão.

1. Lookahead: verifica se um padrão existe "depois" da posição atual na string, é útil para:
# Validar formatos de strings
# Extrair informações de strings
# Implementar algoritmos de busca que consideram o contexto
Sintaxe:
# (?=sub_expressão): Positivo (verifica se a sub-expressão existe)
# (?!sub_expressão): Negativo (verifica se a sub-expressão não existe)

2. Lookbehind: verifica se um padrão existe "antes" da posição atual na string, é útil para:
# Validar formatos de strings
# Extrair informações de strings
# Implementar algoritmos de busca que consideram o contexto
Sintaxe:
# (?<=sub_expressão): Positivo (verifica se a sub-expressão existe)
# (?<!sub_expressão): Negativo (verifica se a sub-expressão não existe)
'''

import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# Positive lookahead (olhe para frente)
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))
# Negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# Positive lookahead (olhe para frente)
pprint(re.findall(r'(?=.*inactive).+', texto))
# Negative lookahead (olhe para frente)
pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive lookbehind (olhar para trás)
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# Negative lookbehind (olhar para trás)
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

# Positive lookbehind (olhar para trás)
pprint(re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))
# Negative lookbehind (olhar para trás)
pprint(re.findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))

#-----------------------------------------------------------------------------
# Exercício validação de IP:

import re

ip_reg_exp = re.compile(
    r'^'  # Começa com
    r'(?:'
    r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'){3}'  # Sequência de 3 digitos e um ponto repete 3x
    r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])'
    r'$',  # Termina com
    flags=0
)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'

    print(ip, ip_reg_exp.findall(ip))

#-----------------------------------------------------------------------------

# Exercício CPF eliminar captura de sequencia numérica (negative lookahead):
# aula 11
import re
from pprint import pprint

regex = re.compile(
    r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
    flags=re.MULTILINE
)

test_str = ("698.547.520-54\n"
            "060.235.190-16\n"
            "683.134.960-96\n"
            "899.344.730-62\n"
            "103.778.870-21\n"
            "721.478.580-30\n"
            "366.310.090-14\n"
            "794.289.350-26\n"
            "190.259.410-01\n"
            "000.000.000-01\n"
            "900.000.000-00\n\n"
            "000.000.000-00\n"
            "111.111.111-11\n"
            "222.222.222-22\n"
            "333.333.333-33\n"
            "444.444.444-44\n"
            "555.555.555-55\n"
            "666.666.666-66\n"
            "777.777.777-77\n"
            "888.888.888-88\n"
            "999.999.999-99\n\n"
            )

pprint(regex.findall(test_str))

#-----------------------------------------------------------------------------
# Exercício validar número de telefone (lookahead):
# https://regex101.com/r/DfXYXM/1/

import re

regexp = re.compile(r'^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4})$', flags=re.M)

texto = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''

for telefone in regexp.findall(texto):
    print(telefone)

#-----------------------------------------------------------------------------
# Exercício validação de número inteiro ou ponto flutuante:
# https://regex101.com/r/wjfSus/1/

import re

string = '''
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1

Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
'''

def is_float(string):
    return bool(re.search(r'^[+-]?\d+(?:\.\d+)?$', string))


def is_int(string):
    return bool(re.search(r'^[+-]?\d+$', string))


while True:
    numero = input('Digite um número: ')

    if is_int(numero):
        numero = int(numero)
        print(f'O número {numero} foi convertido para int')
        continue

    if is_float(numero):
        numero = float(numero)
        print(f'O número {numero} foi convertido para float')
        continue

#-----------------------------------------------------------------------------
# Exercício validação de email:

# Básica 1 => https://regex101.com/r/9s4bgv/1/
# ^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$


# Básica 2 => https://regex101.com/r/mH4ChC/2/
# ^[^\s@<>\(\)[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(?:[\.\-_]\w+)*$


# Norma (rfc 5322) => https://regex101.com/r/fkxI15/1/
# ^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$



emails = """
Valid email addresses
o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br
simple@example.com
very.common@example.com
disposable.style.email.with+symbol@example.com
other.email-with-hyphen@example.com
fully-qualified-domain@example.com
user.name+tag+sorting@example.com
x@example.com
example-indeed@strange-example.com
example@s.example
a@a.com.br
mailhost!username@example.org
user%example.com@example.org
email@example.com
firstname.lastname@example.com
email@subdomain.example.com
firstname+lastname@example.com
email@123.123.123.123
"email"@example.com
1234567890@example.com
email@example-one.com
_______@example.com
email@example.name
email@example.museum
email@example.co.jp
firstname-lastname@example.com


Invalid email addresses
Abc.example.com
<aqui-te-um@email-pra-validar.com.br>
A@b@c@example.com
a"b(c)d,e:f;g<h>i[j\k]l@example.com
just"not"right@example.com
this is"not\allowed@example.com
this\ still\"not\\allowed@example.com
plainaddress
#@%^%#$@#$@#.com
@example.com
<email@example.com>
email.example.com
email@example@example.com
.email@example.com
email.@example.com
email..email@example.com
あいうえお@example.com
email@example
email@-example.com
email@example..com
Abc..123@example.com
”(),:;<>[\]@example.com
just”not”right@example.com
this\ is"really"not\allowed@example.com
"""
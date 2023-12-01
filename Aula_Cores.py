# TABELA DE CORES

'''
    Para adicionar cores em texto em Python, você pode usar as sequências de escape ANSI. 
    Essas sequências são usadas para controlar as cores do texto exibido no terminal.
'''
limpar = '\033[m'
preto = '\033[30m'
vermelho = '\033[31m'
verde = '\033[32m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
ciano = '\033[36m'
cinza = '\033[37m'
vermelho_claro = '\033[91m'
verde_claro = '\033[92m'
amarelo_claro = '\033[93m'
azul_claro = '\033[94m'
rosa = '\033[95m'
ciano_claro = '\033[96m'
branco = '\033[97m'
sub = '\033[4m'
neg = '\033[1m'
inv = '\033[7m'

'''
Os tipos de formatação possíveis são:
Negrito: 1
Sublinhado: 4
Invertido: 7
'''
print("\033[31mOlá, mundo!\033[0m\n")
print("\033[1;31mOlá, mundo!\033[0m\n")
print("\033[4;31mOlá, mundo!\033[0m\n")
print("\033[7;31mOlá, mundo!\033[0m\n")
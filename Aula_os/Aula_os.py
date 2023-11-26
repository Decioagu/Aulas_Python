# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.



import os

os.system('clear') # limpa o terminal
os.system('echo "Hello world"') # repete o texto como um print()
#-----------------------------------------------------------------------------------------------

# exibir rota
'''
  A função em Python é usada para retornar o caminho absoluto de um arquivo ou diretório. 
  Essa função usa um objeto semelhante a um caminho como um argumento e retorna uma versão 
  normalizada do caminho.
'''
# OBS: novos caminhos estão armazenados em memória
import os

# local
current_dir = os.path.abspath('.')
print(current_dir) # resposta = P:\REPOSITORIO\PUBLICO\PYTHON_UDEMY

# arquivo
file_path = os.path.abspath('data.json')
print(file_path) # resposta = P:\REPOSITORIO\PUBLICO\PYTHON_UDEMY\data.json

# pasta
dir_path = os.path.abspath('BANCO')
print(dir_path) # resposta = P:\REPOSITORIO\PUBLICO\PYTHON_UDEMY\BANCO
#-----------------------------------------------------------------------------

# pasta
'''
A função os.path.join() é uma função embutida do Python que é usada para concatenar 
vários segmentos de caminho em um único caminho. Os segmentos de caminho são 
especificados como uma sequência de strings, separadas por vírgulas.

A função os.path.join() usa o separador de caminho da plataforma como delimitador 
para concatenar os segmentos de caminho. No Windows, o separador de caminho é "\", 
enquanto no Unix e no macOS é "/".
'''

import os

# unir o texto conforme sistema operacional
caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
print(os.path.dirname(caminho)) # exibir diretório
print(os.path.basename(caminho)) # exibir arquivo

print('<==========================================================>')

# separar diretório do arquivo
diretorio, arquivo = os.path.split(caminho)
print(diretorio) # exibir diretório
print(arquivo) # exibir arquivo

print('<==========================================================>')

# separar nome do arquivo de sua extensão
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(nome_arquivo)
print(extensao_arquivo)

print('<==========================================================>')

print(os.path.exists('Z:\REPOSITORIO\PUBLICO\PYTHON_UDEMY\Aula_os')) # caminho existe (True ou False)
print(os.path.abspath('.')) # mostrar caminho atual onde programa é executado
 
print('<==========================================================>')

#aula 283
'''
    A função listdir() em Python é usada para listar o conteúdo de um diretório. 
    Ela retorna uma lista de strings contendo os nomes dos arquivos e diretórios 
    no diretório especificado.

    A função isdir() do módulo os.path do Python é usada para verificar se um caminho 
    especificado é um diretório existente ou não. Ela retorna True se o caminho for um 
    diretório existente e False caso contrário.
'''

import os

caminho = os.path.join('/REPOSITORIO', 'PUBLICO', 'PYTHON_UDEMY', 'Aula_os', 'exemplo')
# caminho = os.path.join('/REPOSITORIO', 'PUBLICO', 'PYTHON_UDEMY', 'Aula_os')

for pasta in os.listdir(caminho): 
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for itens in os.listdir(caminho_completo_pasta):
        print('  ', itens)
    
print('<==========================================================>')

# Ver todas as rotas, pastas e arquivos existentes no "caminho" desaguando 
import os
from itertools import count

caminho = os.path.join('/REPOSITORIO', 'PUBLICO', 'PYTHON_UDEMY', 'Aula_os')
contador = count()

for rota, pastas, arquivos in os.walk(caminho):
    meu_contador = next(contador)
    print(meu_contador, 'Rota:', rota)

    for _pasta_ in pastas:
        print('  ', meu_contador, 'Pasta:', _pasta_)

    for _arquivo_ in arquivos:
        caminho_completo_arquivo = os.path.join(rota, _arquivo_)
        print('  ', meu_contador, 'Arquivo:', caminho_completo_arquivo)
        
        # os.unlink(caminho_completo_arquivo) # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
#-----------------------------------------------------------------------------------------------

# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
import math
import os
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1024) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


caminho = os.path.join('/REPOSITORIO' , 'PUBLICO', 'PYTHON_UDEMY', 'Aula_os', 'exemplo', 'pasta1') 
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print('  ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))
        # NÃO FAÇA ISSO (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)
#-----------------------------------------------------------------------------------------------

# criar pasta, copiar arquivo e mover arquivo
import os
import shutil

HOME = os.path.expanduser('~') # resposta => C:\Users\decio
TESTE_PY = os.path.join(HOME, 'TESTE_PY') # unir "C:\Users\decio" com "\TESTE_PY" 
# OBS: (pasta deve esta previamente criada)
NOVA_PASTA = os.path.join(TESTE_PY, 'NOVA_PASTA') # já existe
NOVA_PASTA_1 = os.path.join(TESTE_PY, 'NOVA_PASTA_1') # caminho (novo)
NOVA_PASTA_2 = os.path.join(TESTE_PY, 'NOVA_PASTA_2') # caminho (novo)
NOVA_PASTA_3 = os.path.join(TESTE_PY, 'NOVA_PASTA_3')  # caminho (novo)
NOVA_PASTA_4 = os.path.join(TESTE_PY, 'NOVA_PASTA_4')  # caminho (novo)


# caminhos
print(HOME)
print(TESTE_PY)
print(NOVA_PASTA)

os.makedirs(NOVA_PASTA_1, exist_ok=True) # cria nova pasta (caminho)
os.makedirs(NOVA_PASTA_2, exist_ok=True) # cria nova pasta (caminho)
os.makedirs(NOVA_PASTA_3, exist_ok=True) # cria nova pasta (caminho)
os.makedirs(NOVA_PASTA_4, exist_ok=True) # cria nova pasta (caminho)

''' se arquivo solicitado já existir na nova pasta ocorrerá uma erro de exceção '''

# copia um arquivo para uma nova pasta
shutil.copy(NOVA_PASTA + '/SUN.docx', NOVA_PASTA_1) 

# copia um arquivo para uma nova pasta (também usado para alterar nomes)
shutil.copy(NOVA_PASTA + '/SUN.docx', NOVA_PASTA_1 + '/NOVO_SUN.docx') 

# move o arquivo para nova pasta com novo nome
shutil.move(NOVA_PASTA_1 + '/NOVO_SUN.docx', NOVA_PASTA_2)

# move a pasta para outra pasta (também usado para alterar nomes)
shutil.move(NOVA_PASTA_3 , NOVA_PASTA_1)

'''
    # shutil.rmtree(pasta)
    A função é usada para excluir recursivamente uma árvore de diretórios inteira, 
    incluindo todos os arquivos e subdiretórios dentro do caminho especificado.
    OBS: caso pasta não exista haverá erro de exceção utilize "ignore_errors=True"

'''
shutil.rmtree(NOVA_PASTA_4, ignore_errors=True)

# cria uma nova pasta com todos os arquivos
shutil.copytree(NOVA_PASTA, NOVA_PASTA_4)

# apagar arquivo
os.unlink(NOVA_PASTA_4 + '/SUN.docx')

# exibir rotas/pastas/arquivos
for rota, pastas, arquivos in os.walk(TESTE_PY):
    print ('Rota:', rota)

    for _pasta_ in pastas:
        print('  ', 'Pasta:', _pasta_)

    for _arquivo_ in arquivos:
        caminho_completo_arquivo = os.path.join(rota, _arquivo_)
        print('  ', 'Arquivo:', caminho_completo_arquivo)
#-----------------------------------------------------------------------------------------------

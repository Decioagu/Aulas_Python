'''
    # CSV (Comma Separated Values - Valores separados por vírgulas)
    # É um formato de arquivo que armazena dados em forma de tabela, onde cada
    # linha representa uma linha da tabela e as colunas são separadas por vírgulas.
    # Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
    # plataformas, como por exemplo, para importar ou exportar dados para uma
    # planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
    # Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
    # editor de texto ou em uma planilha eletrônica.
    # Um exemplo de um arquivo CSV pode ser:
    # Nome,Idade,Endereço
    # Luiz Otávio,32,"Av Brasil, 21, Centro"
    # João da Silva,55,"Rua 22, 44, Nova Era"
    # A primeira linha do arquivo define os nomes das colunas da, enquanto as
    # linhas seguintes contêm os valores das linhas, separados por vírgulas.
    # Regras simples do CSV
    # 1 - Separe os valores das colunas com um delimitador único (,)
    # 2 - Cada registro deve estar em uma linha
    # 3 - Não deixar linhas ou espaços sobrando
    # 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.
'''

#-----------------------------------------------------------------------------------------------
'''
    # newline=''
    É um argumento que não deseja que nenhum caractere de nova linha seja usado para separar
    as linhas do arquivo CSV. Isso significa que cada linha do arquivo CSV será escrita em 
    uma única linha, sem quebras de linha.
'''
import csv

with open('data1.csv', 'w', newline='' , encoding='utf8') as arquivo_csv:
    writer = csv.writer(arquivo_csv) # modo de gravação
    writer.writerow(['nome', 'idade', 'cidade']) # escrever uma linha
    writer.writerow(['Alice', 30, 'Rio de Janeiro']) # escrever uma linha
    writer.writerow(['Bob', 25, 'São Paulo']) # escrever uma linha

print('<==========================================================>')

# escrever arquivo CSV (como dicionário)
import csv

with open('data2.csv', 'w', newline='' , encoding='utf8') as arquivo_csv:
    dados = ['nome', 'idade', 'cidade']
    writer = csv.DictWriter(arquivo_csv, fieldnames=dados) # modo de gravação
    writer.writeheader() # método para escrever a linha de cabeçalho de um arquivo CSV (fieldnames=)
    writer.writerow({'nome': 'Alice', 'idade': 30, 'cidade': 'Seattle'}) # escrever uma linha
    writer.writerow({'nome': 'Bob', 'idade': 25, 'cidade': 'New York'}) # escrever uma linha
#-----------------------------------------------------------------------------------------------

# ler arquivo CSV (como dicionário)
import csv
from pathlib import Path

# caminho do arquivo
CAMINHO_CSV = Path(__file__).parent / 'data1.csv' 

# exibir CSV
with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.DictReader(arquivo) # exibir como dicionario

    for linha in leitor:
        print(linha)

print('<==========================================================>')

# ler arquivo CSV (como lista)
import csv
from pathlib import Path

# caminho do arquivo
CAMINHO_CSV = Path(__file__).parent / 'data2.csv' 

# exibir CSV
with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.reader(arquivo) # exibir como lista

    for linha in leitor:
        print(linha)
#-----------------------------------------------------------------------------------------------

# escrever arquivo CSV (como dicionário)

import csv
from pathlib import Path

# caminho do arquivo
CAMINHO_CSV = Path(__file__).parent / 'aula180.csv'

# lista com dicionários
lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

# escrever
with open(CAMINHO_CSV, 'w', newline='' , encoding='utf8') as arquivo:
    nome_colunas = lista_clientes[0].keys() # chaves dos dicionários na lista
    escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)  # modo de gravação
    escritor.writeheader()# método para escrever a linha de cabeçalho de um arquivo CSV (fieldnames=)

# =============== OU ================
    # for cliente in lista_clientes:
    #     escritor.writerow(cliente) # escrever linha de dados
# ===================================
    escritor.writerows(lista_clientes) # escrever todas as linhas de dados

#-----------------------------------------------------------------------------------------------

# escrever arquivo CSV (como dicionário)

import csv
from pathlib import Path

# caminho do arquivo
CAMINHO_CSV = Path(__file__).parent / 'aula181.csv'

lista_clientes = [
    ['Luiz Otávio', 'Av 1, 22'],
    ['João Silva', 'R. 2, "1"'],
    ['Maria Sol', 'Av B, 3A'],
]
with open(CAMINHO_CSV, 'w', newline='' , encoding='utf8') as arquivo:
    nome_colunas = ['Nome', 'Endereço'] # chave para coluna
    escritor = csv.writer(arquivo) # modo de gravação

    escritor.writerow(nome_colunas) # escrever chave para coluna

# =============== OU ================
    for cliente in lista_clientes:
        escritor.writerow(cliente) # escrever linha de dados
# ===================================
    # escritor.writerows(lista_clientes) # escrever todas as linhas de dados
#-----------------------------------------------------------------------------------------------


# openpyxl - criando uma planilha do Excel (Workbook e Worksheet)
# Instalação necessária: pip install openpyxl
# Documentação: https://openpyxl.readthedocs.io/en/stable/

'''
    "openpyxl" é uma biblioteca open-source escrita em Python utilizada para ler, 
    escrever e manipular arquivos do Microsoft Excel. Ela oferece uma forma fácil 
    e eficiente de automatizar tarefas relacionadas a planilhas.

    Principais funcionalidades do openpyxl:

    Leitura e escrita de arquivos Excel:
        # Suporta formatos .xlsx, .xlsm, .xltx e .xltm.
        # Carregamento e salvamento de planilhas do Excel.
    Manipulação de planilhas:
        # Criação, exclusão e renomeação de planilhas.
        # Acesso e iteração sobre células, linhas e colunas.
        # Adição, remoção e atualização de dados nas células.
    Formatação de planilhas:
        # Aplicação de estilos de fonte, cor, bordas e preenchimento.
        # Alinhamento de texto e números.
        # Formatação condicional de células.
    Fórmulas e funções:
        # Inserção de fórmulas do Excel nas células.
        # Acesso e modificação de fórmulas existentes.
        # Utilização de funções do Excel dentro das fórmulas. 
    Gráficos e tabelas dinâmicas:
        # Criação de diversos tipos de gráficos a partir dos dados da planilha.
        # Inserção de tabelas dinâmicas para análise e filtragem de dados.
'''

from pathlib import Path
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet # tipagem para VS Code

# caminho do arquivo
ROOT_FOLDER = Path(__file__).parent
WORKBOOK_PATH = ROOT_FOLDER / 'estudantes.xlsx'

workbook = Workbook() # criar arquivo vazio do Excel

# Criando os cabeçalhos
worksheet: Worksheet = workbook.active # tipagem para VS Code
worksheet.cell(1, 1, 'Nome')    # (linha, coluna, valor)
worksheet.cell(1, 2, 'Idade')   # (linha, coluna, valor)
worksheet.cell(1, 3, 'Nota')    # (linha, coluna, valor)

# lista de objetos
estudantes = [
    # nome      idade nota
    ['João',    14,   5.5],
    ['Maria',   13,   9.7],
    ['Luiz',    15,   8.8],
    ['Alberto', 16,   10],
]

# ================================ TESTE DIDÁTICO ============================== 
for i, estudante_linha in enumerate(estudantes, start=2): # "start" manipula inicio da linha
    for j, estudante_coluna in enumerate(estudante_linha, start=1):
        worksheet.cell(i, j, estudante_coluna) # (linha, coluna, valor)
        print(f'linha = {i} |',f'coluna = {j} |', f'salvar = {estudante_coluna}')

# ==================================== OU ======================================= 

# adicionar lista de objetos
for student in estudantes:
    worksheet.append(student) # adicionar como lista
    print(student)
# ===============================================================================

workbook.save(WORKBOOK_PATH) # salvar arquivo
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from pathlib import Path


'''
pip install reportlab

O que é canvas?
O módulo canvas contém a classe Canvas, que representa uma “folha em branco”
para desenhar conteúdos: texto, formas geométricas, imagens, etc.
'''

caminho_do_arquivo = Path(__file__).parent # ver caminho do arquivo executado

# Cria o documento
pdf = SimpleDocTemplate(f"{caminho_do_arquivo}/teste_02.pdf", pagesize=A4)

# Dados da tabela
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Maria', '30', 'São Paulo'],
    ['João', '25', 'Rio de Janeiro'],
    ['Ana', '28', 'Curitiba']
]

# Cria a tabela
tabela = Table(dados)

# Estilo da tabela
style = TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ('GRID', (0,0), (-1,-1), 1, colors.black)
])

# Aplica o estilo
tabela.setStyle(style) 

# Adiciona a tabela ao PDF
pdf.build([tabela])

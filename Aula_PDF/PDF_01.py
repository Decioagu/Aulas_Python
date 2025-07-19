from reportlab.pdfgen import canvas
from pathlib import Path


'''
pip install reportlab

O que é canvas?
O módulo canvas contém a classe Canvas, que representa uma “folha em branco”
para desenhar conteúdos: texto, formas geométricas, imagens, etc.
'''

caminho_do_arquivo = Path(__file__).parent # ver caminho do arquivo executado

# Cria o PDF e define o nome do arquivo
# c = canvas.Canvas("arquivo.pdf", pagesize=(largura, altura))
c = canvas.Canvas(f"{caminho_do_arquivo}/teste_01.pdf")

# Adiciona texto no PDF
# drawString(x, y, texto): escreve texto em (x, y).
c.drawString(50, 750, "Pagina 1 - Olá, este é um PDF gerado pelo ReportLab!")

c.showPage()  # Finaliza a página atual e inicia uma nova

# Adiciona texto no PDF
c.drawString(10, 300 , "Pagina 2 - Olá, este é um PDF gerado pelo ReportLab!")

# Salva o arquivo
c.save()



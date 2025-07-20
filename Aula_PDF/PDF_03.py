from weasyprint import HTML
from pathlib import Path

'''
pip install weasyprint

O WeasyPrint é uma biblioteca em Python que transforma HTML e CSS em PDFs e arquivos de imagem (PNG).
Ele é muito usado quando você quer gerar relatórios, faturas, etiquetas, 
certificados ou qualquer documento em PDF a partir de páginas web.
📄 - Entrada: HTML + CSS
📄 - Saída: PDF ou PNG

WeasyPrint: depende de bibliotecas externas do sistema 
(como o GTK/Pango/Cairo) que não vêm instaladas por padrão no Windows.

https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases/download/2022-01-04/gtk3-runtime-3.24.31-2022-01-04-ts-win64.exe

'''

caminho_do_arquivo = Path(__file__).parent # ver caminho do arquivo executado

html = """
<html>
  <body>
    <h1 style="color:blue;">Olá WeasyPrint!</h1>
  </body>
</html>
"""

HTML(string=html).write_pdf(f"{caminho_do_arquivo }/teste_03.pdf")
print("✅ PDF gerado com sucesso!")


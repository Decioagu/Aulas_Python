# (aulas 327 até 330)
'''
O PyPDF2 é uma biblioteca Python que permite manipular arquivos PDF. 
Ele pode ser usado para realizar uma variedade de tarefas, incluindo:

    # Extrair texto de PDFs: O PyPDF2 pode ser usado para extrair o texto de um PDF 
    em um formato de texto legível. Isso pode ser útil para converter PDFs em documentos 
    de texto ou para extrair informações de PDFs.

    # Concatenar PDFs: O PyPDF2 pode ser usado para concatenar dois ou mais PDFs em um 
    único PDF. Isso pode ser útil para combinar vários documentos PDF em um único documento.

    # Dividir PDFs: O PyPDF2 pode ser usado para dividir um PDF em dois ou mais PDFs menores. 
    Isso pode ser útil para dividir um documento PDF grande em partes menores.

    # Adicionar ou remover páginas de PDFs: O PyPDF2 pode ser usado para adicionar 
    ou remover páginas de um PDF. Isso pode ser útil para personalizar um documento PDF 
    ou para remover páginas indesejadas.

    # Converter PDFs: O PyPDF2 pode ser usado para converter PDFs em outros formatos de 
    arquivo, como imagens, documentos de texto ou arquivos de código.

    # Link: https://pypdf2.readthedocs.io/en/3.0.0/ (documentação)
    # Ative seu ambiente virtual
    # pip install pypdf2
    # pip install PyPDF2[image]
'''

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# caminho do arquivo
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'pdfs_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20231208.pdf'

PASTA_NOVA.mkdir(exist_ok=True) # criar nova pasata

readerPDF = PdfReader(RELATORIO_BACEN) # ler arquivo em PDF

# ================ CONTAR QUNTIDADE DE PAGINAS DO PDF ================ 
print(len(readerPDF.pages)) # quantidde de paginas

# ======================== LER TEXTO EM PDF ========================== 
for page in readerPDF.pages:
    print(page.extract_text()) # ler paginas
    print('<==================================================>')

# ======================== LER TEXTO EM PDF ========================== 
page0 = readerPDF.pages[0] # ler pagina [0]
page1 = readerPDF.pages[1] # ler pagina [1]
print('\n<===================================================================>')
print(page0.extract_text()) # obtér o texto do documento 
print('<===================================================================>')
print(page1.extract_text()) # obtér o texto do documento 
print('<===================================================================>\n')

# ================ EXTRAIR IMAGEM DE "PDF" E SALVAR EM ARQUIVO "PNG" ================ 
page0 = readerPDF.pages[0] # ler pagina [0]

imagem = page0.images # lista de objetos de imagem extraídos do arquivo PDF.

# ver lista de imagens
for e, i in enumerate(imagem):
    print(f'Imagem {e} =', i)

# Extrair imagens na lista => File(name=X24.png, data: 42.4 kB)
escolhe_imagem = page0.images[3] # Imagem ? = File(name=?.png, data: ? kB)

# SALVAR imagem escolhida em arquivo com extensão PNG
with open(PASTA_NOVA / escolhe_imagem.name, 'wb') as arquivo: # local pasta
    arquivo.write(escolhe_imagem.data) # escrever (salvar imagem)
print('===================================================================\n')

# ================ COPIAR ARQUIVO PDF E RENOMEAR ================    

# CRIAR replica 
writerPDF = PdfWriter() # escrever arquivo em PDF

for enum, i in enumerate(readerPDF.pages):

    writerPDF.add_page(readerPDF.pages[enum]) # adiciona uma nova página em PDF

    # criar novo arquivo com nome diferente 
    with open(PASTA_NOVA / f'replica_page.pdf', 'wb') as arquivo:
        writerPDF.write(arquivo) # escrever
print('===================================================================\n')

# ================ SEPARAR PAGINAS DO PDF POR PAGINA INDIVIDUAL ================
# page0 = readerPDF.pages[0] # ler pagina [0]
# page1 = readerPDF.pages[1] # ler pagina [1]

# # CRIAR separa paginas (1)
# writerPDF = PdfWriter() # escrever arquivo em PDF

# writerPDF.add_page(page1) # adiciona uma nova página em PDF
# # criar novo arquivo 
# with open(PASTA_NOVA / f'nova_page1.pdf', 'wb') as arquivo:
#     writerPDF.write(arquivo) #

# writerPDF.add_page(page0) # adiciona uma nova página em PDF
# with open(PASTA_NOVA / f'nova_page2.pdf', 'wb') as arquivo:
#     writerPDF.write(arquivo)

# =================================== OU ========================================

# CRIAR separa paginas (2)
for enum, i in enumerate(readerPDF.pages):

    writerPDF = PdfWriter() # escrever arquivo em PDF

    writerPDF.add_page(readerPDF.pages[enum]) # adiciona uma nova página em PDF
    with open(PASTA_NOVA / f'nova_page{enum}.pdf', 'wb') as arquivo:
        writerPDF.write(arquivo) # escrever
print('===================================================================\n')

# ================= UNIR ARQUIVO EM PDF EM UM ÚNICO ARQUIVO============

mergerPDF = PdfMerger() # unir arquivo em PDF

# caminho e nome de arquivos
unir = [PASTA_NOVA / "nova_page1.pdf", PASTA_NOVA /"nova_page0.pdf"]

for pdf in unir:
    mergerPDF.append(pdf) # unir na ordem inversa

mergerPDF.write(PASTA_NOVA / "inverter_unir.pdf") # caminho e arquivo PDF
mergerPDF.close() # fechar arquivo

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger

# caminho do arquivo
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'pdfs_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20231208.pdf'

PASTA_NOVA.mkdir(exist_ok=True) # criar nova pasata

readerPDF = PdfReader(RELATORIO_BACEN) # ler arquivo em PDF


# ================ SEPARAR PAGINAS DO PDF POR PAGINA INDIVIDUAL ================
# ================= UNIR ARQUIVO EM PDF EM UM ÚNICO ARQUIVO============

mergerPDF = PdfMerger() # unir arquivo em PDF

# caminho e nome de arquivos
unir = [PASTA_NOVA / "nova_page1.pdf", PASTA_NOVA /"nova_page0.pdf"]

for pdf in unir:
    mergerPDF.append(pdf) # unir na ordem inversa

mergerPDF.write(PASTA_NOVA / "inverter_unir.pdf") # caminho e arquivo PDF
mergerPDF.close() # fechar arquivo
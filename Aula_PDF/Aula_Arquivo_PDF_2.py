
'''
pip install PyMuPDF


PyMuPDF é uma biblioteca Python de alto desempenho para extração de dados, 
análise, conversão e manipulação de documentos PDF (e outros).

https://pypi.org/project/PyMuPDF/
https://pymupdf.readthedocs.io/en/latest/
'''
import fitz
from pathlib import Path

# caminho do arquivooo
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'pdfs_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'rio_de_janeiro_2024-01-10_completo.pdf'

doc = fitz.open(RELATORIO_BACEN) # abrir documento

out = open(PASTA_NOVA / "meu_texto.txt", "wb") # criar arquivo em texto

for page in doc: # iterar as páginas do documento
	text = page.get_text().encode("utf8") # obter texto simples (em UTF-8)
	out.write(text) # escrever o texto da página
	
out.close()
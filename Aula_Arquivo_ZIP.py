# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile

'''
 O "módulo zipfile" fornece várias funções para manipular arquivos zip, incluindo 
 a função extractall(), que pode ser usada para descompactar todos os arquivos 
 de um arquivo zip para um diretório especificado.
'''
import zipfile

arquivo_zip = "arquivo.zip"
arquivo_destino = "destino/arquivo.txt"

with zipfile.ZipFile(arquivo_zip, "r") as zip:
    zip.extract("arquivo.txt", diretorio_destino)

#-------------------------------------------------------------------

import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'arquivo_compactado_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'arquivo_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'arquivo_descompactado'

# limpar diretórios
shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True) # apagar pasta (delete)
Path.unlink(CAMINHO_COMPACTADO, missing_ok=True) # apagar arquivo (delete)
shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True) # apagar pasta (delete)
shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True) # apagar pasta (delete)

# raise Exception() #  exceção é um evento

# Cria o diretório para a aula
CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

# função para criar arquivo de texto
def criar_arquivos(qtd: int, zip_dir: Path): # (quantidade, pasta)
    for i in range(qtd):
        i += 1
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(5, CAMINHO_ZIP_DIR) # instanciar função "criar_arquivos"

# Criando um zip e adicionando arquivos
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR): # (rotas, pastas, arquivos)
        for file in files:
            # print(file)
            # método para gravar arquivos em um arquivo ZIP.
            zip.write(os.path.join(root, file), file) # (intrusão(rota, arquivo), nome arquivo) 

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)
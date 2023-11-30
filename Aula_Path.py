'''
    Path é um módulo incluído na biblioteca padrão do Python que fornece ferramentas 
    para manipular caminhos de arquivos e diretórios. Ele oferece uma interface abrangente 
    e consistente para trabalhar com caminhos, independentemente do sistema operacional
    em que o Python está sendo executado.

    O módulo Path fornece várias funções úteis para manipular caminhos, incluindo:

    # Path.join(): Combina vários componentes de caminho em um único caminho.
    # Path.parents: Retorna uma lista de diretórios ancestrais do caminho.
    # Path.is_file(): Verifica se o caminho aponta para um arquivo.
    # Path.is_dir(): Verifica se o caminho aponta para um diretório.
    # Path.exists(): Verifica se o caminho existe no sistema de arquivos.
    # Path.mkdir(): Cria um diretório no caminho.
    # Path.rename(): Renomeia o caminho.
    # Path.unlink(): Exclui o arquivo ou diretório apontado pelo caminho.
'''

from pathlib import Path

print()
caminho_do_projeto = Path()
print(caminho_do_projeto.absolute()) # ver caminho da pasta

print('<==========================================================>')

caminho_do_arquivo = Path(__file__) # ver caminho do arquivo executado
print(caminho_do_arquivo)

# exibir pasta acima utilize método ".parent"  
print(caminho_do_arquivo.parent)
print(caminho_do_arquivo.parent.parent)
print(caminho_do_arquivo.parent.parent.parent)

print('<==========================================================>')

# OBS: novos caminhos estão armazenados em memória
nova_pasta = caminho_do_arquivo.parent / 'meu' # OBS: acrescentar barra gera novo caminho
print(nova_pasta / 'novo') # OBS: acrescentar barra gera novo caminho

print('<==========================================================>')

print(Path.home() / 'novo') # ver caminho da pasta usuário
print()

#-----------------------------------------------------------------------------------------------

# criar pasta
from pathlib import Path
import shutil

nova_pasta = Path() / 'nova_pasta'
# criar pasta nova_pasta.
nova_pasta.mkdir(exist_ok=True) # exist_ok=True para não da erro se existir pasta

# criar pasta outra_pasta
outra_pasta = Path() / 'nova_pasta' / 'outra_pasta'
outra_pasta.mkdir(exist_ok=True)
# shutil.rmtree(nova_pasta) # apagar pasta
#-----------------------------------------------------------------------------------------------

# criar arquivo
from pathlib import Path

'''
    O método , definido na classe  do módulo , é usado para criar um arquivo
    ou atualizar a data e a hora de modificação de um arquivo existente.
'''

novo_arquivo = Path() / 'nova_pasta' / 'outra_pasta' / 'teste123.txt'
novo_arquivo.touch()  # criar arquivo
novo_arquivo.write_text('Décio Santana de Aguiar') # adicionar texto (Windows => encoding='utf8')
print(novo_arquivo.read_text()) # ler arquivos
print(novo_arquivo.is_file()) # é arquivo?
print(novo_arquivo.is_dir()) # é pasta?
print(novo_arquivo.exists()) # existe?
print(novo_arquivo.absolute()) # caminho
# novo_arquivo.unlink() # apaga o texto
#-----------------------------------------------------------------------------------------------

# criar arquivo
import shutil
from pathlib import Path

# Caminhos para pasta
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_DIR = CAMINHO_RAIZ / 'pasta_de_arquivos_txt'


# limpar diretórios caso exista
shutil.rmtree(CAMINHO_DIR, ignore_errors=True) # apagar pasta (delete)

# Cria o diretório para a aula
CAMINHO_DIR.mkdir(exist_ok=True)

# função para criar arquivo de texo
def criar_arquivos(qtd: int, zip_dir: Path): # (quantidade, pasta)
    for i in range(qtd):
        i += 1
        texto = 'arquivo_%s' % i # Nº arquivos
        with open(zip_dir / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)

criar_arquivos(5, CAMINHO_DIR) # instanciar função "criar_arquivos"
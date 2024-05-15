# criar pasta, copiar arquivo e mover arquivo
import os
import shutil

HOME = os.path.expanduser('~') # resposta => C:\Users\decio
print(HOME)
TESTE_PY = os.path.join(HOME, 'TESTE_PY') # unir "C:\Users\decio" com "\TESTE_PY" 
# OBS: (pasta deve esta previamente criada)
NOVA_PASTA = os.path.join(TESTE_PY, 'NOVA_PASTA') # já existe
NOVA_PASTA_1 = os.path.join(TESTE_PY, 'NOVA_PASTA_1') # caminho (novo)
NOVA_PASTA_2 = os.path.join(TESTE_PY, 'NOVA_PASTA_2') # caminho (novo)
NOVA_PASTA_3 = os.path.join(TESTE_PY, 'NOVA_PASTA_3')  # caminho (novo)
NOVA_PASTA_4 = os.path.join(TESTE_PY, 'NOVA_PASTA_4')  # caminho (novo)


# caminhos
print(HOME)
print(TESTE_PY)
print(NOVA_PASTA)

os.makedirs(NOVA_PASTA_1, exist_ok=True) # cria nova pasta (caminho)
os.makedirs(NOVA_PASTA_2, exist_ok=True) # cria nova pasta (caminho)
os.makedirs(NOVA_PASTA_3, exist_ok=True) # cria nova pasta (caminho)
os.makedirs(NOVA_PASTA_4, exist_ok=True) # cria nova pasta (caminho)

''' OBS: se arquivo solicitado já existir na nova pasta ocorrerá uma erro de exceção '''

# copia um arquivo para uma nova pasta
shutil.copy(NOVA_PASTA + '/SUN.docx', NOVA_PASTA_1) 

# copia um arquivo para uma nova pasta (também usado para alterar nomes)
shutil.copy(NOVA_PASTA + '/SUN.docx', NOVA_PASTA_1 + '/NOVO_SUN.docx')

# alterar nomes
shutil.copy(NOVA_PASTA_1 + '/NOVO_SUN.docx', NOVA_PASTA_1 + '/SUPER_SUN.docx') 

# move o arquivo para nova pasta com novo nome ()
shutil.move(NOVA_PASTA_1 + '/NOVO_SUN.docx', NOVA_PASTA_4)

# move a pasta para outra pasta (também usado para alterar nomes)
shutil.move(NOVA_PASTA_3 , NOVA_PASTA_1)

'''
    # shutil.rmtree(pasta)
    A função é usada para excluir recursivamente uma árvore de diretórios inteira, 
    incluindo todos os arquivos e subdiretórios dentro do caminho especificado.
    OBS: caso pasta não exista haverá erro de exceção utilize "ignore_errors=True"

'''
shutil.rmtree(NOVA_PASTA_4, ignore_errors=True) # apagar pasta (delete)

# cria uma nova pasta com todos os arquivos
shutil.copytree(NOVA_PASTA, NOVA_PASTA_4)

# apagar arquivo (delete)
os.unlink(NOVA_PASTA_4 + '/SUN.docx')

# exibir rotas/pastas/arquivos
for rota, pastas, arquivos in os.walk(TESTE_PY):
    print ('Rota:', rota)

    for _pasta_ in pastas:
        print('  ', 'Pasta:', _pasta_)

    for _arquivo_ in arquivos:
        caminho_completo_arquivo = os.path.join(rota, _arquivo_)
        print('  ', 'Arquivo:', caminho_completo_arquivo)
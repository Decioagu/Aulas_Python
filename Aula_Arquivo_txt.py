# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# aula 185 até 188
'''
    Especificar a codificação UTF-8 ao abrir um arquivo é importante para garantir que o 
    conteúdo do arquivo seja lido ou escrito corretamente. Isso é especialmente importante 
    se o arquivo contém caracteres de idiomas diferentes do inglês. Apenas no Windows.

    OBS: todo arquivo.txt aberto deve ser fechado apos seu uso para não haver erro.
'''
arquivo = open('aula.txt', 'w', encoding='utf8') # Abre o arquivo "myfile.txt" para leitura
arquivo.write('Bem vindo!') # Escrever texto no arquivo
arquivo.close() # Fecha o arquivo

#-----------------------------------------------------------------------------------------------

import os
caminho_arquivo = 'aula.txt'

'''
    caminho_arquivo = "Z:\\REPOSITORIO\PUBLICO\\PYTHON_UDEMY\\teste\\'aula116.txt'"
    arquivo = open(caminho_arquivo, 'w') # abrir
    arquivo.close() # fechar
'''
# escrever arquivo
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo: # with (abre e fecha)
    arquivo.write('linha1\n') # escrever no arquivo
    arquivo.write('linha2\n') # escrever no arquivo
    arquivo.writelines(
        ('linha3\n', 'linha4\n', 'linha5\n')
    )
    print(arquivo.seek(0,0)) # cursor posição inicial 
    print(arquivo.read()) # ler o arquivo
    
#-----------------------------------------------------------------------------------------------

# escrever no final do arquivo
with open(caminho_arquivo, 'a', encoding='utf8') as arquivo: # with (abre e fecha)
    arquivo.writelines(
        ('linha6\n', 'linha7\n', 'linha8\n')
    )
    ''' 
        WINDOWS:
        Erro na acentuação do arquivo.txt utilizar :
        with open(caminho_arquivo, 'a', encoding='utf8') as arquivo:
    '''
    arquivo.write('Atenção\n')   
    
#-----------------------------------------------------------------------------------------------

# ler arquivo
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: # with (abre e fecha)
    print(arquivo.read()) # ler o arquivo
    print(arquivo.seek(0,0)) # cursor posição inicial 
    print('Ler linha')
    print(arquivo.readline(), end='') # ler o arquivo
    print(arquivo.readline(), end='') # ler o arquivo
    print(arquivo.readline(), end='') # ler o arquivo
    print(arquivo.readline())
   
    print('Ler linhas')
    arquivo.seek(0, 0) # cursor posição inicial 
    for linha in arquivo.readlines():
        print(linha, end='')

# apagar arquivo
# os.remove(caminho_arquivo)

# apagar arquivo
# os.unlink(caminho_arquivo)

# renomear arquivo ou mover para outra local
os.rename(caminho_arquivo, 'arquivo.txt')

#-----------------------------------------------------------------------------------------------

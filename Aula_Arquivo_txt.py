# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# 'w': Escrita apenas. Apaga todo o conteúdo existente.
# 'a': Escrita no final. Preserva o conteúdo existente.
# 'r': Leitura somente. Erro se o arquivo não existir.
# 'w+': Leitura e escrita. Apaga o conteúdo e cria se necessário.
# 'a+': Leitura e escrita. Escreve sempre no final, mesmo com seek().
# 'r+': Leitura e escrita. Não apaga o conteúdo, mas não cria o arquivo.
# 'x': Criação exclusiva. Erro se o arquivo já existir.
# 'x+': Criação exclusiva com leitura e escrita. Erro se o arquivo já existir.
# 'b': Modo binário. Pode ser combinado com outros modos (ex: 'rb', 'wb', 'ab, 'xb').
# 't': Modo texto (padrão). Combinado com outros modos (ex: 'rt', 'wt', 'at', 'xt').

# Context manager "-" with (abre e fecha)
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
arquivo = open('aula.txt', 'w', encoding='utf8') # Abre o arquivo "aula.txt" para escrita
arquivo.write('Bem vindo!') # Escrever texto no arquivo
arquivo.close() # Fecha o arquivo
arquivo = open('aula.txt', 'a', encoding='utf8') # Abre o arquivo "aula.txt" para escrita
arquivo.write('\nAdição!') # Escrever texto no arquivo
arquivo.close() # Fecha o arquivo
arquivo = open('aula.txt', 'r', encoding='utf8') # Abre o arquivo "aula.txt" para leitura
print(arquivo.read()) # ler o arquivo
arquivo.close() # Fecha o arquivo
#-----------------------------------------------------------------------------------------------

# escrever arquivo com "with" não é necessario o uso de "arquivo.close()"
with open('aula.txt', 'w+', encoding='utf8') as arquivo: # with (abre e fecha)
    arquivo.write('linha1\n') # escrever no arquivo
    arquivo.write('linha2\n') # escrever no arquivo
    arquivo.writelines(
        ('linha3\n', 'linha4\n', 'linha5\n')
    )
    print(arquivo.seek(0,0)) # cursor posição inicial 
    print(arquivo.read()) # ler o arquivo
    
#-----------------------------------------------------------------------------------------------


'''
    caminho_arquivo = "Z:\\REPOSITORIO\PUBLICO\\PYTHON_UDEMY\\teste\\'aula116.txt'"
    arquivo = open(caminho_arquivo, 'w') # abrir
    arquivo.close() # fechar
'''
import os
caminho_arquivo = 'aula.txt' # caminho do arquivo

# escrever no final do arquivo
with open(caminho_arquivo, 'a+', encoding='utf8') as arquivo: # with (abre e fecha)
    arquivo.writelines(
        ('linha6\n', 'linha7\n', 'linha8\n')
    )
    ''' 
        WINDOWS:
        Erro na acentuação do arquivo.txt utilizar :
        with open(caminho_arquivo, 'a', encoding='utf8') as arquivo:
    '''
    arquivo.write('Atenção\n')
    arquivo.seek(0)
    print(arquivo.read()) # ler o arquivo   
    
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

# escrita em binário
with open('dados.bin', 'a+b') as f:
    f.write(b'\x01\x02\x03')  # escreve no final
    f.seek(0)                 # volta ao início para ler
    conteudo = f.read()
    print(conteudo)
'''
Exceções Comuns ao Manipular Arquivos .txt em Python
Ao trabalhar com arquivos .txt em Python, diversas exceções podem surgir. 
Compreender e lidar com essas exceções é crucial para garantir a robustez e 
confiabilidade do seu código.

1. Erro de Permissão:
    # OSError: [Errno 13] Permission denied: Permissão negada para acessar ou 
    modificar o arquivo. Verifique se o script possui as permissões necessárias 
    e se o arquivo não está bloqueado.
    # FileNotFoundError: [Errno 2] No such file or directory: Arquivo não encontrado. 
    Certifique-se de que o nome do arquivo e o caminho estejam corretos.

2. Erros de Leitura/Escrita:
    # IOError: [Errno 28] No space left on device: Sem espaço em disco. 
    Libere espaço no disco ou utilize um arquivo menor.
    # EOFError: EOF when reading from empty file: Fim de arquivo inesperado 
    durante a leitura. Verifique se o arquivo está vazio ou corrompido.

3. Erros de Formato:
    # ValueError: invalid literal for int(): Tentativa de converter um valor não 
    numérico para um inteiro. Verifique se os dados do arquivo estão no formato correto.
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb5 in position 0: 
    Erro de decodificação de caracteres. Certifique-se de que o arquivo esteja 
    codificado na codificação correta (por exemplo, UTF-8).

4. Manipulação Inadequada:
    # TypeError: not a seekable object: Tentativa de buscar em um objeto 
    não pesquisável. Verifique se o objeto é um arquivo válido.
    # AttributeError: 'str' object has no attribute 'seek': 
    Tentativa de usar um método de arquivo em uma string. 
    Certifique-se de estar acessando o objeto arquivo correto.

'''
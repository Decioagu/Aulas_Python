# Usando subprocess para executar e comandos externos
# subprocess é um módulo do Python para executar
# processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usando subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stderr -> Redirecionam saída, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entradas e saídas serão tratadas como texto
# e automaticamente codificadas ou decodificadas com o conjunto
# de caracteres padrão da plataforma (geralmente UTF-8).
# - shell -> Se True, terá acesso ao shell do sistema. Ao usar
# shell (True), recomendo enviar o comando e os argumentos juntos.
# - executable -> pode ser usado para especificar o caminho
# do executável que iniciará o subprocesso.
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificação de caracteres do Windows pode ser
# diferente. Tente usar cp1252, cp852, cp850 (ou outros). Linux e
# mac, use utf_8.
# Comando de exemplo:
# Windows: ping 127.0.0.1
# Linux/Mac: ping 127.0.0.1 -c 4

'''

O subprocess é um módulo Python que permite executar programas externos 
e comandos de shell e interagir com eles. Ele fornece funções para criar novos 
processos, enviar e receber dados de/para os processos, e esperar por sua execução.

Principais Funções do subprocess:

Popen(args, *, stdin=None, stdout=None, stderr=None, ...): 
* Cria um novo processo filho e executa o comando especificado.

run(args, *, stdin=None, stdout=None, stderr=None, ...): 
* Executa o comando especificado e espera sua conclusão.

check_output(args, *, stdin=None, stderr=None, ...): 
* Executa o comando especificado e retorna sua saída padrão como bytes.

call(args, *, stdin=None, stdout=None, stderr=None, ...): 
* Executa o comando especificado e retorna seu código de saída.
'''

import subprocess
import sys

# sistema operecional
system = sys.platform 
print(system)

# sys.platform = linux, linux2, darwin (MAC)
cmd = ['ping', '127.0.0.1', '-c', '4']
encod = 'utf_8' # texto

# sys.platform = win32 (Windows)
if system == "win32":
    cmd = ['ping', '127.0.0.1']
    encod = 'cp850' # texto

# executar
proc = subprocess.run(
    cmd, capture_output=True,
    text=True,
    encoding=encod,
    shell=True
)

 
# print(proc.args)
# print(proc.stderr)
print(proc.stdout)
# print(proc.returncode)
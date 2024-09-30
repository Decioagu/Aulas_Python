
import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
'''
É útil quando se deseja manter a estrutura do projeto organizada:
    - sys.path.append(...) - Adiciona um novo caminho ao sys.path.
    - os.path.abspath(...) converte esse caminho em um caminho absoluto.
    - os.path.join(..., '..') sobe um nível na estrutura de diretórios (para o diretório pai).
    - os.path.dirname(__file__) retorna o diretório do arquivo atual.
'''
from config.conf import fala
fala()
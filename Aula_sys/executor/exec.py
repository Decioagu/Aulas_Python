
import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulo.meu_modulo import impotar_modulo
impotar_modulo()


'''
É útil quando se deseja manter a estrutura do projeto organizada:
    - os.path.dirname(__file__) retorna o diretório do arquivo atual.
    - os.path.join(..., '..') sobe um nível na estrutura de diretórios (para o diretório pai).
    - sys.path.append(...) - Adiciona um novo caminho ao sys.path.
    - os.path.abspath(...) converte esse caminho em um caminho absoluto.

- # Modelo 1:
- import sys
- import os
- sys.path.append(os.path.abspath(os.path.dirname(__file__)))
- # Adiciona ao sys.path o próprio diretório onde o script está sendo executado (__file__).

- # Modelo 2:
- import sys
- import os
- sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
- # Adiciona o diretório pai (diretório acima do diretório onde o script está) ao sys.path.

projeto/
├── principal.py
├── modulo_auxiliar.py
└── subdiretorio/
    └── outro_modulo.py
Se (principal.py) usar o Modelo 1, ele poderá importar (modulo_auxiliar.py) diretamente.
Se (principal.py) usar o Modelo 2, ele poderá importar (outro_modulo.py) de subdiretorio/.
'''
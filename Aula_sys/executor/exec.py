
import sys
import os

# Adicionar o caminho do diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modulo.meu_modulo import impotar_modulo
impotar_modulo()


'''
# Modelo 1:
- import sys
- import os
- sys.path.append(os.path.abspath(os.path.dirname(__file__)))
- from modulo_auxiliar import MINHA_FUNÇÃO
# sys.path.append(): permitindo que módulos localizados diretório (pasta).
# os.path.abspath(): Converte o caminho relativo para um caminho absoluto.
# os.path.join(, '..'): Mover para nível 
# os.path.dirname(__file__): Informa diretório atual


# Modelo 2:
- import sys
- import os
- sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
- from outro_modulo import MINHA_FUNÇÃO
# sys.path.append(): permitindo que módulos localizados diretório (pasta).
# os.path.abspath(): Converte o caminho relativo para um caminho absoluto.
# os.path.join(, '..'): Mover para nível 
# os.path.dirname(__file__): Informa diretório atual
# , '..': Aponta para pasta fora do diretório atual

projeto/
├── subdiretorio 1/
├   └── principal.py
├   └── modulo_auxiliar.py
├── subdiretorio 2/
├   └── outro_modulo.py

Se (principal.py) usar o Modelo 1, ele poderá importar (modulo_auxiliar.py) diretamente:
from modulo_auxiliar import MINHA_FUNÇÃO

Se (principal.py) usar o Modelo 2, ele poderá importar (outro_modulo.py) de subdiretorio/.
from outro_modulo import MINHA_FUNÇÃO
'''
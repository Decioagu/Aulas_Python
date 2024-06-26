'''
    Arquivos JSON podem ser usados para representar uma variedade de dados, incluindo objetos, listas, números, strings e booleanos. 
    Eles são um formato de dados leve e legível por máquinas, o que os torna uma opção popular para transferir dados entre sistemas.
    
    # O que é JSON - JavaScript Object Notation
    # JSON - JavaScript Object Notation (extensão .json)
    # É uma estrutura de dados que permite a serialização
    # de objetos em texto simples para facilitar a transmissão de
    # dados através da rede, APIs web ou outros meios de comunicação.
    # O JSON suporta os seguintes tipos de dados:
    # Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
    # Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
    #   As strings devem ser envolvidas por aspas duplas
    # Booleanos: são os valores verdadeiro (true) ou falso (false)
    # Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
    #   ["Oi", "Olá", "Bom dia"]
    # Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
    # null: é um valor especial que representa ausência de valor
    
    # Ao converter de Python para JSON:
    # Python ...... JSON
    # dict ........ object
    # list, tuple . array
    # str ......... string
    # int, float .. number
    # True ........ true
    # False ....... false
    # None ........ null 
'''

#-----------------------------------------------------------------------------
# Exemplo OBJETO em JSON (instância):
# JSON - OBS: utilizar aspas duplas
{
  "nome": "Bard",
  "idade": 3,
  "espécie": "IA",
  "habilidades": ["gerar texto", "traduzir idiomas", "responder perguntas"],
  "localização": {
    "latitude": -22.909722,
    "longitude": -43.210278
  }  
}
'''
    * OBS:
    Este arquivo JSON representa "UM objeto" com as seguintes propriedades:
    # nome: O nome do objeto.
    # idade: A idade do objeto.
    # espécie: A espécie do objeto.
    # habilidades: Uma lista de habilidades do objeto.
    # localização: Um objeto que representa a localização do objeto.
'''
print('===================================================================')

# Exemplo LISTA DE OBJETOS em JSON (coleção):
# JSON - OBS: utilizar aspas duplas
[
  {
    "nome": "Produto 1",
    "preço": 100,
    "quantidade": 10
  },
  {
    "nome": "Produto 2",
    "preço": 200,
    "quantidade": 20
  }
]

'''
    * OBS:
    Este arquivo JSON representa "uma LISTA de objetos", cada um com as seguintes propriedades:
    # nome: O nome do produto.
    # preço: O preço do produto.
    # quantidade: A quantidade do produto.
'''

#-----------------------------------------------------------------------------
# diferença entre json.dump() e json.dumps() | (ESCREVER)
'''
    json.dump() e json.dumps() são duas funções do módulo json em Python que são usadas para 
    transformar objetos Python em formato JSON. A principal diferença entre as duas funções é 
    que json.dump() serializa os dados para um arquivo, enquanto json.dumps() serializa os 
    dados para uma string.
'''
# json.dump() (arquivo JSON) | OBS: Arquivo "data.json" deve ser criado previamente
import json

dados = {"nome": "Fulano", "idade": 30}

# criar e escrever em um objeto JSON
with open("data.json", "w") as f:
    dados_arquivo_json = json.dump(dados, f) # escrever

print(type(dados_arquivo_json)) # <class 'NoneType'>

print('===================================================================')

# json.dumps() (string JSON)
import json

dados = {"nome": "Fulano", "idade": 30}


json_str = json.dumps(dados) # formatação -> tipo "str" do objeto JSON

print(type(json_str)) # <class 'str'>
print(json_str)

#-----------------------------------------------------------------------------

# diferença entre json.load() e json.loads() | (LER)
'''
    Os métodos json.load() e json.loads() são usados para ler dados JSON em objetos Python. 
    A diferença entre os dois métodos é que json.load() aceita um objeto de arquivo como entrada, 
    enquanto json.loads() aceita uma string como entrada.
'''
# json.load() (arquivo JSON)
import json

# ler arquivo objeto JSON
with open("data.json", "r") as f:
    ler_arquivo_json = json.load(f) # ler arquivo JSON para objeto 'dict'

print(type(ler_arquivo_json)) # <class 'dict'>
print(ler_arquivo_json) 

print('===================================================================')

# json.loads() (string JSON)
import json

# string
json_string = """
{
    "nom": "John Doe",
    "age": 30,
    "adresse": "123 Main Street, Anytown, USA"
}
"""
person = json.loads(json_string) # ler string para objeto 'dict'

print(type(person)) # tipo "dict" = objeto JSON
print(person)

#-----------------------------------------------------------------------------

# uso de json.dump() e json.load() (arquivo JSON | ESCREVER & LER)
'''
  A função  no Python é usada para carregar um objeto JSON de um arquivo ou uma string. 
  Esta função retorna um objeto Python que representa o objeto JSON carregado.json.load()
'''

import json

data = {
  "nome": "Bard",
  "idade": 3,
  "especie": "IA",
  "habilidades": ["gerar texto", "traduzir idiomas", "responder perguntas"],
  "localizacao": {
    "latitude": -22.909722,
    "longitude": -43.210278
  },
  "numeros": (1, 2, 3, 4, 5)
}

'''
    WINDOWS:
    Erro na acentuação do arquivo.txt utilizar :
    with open("data.json", "w", encoding='utf8') as criar_arquivo_json
'''

# criar e escrever em um objeto JSON
with open("data.json", "w", encoding='utf8') as criar_arquivo_json:
  json.dump(data, criar_arquivo_json) # criar arquivo json 

# ler arquivo de objeto JSON
with open("data.json", "r") as texto:
  ver = json.load(texto)  # ler arquivo JSON para objeto 'dict'
  print(f'{ver["nome"]=}')
  print(f'{ver["idade"]=}')
#-----------------------------------------------------------------------------

# uso de json.dumps() e json.loads() (leitura string JSON)
'''
    A função json.loads() é uma função da biblioteca padrão do Python 
    que é usada para converter um objeto JSON em um objeto Python (dicionário).
'''
import json

string_json = '''
                {
                "title": "O Senhor dos Anéis: A Sociedade do Anel",
                "original_title": "The Lord of the Rings: The Fellowship of the Ring",
                "is_movie": true,
                "imdb_rating": 8.8,
                "year": 2001,
                "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
                "budget": null
                }
              '''
filme = json.loads(string_json) # ler string para objeto 'dict'
print(filme, "\nTIPO =>",type(filme)) # tipo "dict" = objeto JSON

print('-' * 100)

exibir_joson = json.dumps(filme) # formatação -> tipo "str" do objeto JSON
print(exibir_joson, "\nTIPO =>",type(exibir_joson)) # tipo string

#-----------------------------------------------------------------------------

# Exemplo json.dumps e json.loads (string JSON)
import json
from typing import TypedDict

# tipagem
class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

# string
string_json = '''
                    {
                    "title": "O Senhor dos Anéis: A Sociedade do Anel",
                    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
                    "is_movie": true,
                    "imdb_rating": 8.8,
                    "year": 2001,
                    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
                    "budget": null
                    }
              '''

filme: Movie = json.loads(string_json) # ler string para objeto 'dict'
print(filme, "\nTIPO =>",type(filme)) # tipo "dict" = objeto JSON
print('-' * 100)
print(filme['title']) # tipo "dict" = objeto JSON


'''
  # json.dumps()
  A função json.dumps() é uma função da biblioteca padrão do Python que é usada para 
  converter um objeto Python em um objeto JSON.
  A função json.dumps() retorna uma string que representa o objeto JSON.
  
  # ensure_ascii=False
  O argumento ensure_ascii da função json.dumps() determina se os caracteres não-ASCII 
  devem ser convertidos para sua representação em ASCII. O valor padrão para ensure_ascii 
  é True, o que significa que os caracteres não-ASCII serão convertidos. Se ensure_ascii 
  for definido como False, os caracteres não-ASCII serão mantidos como estão.

  # indent=2
  O argumento indent da função json.dumps() determina o nível de indentação do JSON serializado.
  Se indent for definido como um número inteiro, o JSON será indentado usando espaços ou tabulações.
'''
print('-' * 100)
exibir_json = json.dumps(filme, ensure_ascii=False, indent=2) # formatação -> tipo "str" do objeto JSON
print(exibir_json, "\nTIPO =>",type(exibir_json)) # string que representa o objeto JSON
#-----------------------------------------------------------------------------

# Exemplo json.dump e json.load  (arquivos JSON)
import json
import os

NOME_ARQUIVO = 'aula177.json'

#============== CAMINHO_ABSOLUTO_ARQUIVO ============== 
# exibe caminho da pasta atual
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), # caminho atual
        NOME_ARQUIVO # nome arquivo
    )
)
#=====================================================

#============== equivalente procedimento acima ============== 
# CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath (NOME_ARQUIVO )
#============================================================


print('caminho onde esta o arquivo python =',__file__)
print(CAMINHO_ABSOLUTO_ARQUIVO)

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

# criar e escrever em um objeto JSON
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2) # altera visualização dentro do arquivo JSON

# ler arquivo objeto JSON
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)  # ler arquivo JSON para objeto 'dict'
    print(filme_do_json)
#-----------------------------------------------------------------------------

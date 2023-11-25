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
    # Python        JSON
    # dict          object
    # list, tuple   array
    # str           string
    # int, float    number
    # True          true
    # False         false
    # None          null 
'''

# Exemplo JSON:

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
    Este arquivo JSON representa um objeto com as seguintes propriedades:
    # nome: O nome do objeto.
    # idade: A idade do objeto.
    # espécie: A espécie do objeto.
    # habilidades: Uma lista de habilidades do objeto.
    # localização: Um objeto que representa a localização do objeto.
'''

# Aqui está outro exemplo de um arquivo JSON:

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
    Este arquivo JSON representa uma lista de objetos, cada um com as seguintes propriedades:
    # nome: O nome do produto.
    # preço: O preço do produto.
    # quantidade: A quantidade do produto.
'''

#-----------------------------------------------------------------------------

'''
    json.dump() e json.dumps() são duas funções do módulo json em Python que são usadas para serializar dados 
    Python em formato JSON. A principal diferença entre as duas funções é que json.dump() serializa os dados 
    para um arquivo, enquanto json.dumps() serializa os dados para uma string.

    Para usar json.dump(), você precisa passar dois argumentos para a função: os dados que você deseja serializar 
    e o objeto de arquivo onde deseja escrever os dados. Por exemplo, o seguinte código serializa um dicionário 
    Python para um arquivo chamado data.json:
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

json_data = json.dumps(data)
print(json_data) # cria string json

#-----------------------------------------------------------------------------

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

# escrever arquivo externo
with open("data.json", "w", encoding='utf8') as criar_arquivo_json:
  json.dump(data, criar_arquivo_json) # criar arquivo json 

# ler arquivo externo
with open("data.json", "r") as texto:
  ver = json.load(texto)
  print(f'{ver["nome"]=}')
  print(f'{ver["idade"]=}')
#-----------------------------------------------------------------------------

'''
    A função json.loads() é uma função da biblioteca padrão do Python 
    que é usada para converter um objeto JSON em um objeto Python.
'''
import json
from pprint import pprint

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
filme = json.loads(string_json)

print(filme)
print('-' * 100)
print(filme["year"])
print('-' * 100)
pprint(filme)

print('===================================================================')

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
filme: Movie = json.loads(string_json) # tipagem

print(filme) # tipo "dict"
print('-' * 100)
print(filme['title']) # tipo "dict"
print('-' * 100)

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
exibir_joson = json.dumps(filme, ensure_ascii=False, indent=2) # formatação -> tipo "str"

print(exibir_joson)
#-----------------------------------------------------------------------------

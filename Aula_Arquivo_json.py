'''
    Arquivos JSON podem ser usados para representar uma variedade de dados, incluindo objetos, listas, números, strings e booleanos. 
    Eles são um formato de dados leve e legível por máquinas, o que os torna uma opção popular para transferir dados entre sistemas.
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
print('===================================================================')
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




from dotenv import load_dotenv 
import os

'''
Um arquivo .env (abreviação de "environment") é usado para armazenar variáveis 
de ambiente de forma segura e organizada, especialmente em projetos de software.

pip install python-dotenv

.env
    login = DECIOSAN
    senha = 123456
'''

load_dotenv() # Carrega as variáveis do .env

login = os.getenv('LOGIN') # Acessar variáveis de ambiente
senha = os.getenv('SENHA') # Acessar variáveis de ambiente

print(login)
print(senha)

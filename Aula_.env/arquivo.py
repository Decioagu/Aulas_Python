from dotenv import load_dotenv 
import os

'''
Um arquivo .env (abreviação de "environment") é usado para armazenar variáveis 
de ambiente de forma segura e organizada, especialmente em projetos de software.

pip install python-dotenv
'''

load_dotenv()

login = os.getenv('LOGIN')
senha = os.getenv('SENHA')

print(login)
print(senha)
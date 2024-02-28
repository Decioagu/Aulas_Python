'''
# Você pode dar o nome que preferir para um ambiente virtual, mas os mais comuns são:
# venv env .venv .env
# Como criar ambientes virtuais
# Abra a pasta do seu projeto no terminal
# e digite:


*********************** Windows PowerShell**************************
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Opção: S
# https://www.youtube.com/watch?v=m1TYpvIYm74&t=326s
********************************************************************

================================= Debugger =====================================
# O Debugger do VS Code = Aula 36

============================== ambiente virtual ================================
# ambiente virtual
py -m venv venv
py -m venv "NOME"
python -m venv "NOME"
python 3 -m venv "NOME"

# ativa um ambiente virtual
.\venv\Scripts\activate
.\"NOME"\Scripts\activate

# desativar um ambiente virtual
deactivate

# versão python
py -V
python -V
pip --version

# atualizar pip
python.exe -m pip install --upgrade pip

=================================== pacote =====================================
# instalar pacote
py -m pip install "pacote"
pip install "pacote"

# desinstalar pacote 
pip uninstall  "pacote"

# instalar versão pacote antigo código
pip install "pacote"=="código"

# instalar versão mais recente do pacote
pip install "pacote" --upgrade

# ver versão do pacote
pip show "pacote"
pip index versions "pacote"

# ver pacotes instalados no ambiente virtual
pip freeze

# gerar arquivo.txt de pacotes instalados
py -m pip freeze > requirements.txt (OBS: nome requirements.txt pode ser alterado)
pip freeze > requirements.txt

# recuperar pacotes em pip freeze em arquivo.txt
py -m pip install -r requirements.txt (OBS: nome requirements.txt pode ser diferente)
pip install -r requirements.txt

================================== gitignore =====================================
# arquivo ".gitignore" (consultar arquivo "gitignore_padrão.txt")
Abra o VS Code e navegue até o diretório do seu projeto.
Crie um novo arquivo chamado .gitignore.
Abra o arquivo .gitignore recém-criado.

Adicione os arquivos ou diretórios que você deseja excluir, exemplo:
consultar arquivo "gitignore_padrão.txt", na pasta P:\REPOSITORIO\PRIVADO\Aulas_Python

# PyInstaller Manual = Aula374
pip install -U pyinstaller
https://pyinstaller.org/en/stable/

============================= pacote jupyter notebook ============================
# instalar jupyter notebook
py -m pip install notebook

# ativar jupyter notebook
jupyter notebook

===================== PyInstaller converter scripts em executáveis ===============
pip install pyinstaller
https://www.youtube.com/watch?v=FdwSS1TlluQ
Exemplo:
pyinstaller --noconsole --name="NOME" --onefile NOME.py
https://www.youtube.com/watch?v=el9nLY4ewHI
'''




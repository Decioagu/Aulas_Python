import string

texto = "Olá, meu nome é ${nome} e tenho ${idade} anos."

pessoa = {
    "nome": "Ana",
    "idade": 30
}

'''
    # string.Template()
    É uma função que substitui espaços reservados em uma cadeia de caracteres, 
    geralmente é feito usando um dicionário ou outra estrutura de dados que 
    mapeia nomes de espaço reservado para seus valores correspondentes. 
'''
template = string.Template(texto) 
result = template.safe_substitute(pessoa) # método usado para substituir variáveis em um template. 
print(result)

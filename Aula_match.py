'''
Introduzido no Python 3.10, fornece uma maneira mais limpa e concisa de lidar 
com várias condições em comparação com as cadeias tradicionais (if/elif/else). 

match expression:
    case pattern1:
        code_to_execute_if_pattern1_matches
    case pattern2:
        code_to_execute_if_pattern2_matches
    ...
    case _:  # Optional catch-all case (like "else")
        code_to_execute_if_no_match

        Avaria:

    # match expression: A variável ou expressão cujo valor você deseja comparar com padrões.

    # case pattern: Cada bloco define um padrão para corresponder. Os padrões podem ser 
    literais (como números ou cadeias de caracteres), curingas () ou classes de padrão.case_

    # code_to_execute: O código que é executado se o padrão correspondente corresponder.

    # case _: Este caso catch-all opcional (semelhante a ) é executado se nenhum dos 
    outros padrões corresponder.else
'''

dia = "Sexta"

match dia:
    case "Segunda":
        print("Hoje é o pior dia da semana!")
    case "Terça" | "Quarta" | "Quinta":
        print("Segue para o proximo...")
    case "Sexta":
        print("Sextou...")
    case _:
        print("Zzzz...")

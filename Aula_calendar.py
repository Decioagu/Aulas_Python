
# https://docs.python.org/3/library/calendar.html
'''
    A função calendar() é uma função interna em Python que retorna um calendário. 
    O calendário pode ser mensal, semanal ou anual. A função calendar() usa dois argumentos:
'''
import calendar

# exibir calendário
print(calendar.calendar(2022)) # (ano) => resposta = calendário anual

print('<==========================================================>')

print(calendar.month(2022, 12)) # (ano, mês) => resposta = calendário do mês
#-----------------------------------------------------------------------------------------------

# exibir informações da semana
import calendar

print(list(enumerate(calendar.day_name))) # resposta = lista de dias da semana

print('<==========================================================>')

print(calendar.weekday(2022, 11, 30)) # (ano, mês, dia) => resposta = valor numérico dia da semana

print('<==========================================================>')

print(calendar.day_name[0]) # resposta = dia da semana

print('<==========================================================>')

print(calendar.day_name[calendar.weekday(2022, 11, 30)]) # (ano, mês, dia) => resposta = dia da semana

#-----------------------------------------------------------------------------------------------

# exibir informações do mês
import calendar
'''
    A função calendar.monthrange() retorna um tuple de dois inteiros, representando: 
    # o primeiro dia do mês: Os valores possíveis são de 0 a 6.
    # o número de dias no mês.
'''

print(calendar.monthrange(2022, 12)) # (ano, mês) => resposta = (número da semana, quantidade de dias no mês)

print('<==========================================================>')

# (ano, mês) => resposta = (primeiro dia no valor numérico da semana, ultimo dia no mês)
primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12) 

print(calendar.day_name[primeiro_dia]) # primeiro dia no mês = (valor numérico dia da semana)
print(calendar.day_name[calendar.weekday(2022, 12, ultimo_dia)]) # ultimo dia no mês

print('<==========================================================>')

'''
    Cada linha da matriz representa uma semana; os dias fora do mês são representados por zeros. 
    # Cada semana começa com segunda-feira  #
'''
print(list(calendar.day_name)) # lista de dias da semana
print(calendar.monthcalendar(2022, 12))  

print('<==========================================================>')

# dias do mês
for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        print(day, end='-')
print()
#-----------------------------------------------------------------------------------------------

import calendar
import locale

# locale.setlocale(locale.LC_ALL, 'pt_BR')
locale.setlocale(locale.LC_ALL, '')


print(calendar.calendar(2022))
print('<==========================================================>')
print(list(calendar.day_name)) # lista de dias da semana
print('<==========================================================>')
print(locale.getlocale())



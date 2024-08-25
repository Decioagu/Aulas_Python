'''
    O módulo datetime em Python fornece classes para manipular datas e horas. 
    Ele suporta uma ampla gama de operações, incluindo:
    
    https://docs.python.org/3/library/datetime.html
'''

# criar data e hora (FIXO)
from datetime import datetime

data1 = datetime(2023, 5, 15) # (ano, mês, dia)
print(data1, type(data1))

print('<==========================================================>')

data2 = datetime(2022, 4, 20, 7, 49, 23) # (ano, mês, dia, hora, min., seg.)
print(data2, type(data2))

print('<==========================================================>')

data_str_data = '20/04/2023 07:49:23' # "str"
data_str_fmt = '%d/%m/%Y %H:%M:%S' # "str"
# data_str_data = '20/04/2023'
# data_str_fmt = '%d/%m/%Y'
data3 = datetime.strptime(data_str_data, data_str_fmt) # formatar data para "datetime"
print(data3, type(data3))
print(data3.date(), type(data3))
data4 = data3.strftime('%d/%m/%Y %H:%M:%S') # formatar "datetime" para "str"
print(data4, type(data4)) # data formatada para "str"

#-----------------------------------------------------------------------------------------------

# separa data e hora criada (FIXO)
from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53, 11)
print("Datetime:", dt, type(dt)) # Datetime: 2019-11-04 14:53:11 <class 'datetime.datetime'>
print("Data:", dt.date(), type(dt.date())) # Data: 2019-11-04 <class 'datetime.date'>
print("Tempo:", dt.time(), type(dt.time())) # Tempo: 14:53:11 <class 'datetime.time'>

#-----------------------------------------------------------------------------------------------

# criar data (FIXO)
'''
    A norma ISO 8601 define a forma como a data e a hora são representadas
'''
from datetime import date

data = date.fromisoformat('2019-11-04') # Ano, mês, dia <=norma ISO 8601
print(data, type(data))

#-----------------------------------------------------------------------------------------------

# alterar data já existente (FIXO)
from datetime import date

data = date(2000, 1, 17) # data
print(data) 
#-----------------------------------------------------------------------------------------------

# data de hoje (DINÂMICO)
from datetime import date, datetime

# datetime.now() = datetime.today()
print(datetime.now()) # data | hora:minuto:segundo:mile segundo
print(datetime.today()) # data | hora:minuto:segundo:mile segundo

hoje = date.today() # data de hoje

print("Data:", hoje) # ano/mês/dia
print("Ano:", hoje.year) # ano
print("Mês:", hoje.month) # mês
print("Dia:", hoje.day) # dia
#-----------------------------------------------------------------------------------------------

# Unix (DINÂMICO)
'''
Em Unix, o timestamp expressa o número de segundos desde 1 de janeiro de 1970, 00:00:00 (UTC). 
Esta data é chamada a época Unix, porque foi quando a contagem do tempo começou nos sistemas Unix.
O timestamp é na realidade a diferença entre uma determinada data (incluindo a hora) e 1 de janeiro 
de 1970, 00:00:00 (UTC), expressa em segundos
'''

from datetime import date
import time

timestamp = time.time() # Unix
print("Timestamp:", timestamp, 's') # 1 de janeiro de 1970, 00:00:00 (UTC) em segundos

print('<==========================================================>')

data = date.fromtimestamp(timestamp) # data atual
print("Date:", data) 
#-----------------------------------------------------------------------------------------------

# dia da semana em "int" (DINÂMICO) 
'''
    Expressa o dia da semana em número inteiro, sendo:

    # Segunda = 0
    # Terça   = 1
    # Quarta  = 2
    # Quinta  = 3
    # Sexta   = 4
    # Sábado  = 5 
    # Domingo = 6
'''
from datetime import date

d = date.today()
print(d) # Data de hoje
print(d.weekday(), type(d.weekday())) # Dia da semana em "int"
#-----------------------------------------------------------------------------------------------

# criar hora (FIXO)
from datetime import time

t = time(14, 53, 20, 1) # (hora, min., seg., ms)

print("Tempo:", t) # Hora atual
print("Hora:", t.hour) # O parâmetro hora deve ser maior ou igual a 0 e inferior a 23
print("Minuto:", t.minute) # O parâmetro minuto deve ser maior ou igual a 0 e inferior a 59.
print("Segubdo:", t.second) # O parâmetro segundo deve ser maior ou igual a 0 e inferior a 59.
print("Microsegundo:", t.microsecond) # O parâmetro microssegundo deve ser maior ou igual a 0 e inferior a 1000000.
#-----------------------------------------------------------------------------------------------

# data atual (DINÂMICO) 
from datetime import datetime

print("today:", datetime.today()) # data atual  (fuso horário local do computador)
print("now:", datetime.now()) # data atual (fuso horário local do computador)

#-----------------------------------------------------------------------------------------------
'''
UTC (Tempo Universal Coordenado). 
Padrão de hora internacional que é usado como referência para todos os outros fusos horários.
É uma escala de tempo coordenado, mantida pela Agência Internacional de Pesos e Medidas e utilizada 
como padrão de "hora certa" no controle de tráfego aéreo e serviços de meteorologia aeronáutica.
O sistema UTC foi desenvolvido pela ITU/UIT em 1970.
https://24timezones.com/fuso-horario/utc
'''
# data atual (DINÂMICO) 

from datetime import datetime, timezone

print("utcnow:", datetime.utcnow()) # data atual (fuso padrão internacional) => "forma desatualizado"
print("utcnow:", datetime.now(timezone)) # data atual (fuso padrão internacional) => "forma atualizado"

#-----------------------------------------------------------------------------------------------

# manipula apresentação da data ao imprimir - formatar data - (DINÂMICO) ou (FIXO)
from datetime import datetime

today = datetime.today()
print(today)
print(today.strftime('%Y/%m/%d'))
print(today.strftime('%d/%m/%Y'))

print('<==========================================================>')

data = datetime(2023, 5, 15) # (ano, mês, dia)
print(data.strftime('%d\\%m\\%Y %H:%M:%S'))

print('<==========================================================>')

str_date = '2018-07-11'
date = datetime.strptime(str_date, '%Y-%m-%d').date()
print(date, type(date))

print('<==========================================================>')

str_date = '11/07/2018'
date = datetime.strptime(str_date, '%d/%m/%Y').date()
print(date, type(date))

print('<==========================================================>')

datetime_str = '19/09/18 13:55:26'
datetime_object = datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S')
print(datetime_object, type(datetime_object))

print('<==========================================================>')

dates = ['01/01/2016 04:50','01/01/2016 05:50','01/01/2016 06:50','01/01/2016 07:50']
DATE = [datetime.strptime(x,'%m/%d/%Y %H:%M') for x in dates]
for n in DATE:
    print(n, type(n))

print('<==========================================================>')

fmt = '%d/%m/%Y %H:%M:%S'
data = datetime.strptime('20/04/1987 09:30:30', fmt)
print(data)

print('<==========================================================>')

data = datetime.strptime('2000-06-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime('%d/%m/%Y'))
print(data.strftime('%d/%m/%Y %H:%M'))
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%Y'), data.year)
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print(data.strftime('%H'), data.hour)
print(data.strftime('%M'), data.minute)
print(data.strftime('%S'), data.second)
#-----------------------------------------------------------------------------------------------

# Objeto do "timedelta" é representa uma duração, a diferença entre duas datas ou hora (FIXO)

from datetime import timedelta

d = timedelta(weeks=0, days=1, hours=2, minutes=3, seconds=4, milliseconds=5, microseconds=6)
print(f'timedelta => {d}', type(d))
print()
delta = timedelta(weeks=2, days=2, hours=3)
print(delta, type(delta))
print()
delta = timedelta(weeks=2, days=2, hours=3)
print("Days:", delta.days, type(delta.days))
print("Seconds:", delta.seconds, type(delta.seconds))
print("Microseconds:", delta.microseconds, type(delta.microseconds))
#-----------------------------------------------------------------------------------------------
# relativedelta (DINÂMICO) ou (FIXO)
'''
    O dateutil.relativedelta é um módulo do Python que fornece uma classe chamada relativedelta, 
    que pode ser usada para representar intervalos de tempo. A classe relativedelta pode ser 
    usada para calcular a diferença entre duas datas e horas, bem como para criar novas datas 
    e horas com base em um intervalo de tempo.
'''

from dateutil.relativedelta import relativedelta

delta = relativedelta(years=1, months=2, days=3, hours=4, minutes=5, seconds=6, microseconds=7)
print(delta, type(delta))
print(delta.years, type(delta.years))
print(delta.months, type(delta.months))
print(delta.days, type(delta.days))
print(delta.hours, type(delta.hours))
print(delta.minutes, type(delta.minutes))
print(delta.seconds, type(delta.seconds))
print(delta.microseconds, type(delta.microseconds))
#-----------------------------------------------------------------------------------------------

# calcular data (DINÂMICO) ou (FIXO)
'''
    Para instalar o dateutil.relativedelta em Python, você pode usar o gerenciador de pacotes pip. 
    Abra um terminal e execute o seguinte comando:

    # pip install python-dateutil

    # https://dateutil.readthedocs.io/en/stable/relativedelta.html
    # https://docs.python.org/3/library/datetime.html#timedelta-objects
'''
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

d1 = date(2018, 11, 4)
d2 = date(2019, 11, 4)
data = d1 - d2
print(data, type(data))

print('<==========================================================>')

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
data = dt1 - dt2
print(data, type(data))

print('<==========================================================>')

a = datetime(2001, 2, 1, 1, 2, 3)
b = datetime(2001, 2, 1, 0, 0, 0)
c = a - b
print(c) # horas
print(c.days) # valor em dias
print(c.seconds) # valor em segundos

print('<==========================================================>')

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
delta = data_inicio - data_fim # diferença em dias
print(delta)
print(delta.total_seconds()) # total em segundo
print(data_fim + timedelta(days=10)) # somar 10 dias
print(data_fim > data_inicio)

relativa = relativedelta(data_fim, data_inicio)
print(relativa)

print('<==========================================================>')

nascimento = datetime(1981, 5, 15)
aniversario = relativedelta(datetime.now(), nascimento)
print(aniversario) # tempo de vida

print('<==========================================================>')

inicio_emprestimo = datetime(2020, 12, 20) # inicio do empréstimo
tempo_de_emprestimo = relativedelta(years=5) # tempo do empréstimo em anos
fim_emprestimo = inicio_emprestimo + tempo_de_emprestimo # fim do empréstimo

print(inicio_emprestimo, type(inicio_emprestimo))
print(tempo_de_emprestimo, type(tempo_de_emprestimo))
print(fim_emprestimo, type(fim_emprestimo))
#-----------------------------------------------------------------------------------------------

# calcular idade  (DINÂMICO)  
# Este comando irá baixar e instalar a biblioteca dateutil e suas dependências (pip install python-dateutil)
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

nascimento = datetime(1981, 5, 15)
hoje = datetime.now()
aniversario = relativedelta(hoje, nascimento)
print(aniversario, type(aniversario)) # tempo de vida
print(aniversario.years, 'anos', type(aniversario.years)) # tempo de vida
#-----------------------------------------------------------------------------------------------

# operações matemática com datas (DINÂMICO)
from datetime import datetime, timedelta

hoje = datetime.today()
tdelta = timedelta(days=5)
calculo = hoje + tdelta
print(f'Soma de {hoje} + {tdelta.days} dias = {calculo}')
soma = calculo
print()
print(f'Soma de {hoje.strftime("%d")} dias + {tdelta.days} dias = {soma.strftime("%d")}')
#-----------------------------------------------------------------------------------------------

# informações da semana (DINÂMICO) ou (FIXO)
from datetime import datetime

my_date = datetime.now()

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%M:%S %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Semana: %w"))
print(my_date.strftime("Dia do ano: %j"))
print(my_date.strftime("Número da semana no ano: %W"))
#-----------------------------------------------------------------------------------------------
# contador de segundos em data (DINÂMICO) ou (FIXO)
'''
A função time fornece uma função chamada "ctime", que converte o tempo em segundos 
desde 1 de janeiro de 1970 (época Unix) para uma string.
''' 

import time

timestamp = 2572879180 # tempo em segundos
print(time.ctime(timestamp)) 

print('<==========================================================>')

print(time.ctime(), type(time.ctime())) # Unix
#-----------------------------------------------------------------------------------------------

# (DINÂMICO) ou (FIXO)
'''
    A função  do módulo  em Python retorna um objeto  que representa a hora atual 
    no fuso horário UTC (Coordinated Universal Time).
'''
import time

now = time.gmtime()

print(now)

#-----------------------------------------------------------------------------------------------
# (DINÂMICO) ou (FIXO)
'''
    A função  do módulo  em Python converte um objeto  em uma string que representa 
    a hora e a data. A string é formatada no formato seguinte
'''
import time

print(time.asctime())
#-----------------------------------------------------------------------------------------------
# (FIXO)
'''
    A função sleep() é uma função de tempo que suspende a execução do 
    programa por um determinado número de segundos.
'''
from time import sleep

print('CRECK!!!')
sleep(1) # Suspende a execução do programa tempo em segundos
print(' Xiiiiiii..')
sleep(1) # Suspende a execução do programa tempo em segundos
print('   Chuuuuuu...')
print()
for c in  range(3, 0, -1):
    print(c)
    sleep(1) # Suspende a execução do programa tempo em segundos
print('Pa.')
print(' Papa..')
print('  Papa..')
print('   Papapa...')
print('    Papapapa....')
sleep(2) # Suspende a execução do programa tempo em segundos
print('     Boooooooom....')
sleep(1) # Suspende a execução do programa tempo em segundos
print('      Rojão 13 tiros...'.upper())
#-----------------------------------------------------------------------------------------------

# data e horário de qualquer lugar do mundo (DINÂMICO) ou (FIXO)
'''
    # Para timezones
    # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    # Instalando o pytz:
    # pip install pytz types-pytz
'''

from datetime import datetime
from pytz import timezone

data = datetime.now(timezone('Japan')) # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
print(data)  # Isso está na base de dados


# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)
#-----------------------------------------------------------------------------------------------


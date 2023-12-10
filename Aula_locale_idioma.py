'''
    O módulo locale em Python fornece funções para trabalhar com configurações regionais e de idioma, 
    permitindo que você adapte seus programas às configurações de idioma e cultura do usuário. 
    Ele oferece suporte a uma ampla gama de configurações regionais, incluindo aquelas que 
    abrangem diferentes idiomas, formatos de data e moeda, e convenções de classificação.locale

    Principais funções do módulo locale:

    setlocale(category, locale=None): Define a configuração regional para a categoria 
    especificada. As categorias disponíveis são:

    * LC_CTYPE
    * LC_COLLATE
    * LC_MONETARY
    * LC_NUMERIC
    * LC_TIME
    * LC_MEASUREMENT
    * LC_ALL

    getlocale(category=LC_ALL): Obtém a configuração regional atual para a categoria especificada, 
    ou para  se nenhuma categoria for fornecida.LC_ALL

    gettext(message): Traduz uma mensagem para o idioma atual usando o domínio de texto padrão.

    pgettext(msgid, msgstr): Traduz uma mensagem para o idioma atual usando o domínio de texto fornecido.

    textdomain(domain): Define o domínio de texto atual para traduções.

    bindtextdomain(domain, dir): Associa um diretório específico ao domínio de texto fornecido.

    # locale para internacionalização (tradução)
    # https://docs.python.org/3/library/locale.html
    # https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

'''
import calendar
import locale

# locale.setlocale(locale.LC_ALL, 'pt_BR')
locale.setlocale(locale.LC_ALL, '')


print(calendar.calendar(2022))
print('<==========================================================>')
print(list(calendar.day_name)) # lista de dias da semana
print('<==========================================================>')
print(locale.getlocale())

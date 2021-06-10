from datetime import date

sexo = str(input('Qual o seu sexo? [M/F]')).strip()
ano = date.today().year

if sexo == 'm' or sexo == 'M':
    nasc = int(input('Informe seu ano de nascimento: '))
    if ano - nasc < 18:
        print('''Você ainda vai se alistar!
        Faltam {} anos para se alistar!'''.format(18-(ano - nasc)))
    elif ano - nasc == 18:
        print('Você deve se alistar neste ano de {}!'.format(ano))
    else:
        print('''Passou do tempo de se alistar!
        Você está atrasado {} anos. CORRA!'''.format((ano - nasc)-18))
elif sexo == 'f' or sexo == 'F':
    print('''Você é uma mulher!
    O alistamento é PARA homens!''')
else:
    print('ERRO! Tente novamente')

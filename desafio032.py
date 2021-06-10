from datetime import date

ano = int(input('Digite um ano: '))

if ano == 0:
    ano = date.today().year

if ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
elif ano % 4 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))

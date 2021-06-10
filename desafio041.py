from datetime import date

nasc = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('Você tem {} anos e sua categoria na natação é MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e sua categoria na natação é INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e sua categoria na natação é JÚNIOR!'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e sua categoria na natação é SÊNIOR!'.format(idade))
elif idade > 25:
    print('Você tem {} anos e sua categoria na natação é MASTER!'.format(idade))

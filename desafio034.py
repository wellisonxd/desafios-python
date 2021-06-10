sal = float(input('Informe seu salário R$'))

if sal > 1250.0:
    sal = sal * 1.10
    print('O valor do seu salário atualizado é R${:.2f}'.format(sal))
else:
    sal = sal * 1.15
    print('O valor do seu salário atualizado é R${:.2f}'.format(sal))
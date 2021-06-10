num1 = int(input('Informe um numero: '))
num2 = int(input('Informe outro numero: '))

if num1 > num2:
    print('O primeiro número {} é maior!'.format(num1))
elif num2 > num1:
    print('O segundo número {} é maior!'.format(num2))
else: 
    print('Os dois números são iguais {} e {}.'.format(num1, num2))
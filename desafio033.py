n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

if n1 > n2 and n1 > n3:
    print('O {} é o maior número.'.format(n1))
elif n2 > n3:
    print('O {} é o maior número.'.format(n2))
else:
    print('O {} é o maior número.'.format(n3))

if n1 < n2 and n1 < n3:
    print('O {} é o menor número.'.format(n1))
elif n2 < n3:
    print('O {} é o menor número.'.format(n2))
else:
    print('O {} é o menor número.'.format(n3))
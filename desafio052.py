num = int(input('Digite um número: '))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

print('\n\033[mO número {} foi divísivel {} vezes.'.format(num, cont))
if cont == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

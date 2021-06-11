inicio = int(input('Diga quantos termos quer ver da Sequência: '))

tot = 3
fib = 0
fib2 = 1
fib3 = 0
print('{} - {} '.format(fib, fib2), end='-')
while tot <= inicio:
    fib3 = fib + fib2
    print(' {} '.format(fib3), end='-')
    fib = fib2
    fib2 = fib3
    tot += 1
print(' ACABOU!')

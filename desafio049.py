tabuada = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    total = tabuada * c
    print('{} X {:2} = {}'.format(tabuada, c, total))
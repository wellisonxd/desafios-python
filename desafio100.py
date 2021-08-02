from random import randint

escolhidos = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for s in range(5):
        num = randint(1, 10)
        print(f'{num}', end=' ')
        escolhidos.append(num)
    print()

def somaPar(x):
    soma = 0
    for c in x:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {escolhidos} dá = {soma}')


sorteia()
somaPar(escolhidos)
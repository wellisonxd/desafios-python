from random import randint

'''sort = []
maior = menor = 0
for num in range(1, 6):
    sorteio = randint(1, 9)
    if num == 1:
        menor = sorteio
    elif sorteio < menor:
        menor = sorteio
    if sorteio > maior:
        maior = sorteio
    sort.append(sorteio)
tuple(sort)
print(f'Os valores sorteados foram: {sort[0]} {sort[1]} {sort[2]} {sort[3]} {sort[4]}')
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')'''

numero = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
print('Os valores sorteados foram: ', end='')
for n in numero:
    print(f' {n}', end='')
print(f'\nO maior valor sorteado foi: {max(numero)}')
print(f'O menor valor sorteado foi: {min(numero)}')


from random import randint
from time import sleep
sorteio = []
jogos = []
cont = 0
print('-' * 30)
print('  SORTEIO JOGOS DA MEGA SENA  ')
print('-' * 30)
quant = int(input('Quantos jogos você deseja? '))
print('-' * 30)
for j in range(quant):
    cont = 0
    while cont < 6:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        elif cont >= 6:
            break
    jogos.sort()
    sorteio.append(jogos[:])
    jogos.clear()
for j, i in enumerate(sorteio):
    print(f'Jogo {j+1} = {i}')
    sleep(1)
print('-' * 30)

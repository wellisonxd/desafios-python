from random import randint
from operator import itemgetter
game = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('VALORES SORTEADOS')
for k, v in game.items():
    print(f'O {k} tirou {v}')
ranking = dict()
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('=-=' * 20)
print('== RESULTADO FINAL ==')
for p, i in enumerate(ranking):
    print(f'{p+1}º lugar: {i[0]} com {i[1]}')
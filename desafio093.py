dadosJogador = dict()
gols = list()
totGols = 0
dadosJogador['nome'] = str(input('Qual o nome do jogador? '))
partidas = int(input(f'Quantas partidas o {dadosJogador["nome"]} jogou? '))
for i in range(partidas):
    gol = int(input(f'Quantos gols na partida {i} = '))
    gols.append(gol)
    totGols += gol
#ou posso fazer o sum(gols), no caso da lista, e ter a soma de tudo
dadosJogador['gols'] = gols[:]
dadosJogador['total'] = totGols
print('-=-' * 20)
print(dadosJogador)
print('-=-' * 20)
for k, v in dadosJogador.items():
    print(f'{k} tem como valor {v}')
print('-=-' * 20)
print(f'O jogador {dadosJogador["nome"]} jogou {partidas}: ')
for p, v in enumerate(dadosJogador["gols"]):
    print(f' => Na partida {p}, fez {v} gols')
print(f'Foi um total de {dadosJogador["total"]} gols.')
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')


nome = input('Nome do jogador: ')
gol = input('Número de gols: ')
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)

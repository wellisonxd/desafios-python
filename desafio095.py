time = list()
dadosJogador = dict()
gols = list()
totGols = 0
while True:
    gols.clear()
    dadosJogador['nome'] = str(input('Qual o nome do jogador? '))
    partidas = int(input(f'Quantas partidas o {dadosJogador["nome"]} jogou? '))
    for i in range(partidas):
        gol = int(input(f'Quantos gols na partida {i+1} = '))
        gols.append(gol)
        totGols += gol
    dadosJogador['gols'] = gols[:]
    dadosJogador['total'] = totGols
    time.append(dadosJogador.copy())
    #ou posso fazer o sum(gols), no caso da lista, e ter a soma de tudo
    while True:
        resp = str(input('Deseja continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break
print('-=-' * 20)
print(f'{"cod":<4} {"nome":<15} {"gols":<20} {"total":<6}')
for p, i in enumerate(time):
    print(f'{p:<4} {str(i["nome"]):<15} {i["gols"]} {i["total"]}')
print('-=-' * 20)
while True:
    while True:
        escolha = int(input('Mostrar dados de qual jogador? (999 para parar) = '))
        if escolha >= 0 and escolha < len(time) or escolha == 999:
            break
        else:
            print('ERRO! Digite um numero válido!')
    if escolha == 999:
        break
    print(f' --LEVANTAMENTO DO JOGADOR {time[escolha]["nome"]}: ')
    for p, i in enumerate(time[escolha]['gols']):
        print(f'    No jogo {p+1} fez {i}')
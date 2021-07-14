dados = []
pessoas = []
pesoMaior = pesoMenor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso em KG: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar [S/N]? ')).strip()[0]
    if resp in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas são: ', end='')
for p in pessoas:
    if p[1] >= pesoMaior:
        pesoMaior = p[1]
        print(f'{p[0]}', end=' ')
print(f'\nAs pessoas mais leves são: ', end='')
for p in pessoas:
    if pesoMenor == 0:
        pesoMenor = p[1]
    elif p[1] <= pesoMenor:
        pesoMenor = p[1]
        print(f'{p[0]}', end=' ')

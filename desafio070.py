totc = totmil = preco2 = 0
nomeP = ' '
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço do produto: R$'))

    totc += preco
    if preco > 1000:
        totmil += 1
    if preco2 == 0:
        preco2 = preco
        nomeP = nome
    elif preco < preco2:
        nomeP = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais produtos [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total gasto foi R${totc:.2f} .')
print(f'{totmil} produtos custam mais de R$1000.')
print(f'O produto mais barato é {nomeP}')
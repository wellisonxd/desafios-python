prim = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
soma = prim

for c in range(1, 11):
    print(soma, end=' -> ')
    soma += razao
print('ACABOU!')

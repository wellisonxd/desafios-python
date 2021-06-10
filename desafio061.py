prim = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = prim
cont = 0
while cont != 10:
    print(pa, end=' -> ')
    pa += razao
    cont += 1
print('ACABOU!')
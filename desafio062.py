prim = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = prim
cont = 0
while cont != 10:
    print(pa, end=' -> ')
    pa += razao
    cont += 1
print('PAUSA')
termo = int(input('Quantos termos você quer mostrar a mais? '))
while termo != 0:
    print(pa, end=' -> ')
    pa += razao
    termo -= 1
    if termo == 0:
        print('PAUSA')
        termo = int(input('Quantos termos você quer mostrar a mais? '))
print('ACABOU!')
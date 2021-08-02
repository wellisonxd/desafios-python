from time import sleep
def contador(ini, f, p):
    if f == 0:
        f = -1
    else:
        f += 1
    if f < ini and p > 0:
        p = -p 
    for u in range(ini, f, p):
        sleep(0.5)
        print(f'{u}', end=' ')
    

for i in range(0, 10, 1):
    sleep(0.5)
    print(f'{i+1}', end=' ')
print()
for t in range(10, -1, -2):
    sleep(0.5)
    print(f'{t}', end=' ')
print()
print('Agora é a sua vez de personalizar uma contagem!')
ini = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
contador(ini, f, p)

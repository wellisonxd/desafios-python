from random import randint
from time import sleep

print('{:=^40}'.format(' JOGANDO JOKENPO '))
print('''Escolha:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
player = int(input('Sua escolha: '))
maquina = randint(1, 3)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

if player == 1:
    if maquina == 2:
        print('MÁQUINA = PAPEL | VOCÊ = PEDRA |')
        print('\033[31mDERROTA\033[m')
    elif maquina == 3:
        print('MÁQUINA = TESOURA | VOCÊ = PEDRA |')
        print('\033[32mVITÓRIA!\033[m')
    elif maquina == 1:
        print('MÁQUINA = PEDRA | VOCÊ = PEDRA |')
        print('\033[32mSEM VENCEDOR!\033[m')
elif player == 2:
    if maquina == 1:
        print('MÁQUINA = PEDRA | VOCÊ = PAPEL |')
        print('\033[32mVITÓRIA!\033[m')
    elif maquina == 2:
        print('MÁQUINA = PAPEL | VOCÊ = PAPEL |')
        print('\033[35mSEM VENCEDOR!\033[m')
    elif maquina == 3:
        print('MÁQUINA = TESOURA | VOCÊ = PAPEL |')
        print('\033[31mDERROTA!\033[m')
elif player == 3:
    if maquina == 1:
        print('MÁQUINA = PEDRA | VOCÊ = TESOURA |')
        print('\033[31mDERROTA!\033[m')
    elif maquina == 2:
        print('MÁQUINA = PAPEL | VOCÊ = TESOURA |')
        print('\033[32mVITÓRIA!\033[m')
    elif maquina == 3:
        print('MÁQUINA = TESOURA | VOCÊ = TESOURA |')
        print('\033[35mSEM VENCEDOR!\033[m')
else:
    print('Opção inválida. Tente novamente!')

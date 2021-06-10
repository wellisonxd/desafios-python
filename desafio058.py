from random import randrange
from time import sleep

print('===== JOGO DA ADIVINHAÇÃO =====')
print('QUAL SERÁ O NÚMERO QUE ESCOLHI?')

cont = 1
num = int(input('Qual o número de [1 a 10]? '))
ale = randrange(1, 10)

print('PROCESSANDO...')
sleep(1)

if num > 10 or num < 1:
    print('=-=-= DIGITOU ERRADO! =-=-=')
    print('=-=-= Digite um número entre 1 ~ 10 =-=-=')
elif num != ale:
        print('QUE PENA! O número era {} e você escolheu {}. Tente novamente.'.format(ale, num))

while num != ale: 
    num = int(input('Digite outro entre [1 e 10]? '))
    ale = randrange(1, 10)
    cont += 1

    print('PROCESSANDO...')
    sleep(1)

    if num > 10 or num < 1:
        print('=-=-= DIGITOU ERRADO! =-=-=')
        print('=-=-= Digite um número entre 1 ~ 10 =-=-=')
    elif num != ale:
        print('QUE PENA! O número era {} e você escolheu {}. Tente novamente.'.format(ale, num))

if num == ale:
    print('PARABÉNS! O número era {} e você escolheu o {}.'.format(ale, num))
    print('Você precisou de {} tentativas.'.format(cont))

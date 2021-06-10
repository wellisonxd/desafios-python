from random import randrange
from time import sleep

print('===== JOGO DA ADIVINHAÇÃO =====')
print('QUAL SERÁ O NÚMERO QUE ESCOLHI?')
num = int(input('Qual o número de [1 a 5]? '))
ale = randrange(1, 5)

print('PROCESSANDO...')
sleep(3)

if num > 5 or num < 1:
    print('=-=-= DIGITOU ERRADO! =-=-=')
    print('=-=-= Digite um número entre 1 ~ 5 =-=-=')
elif num == ale:
    print('PARABÉNS! O número era {} e você escolheu o {}.'.format(ale, num))
else:
    print('QUE PENA! O número era {} e você escolheu {}. Tente novamente.'.format(ale, num))

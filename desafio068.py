from random import randint
print('=-='*10)
print('JOGO DO PAR OU ÍMPAR')
print('=-='*10)
contP = 0
while True:
    n = int(input('Digite um número para jogar: '))
    game = str(input('Par ou Impar [P/I]? ')).strip().upper()[0]
    comp = randint(1, 5)
    print(f'Maquina escolheu {comp}.')
    resul = (n + comp) % 2
    if game == 'P' and resul == 0:
        contP += 1
        print('VOCÊ VENCEU! JOGUE DE NOVO ')
        print('=-='*10)
    elif game == 'I' and resul == 1:
        contP += 1
        print('VOCÊ VENCEU! JOGUE DE NOVO ')
        print('=-='*10)
    else:
        print('VOCÊ PERDEU!')
        print('=-='*10)
        break
print(f'Jogo acabou! Você teve {contP} vitórias.')
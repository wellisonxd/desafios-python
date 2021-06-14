extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 
'quatorze', 'quinze', 'dezesseis', 'dezessete', 
'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número [0 e 20]: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')

    print(f'O numero {num} por extenso é {extenso[num]}')
    resp = str(input('Quer continuar no app [S/N]? ')).strip().upper()
    if resp == 'N':
        break

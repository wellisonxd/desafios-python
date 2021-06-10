frase = str(input('Digite alguma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverter = juntar[::-1]

#for letra in range(len(juntar) - 1, -1, -1):
#    inverter += juntar[letra]

print('O inverso de {} é {}!'.format(juntar, inverter))
if inverter == juntar:
    print('Temos um palíndromo!')
else:
    print('A frase nao é palíndroma!')
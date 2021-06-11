confirma = 'S'
media = cont = maior = menor = soma = 0
while confirma in 'Ss':
    num = int(input('Informe um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else: 
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    confirma = str(input('Deseja digitar mais números? [S/N] ')).strip().upper()[0]
media = soma / cont
print('A soma de {} nºs deu {}. A média entre eles deu {}, o maior valor é {} e o menor valor é {}'.format(cont, soma, media, maior, menor)) 

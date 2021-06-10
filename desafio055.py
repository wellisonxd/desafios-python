maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa (kg): '.format(c)))
    if c == 1:
        maior, menor = peso, peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso foi {} e o MENOR {}'.format(maior, menor))

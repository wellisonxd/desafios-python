soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        cont += 1
        soma += num
print('A soma de {} números pares digitados é {}.'.format(cont, soma))
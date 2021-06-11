num = int(input('Digite um número [999 para parar]: '))
cont = 0
total = 0
while num != 999:
    cont += 1
    total += num
    num = int(input('Digite mais um número: '))
print('O resultado foi = a soma de {} nºs digitados, deu {}!'.format(cont, total))
num = int(input('Digite um número para saber seu Fatorial: '))
cont = num
multi = 1
while cont > 0:
    multi *= num
    num -= 1
print(multi)
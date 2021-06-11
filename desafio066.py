cont = total = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    total += n
print(f'Foram digitados {cont} e o soma deles é {total}')
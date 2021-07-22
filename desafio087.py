matriz = [[], [], []]
somaPares = somaT = maior = 0
for c in range(3):
    for i in range(3):
        num = int(input(f'Digite o espaço [{c}, {i}]: '))
        matriz[c].append(num)
        if num % 2 == 0:
            somaPares += num

for i in range(len(matriz)):
    somaT += matriz[i][2]
    for c in matriz[i]:
        if i == 1:
            if c >= maior:
                maior = c
        print(f'[{c:^5}] ', end='')
    print()

print(f'A soma de todos os pares na matriz é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaT}.')
print(f'O maior valor da segunda linha é {maior}')

matriz = [[], [], []]
for i in range(len(matriz)):
    for c in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {c+1}] = ')))
print('=-' * 20)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}] ', end='')
    print()

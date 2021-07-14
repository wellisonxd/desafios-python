geral = []
pares = []
impares = []
for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        if c == 0 or num >= pares[-1]:
            pares.append(num)
        else:
            for pos, i in enumerate(pares):
                if num < i:
                    pares.insert(pos, num)
                    break
    else:
        if len(impares) == 0 or num >= impares[-1]:
            impares.append(num)
        else:
            for pos, im in enumerate(impares):
                if num < im:
                    impares.insert(pos, num)
                    break
geral.append(pares[:])
geral.append(impares[:])
print(f'Os valores PARES digitados foram: {geral[0]}')
print(f'Os valores IMPARES digitados foram: {geral[1]}')

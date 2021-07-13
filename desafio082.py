valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if r in 'Nn':
        break
for c in range(len(valores)):
    if valores[c] % 2 == 0:
        pares.append(valores[c])
    else:
        impares.append(valores[c])
print(f'A lista completa {valores}')
print(f'A lista só com nºs pares {pares}')
print(f'A lista só com os nº impares {impares}')

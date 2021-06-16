valores = []
maior = menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite o {c+1}º valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('=-=' * 20)            
print(f'Você digitou os valores {valores}')
print(f'O maior valor é {maior} e sua posição é... ', end='')
for pos, i in enumerate(valores):
    if i == maior:
        print(f'{pos}...', end='')
print(f'\nO menor valor é {menor} e sua posição é... ', end='')
for pos, i in enumerate(valores):
    if i == menor:
        print(f'{pos}...', end='')

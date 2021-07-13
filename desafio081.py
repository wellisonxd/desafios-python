valores = list()
while True:
    valores.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if r in 'Nn':
        break
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 NÃO faz parte da lista!')
else:
    print('O valor 5 FAZ parte da lista!')
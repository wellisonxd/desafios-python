def maior(* num):
    maior = 0
    print('Os números escolhidos foram: ', end='')
    for cont in num:
        print(f'{cont}', end=' ')
        if cont > maior:
            maior = cont
    print(f'\nO maior número de uma lista de {len(num)} é {maior}')
    print('=-=' * 20)

print('=-= Descobrindo o maior número com FUNÇÃO =-=')
maior(2, 5, 9, 5, 3, 15, 2, 1)
maior(5, 2, 3, 5, 2, 4, 10, 1, 0, 1)
maior(4, 7, 0)
maior(6)
maior()
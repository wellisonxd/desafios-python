lista = ('Feijão', 7.90, 'Arroz', 4.60, 'Macarrão', 1.89, 'Grão de Bico', 6.99, 'Lentilha', 7.50,
        'Cebola', 2.99, 'Carne', 51.25, 'Frango', 14.69, 'Farinha', 2.99)
print('-='*20)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-='*20)
c = 1
n = 0
for i in range(0, 9):
    print(f'{lista[n]:.<30}R$ {lista[c]:>5.2f}')
    c += 2
    n += 2
print('-='*20)

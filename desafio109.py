import moeda

num = float(input('Digite o preço: R$'))

print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10)}')
print(f'Diminuindo 22%, temos {moeda.diminuir(num, 22, True)}')
print('===== PRODUTO COM DESCONTO DE 5% =====')
prod = input('Digite o nome do produto: ')
preco = float(input('Digite o valor original do produto: R$'))
des = preco * 0.95
print('{} com desconto fica R${:.2f}. Deseja comprar? '.format(prod, des))
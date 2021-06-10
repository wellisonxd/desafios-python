print('{:=^40}'.format('| LOJAS WELLISON |'))
nome = str(input('Qual o nome do produto? ')).strip()
preco = float(input('Qual o valor do produto? R$'))
print('''Qual a forma de pagamento?
[ 1 ] A VISTA DINHEIRO/CHEQUE [ 1 ]
[ 2 ] A VISTA NO CARTÃO [ 2 ]
[ 3 ] 2x NO CARTÃO [ 3 ]
[ 4 ] 3x OU MAIS NO CARTÃO [ 4 ]''')
forma = int(input('Sua Opção: '))

if forma == 1:
    preco = preco * 0.90
    print('O valor que você pagará pelo(a) {} será R${:.2f}'.format(nome, preco))
elif forma == 2:
    preco = preco * 0.95
    print('O valor que você pagará pelo(a) {} será R${:.2f}'.format(nome, preco))
elif forma == 3:
    print('O valor que você pagará pelo(a) {} será R${:.2f}'.format(nome, preco))
    print('O valor mensal em x2 é R${:.2f}'.format(preco / 2))
elif forma == 4:
    parc = int(input('Em quantas vezes sera? '))
    preco = preco * 1.20
    print('O valor que você pagará pelo(a) {} será R${:.2f}'.format(nome, preco))
    print('O valor mensal em x{} é R${:.2f}'.format(parc, preco / parc))
else:
    print('Opção Inválida! Tente novamente!')
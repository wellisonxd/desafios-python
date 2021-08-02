def area(base, altura):
    area = base * altura
    print(f'A área de um terreno {base} x {altura} é de {area}m²')


print('   Controle de terrenos')
print('---' * 20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
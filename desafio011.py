print('===== QUANTO DE TINTA COMPRAR =====')
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = largura * altura
tinta = area / 2
print('Você irá precisar de {} litros de tinta para pintar a sua parede de {}m²!'.format(tinta, area))
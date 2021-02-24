print('=' * 20)
print('    WELL ALUGUEL    ')
print('=' * 20)
print(' ' * 20)
d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos KM você percorreu com o veículo? '))

dias = d * 60.0
kmt = km * 0.15

print('O preço por dias utilizados fica R${:.2f}.'.format(dias))
print('O preço por KM rodado fica R${:.2f}.'.format(kmt))
print('O total do aluguel do veículo ficou R${:.2f}'.format(dias + kmt))
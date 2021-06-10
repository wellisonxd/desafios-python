dist = float(input('Informe a distância da viagem em KM: '))

if dist <= 200.0:
    valor = dist * 0.50
    print('O valor da sua viagem de {}KM será de R${:.2f}'.format(dist, valor))
else:
    valor = dist * 0.45
    print('O valor da sua viagem de {}KM será de R${:.2f}'.format(dist, valor))

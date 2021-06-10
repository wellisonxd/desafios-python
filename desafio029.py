velo = float(input('Qual foi a velocidade do carro que passou? '))

if velo > 80:
    print('O veículo ultrapassou o limite de 80KM')
    multa = (velo - 80) * 7.0
    print('A multa dele será no valor de R${:.2f}'.format(multa))
else:
    print('O veículo não ultrapassou o limite de velocidade!')
    print('=-=-= LIBERADO =-=-=')
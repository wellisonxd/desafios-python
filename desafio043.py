peso = float(input('Informa seu peso em KG = '))
altura = float(input('Informe sua altura = '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você está ABAIXO DO PESO. IMC => {:.2f}'.format(imc))
elif imc <= 25.0:
    print('Você está com o PESO IDEAL. IMC => {:.2f}'.format(imc))
elif imc <= 30.0:
    print('Você está com SOBREPESO. IMC => {:.2f}'.format(imc))
elif imc <= 40.0:
    print('Você está com OBESIDADE. IMC => {:.2f}'.format(imc))
else:
    print('Você está com OBESIDADE MÓRBIDA. IMC => {:.2f}'.format(imc))

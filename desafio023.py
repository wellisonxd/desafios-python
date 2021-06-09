digito = int(input('Digite um numero: '))
u = digito // 1 % 10
d = digito // 10 % 10
c = digito // 100 % 10
m = digito // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
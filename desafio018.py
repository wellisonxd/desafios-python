from math import hypot, sin, tan, cos
co = float(input('Digite o cateto oposto = '))
ca = float(input('Digite o cateto adjacente = '))
h = hypot(co, ca)
print('Os valores que temos:\n Cateto Oposto = {}\n Cateto Adjacente = {}\n Hipotenusa = {:.2f}'.format(co, ca, h))
seno = co / h
cosseno = ca / h
tangente = co / ca
print('O valor do seno é {:.3f}'.format(seno))
print('O valor do cosseno é {:.3f}'.format(cosseno))
print('O valor da tangente é {:.3f}'.format(tangente))

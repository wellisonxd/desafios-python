from math import sqrt, hypot
oposto = float(input('Digite o comprimento do cateto oposto = '))
adj = float(input('Digite o comprimento do cateto adjacente = '))
#hipo = (oposto ** 2 + adj ** 2) ** (1/2) 
hipo = sqrt(pow(oposto, 2) + pow(adj, 2))
#hipo = hypot(oposto, adj) importando da biblio
print('O comprimento da hipotenusa é {:.2f}.'.format(hipo))
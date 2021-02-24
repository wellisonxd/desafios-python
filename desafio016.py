from math import floor, trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, floor(num)))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))
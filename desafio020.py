from random import shuffle
print('== Ordem de apresentação de trabalho ==')
n1 = input('Digite o nome do aluno: ')
n2 = input('Digite o nome de outro aluno: ')
n3 = input('Digite outro nome de aluno: ')
n4 = input('Digite o último nome de aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação dos trabalhos será: ')
print(' 1º {}\n 2º {}\n 3º {}\n 4º {}'.format(lista[0], lista[1], lista[2], lista[3]))
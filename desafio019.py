from random import choice
print('Quem irá apagar o quadro? ')
nome1 = input('Digite o nome do 1º aluno: ')
nome2 = input('Digite o nome do 2º aluno: ')
nome3 = input('Digite o nome do 3º aluno: ')
nome4 = input('Digite o nome do 4º aluno: ')
lista = [nome1 , nome2, nome3, nome4]
apagar = choice(lista)
print('Após o sorteio o aluno que irá apagar o quadro é... {}'.format(apagar))

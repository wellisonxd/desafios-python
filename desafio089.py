cadastro = list()
pessoa = list()
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('NOTA 1: ')))
    pessoa.append(float(input('NOTA 2: ')))
    cadastro.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Deseja continuar [S/N]? '))[0]
    if resp in 'Nn':
        break
print(cadastro)
print('-' * 30)
print('No.  NOME          MÉDIA')
print('-' * 30)
for n in range(len(cadastro)):
    print(f'{n:<5}', end='')
    #for c in range(2):
    print(f'{cadastro[n][0]:14}', end='')
    media = (cadastro[n][1] + cadastro[n][2]) / 2
    print(f'{media:.2f}')
print('-' * 30)
escolha = int(input('Digite o ID do aluno p/ saber detalhes [digite 999 p/ encerrar]: '))
while escolha != 999:
    print(f'Notas de {cadastro[escolha][0]} são {cadastro[escolha][1:]}')
    print('-' * 30)
    escolha = int(input('Digite o ID do aluno p/ saber detalhes [digite 999 p/ encerrar]: '))
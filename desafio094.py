cadastroPessoas = list()
pessoas = dict()
contPeople = totIdade = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
    pessoas['idade'] = int(input('Idade: '))
    totIdade += pessoas['idade']
    cadastroPessoas.append(pessoas.copy())
    while True:
        resp = str(input('Deseja continuar com outro cadastro [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
for i in range(len(cadastroPessoas)):
    totIdade += cadastroPessoas[i]['idade']
    contPeople += 1
media = totIdade / len(cadastroPessoas)
print('-=-' * 30)
print(f'A) Ao todo temos {len(cadastroPessoas)} pessoas cadastradas.')
print(f'B) A média da idade é de {media:.2f}')
print(f'C) As mulheres cadastradas foram ', end='')
for p in cadastroPessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}, ',end='')
print()
print(f'D) Listas de pessoas que estão acima da média: ')
for p in cadastroPessoas:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()



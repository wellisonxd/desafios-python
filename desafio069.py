cont_idade = cont_sexo = cont_F = 0
while True:
    idade = int(input('IDADE: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('SEXO [M/F]: ')).strip().upper()[0]
    
    if idade > 18:
        cont_idade += 1
    if sexo == 'M':
        cont_sexo += 1
    if sexo == 'F' and idade < 20:
        cont_F += 1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar mais 1 pessoa [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você cadastrou {cont_idade} com +18.')
print(f'{cont_sexo} homens.')
print(f'E {cont_F} mulheres com menos de 20 anos.')
sexo = 'n'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('SEXO: ')).strip().upper()[0]
    if sexo != 'M' and sexo != 'F':
        print('Opção inválida, digite corretamente.')
print('Obrigado, bom dia!')
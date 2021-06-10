totidade = 0
homem = 0
nomehomem = ''
totidademulher = 0

for c in range(1, 5):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('SEU NOME: ')).strip()
    idade = int(input('SUA IDADE: '))
    sexo = str(input('SEXO [F/M]: ')).upper()
    totidade += idade
    if sexo == 'M':
        if idade > homem:
            homem = idade
            nomehomem = nome
    elif sexo == 'F':
        if idade < 20:
            totidademulher += 1

print('Média de IDADE do grupo: {} anos'.format(totidade / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(homem, nomehomem))
print('Há {} mulheres com menos de 20 anos!'.format(totidademulher))

from datetime import date
atual = date.today().year

cont_maioridade = 0
cont_menoridade = 0
for c in range(1, 8):
    ano = int(input('Ano de Nascimento da {}º pessoa: '.format(c)))
    maior = atual - ano
    if maior >= 18:
        cont_maioridade += 1
    else:
        cont_menoridade += 1

print('Quantidade de Pessoas que atingiram a maioridade: {}'.format(cont_maioridade))
print('QUantidade de Pessoas que NÃO atingiram a menoridade {}'.format(cont_menoridade))
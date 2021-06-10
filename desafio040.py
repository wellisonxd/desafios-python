nota1 = float(input('PRIMEIRA NOTA: '))
nota2 = float(input('SEGUNDA NOTA: '))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print('Aluno APROVADO!!! Média {:.1f}'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Aluno em RECUPERAÇÃO! Média {:.1f}'.format(media))
elif media < 5.0:
    print('Aluno REPROVADO! Média {:.1f} :('.format(media))
else:
    print('Algo está errado.')

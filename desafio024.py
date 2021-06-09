cidade = str(input('CIDADE: ')).strip()
cidadeS = cidade.upper().split()
con = 'SANTO' in cidadeS[0]
print('O nome da sua cidade {} começa com SANTO? {}'.format(cidade, con))
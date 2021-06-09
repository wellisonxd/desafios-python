nome = str(input('Digite seu nome completo: ')).strip()
nomeC = nome.split()
ult = nome.rfind(' ')
print('Seu primeiro nome é {} e seu último nome é {}'.format(nomeC[0], nome[ult+1:]))

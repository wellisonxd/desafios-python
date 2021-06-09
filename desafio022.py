nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em MAIÚSCULO: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))

nomeCont = len(''.join(nome.split()).lower())
nomeP = nome[:nome.find(' ')]
nomePrim = len(nome[:nome.find(' ')])
#nomePrim = nome.split()
#nomePrim = len(nomePrim[0])

print('O seu nome tem {} letas (sem os espaços).'.format(nomeCont))
print('O seu primeiro nome é {} e tem {} letras.'.format(nomeP, nomePrim))

frase = str(input('Digite uma frase: ')).strip().lower()

print('Na frase digitada aparece {} letra [A]'.format(frase.count('a')))
print('A primeira vez que a letra [A] aparece é na posição {}'.format(frase.find('a')+1))
print('A última vez que a letra [A] aparece é na posição {}'.format(frase.rfind('a')+1))

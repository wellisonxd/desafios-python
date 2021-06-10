num = int(input('Informe um numero: '))
print('''[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL''')
base = int(input("Sua opção: "))

if base == 1:
    print('O {} em BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif base == 2:
    print('O {} em OCTAL é {}.'.format(num, oct(num)[2:]))
elif base == 3:
    print('O {} em HEXADECIMAL é {}.'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVÁLIDA. FAÇA NOVAMENTE.')
l1 = float(input('Informe o 1º lado: '))
l2 = float(input('Informe o 2º lado: '))
l3 = float(input('Informe o 3º lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os valores {}, {} e {} \033[0;32mFORMAM\033[m um triângulo!'.format(l1, l2, l3))
    if l1 == l2 == l3:
        print('... e o seu triângulo é EQUILÁTERO!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('... e o seu triângulo é ISÓSCELES!')
    elif l1 != l2 != l3 != l1:
        print('... e o seu triângulo é ESCALENO!')
else:
    print('Os valores {}, {} e {} \033[0;31mNÃO\033[m formam um triângulo!'.format(l1, l2, l3))
    
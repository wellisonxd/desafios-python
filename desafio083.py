expre = str(input('Digite a expressão: '))
contA = contB = 0
for c in expre[:]:
    if c == '(':
        contA += 1
    elif c == ')':
        contB += 1
if contA == contB:
    print('Expressão válida.')
else:
    print('Expressão não válida.')
valores = []
for c in range(0,5):
    num = int(input('Informe um número: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
    else:
        for pos, i in enumerate(valores):
            if num <= i:
                valores.insert(pos, num)
            break
print(valores)
        

while True:
    n = int(input('Quer ver a tabuada de qual nº: '))
    if n <= 0:
        break
    for c in range(1, 11):
        mult = c * n
        print(f'{n} X {c} = {mult}')
print('PROGRAMA ENCERRADO COM SUCESSO! Volte sempre.')
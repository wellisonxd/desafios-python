def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Erro! Digite um numeros')
    return num


n = leiaInt('Digite um numero: ')
print(f'O numero digitado foi {n}.')
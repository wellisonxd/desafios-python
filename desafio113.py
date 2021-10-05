def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite um número REAL válido!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário!')
            return 0
        else:
           return num

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Por favor digite um número INTEIRO válido!')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário!')
            return 0
        else:
           return num

num = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num} e o real {num2}')
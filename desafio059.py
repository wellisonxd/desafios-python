from time import sleep

num1 = int(input('Informe o 1º número: '))
num2 = int(input('Informe o 2º número: '))

escolha = 0
while escolha != 5:
    print('==-== O que deseja fazer com esses dois números? ==-==')
    print('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] DIGITE NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    escolha = int(input())
    if escolha == 1:
        print('A soma é: {}'.format(num1 + num2))
    elif escolha == 2:
        print('A multiplicação entre eles é: {}'.format(num1 * num2))
    elif escolha == 3:
        if num1 > num2:
            print('O maior número entre eles é: {}'.format(num1))
        elif num2 > num1:
            print('O maior número entre eles é: {}'.format(num2))
        else:
            print('Os números são iguais!')
    elif escolha == 4:
        num1 = int(input('Informe outro número: '))
        num2 = int(input('Informe mais outro número: '))
    elif escolha == 5:
        print('Programa ENCERRADO!')
    else:
        print('Opção inválida! Digite um número válido no MENU!')
    sleep(2)

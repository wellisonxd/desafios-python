casa = float(input('Informe o valor da casa = R$'))
salario = float(input('Informe seu sálario = R$'))
anos = int(input('Informe em quantos ano pretende pagar = '))

meses = anos * 12
casa_mes = casa / meses
salario_30 = salario * 0.30

if casa_mes <= salario_30:
    print('=-= PARABÉNS! SEU EMPRÉSTIMO FOI APROVADO! =-=')
    print('CASA AVALIADA: R${:.2f}'.format(casa))
    print('MENSALIDADE: R${:.2f} x{} meses'.format(casa_mes, meses))
else:
    print('=-= EMPRÉSTIMO REPROVADO =-=')
    print('O valor da mensalidade ultrapassa 30% do seu salário')
    print('MENSALIDADE: R${:.2f}'.format(casa_mes))
    print('SEU SALÁRIO: R${:.2f} // 30% SALÁRIO: R${:.2f}'.format(salario, salario_30))

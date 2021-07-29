from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
anoNasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - anoNasc
trabalhador['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
trabalhador['aposentar'] = (trabalhador['contratacao'] + 35) - anoNasc
print()
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}')
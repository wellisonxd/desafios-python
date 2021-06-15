numeros = (int(input('Digite quatro numeros: ')), int(input('Digite quatro numeros: ')), 
int(input('Digite quatro numeros: ')), int(input('Digite quatro numeros: ')))
print(f'A) Quantas vezes aparece o valor 9? {numeros.count(9)}')
if numeros.count(3) == 0:
    print(f'B) Em que posição foi digitado o primeiro valor 3? NÃO FOI DIGITADO')
else:
    print(f'B) Em que posição foi digitado o primeiro valor 3? {numeros.index(3)+1}ª posição')
print(f'C) Quais foram os números pares digitados? ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')

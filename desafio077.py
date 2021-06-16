palavras = ('amor', 'bela', 'joao', 'carinho', 'abelha', 'jegue',
            'sabor', 'jotape', 'sentimento')
for i in palavras:
    print(f'\nNa palavras {i.upper()} temos as vogais = ', end='')
    for l in i:
        if l.lower() in 'aeiou':
            print(l, end=' ')
    

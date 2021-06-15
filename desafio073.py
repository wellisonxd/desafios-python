colocacao = ('Bragantino', 'Bahia', 'Ceará', 'Fortaleza', 'Athletico-PR',
'Flamengo', 'Atlético-GO', 'Sport Recife', 'Juventude', 'Cuiabá', 'Internacional',
'São Paulo', 'Fluminense', 'Grêmio', 'Atlético-MG', 'América-MG', 'Palmeiras', 'Corinthians',
'Chapecoense', 'Santos')

print(f'Os 5 primeiros colocados são {colocacao[:5]}')
print(f'Os 4 últimos colocados são {colocacao[16:20]}')
print(f'Times em ordem alfábetica: {sorted(colocacao)}')
print(f'Chapecoense está na {colocacao.index("Chapecoense")+1}º posição.')
def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    resu = ano_atual - ano_nasc
    if resu >= 18 and resu < 60:
        return "VOTO OBRIGATORIO"
    elif resu == 16 or resu == 17 or resu >= 60:
        return "VOTO OPCIONAL"
    else:
        return "VOTO NEGADO"


print(voto(int(input('Qual seu ano de nascimento: '))))

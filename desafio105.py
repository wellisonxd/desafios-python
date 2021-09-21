def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e situações de varios alunos
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situacao
    :return: dicionario com varias informacoes sobre as notas da turma
    """
    dados = {}
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)
    if sit:
        if dados['media'] <= 5:
            dados['situação'] = 'RUIM'
        elif dados['media'] <= 8:
            dados['situação'] = 'BOA'
        else:
            dados['situação'] = 'ÓTIMA'
    return dados


resp = notas(5.0, 6.5, 9.0, 8.0)
print(resp)
help(notas)
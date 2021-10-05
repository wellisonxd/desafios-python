import bibli115
from time import sleep

arq = 'cursoemvideo.txt'

if not bibli115.arquivoExiste(arq):
    bibli115.criarArquivo(arq)

bibli115.cabecalho('PRIMEIRO SISTEMA SIMPLES')
while True:
    resposta = bibli115.menu(['Ver Pessoas Cadastradas', 'Cadastrar Novas Pessoas', 
                'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo
        bibli115.lerArquivo(arq)
    elif resposta == 2:
        bibli115.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = bibli115.leiaInt('Idade: ')
        bibli115.cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(2)
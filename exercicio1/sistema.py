"""crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
O sistema so vai ter 2 opções: CADASTRAR uma nova pessoa e LISTAR todas as pessoas cadastradas."""
from exercicio1.lib.interface import *
from exercicio1.lib.arquivo import *
from time import sleep

arq = 'Cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        # Opção  de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa!
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = leiaInt('Idade: ')
        cadastrarPessoa(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...Até logo.')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
        sleep(2)

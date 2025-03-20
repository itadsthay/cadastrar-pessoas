from exercicio1.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro ao criar o arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            if isinstance(linha, str):
                dado = linha.split(',')
                if len(dado) > 1 and isinstance(dado[1], str):
                    dado[1] = dado[1].replace('\n', '')
                    print(f'{dado[0]:<30}{dado[1]:>3} anos')
                else:
                    print(f"Erro: linha mal formatada - {linha}")
            else:
                print(f"Erro: linha não é uma string - {linha}")
    finally:
        a.close()


def cadastrarPessoa(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome},{idade}\n')
        except:
            print('Houve um erro ao escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionados com sucesso')
            a.close()

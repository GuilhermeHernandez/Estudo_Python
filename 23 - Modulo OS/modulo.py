'''
OS
Tarefas de arquivos , pastas e etc
    - os.getcwd() -> Diretorio de trabalho atual
    - os.curdir -> Diretorio atual
    - os.listdir() -> Lista todos os diretorios,
    - os.chdir('C:\\') -> Vai ate o diretorio informado no caso C:
    - os.mkdir('caminho_da_pasta ou so o nome') -> Cria pasta
    - caminho_completo = os.path.join(pasta_pai,pasta_nova) -> Cria um objeto de caminho
    - os.rename('nome_atual','novo_nome') -> Renomeia a pasta
    - os.rmdir('nome_pasta') -> Remove pasta quando ela estiver vazia
    - os.path.basename(os.getcwd()) -> Retorna o nome da pasta atual
    - os.path.dirname(os.getcwd()) -> Retorna o nome do diretorio que a pasta esta
    - os.path.exists('caminho') -> Retorna True se o caminho existe
    - os.path.isdir('caminho') -> Retorna true se o caminho for diretorio
    - os.path.isfile('caminho') -> Retorna True se for arquivo
    - os.path.splitext('arquivo') -> Retorna texto separados em uma lista 
    - os.remove('nome_arquivo') -> Exclui arquivo 

    Ex Criação de diversas pastas
        - pasta_pai = os.getcwd()
        - novas_pasta = 'America\\Brasil\\Ilhabela'
        - caminho = os.path.join(pasta_pai,novas_pasta)
        - os.makedirs(caminho) -> Cria recursivamente as pastas
        
        
PATHLIB
Parecido com OS 
    - pathlib.Path() -> Caminho atual 

Shutil
    - shutil.rmtree('Caminho') -> Remove a arvore de pastas
'''


# Renomenado todos os arquivos de uma pasta 
import os

pasta_arquivos = os.chdir('C:\\Users\\guilherme.batista\\Desktop\\Curso_Python\\Estudo_Python_FullStack\\23 - Modulo OS\\Arquivos')

padrao_nome = input("Qual o padrão de nome que o arquivo vai usar (sem extensão) : ")

# Para cada arquivo na pasta ele tem um contador
for contador , arq in enumerate(os.listdir(pasta_arquivos)):

    # Se for arquivo
    if os.path.isfile(arq):

        # Nome arquivo e Extensão do arq(.txt)
        nome_arq , ext_arq = os.path.splitext(arq)

        # novo padrão de nome do arquivo
        nome_arq = padrao_nome + '_' + str(contador)

        # Novo nome de arquivo com extensão
        nome_novo = f'{nome_arq}{ext_arq}'

        os.rename(arq,nome_novo)

print(f'\nArquivos renomeados.')
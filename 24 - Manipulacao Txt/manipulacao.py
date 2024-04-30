'''

Manipulação de arquivo

Open() -> Retorna o manipulador de arquivos
    - r -> Somente leitura 
    - r+ -> Leitura e escrita , texto inserido no inicio do arquivo
    - w -> Escrita , apagando (truncado ) o conteudo existente no arquivo
    - w+ -> Leitura e escrita . O arquivo é criado , se não existir ; se existir é truncado . O texto é inserido no inicio do arquivo
    - a -> Escrita , preservando o conteudo existente (append). O arquivo é criado , se não existir . O texto é inserido no final do arquivo
    - b -> Modo binario 
    - + -> Atualização - Leitura e escrita
    - x -> Abre o arquivo para criação exclusiva , falhando se o arquivo ja existir

'''

# ---> Criando o manipulador 
manipulador = open(fr'C:\Users\guilherme.batista\Desktop\Curso_Python\Estudo_Python_FullStack\24 - Manipulacao Txt\arquivo.txt','r',encoding='UTF-8')

# print(f'Usando o metodo read(): \n')
# print(manipulador.read(),'\n')

# ---> Mostrando apenas uma linha

# print(f'Usando o metodo readline(): \n')
# print(manipulador.readline())
# print(manipulador.readline())

# ---> Readlines() -> Retorna uma lista , e cada linha é um item da lista

# print(f'Usando o metodo readlines(): \n')
# print(manipulador.readlines())

# ---> Ler arquivos txt
# texto = input('Qual termo deseja procurar no arquivo ?')

# try:
#     manipulador = open(fr'C:\Users\guilherme.batista\Desktop\Curso_Python\Estudo_Python_FullStack\24 - Manipulacao Txt\arquivo.txt','r',encoding='UTF-8')

#     for linha in manipulador:

#         linha = linha.strip()

#         if texto in linha:
#             print(f'A string foi encontrada!')

#         else:
#             print('String não encontrada !')


# except IOError:
#     print('Não foi possivel abrir o arquivo!')

# else:
#     manipulador.close()

texto = 'Variavel que armazena o texto , e vamos inserir ela no arquivo,txt'

# ---> Escrevendo em arquivo de texto porem apagando tudo escrito antes
try:
    # ---> Criando o manipulador 
    manipulador = open(fr'C:\Users\guilherme.batista\Desktop\Curso_Python\Estudo_Python_FullStack\24 - Manipulacao Txt\arquivo.txt','w',encoding='UTF-8')

    # Escrevendo
    manipulador.write('Criador Guilherme Hernandez DEV\n')

    # Escrevendo
    manipulador.write('\nCriando um arquivo de texto com pyhton')

except IOError:
    print('Não foi possivel abrir o arquivo!')

else:
    manipulador.close()


# ---> Escrevendo em arquivo de texto , apenas adicionas strings
try:
    # ---> Criando o manipulador 
    manipulador = open(fr'C:\Users\guilherme.batista\Desktop\Curso_Python\Estudo_Python_FullStack\24 - Manipulacao Txt\arquivo.txt','a',encoding='UTF-8')

    # Escrevendo
    manipulador.write('\nTreinando em python para virar FullStack')

    # Escrevendo
    manipulador.write('\nPython é usado para inteligencia artificial !')

    manipulador.write(f'\n{texto}')

except IOError:
    print('Não foi possivel abrir o arquivo!')

else:
    manipulador.close()


# ---> Criando um novo arquivo apartir de uma lista de valores 

frutas = ['Pera\n','Maça\n','Morango\n','Melancia\n','Amora\n','Limão']

try:
    manipulador = open('frutas.txt','w',encoding='UTF-8')

    manipulador.writelines(frutas)

except IOError:
    print('Não foi possivel criar ou manipular o arquivo!')

else:
    manipulador.close()

# ---> Lendo arquivo criado
try:
    manipulador = open('frutas.txt','r',encoding='UTF-8')

    print(manipulador.read())

except IOError:
    print('Não foi possivel criar ou manipular o arquivo!')

else:
    manipulador.close()
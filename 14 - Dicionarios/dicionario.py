'''

Dicionario
    Funcionamento baseado em Chave : Valor 

'''

elemento = {
    'Z': 3,
    'nome' : 'Litio',
    'grupo' : 'Metais Alcalinos',
    'densidade' : 0.534
}

# Acessando item
print(f'Elemento : {elemento['nome'].title()}')
print(f'Densidade : {elemento['densidade']}')
print(f'O dicionario possui : {len(elemento)} elementos')

# Atualizando 
elemento['grupo'] = 'Alcalinos'
print(f'Elemento agora faz parte do grupo dos : {elemento['grupo']}')

# Adicionando uma entrada
elemento['periodo'] = 1
print(elemento,"\n")

# Exclusão de item em dicionário
del elemento['periodo']
print(elemento)

# limpando o dicionario
#elemento.clear()
#print(elemento)

# Excluindo dicionario
#del elemento

# Retorna uma lista de tuplas do elemento
print(elemento.items(),"\n")

# Para cada chave : valor (tupla) na lista de elemento
for e in elemento.items():
    print(e)
print(f'\n')

# Para cada chave 
for chave in elemento.keys():
    print(chave)
print(f'\n')

# Para cada valor
for valor in elemento.values():
    print(valor)
print(f'\n')

# Retonando valores em 2 variavel de controle
for chave , valor in elemento.items():
    print(f'{chave} : {valor}')
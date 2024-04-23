'''

Compreensão de lista
    - Sintaxe :
        [expressão for i in lista_de_itens]

    - Dica : Usamos apenas para lista simples

'''

# -> Usando função Map

numeros = [1,4,7,9,10,12,21]

# quadrados = list(map(lambda x: x ** 2,numeros))

# print(quadradros)

# -> Usando compreensão de lista

quadrados = [num ** 2 for num in numeros]
print(quadrados)

# -> Criando lista de numeros pares de 0 a 10

pares = [i for i in range(11) if i % 2 == 0]
print(pares,'\n')

# - > quantidade de vogais
frase = 'A lógica é apenas o princípio da sabedoria , e não o seu fim.'
vogais = ['a','e','i','o','u','á','é','í','ó','ú']

lista_vogais = [letra for letra in frase if letra in vogais]
print(f'A frase possui : {len(lista_vogais)} vogais !')
print(lista_vogais,'\n')


# -> Trabalhando com 2 lista (Distributiva entre os valores)
Distributiva = [x * y for x in [1,2,3] for y in [10,20,30]]
print(Distributiva)
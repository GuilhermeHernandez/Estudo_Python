'''

Listas
    Representa uma sequencia de valores
    
    Sintaxe:
        - nome_da_lista = []
        - Indice começa no 0 e pode ser acessado[0]
            - podemos usar -1 para pegar o ultimo elemento da lista
        - Pode ser concatenada (+)
        - Pode alterar apenas 1 valor 
            - lista[0] = 9 
        - Slice[0:2]
            - lista[0:2] -> Apartida da posição 0 quero 2 valores 
        - Len() -> retorna o comprimento da lista
        - sorted(nome_lista,reverse=False) -> Organiza de forma crescente uma lista
        - sum() -> Retorna a soma de todos elementos
        - min() -> Retorna o menor valor de uma lista de elementos
        - max() -> Retorna o maior valor de uma lista de elementos
        - append() -> acrescenta um novo valor na lista
        - pop() -> Remove o ultimo elemento da lista
            - pop(3) -> Remove da uma posição especifica
        - insert(posição, valor) -> insere o valor em uma posição
        - valor in lista_valor -> retorna true ou false conforme a resposta
        - .sort() -> Orderna permanente na variavel 
        - sorted(obj) - Retorna ordenação temporaria
'''

# notas1 = [5,7,8,6,9]
# notas2 = [1,6,5,7,8]

# valores = notas1 + notas2

# valores[0] = 100

# print(valores[1])
# print(valores[:4])
# print(valores[-2:])
# print(len(valores))
# print(sorted(valores))
# print(sum(valores))
# print(min(valores))
# print(max(valores))

planetas = ['Mercúrio','Venus','Marte','Saturno','Urano','Netuno']

for planeta in planetas:
    print(planeta + ',',end='')


lista_bebida = []

for i in range(5):

    if (i == 0):
        bebida = input(f"\n\nDigite sua bebida favorita: ")
    else :
        bebida = input(f"Digite outra bebida favorita:")

    lista_bebida.append(bebida)

lista_bebida = sorted(lista_bebida)
print(f"\nBebida escolhida:")

for bebida in lista_bebida:
    print(f"\t{bebida}")
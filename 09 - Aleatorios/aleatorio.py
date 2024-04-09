'''

    Sorteio de numero aleatorios

    randint(v1,v2) -> Retorna um numero aleatorio ente v1 e v2 inteiro
    random() -> Retorna um numero aleatorio ente 0 e 1 de ponto flutuante
    round(valor,quantidade casa decimais) - arredonda o valor para int
    uniform(v1,v2) -> Retorna um numero aleatorio 
    choice(Lista) -> Retorna um numero de uma lista
    sample(lista,n de elemento..) -> Amostragem , retorna mais de um valor
    shuffle(lista) -> retorna uma lista embaralhada

'''
import random

print("\nGerar 5 numero aleatorios entre 1 e 50: \n")

for i in range(5):
    n = random.randint(1,50)
    
    print(f"\tNumero gerado : {n}")

print(f"\nGerar 5 numero aleatorio entra 0 e 10 : \n")

for i in range(5):
    vr = random.random()*10
    print(f"\tNumero gerado : {round(vr,2)}")

# Especifica inicio e fim
valor = random.uniform(1,100)
print(f"\nNumero : {round(valor,2)}")

# Exemplo 1 -> Retorno de um valor
lista = [2,4,6,9,10,13,15,27,85,6,4,91,564,21,78,44,6565,25,333]
n = random.choice(lista)
print(f"\nNumero escolhido : {n}")

# Exemplo 2 -> Retorno de mais de um valor de uma lista
n = random.sample(lista,3) 
print(f"\nNumero escolhido : {n}")

# Exemplo 3 -> Embaralhar
print(f"\nExibir a lista original: {lista}")
print(f"\nEmbaralhando a lista original")

random.shuffle(lista)

print(f"\n{lista}")
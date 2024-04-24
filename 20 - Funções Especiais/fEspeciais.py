from reduce import tools

# -> Funções lambda (anonimas)
'''
Sintaxe
    - lambda argumentos: expressões
'''

quardrado = lambda x: x**2

for i in range(1,11):
    print(quardrado(i))

par = lambda x: x %2 == 0
print(par(8))

f_c = lambda f: (f - 32) * 5/9
print(f_c(68))

# -> Função map()
'''
map(função, iteravel)
'''

num = [1,2,3,4,5,6,7,8,9]
dobro = list(map(lambda x: x * 2, num))

print(dobro)

palavras = ['Python','é','uma','linguagem','de','programação']
maiuscular = list(map(str.upper,palavras))

print(maiuscular)

# - > Função filter
'''

Filtra elementos de uma sequencia
filter(função,sequencia)

'''

def numeros_pares(num):
    return num % 2 == 0

numeros_ = [1,2,3,4,5,6,7,8,9,10,11,12,23]
num_par = list(filter(numeros_pares,numeros_))
print(num_par)

# Impares

num_impar = list(filter(lambda x: x % 2 !=0,numeros_))
print(num_impar)

# - > Função reduce()
'''

Aculmula um valor
    reduce(função,sequencia,valor_inicial)
'''

def mult (x , y):
    return x * y

numeros = [1,2,3,4,5,6,7,8,9,5,6,6,6,6]

total = reduce(mult,numeros)
print(total)
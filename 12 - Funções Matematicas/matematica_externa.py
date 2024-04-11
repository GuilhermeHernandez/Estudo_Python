'''

Funções matematicas externas (Modulo:Math)


'''

import math

x = 8 
y = 100

# Extraindo Raiz quadrada
raiz = math.sqrt(x)

# Arredondando pra cima retorno 
print(math.ceil(raiz))

# Arredondando pra baixo retorno 
print(math.floor(raiz))

# Arredondando  
print(round(raiz,2))

# Extraindo Logaritmo
logaritmo = math.log10(y)
print(logaritmo)

# Usando Pi
print(math.pi)

# Fatorial
print(math.factorial(x))

# Usando infinito
print(x / math.inf)
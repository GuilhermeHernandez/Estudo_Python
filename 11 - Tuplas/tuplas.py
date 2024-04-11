'''

Igual a lista porem é imutavel
    - sequencia de constantes
    - Não podemos organizar os elementos de uma tupla
        - Pordemos usar o metodo sort() -> Orderna permanente 
        - Podemos usar o memtodo sorted(obj) - Retorna ordenação temporaria

'''

tupla = (2,4,6,7,9)
# tupla[1] = 5

halogenios = ('F','Ci','Br','I','At')
gases_nobres = ('He','Ne','Ar','Xe','Kr','Rn')

# Juntando elementos em 1 lista 
elementos = halogenios + gases_nobres

# Numeros
numeros = (1,5,6,4,8,8,9,6,4,78,7,123,6,3,5,4,15,6)

print(len(halogenios))
print(halogenios)

print(gases_nobres[:2])

print(numeros.count(8),"\n")

# Percorrendo tupla
for elemento in halogenios:
    print(elemento)

#  Criando uma lista apartir da tupla
grupo17 = list(halogenios)

# Alterando lista
grupo17[0] = 'H'

print(grupo17,"\n")

# Criando uma lista apartir de uma tupla
grupo1 = ['Li','Na','K','Rb','Cs','Fr']
alcalinos = tuple(grupo1)

# Ordenando tupla
print(sorted(alcalinos),"\n")
#print(alcalinos.sort())
grupo1.sort(reverse=True)

print(grupo1)
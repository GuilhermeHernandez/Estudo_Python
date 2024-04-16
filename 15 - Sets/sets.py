'''

Conjuntos
    Coleções de valores não ordenado sendo unicos
    Não podemos mudar os itens de set
'''

planeta_anao = {'Plutão','Ceres','eris','haumea','makemake'}
print(planeta_anao)

# Tamanho de um set 
print(len(planeta_anao))

# Verificando se o conjunto tem um valor especifico armazenado nele
print('Ceres' in planeta_anao)

for astro in planeta_anao:
    print(astro.upper(),end=',')

astros = ['Lua','Venus','Sirius','Marte','Lua']
print(astros,end=',')

# Criando um novo set -> Remove duplicados
astros_sets = set(astros)
print("\n",astros_sets)

astros_2 = {'Plutão','Ceres','eris','haumea','makemake','Lua'}

# Comparando sets
print(astros_sets == astros_2)

# Unico conjuntos
print(astros_sets | astros_2)
print(astros_sets.union(astros_2))

# Intersecção -> Tras somente elementos que estão em ambas lista
print(astros_sets & astros_2)
print(astros_sets.intersection(astros_2))

# Diferença simetrica -> Diferença em ambos conjuntos
print(astros_sets ^ astros_2)
print(astros_sets.symmetric_difference(astros_2))

# Adicionando elemento em conjuntos
astros_2.add('Uranio')
astros_2.add('Sol')

print(astros_2)

# Removendo itens
astros_2.remove('makemake')
astros_2.discard('Lua')
astros_2.pop()

print(astros_2)
'''

    Sequencia de caracteres (igual lista)
        - tem indice 

'''

nome = 'guilherme'
sobrenome = 'hernandez'

# Capturando caracter individual
letra = nome[1]

print(letra)

# Tamanho da string
print(len(nome))

# Concatenando string 
print(nome + ' ' + sobrenome)

# Vamos separar as palavras pelo o espaço
#   - Retorna uma lista de string
frase = 'vamos aprender Python hoje.'
palavras = frase.split()
print(palavras[1],'\n')

for palavra in palavras:
    print(palavra)

# Iterando na string
for letra in nome:
    print(letra)

# Usando slices
print(frase[6:15])

# Usando find
email = input("Digite seu endereço de email : ")
arroba = email.find('@') # Retorna a posição do elemento na variavel ,
print(arroba)

# Sepando nome do usuario com nome do dominio
usuario = email[:arroba]
dominimo = email[arroba+1:]

print(f"Nome do usuario : {usuario}")
print(f"Nome do dominio : {dominimo}\n")

# Verificando se uma string esta em outra string
produtos = 'carbonato de sódio e óxido de zinco'

print('sódio' in produtos)
print('magnésio \n' not in produtos)

# Consultando a posição de uma string na string
item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos)

# Formatando string
objeto_celeste = 'galaxia esPiral M31'
print(objeto_celeste)

# Tudo maiuscula
print(objeto_celeste.upper())

# Tudo minuscula
print(objeto_celeste.lower())

# Primeira letra da frase
print(objeto_celeste.capitalize())

# Primeira letra de cada palavra
print(objeto_celeste.title())

# Exemplo
suplimento = 'cloreto de magnésio'
n_suplimento = suplimento.replace('magnésio','zinco')

print(suplimento)
print(n_suplimento)


# Exemplo de espaços em branco 
frase = '      o rato roeu a roupa do rei de roma     '
print(frase.lstrip())
print(frase.rstrip())
print(frase.strip())
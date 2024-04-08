'''
Variaveis

    - Precisa começar com letras , e espaço é _ .
    - Começar com letrar minusculas
    - Case sensitive (Diferencia letra maiuscula de minuscula)
    - Para atribuir um valor usamos (=)
    - Tipagem dinamica

'''

'''

Alt + Shift + Seta Baixa -> Duplica linha
Ctrl + K + C -> Comenta varias linhas
Ctrl + K + U -> Descomenta varias linhas 

'''

# ---> Atribuindo valores unicos
idade = 22
n1 = n2 = n3 = n4 = 0.0
verdadeiro = True
letra = 'c'

# ---> Atribuindo diversos valores
primeiro_nome , segundo_nome = 'Guilherme' , 'Hernandez'

# ---> Função : type() -> Retorna o tipo da variavel
print(type(idade))
print(type(n1))
print(type(verdadeiro))
print(type(letra))

# ---> Função : isinstance() -> Retorna verdadeiro se for do mesmo tipo
print(isinstance(idade , (int,float)))


a = 40 
b = 3 
resultado = a * b

print(resultado)
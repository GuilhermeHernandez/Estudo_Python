'''

Função 
    - Faz determinada tarefa 
    - pode ter parametros
    - Modularização
        - Reuso de codigo
        - Legibilidade

'''

# -> Definindo função sem argumento
def mensagem():
    print("Guilherme Hernandez Dev")
    print('Idade : 23')

# -> Definindo função com argumento
def soma (a,b):
    print(a + b)

# -> Definindo função com retorno
def mult(x,y):
    return x * y

def div(k,j):
    if j != 0:
        return k / j
    else:
        return "Impossivel dividir por 0"
    
# -> função com retorno e paramento uma lista
def quadrado(lista_valores):
    quadrados = []

    for valor in lista_valores:
        quadrados.append(valor ** 2)

    return quadrados

# -> Função sem retorno e com paramentros pre definidos
def contar(num=11,caracter='+'):
    for i in range(1,num):
        print(caracter)

# -> Função sem retorno com parametro cliente e 1 pre definido
def conta_(caracter,num=11):
    for numero in range(num):
        print(caracter)

# -> Função que muda de comportamento de acordo com os dados que o usuario passar
def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c

# mensagem()

# soma(12,3)

# a = 10
# b = 3
# c = resultado = mult(a,b)

# print(f"O produto de : {a} e {b} \nResulta : {c}")

if __name__ == '__main__':
    # a = int(input("Digite um numero:"))
    # b = int(input("Digite outro numero:"))

    # r = div(a,b)
    # print(f"{a} divido por {b} é igual : {r}\n")

    # valores = [2,5,7,9,12]
    # resultado = quadrado(valores)

    # for quadrado in resultado:
    #     print(quadrado)

    # -> Atribuindo outro valor para o caracter
    # contar(caracter='.')

    # -> Atribuindo os 2 paramentros pre definidos 
    # contar(num=6,caracter='@')

    # -> Atribuindo os 2 paramentros pre definidos , na ordem ja dos parametros
    # contar(3,'#')

    # -> Atribuindo os 1 paramentros obrigatorio
    # conta_('`')

    # -> multiplicação
    resultado = soma_mult(2,5)
    print(resultado)

    # -> soma
    resultado_ = soma_mult(1,5,4)
    print(resultado_)
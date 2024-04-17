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
    
def quadrado(lista_valores):
    quadrados = []

    for valor in lista_valores:
        quadrados.append(valor ** 2)

    return quadrados

mensagem()

soma(12,3)

# a = 10
# b = 3
# c = resultado = mult(a,b)

# print(f"O produto de : {a} e {b} \nResulta : {c}")

if __name__ == '__main__':
    a = int(input("Digite um numero:"))
    b = int(input("Digite outro numero:"))

    r = div(a,b)
    print(f"{a} divido por {b} é igual : {r}\n")

    valores = [2,5,7,9,12]
    resultado = quadrado(valores)

    for quadrado in resultado:
        print(quadrado)
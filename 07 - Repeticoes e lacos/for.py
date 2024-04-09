'''

Laços , repetições e incrementação

    Temos :
        - While -> Teste logico > Execução dos comandos
        - For -> Interador 

    += -> Atribução com incremento cls

    range(valorInicial,valorFinal,incremento) -> Função
        - O ultimo valor é excludente

'''

# ---> Criando lista 
lista = [2,6,9,4,0,12,3,7]
palavra = 'Guilherme'

# for item in lista:
#     print(item)

# for letra in palavra:
#     print(letra)

# ---> Exemplo 1
# for numero in range(1,11):
#     print(numero)

# ---> Exemplo 2
# for numero in range(11):
#     print(numero)

# ---> Exemplo 3
# nome = input("Digite seu nome: ")

# ---> Exemplo 4
# for i in range(10):
#     print(f"{i+1} {nome}")

# ---> Exemplo 4
# for i in range(2,21,2):
#     print(i)

# ---> Exemplo 5
# for i in range(20,2,-2):
#     print(i)

# Exemplos : Tuplas
pedras = ('Rubi','Esmeralda','Quartzo','Safira','Diamante','Turmalina')

for pedra in pedras:

    if (pedra == 'Quartzo'):
        continue # Pula a interação atual

    print(pedra)
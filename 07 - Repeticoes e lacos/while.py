'''

Laços , repetições e incrementação

    Temos :
        - While -> Teste logico > Execução dos comandos
        - For

    += -> Atribução com incremento cls


'''

# ---> While
# num = 1

# while (num <= 1000):
#     print(num)
#     num += 1
# print("Laço encerrado!")

# ---> Exemplo 1
nome = None

while (True):
    print("Digite seu nome ou X para parar : ")
    nome = input()

    if (nome == 'x' or nome == 'X'):
        break

    print(f"Bem-vindo : {nome}\n")

print("\nAté logo!")
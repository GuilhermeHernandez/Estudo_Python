'''

Exceção 
    Objeto que representa um erro que ocorreu ao executar o programa.

    Try -> Aonde pode ter um possivel erro 
    Except -> O tratamento 
        - Pode espeficiar a exceção

'''

def div(x,y):
    return round(x / y,2)

if __name__ == '__main__':

    while True:

        try:
            n1 = int(input("Digite um numero : "))
            n2 = int(input("Digite outro numero : "))
            break
        except ValueError:
            print("Ocorreu um erro ao ler o valor . Tente novamente!\n")

    try:
        r = div(n1,n2)
    except ZeroDivisionError: # -> Tratando exceção
        print("Não é possivel dividir por 0!")
    except:
        print("Ocorreu um erro inesperado ... ")
    else:
        print(f"Resultado: {r}")
    finally: # -> Sempre sera executado
        print(f'\nFim do calculo')
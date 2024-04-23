'''

Trabalhando com o raise

'''

from math import sqrt 

class NumeroNegativoError(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    try:
        num = int(input("Digite um numero positivo: "))

        if num < 0 :
            raise NumeroNegativoError
    
    except NumeroNegativoError:
        print("Foi fornecido um numero negativo!")
    else:
        print(f'A raiz quadrada de {num} é : {sqrt(num)}')
    finally:
        print(f'\nFim do calculo !')
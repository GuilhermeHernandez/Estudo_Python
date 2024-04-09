'''

Pacotes:
    - www.pypi.org -> indice de pacotes do Python

Instalador de pacote do Python:
    Pacote baixa da internet

    - py -m pip list -> lista os pacostes ja disponivel
    - py -m pip install matplotlib -> pacote de graficos
    - py -m pip uninstall nome_do_pacote -> desistala um pacote
    
Instalador de Modulo
    Pode ser criado por nos mesmo

    - import nome_do_modulo(built-in)
    - import math

'''
#import math
#from math import sqrt,sin
from math import *
import mod_func as mod

#print(math.sqrt(81))
#print(sqrt(81))

# __name__ Variavel com o nome do modulo atual
if __name__ == '__main__':
    mod.mensagem()

    valor_potencia = int(input("Digite um valor para fazer a potecialização: "))

    resultado = mod.potenciacao(valor_potencia)

    print(f"\nResultado da potencia : {resultado}")
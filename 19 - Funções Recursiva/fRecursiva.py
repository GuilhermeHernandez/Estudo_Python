'''
Função recursiva
    - Dividir o problema em sub problema
    - ela chama a si propria 
'''

# -> Recursividade
# -> Formula geral para o fatorial

# Fatoria(num) = 1 , se num =  0 ou se num  = 1 ('Caso Base')
# - > Fatoria(num) = num * Fatorial(num-),para num > 1 ('Caso Recurvidade)

# ->  4! = 4 * fatorial(4 - 1 = 3) * fatorial (3 - 1 = 2)  = ... 4 * 3 * 2 * 1
# -> 4! = 4 * 3 * 2 * 1 = 24

def fatorial (numero):
    
    if (numero == 0) or (numero == 1):
        return 1
    else:
        return numero * fatorial(numero - 1)

if __name__  == '__main__':
    x = int(input('Digite para um inteiro positivo para calcular seu fatoria:'))
    
    try:
        res = (fatorial(x))
    except RecursionError:
        print('O numero fornecido é muito grande ou negativo ...')

    print(f'O fatorial de {x} é : {res}')
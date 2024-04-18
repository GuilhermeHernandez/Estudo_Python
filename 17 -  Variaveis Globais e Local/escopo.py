'''

Escopo -> Visibilidade da variavel 
    - Local -> pode ser ultiliza so dentro de uma função
    - Global -> criada fora da função e pode ser acessada de qualquer lugar 
        - Valores constantes 

'''

var_global = "Curso completo de Python"

def escreve_texto():
    # -> Chamando a variavel global para a função
    global var_global

    # -> Variaveis acessivel somente dentro da função
    var_local = "Guilherme Hernandez"

    # -> Alterando o valor da variavel global
    var_global = "Banco de dados <3"

    print(f'Variavel global: {var_global}')
    print(f'Variavel local: {var_local}\n')

if __name__ == "__main__":
    print("Executar a função escreve_texto\n")
    escreve_texto()

    print("Tentar acessar as variaveis diretamente")
    print(f'Variavel global: {var_global}')
    # print(f'Variavel local: {var_local}')
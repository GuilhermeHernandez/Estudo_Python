'''

Print e formatação

    Sintaxe:
        - print(Objeto , argumentos)
        - Caracteres de escape

'''

# mensagem = 'Função print()'
# print(mensagem)
# print('Aula de python')

# ---> Exemplo de argumentos
# nome = 'Guilherme Hernandez Batista'
# anos = 4
# print('Desenvolvedor -',nome,' - Anos desenvolvendo -',anos)

# ---> Exemplo de concatenação
# nome = input("Digite seu nome : ")
# msg  = "Olá " + nome + " ! Bem vindo ao curso de pyhton"
# print(msg)
# print("Outro texto!")

# ---> Exemplo de print
# print("Imprime e muda de linha")
# print("Imprime e não muda de linha.", end='')
# print(" Continuo na mesma linha")

# ---> Exemplo de format <--- #
# nome = 'Guilherme'
# idade = 23
 
# msg_formatado = 'O nome dele é {0} e ela tem {1} anos!'.format(nome,idade)
# print(msg_formatado)

# ---> Exemplo de fstring <--- #
nome = 'Guilherme'
peso = 60

msg = f'Olá, meu nome é {nome} e eu peso : {peso} KGs'
print(msg)

# ---> Exemplo 2
a = 10
b = 5
res = f'A some de {a} com {b} é igual a {a + b}'
print(res)

# ---> Exemplo 3
valor = 125.59863
print(f'O valor é : {valor:.2f}')

# ---> Exemplo 4
nome = 'Guilherme Hernandez'
idade = 23
print(f'Nome:{nome}\tIdade:{idade}')
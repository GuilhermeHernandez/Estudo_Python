'''

Condicionais

    - Permite o programa seguir uma sequencia baseado em uma condição especificada.
    - Pode ser :
        - Simples:
        - Composto:
        - Encadeado:

'''

# ---> Exemplo de simples
nota1 = nota2 = 0.0
media = 0.0

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))

# Calculando as notas
media = (nota1 + nota2) / 2

if (media >= 7):
    print("Resultado : Aprovado!")
    print("Parabéns!")
elif (media >= 5):
    print("Aluna em recuperação ! Se esforce mais !!")
else:
    print("Aluno reprovado!")

print('Sua média é : {}'.format(media))
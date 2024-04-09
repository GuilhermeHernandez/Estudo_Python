'''

Laços encadeados

'''

# ---> Exemplo 1
# for cont_ex in range(1,6):
#     print(f"\nRodada: {cont_ex}")

#     for cont_in in range (5,0,-1):
#         print(f"Valor: {cont_in}")

# print("\nFim do laço!")

# ---> Exemplo 2
import random

for a in range(1,6):
    print(f"\nConjunto {a}")

    for b in range(5):
        num = random.randint(1,101)
        print(f"\tValor : {num}")
'''

Operadores de comparação

    - == -> Operador de igual 
    - != -> Operador de diferente 
    - > -> Operador de maior
    - < -> Operador de igual
    - >= -> Operador de maior igual
    - <= -> Operador de menor igual

'''

a = 5 
b = 5 

resultado_igual = a == b
resultado_dif = a != b
resultado_maior = a > b
resultado_menor = a < b
resultado_maior_ig = a >= b
resultado_menor_ig = a <= b

# print(resultado_igual)
# print(resultado_dif)
# print(resultado_maior)
# print(resultado_menor)
# print(resultado_maior_ig)
# print(resultado_menor_ig)

x = y = z = False

n1 = n2 = 0

n1 = int(input("\nDigite um numero: "))
n2 = int(input("Digite outro numero: "))

x = n1 == n2 

print("\nSão iguais ? " , x , "\n")

z = n1 > n2 

print(n1 , " é maior que ",n2,' ? ',z,'\n')

y = n1 != n2 

print("São diferentes ? " + str(y))
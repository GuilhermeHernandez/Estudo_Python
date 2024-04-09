'''

Operadores logicos 

    - Contem a tabela verdade
    - AND -> Condições tem que ser verdadeiras
    - OR -> Apenas uma das condições deve ser verdadeira 
    - NOT -> Negação

'''

# --- > Exemplo : and
# idade = 17
# altura = 1.75

# resultado = (idade >= 18) and (altura>= 1.70)
# print("O participante pode participar do evento ? " , resultado)


# --- > Exemplo : or
# porta = 'f'
# janela = 'f'

# alarme = (porta == 'a') or (janela == 'a')
# msg = 'Alarme disparado ? ' + str(alarme)
# print(msg)

# --- > Exemplo : not
tem_dinheiro = False

# Recebi um pix
tem_dinheiro = not tem_dinheiro # Negado o estado logico , acontece a inversão do estado logico !

msg = 'Tem dinheiro ? ' + str(tem_dinheiro)
print(msg)
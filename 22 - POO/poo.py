'''

Paradigma de programação - POO
    - multiparadigma (estruturado)
    - Classes
        - Modelos abstratos que representa item real 
        - Sempre começa com letra maiuscula
        - atributos 
            - caracteristicas (variaveis)
        - Metodos
            - Ações , funções
    - Objeto 
        - Ocorrencia da classe

    - Herança
        - Uma classe herda as funções de outra

    - Polimorfismo
        - Uma função herdado pode ser executada de forma diferente

    Self -> Representa a classe atual

    Ex: Como representamos uma pessoa no python
'''

class Veiculo:

    def movimentar(self):
        print(f'Sou um veiculo e me desloco !')

    def __init__(self,fabricante,modelo):

        # -> __ Diz que a variavel é privada
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    # Metodo getter
    def get_fabricante_modelo(self):
        print(f"Modelo : {self.__modelo} , Fabricante : {self.__fabricante}")

    def get_num_registro(self):
        return self.__num_registro

    # Metodo Setter
    def set_numero_modelo(self,nmr_registro):
        self.__num_registro = nmr_registro

# -> Classe carro é um tipo de veiculo
class Carro(Veiculo):

    # -> Metodo init sera herdado

    def movimentar(self):
        print(F'\nSou um carro e ando pela as ruas!')
    
class Motocicleta(Veiculo):

    def movimentar(self):
        print(f'\nSou uma moto e corro muito !')

class Aviao(Veiculo):

    def __init__(self,fabricante,modelo,categoria):
        super().__init__(fabricante,modelo)
        self.__cat = categoria
        
    def get_categoria_aviao(self):
        return self.__cat
    
    def movimentar(self):
        print('Eu voo Alto!')


if __name__ == '__main__':
    # meu_veiculo = Veiculo('BMW','X6')
    # meu_veiculo.movimentar()
    # meu_veiculo.get_fabricante_modelo()
    # meu_veiculo.set_numero_modelo('49851891-1')
    # print(f'Registro : {meu_veiculo.get_num_registro()}')

    # meu_carro = Carro('Audi','RS6')
    # meu_carro.movimentar()
    # meu_carro.get_fabricante_modelo()

    # minha_moto = Motocicleta('BMW','RR1000')
    # minha_moto.movimentar()
    # minha_moto.get_fabricante_modelo()

    meu_aviao = Aviao('Boeing','747','Comercial')
    meu_aviao.movimentar()
    meu_aviao.get_fabricante_modelo()
    print(f'Categoria avião : {meu_aviao.get_categoria_aviao()}')
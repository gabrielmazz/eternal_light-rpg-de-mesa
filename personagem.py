from dados import *

"""
    Este trecho de código apresenta a classe "Personagem" que é usada para modelar personagens em um jogo ou RPG. A classe tem 7 atributos: "escolha", "nome", "pv", "força", "destreza", "constituição" e "ca". 
    A classe tem um método "init" que é usado para inicializar os atributos quando uma nova instância da classe é criada. Dependendo do valor de "escolha", o nome, as habilidades e a quantidade de pontos de vida 
    serão atribuídos ao personagem de forma diferente. A classe "Personagem" é baseada em três tipos diferentes de personagens: "Warrior", "Shielder" e "Berserker". A função "rolagem_10(4, 0)", "rolagem_12(4, 0)" 
    e "rolagem_8(4, 0)" são importadas de um arquivo chamado "dados" e realizão uma rolagem de dados. A quantidade de pontos de vida é determinada pela soma da rolagem de dados com o valor da constituição 
    multiplicado por 4. A CA (Classe de Armadura) é calculada como 12 mais a destreza.
"""

class Personagem:
    def __init__(self, escolha, nome, pv, forca, destreza, constituicao, ca, arma):
        self.escolha = escolha
        self.nome = nome
        self.pv = pv
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.ca = ca
        self.arma = arma

        if escolha == 1:
            self.nome = 'Warrior'
            self.forca = 3
            self.destreza = 3
            self.constituicao = 2
            self.pv = rolagem_10(4, 0) + (4 * self.constituicao) + 10
            self.ca = 12 + self.destreza
            self.arma = 2

        elif escolha == 2:
            self.nome = 'Shielder'
            self.forca = 1
            self.destreza = 5
            self.constituicao = 3
            self.pv = rolagem_12(4, 0) + (4 * self.constituicao) + 10
            self.ca = 12 + self.destreza
            self.arma = 0

        elif escolha == 3:
            self.nome = 'Berserker'
            self.forca = 5
            self.destreza = 0
            self.constituicao = 1
            self.pv = rolagem_8(4, 0) + (4 * self.constituicao) + 10
            self.ca = 12 + self.destreza
            self.arma = 4

        
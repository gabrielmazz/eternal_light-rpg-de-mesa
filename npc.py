from dados import *

"""
    Este trecho de código define a classe Npc. A classe é inicializada com o método init, que define os atributos do objeto Npc: nome, força, destreza, constituição, pontos de vida (pv) e classe de armadura (ca). 
    Além disso, a classe importa a função "rolagem_12" do módulo "dados". A partir desses dados, o objeto Npc terá seus valores para pv calculados como a soma da rolagem de 12 faces (realizada pelo método "rolagem_12") 
    com 4 vezes a constituição, e seu valor para ca será calculado como 12 mais sua destreza. O atributo "arma" também é definido com um valor fixo de 5.
"""

class Npc:
    def __init__(self):
        self.nome = 'Elemental'
        self.forca = 7
        self.destreza = 6
        self.constituicao = 3
        self.pv = rolagem_12(4, 0) + (4 * self.constituicao) + 40
        self.ca = 12 + self.destreza
        self.arma = 7
    
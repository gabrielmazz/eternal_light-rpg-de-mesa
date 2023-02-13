import pygame
import manipulacao_tela as mt

"""
    Esse trecho de código define uma função define_elementos_mapa2() que carrega a imagem de fundo de um mapa de jogo chamado "map2". A função tela_fundo(screen, map2) é então usada para exibir essa 
    imagem como fundo da tela. A função tela_fundo é importada de um módulo chamado "manipulacao_tela" e exibe a imagem como fundo da tela de jogo passada como argumento screen.
"""

def define_elementos_menu_mapa2():
    map2_fundo = pygame.image.load("img/maps/map2.jpg")
    
    return map2_fundo
    
    
def desenha_elementos(screen, map2):
    #Imagem por tras
    mt.tela_fundo(screen, map2)
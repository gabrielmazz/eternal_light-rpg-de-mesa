import pygame
import manipulacao_tela as mt

"""
    Esse trecho de código define uma função define_elementos_mapa1() que carrega a imagem de fundo de um mapa de jogo chamado "map1". A função tela_fundo(screen, map1) é então usada para exibir essa 
    imagem como fundo da tela. A função tela_fundo é importada de um módulo chamado "manipulacao_tela" e exibe a imagem como fundo da tela de jogo passada como argumento screen.
"""

def define_elementos_mapa1():
    # Define o mapa de fundo
    map1_fundo = pygame.image.load("img/maps/map.jpg")
    
    return map1_fundo
    
    
def tela_fundo(screen, map1):
    #Imagem por tras
    mt.tela_fundo(screen, map1)
import pygame
import manipulacao_tela as mt

# Elementos que contem a tela do Menu
def define_elementos_menu_mapas():
    menu_image_mapas = pygame.image.load("img/geral/tela_menu_mapas.jpg")
    map1_image = pygame.image.load("img/maps/map_menu1.jpg")
    map1_image = pygame.transform.scale(map1_image, (map1_image.get_width() // 2.5, map1_image.get_height() // 2.5))

    map2_image = pygame.image.load("img/maps/map_menu2.jpg")
    map2_image = pygame.transform.scale(map2_image, (map2_image.get_width() // 2.5, map2_image.get_height() // 2.5))
    
    map3_image = pygame.image.load("img/maps/map_menu3.jpg")
    map3_image = pygame.transform.scale(map3_image, (map3_image.get_width() // 2.5, map3_image.get_height() // 2.5))
    
    
    return menu_image_mapas, map1_image, map2_image, map3_image

def posicoes_elementos_menu_mapas():
    map1_rect = pygame.Rect(400, 300, 100, 50)
    map2_rect = pygame.Rect(700, 300, 100, 50)
    map3_rect = pygame.Rect(1000, 300, 100, 50)
    
    return map1_rect, map2_rect, map3_rect

def rederizacao_textos_menu_personagens(font_menu):
    # Renderização do mapa 1
    map1_text = font_menu.render("Mapa 01", True, (255, 255, 255))
    map1_text_rect = map1_text.get_rect()
    map1_text_rect.center = (520, 250)

    # Renderização do mapa 2
    map2_text = font_menu.render("Mapa 02", True, (255, 255, 255))
    map2_text_rect = map2_text.get_rect()
    map2_text_rect.center = (820, 250)

    # Renderização do mapa 3
    map3_text = font_menu.render("Mapa 03", True, (255, 255, 255))
    map3_text_rect = map3_text.get_rect()
    map3_text_rect.center = (1120, 250)
    
    return map1_text, map1_text_rect, map2_text, map2_text_rect, map3_text, map3_text_rect
    

# Define a tela do menu de mapas, desenhando tudo que for necessario
def desenha_elementos(screen, menu_image_mapas, 
                      map1_image, map1_rect, map1_text, map1_text_rect,
                      map2_image, map2_rect, map2_text, map2_text_rect,
                      map3_image, map3_rect, map3_text, map3_text_rect):
    
    # Imagem por tras
    mt.tela_fundo(screen, menu_image_mapas)
        
    # Warrior
    mt.elementos_tela(screen, map1_image, map1_rect)
    mt.elementos_tela(screen, map1_text, map1_text_rect)
        
    # Shielder
    mt.elementos_tela(screen, map2_image, map2_rect)
    mt.elementos_tela(screen, map2_text, map2_text_rect)
        
    # Berserker
    mt.elementos_tela(screen, map3_image, map3_rect)
    mt.elementos_tela(screen, map3_text, map3_text_rect)
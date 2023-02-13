import pygame
import manipulacao_tela as mt

"""
    Esta função "define_elementos_menu" está carregando imagens para serem usadas na tela de menu de personagens. Ela está carregando a imagem da tela de menu, a imagem do personagem warrior, 
    a imagem do personagem shielder, e a imagem do personagem berserker. Depois, ela retorna essas imagens para serem usadas posteriormente.
"""
def define_elementos_menu():
    menu_image = pygame.image.load("img/geral/tela_menu_personagens_1.jpg")
    warrior_image = pygame.image.load("img/personagens/warrior.png")
    shielder_image = pygame.image.load("img/personagens/shielder.png")
    berserker_image = pygame.image.load("img/personagens/berserker.png")
    
    return menu_image, warrior_image, shielder_image, berserker_image

"""
    Este trecho de código está criando três retângulos (warrior_rect, shielder_rect e berserker_rect) que serão usados na posição dos elementos de um menu. Cada retângulo é criado com pygame.Rect 
    e tem as coordenadas (400, 300), (700, 300) e (1000, 300), respectivamente, e têm as dimensões 100x50. Por fim, a função retorna os três retângulos para que possam ser usados em outro lugar no 
    código.
"""
def posicoes_elementos_menu():
    warrior_rect = pygame.Rect(400, 300, 100, 50)
    shielder_rect = pygame.Rect(700, 300, 100, 50)
    berserker_rect = pygame.Rect(1000, 300, 100, 50)
    
    return warrior_rect, shielder_rect, berserker_rect

def rederizacao_textos(font_menu):
    
    # Renderização do texto "Warrior"
    warrior_text = font_menu.render("Warrior", True, (255, 255, 255))
    warrior_text_rect = warrior_text.get_rect()
    warrior_text_rect.center = (520, 250)

    # Renderização do texto "Shielder"
    shielder_text = font_menu.render("Shielder", True, (255, 255, 255))
    shielder_text_rect = shielder_text.get_rect()
    shielder_text_rect.center = (820, 250)

    # Renderização do texto "Berseker"
    berserker_text = font_menu.render("Berseker", True, (255, 255, 255))
    berserker_text_rect = berserker_text.get_rect()
    berserker_text_rect.center = (1120, 250)
    
    # Rederização do texto "Player 1"
    player_text_1 = font_menu.render("Player 1", True, (255, 255, 255))
    player_text_1_rect = shielder_text.get_rect()
    player_text_1_rect.center = (820, 700)
    
    return warrior_text, warrior_text_rect, shielder_text, shielder_text_rect, berserker_text, berserker_text_rect, player_text_1, player_text_1_rect
    
# Define a tela do menu de personagens, desenhando tudo que for necessario
def desenha_elementos(screen, menu_image, 
                      warrior_image, warrior_rect, warrior_text, warrior_text_rect,
                      shielder_image, shielder_rect, shielder_text, shielder_text_rect,
                      berserker_image, berserker_rect, berserker_text, berserker_text_rect,
                      player_text_1, player_text_1_rect):
    
    # Imagem por tras
    mt.tela_fundo(screen, menu_image)
        
    # Warrior
    mt.elementos_tela(screen, warrior_image, warrior_rect)
    mt.elementos_tela(screen, warrior_text, warrior_text_rect)
        
    # Shielder
    mt.elementos_tela(screen, shielder_image, shielder_rect)
    mt.elementos_tela(screen, shielder_text, shielder_text_rect)
        
    # Berserker
    mt.elementos_tela(screen, berserker_image, berserker_rect)
    mt.elementos_tela(screen, berserker_text, berserker_text_rect)
    
    # Player 1
    mt.elementos_tela(screen, player_text_1, player_text_1_rect)
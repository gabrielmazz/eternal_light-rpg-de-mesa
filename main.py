import pygame
import time
import pyautogui
import manipulacao_tela as mt
import manipulacao_gameplay as mg
import tela_menu_personagens_1 as tm_per_1
import tela_menu_personagens_2 as tm_per_2
import tela_menu_mapas as tm_map
import map1, map2, map3

""" 
    Este programa tem como objetivo simular um RPG de Mesa, como o Roll20 e o Dnd 5e, utilizando técnicas de 
    inteligência artificial com máquina de estado. O programa irá permitir que os jogadores possam controlar 
    seus personagens e realizar ações em turnos, assim como em um jogo de RPG tradicional. Além disso, o programa 
    será capaz de rolar dados e calcular as consequências das ações dos personagens, como ataques e defesas, utilizando 
    algoritmos de inteligência artificial para garantir a fair-play e uma experiência de jogo enriquecedora. Em resumo, 
    este programa busca trazer a emoção e a imersão de um RPG de Mesa para o ambiente digital, utilizando a inteligência 
    artificial como ferramenta para tornar a jogabilidade ainda mais envolvente.
"""

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

""" 
    Neste trecho de código, está sendo inicializado o módulo Pygame, que é uma biblioteca usada para criar jogos em Python. 
    Em seguida, está sendo configurado o tamanho da tela do jogo e o nome da janela. Logo após, uma imagem de logo está sendo 
    carregada e exibida por 5 segundos na tela. Por fim, uma fonte de texto padrão está sendo criada para ser usada nos menus do jogo.
"""

# Inicialização do Pygame
mt.inicia_pygame()

# Configuração da tela
screen = mt.define_tamanho_tela(1600, 900)
mt.define_nome_janela("Eternal Light")

# Carregamento da imagem da logo
logo_image = mt.carrega_imagem("img/geral/logo_entrada.jpg")

# Exibição da logo por 10 segundos
mt.tela_fundo(screen, logo_image)
mt.update_tela()
time.sleep(5)

# Criação dos textos, no caso essa é a font padrão dos menus
font_menu = mt.criacao_texto("font/font1_elementary.ttf", 36)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

""" 
    Este trecho de código é uma parte da tela de menu dos personagens no seu programa. Primeiramente, são carregadas as imagens 
    do menu e dos personagens através da função "define_elementos_menu()". Em seguida, são definidas as posições das imagens dos 
    personagens no menu através da função "posicoes_elementos_menu()". Por fim, são renderizados os textos do menu através da 
    função "rederizacao_textos()", passando a fonte do menu como argumento.
"""

#Tela do menu dos personagens (1):
# Carregamento das imagens do menu e dos personagens
menu_image_1, warrior_image, shielder_image, berserker_image = tm_per_1.define_elementos_menu()

# Posições das imagens dos personagens no menu
warrior_rect, shielder_rect, berserker_rect = tm_per_1.posicoes_elementos_menu()

# Rederização dos textos do menu
warrior_text, warrior_text_rect, shielder_text, shielder_text_rect, berserker_text, berserker_text_rect, player_text_1, player_text_1_rect = tm_per_1.rederizacao_textos(font_menu)

""" 
    Este trecho de código é mais uma parte do menu dos personagens, no caso aqui é feita as mesma funções da tela de cima, apenas
    mudando para que a seleção seja feita pelo player 2
"""

#Tela do menu dos personagens (2):

# Carregamento das imagens do menu e dos personagens
menu_image_2, warrior_image, shielder_image, berserker_image = tm_per_2.define_elementos_menu()

# Posições das imagens dos personagens no menu
warrior_rect, shielder_rect, berserker_rect = tm_per_2.posicoes_elementos_menu()

# Rederização dos textos do menu
warrior_text, warrior_text_rect, shielder_text, shielder_text_rect, berserker_text, berserker_text_rect, player_text_2, player_text_2_rect = tm_per_2.rederizacao_textos(font_menu)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

""" 
    Este trecho de código é responsável por preparar a tela de seleção de mapas. As imagens dos mapas são carregadas e posicionadas no menu. 
    Além disso, os textos dos mapas são renderizados com uma fonte específica. Essas imagens e textos serão exibidos na tela para que o usuário 
    possa escolher o mapa desejado.
"""

#Tela do menu dos mapas
# Carregamento das imagens do menu e dos mapas
menu_image_mapas, map1_image, map2_image, map3_image = tm_map.define_elementos_menu_mapas()

# Posições das imagens dos mapas no menu
map1_rect, map2_rect, map3_rect = tm_map.posicoes_elementos_menu_mapas()

# Rederização dos textos do menu
map1_text, map1_text_rect, map2_text, map2_text_rect, map3_text, map3_text_rect = tm_map.rederizacao_textos_menu_personagens(font_menu)

# Tela do mapa 1
map1_fundo = map1.define_elementos_mapa1()

# Carregamento das imagens que estão no mapa 3
map2_fundo = map2.define_elementos_menu_mapa2()

# Carregamento das imagens que estão no mapa 3
map3_fundo = map3.define_elementos_menu_mapa3()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

""" 
    É o loop principal do jogo, onde são controladas as ações e eventos para a escolha dos personagens pelos dois jogadores. A variável "screen_mode" 
    controla qual é a tela atual mostrada ao jogador. Se "screen_mode" for igual a 1, então é a tela de escolha do personagem para o jogador 1. 
    Se for igual a 2, é a tela de escolha do personagem para o jogador 2. Se for igual a 3, então o jogo prossegue para a próxima fase.

    O loop principal "while running" verifica se o jogo ainda está sendo executado. Dentro dele, ocorre o tratamento de eventos, como o fechamento da janela do jogo.
    Cada vez que ocorre um evento, a tela é limpa e os elementos (menu, personagens, textos) são desenhados na tela usando a função "desenha_elementos". Em seguida, 
    a tela é atualizada com a função "update_tela".

    Para a escolha dos personagens, é verificado se uma tecla foi pressionada (evento "pygame.KEYDOWN"). Se a tecla pressionada for 1, o jogador escolheu o personagem 
    Warrior; se for 2, escolheu o personagem Shielder; e se for 3, escolheu o personagem Berserker. A escolha do personagem é armazenada em variáveis como "personagem_1" 
    e "name_personagem_1". Se a tecla pressionada for 0, o jogo é finalizado com a função "finaliza_pygame".
"""

# Variável para controlar a tela atual
screen_mode = 1

# Loop principal do jogo
running = True
    
# Loop para as escolhas
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tela do menu de personagens do jogador 1
    if screen_mode == 1:
        # Limpa a tela
        mt.limpa_tela(screen)

        # Desenho do menu e dos personagens na tela
        tm_per_1.desenha_elementos(screen, menu_image_1, 
                                warrior_image, warrior_rect, warrior_text, warrior_text_rect,
                                shielder_image, shielder_rect, shielder_text, shielder_text_rect,
                                berserker_image, berserker_rect, berserker_text, berserker_text_rect,
                                player_text_1, player_text_1_rect)

        mt.update_tela()

        # Verificação de qual personagem será escolhido pelo jogador 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                
            elif event.type == pygame.KEYDOWN:
                mt.update_fila_eventos()
                
                if event.key == pygame.K_1:
                    # Warrior
                    screen_mode = 2 # Troca a tela
                    personagem_1 = "img/personagens/warrior.png" 
                    name_personagem_1 = "Warrior"
                    escolha_player_1 = 1
                    
                elif event.key == pygame.K_2:
                    # Shielder
                    screen_mode = 2
                    personagem_1 = "img/personagens/shielder.png" 
                    name_personagem_1 = "Shielder"
                    escolha_player_1 = 2
                    
                elif event.key == pygame.K_3:
                    # Berseker
                    screen_mode = 2
                    personagem_1 = "img/personagens/berserker.png" 
                    name_personagem_1 = "Berserker"
                    escolha_player_1 = 3
                    
                elif event.key == pygame.K_0:
                    # Saida do game
                    mt.finaliza_pygame()
            else:
                continue
                    
    # Tela do menu de personagens do jogador 2
    elif screen_mode == 2:
        
        # Limpa a tela
        mt.limpa_tela(screen)

        # Desenho do menu e dos personagens na tela
        tm_per_2.desenha_elementos(screen, menu_image_2, 
                                warrior_image, warrior_rect, warrior_text, warrior_text_rect,
                                shielder_image, shielder_rect, shielder_text, shielder_text_rect,
                                berserker_image, berserker_rect, berserker_text, berserker_text_rect,
                                player_text_2, player_text_2_rect)

        mt.update_tela()
        
        # Verificação de qual personagem será escolhido pelo jogador 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                
            elif event.type == pygame.KEYDOWN:
                mt.update_fila_eventos()
                
                if event.key == pygame.K_1:
                    # Warrior
                    screen_mode = 3
                    personagem_2 = "img/personagens/warrior.png" 
                    name_personagem_2 = "Warrior"
                    escolha_player_2 = 1
                    
                elif event.key == pygame.K_2:
                    # Shielder
                    screen_mode = 3
                    personagem_2 = "img/personagens/shielder.png" 
                    name_personagem_2 = "Shielder"
                    escolha_player_2 = 2
                    
                elif event.key == pygame.K_3:
                    # Berseker
                    screen_mode = 3
                    personagem_2 = "img/personagens/berserker.png" 
                    name_personagem_2 = "Berserker"
                    escolha_player_2 = 3
                    
                elif event.key == pygame.K_0:
                    # Saida do game
                    mt.finaliza_pygame()
            else:
                continue
        
    # Menu da tela dos mapas    
    elif screen_mode == 3:
        # Limpa a tela
        mt.limpa_tela(screen)
        
        # Desenho do menu e dos mapas na tela
        tm_map.desenha_elementos(screen, menu_image_mapas,
                                map1_image, map1_rect, map1_text, map1_text_rect,
                                map2_image, map2_rect, map2_text, map2_text_rect,
                                map3_image, map3_rect, map3_text, map3_text_rect)
        
        mt.update_tela()
        
        # Verificação de qual mapa será escolhido
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                
            elif event.type == pygame.KEYDOWN:
                mt.update_fila_eventos()
                
                if event.key == pygame.K_1:
                    # Mapa 01
                    screen_mode = 4
                    
                elif event.key == pygame.K_2:
                    # Mapa 02
                    screen_mode = 5
                    
                elif event.key == pygame.K_3:
                    # Mapa 03
                    screen_mode = 6
                    
                elif event.key == pygame.K_0:
                    # Saida do game
                    mt.finaliza_pygame()
            else:
                continue
            
    elif screen_mode == 4:
        # Limpa a tela
        mt.limpa_tela(screen)
        
        # Função de gameplay
        mg.gameplay(personagem_1, personagem_2, screen, map1_fundo, name_personagem_1, name_personagem_2, escolha_player_1, escolha_player_2)

    elif screen_mode == 5:
        # Limpa a tela
        mt.limpa_tela(screen)
        
        # Função de gameplay
        mg.gameplay(personagem_1, personagem_2, screen, map2_fundo, name_personagem_1, name_personagem_2, escolha_player_1, escolha_player_2)

        
    elif screen_mode == 6:
        # Limpa a tela
        mt.limpa_tela(screen)
        
        # Função de gameplay
        mg.gameplay(personagem_1, personagem_2, screen, map3_fundo, name_personagem_1, name_personagem_2, escolha_player_1, escolha_player_2)

    mt.update_tela()
    
# Fim do jogo
mt.finaliza_pygame()
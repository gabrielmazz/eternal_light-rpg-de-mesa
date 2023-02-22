import pygame
import time
import manipulacao_tela as mt
import manipulacao_gameplay as mg


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

# Carrega a imagem que será usada como ícone
icon = mt.carrega_imagem("img/geral/icon.png")

# Define a imagem como ícone da janela
mt.define_icone(icon)

# Exibição da logo por 10 segundos
mt.tela_fundo(screen, logo_image)
mt.update_tela()
#time.sleep(5)

# Criação dos textos, no caso essa é a font padrão dos menus
font_menu = mt.criacao_font("font/font1_elementary.ttf", 36)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

""" 
    Este trecho de código é uma parte da tela de menu dos personagens no seu programa. Primeiramente, são carregadas as imagens 
    do menu e dos personagens através da função "define_elementos_menu()". Em seguida, são definidas as posições das imagens dos 
    personagens no menu através da função "posicoes_elementos_menu()". Por fim, são renderizados os textos do menu através da 
    função "rederizacao_textos()", passando a fonte do menu como argumento.
"""

#Tela do menu dos personagens (1):
# Define o plano de fundo do menu de personagens 1
plano_de_fundo_menu_personagens_1 = mt.carrega_imagem("img/geral/tela_menu_personagens_1.jpg")


# Carregamento das imagens do menu e dos personagens
warrior_image = mt.carrega_imagem("img/personagens/warrior.png")
shielder_image = mt.carrega_imagem("img/personagens/shielder.png")
berserker_image = mt.carrega_imagem("img/personagens/berserker.png")

# Posições das imagens dos personagens no menu
warrior_rect = mt.posicoes_elemento(400, 300, 100, 50)
shielder_rect = mt.posicoes_elemento(700, 300, 100, 50)
berserker_rect = mt.posicoes_elemento(1000, 300, 100, 50)

# Criação dos textos do menu
warrior_text = mt.cria_textos(font_menu, "Warrior", (255, 255, 255))
shielder_text = mt.cria_textos(font_menu, "Shielder", (255, 255, 255))
berserker_text = mt.cria_textos(font_menu, "Berseker", (255, 255, 255))

# Rederização dos textos do menu
warrior_text_rect = mt.rederiza_textos(520, 250, warrior_text)
shielder_text_rect = mt.rederiza_textos(820, 250, warrior_text)
berserker_text_rect = mt.rederiza_textos(1120, 250, warrior_text)

# Cria o texto "Player 1" na tela de menu
player_text_1 = mt.cria_textos(font_menu, "Player 1", (255, 255, 255))

# Rederiza o texto "Player 1"
player_text_1_rect = mt.rederiza_textos(820, 700, player_text_1)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

#Tela do menu dos personagens (2):
plano_de_fundo_menu_personagens_2 = mt.carrega_imagem("img/geral/tela_menu_personagens_2.jpg")

# Cria o texto "Player 1" na tela de menu
player_text_2 = mt.cria_textos(font_menu, "Player 2", (255, 255, 255))

# Rederiza o texto "Player 1"
player_text_2_rect = mt.rederiza_textos(820, 700, player_text_2)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

""" 
    Este trecho de código é responsável por preparar a tela de seleção de mapas. As imagens dos mapas são carregadas e posicionadas no menu. 
    Além disso, os textos dos mapas são renderizados com uma fonte específica. Essas imagens e textos serão exibidos na tela para que o usuário 
    possa escolher o mapa desejado.
"""
#Tela do menu dos mapas
# Define o plano de fundo
plano_de_fundo = mt.carrega_imagem("img/geral/tela_menu_mapas.jpg")

# Define o elemento 1 da imagem, no caso a primeira escolha e assim respectivamente
map1_image = mt.carrega_imagem("img/maps/map_menu1.jpg")
map1_image = mt.escala_imagem(2.5, map1_image)

map2_image = mt.carrega_imagem("img/maps/map_menu2.jpg")
map2_image = mt.escala_imagem(2.5, map2_image)

map3_image = mt.carrega_imagem("img/maps/map_menu3.jpg")
map3_image = mt.escala_imagem(2.5, map3_image)


# Posições das imagens dos mapas no menu
map1_rect = mt.posicoes_elemento(400, 300, 100, 50)
map2_rect = mt.posicoes_elemento(700, 300, 100, 50)
map3_rect = mt.posicoes_elemento(1000, 300, 100, 50)

# Cria os textos que serão utilizados no menu de mapas
map1_text = mt.cria_textos(font_menu, "Mapa 01", (255, 255, 255))
map2_text = mt.cria_textos(font_menu, "Mapa 02", (255, 255, 255))
map3_text = mt.cria_textos(font_menu, "Mapa 03", (255, 255, 255))

# Rederiza cada texto no menu de personagens
map1_text_rect = mt.rederiza_textos(520, 250, map1_text)
map2_text_rect = mt.rederiza_textos(820, 250, map2_text)
map3_text_rect = mt.rederiza_textos(1120, 250, map3_text)


# Define cada mapa, para que quando for escolhido, ele entre na posição determinada
map1_fundo = mt.carrega_imagem("img/maps/map.jpg")
map2_fundo = mt.carrega_imagem("img/maps/map2.jpg")
map3_fundo = mt.carrega_imagem("img/maps/map3.jpg")

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

        # Imagem por tras
        mt.tela_fundo(screen, plano_de_fundo_menu_personagens_1)
            
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
                    personagem_1_dead = "img/personagens/warrior_dead.png" 
                    name_personagem_1 = "Warrior"
                    escolha_player_1 = 1
                    
                elif event.key == pygame.K_2:
                    # Shielder
                    screen_mode = 2
                    personagem_1 = "img/personagens/shielder.png" 
                    personagem_1_dead = "img/personagens/shielder_dead.png" 
                    name_personagem_1 = "Shielder"
                    escolha_player_1 = 2
                    
                elif event.key == pygame.K_3:
                    # Berseker
                    screen_mode = 2
                    personagem_1 = "img/personagens/berserker.png" 
                    personagem_1_dead = "img/personagens/berserker_dead.png" 
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

        # Imagem por tras
        mt.tela_fundo(screen, plano_de_fundo_menu_personagens_2)
            
        # Warrior
        mt.elementos_tela(screen, warrior_image, warrior_rect)
        mt.elementos_tela(screen, warrior_text, warrior_text_rect)
            
        # Shielder
        mt.elementos_tela(screen, shielder_image, shielder_rect)
        mt.elementos_tela(screen, shielder_text, shielder_text_rect)
            
        # Berserker
        mt.elementos_tela(screen, berserker_image, berserker_rect)
        mt.elementos_tela(screen, berserker_text, berserker_text_rect)
        
        # Player 2
        mt.elementos_tela(screen, player_text_2, player_text_2_rect)

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
                    personagem_2_dead = "img/personagens/warrior_dead.png" 
                    name_personagem_2 = "Warrior"
                    escolha_player_2 = 1
                    
                elif event.key == pygame.K_2:
                    # Shielder
                    screen_mode = 3
                    personagem_2 = "img/personagens/shielder.png" 
                    personagem_2_dead = "img/personagens/shielder_dead.png" 
                    name_personagem_2 = "Shielder"
                    escolha_player_2 = 2
                    
                elif event.key == pygame.K_3:
                    # Berseker
                    screen_mode = 3
                    personagem_2 = "img/personagens/berserker.png" 
                    personagem_2_dead = "img/personagens/berserker_dead.png" 
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
        # Imagem por tras
        mt.tela_fundo(screen, plano_de_fundo_menu_personagens_1)
            
        # Warrior
        mt.elementos_tela(screen, map1_image, map1_rect)
        mt.elementos_tela(screen, map1_text, map1_text_rect)
            
        # Shielder
        mt.elementos_tela(screen, map2_image, map2_rect)
        mt.elementos_tela(screen, map2_text, map2_text_rect)
            
        # Berserker
        mt.elementos_tela(screen, map3_image, map3_rect)
        mt.elementos_tela(screen, map3_text, map3_text_rect)
        
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
        mg.gameplay(personagem_1, personagem_2, personagem_1_dead, personagem_2_dead, screen, map1_fundo, name_personagem_1, name_personagem_2, escolha_player_1, escolha_player_2)

    elif screen_mode == 5:
        # Limpa a tela
        mt.limpa_tela(screen)
        
        # Função de gameplay
        mg.gameplay(personagem_1, personagem_2, personagem_1_dead, personagem_2_dead, screen, map2_fundo, name_personagem_1, name_personagem_2, escolha_player_1, escolha_player_2)

        
    elif screen_mode == 6:
        # Limpa a tela
        mt.limpa_tela(screen)
        
        # Função de gameplay
        mg.gameplay(personagem_1, personagem_2, personagem_1_dead, personagem_2_dead, screen, map3_fundo, name_personagem_1, name_personagem_2, escolha_player_1, escolha_player_2)

    mt.update_tela()
    
# Fim do jogo
mt.finaliza_pygame()
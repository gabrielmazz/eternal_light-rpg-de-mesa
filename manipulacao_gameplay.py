import pygame
import time
import random as rd
import dados as d
import manipulacao_tela as mt
import movimentacao as mv
import funcoes_manipulacao_gameplay as fmg
from personagem import *
from npc import *

def gameplay(personagem_1, personagem_2, personagem_1_dead, personagem_2_dead, screen, mapa, name_personagem_1, name_personagem_2, escolha_player_1, escolha_player_2):
    
    """
        Faz a inicialização e preparação para desenhar a tela do jogo. A primeira coisa que é feita é a definição da fonte que será usada na tela. Em seguida, o fundo do mapa 
        é desenhado na tela. Depois disso, todos os eventos que ocorrerão são zerados. Em seguida, as imagens dos personagens e do NPC são carregadas e suas posições na tela são definidas.
    """
    # Define a font que será usada
    font = mt.criacao_font("font/font1_elementary.ttf", 18)
    font_hp_ca = mt.criacao_font("font/font1_elementary.ttf", 12)
    font_turns = mt.criacao_font("font/font1_elementary.ttf", 14)
    

    # Desenha o mapa na screen
    mt.tela_fundo(screen, mapa)
        
    # Zera todos os eventos que ocorrerão
    mt.zera_eventos()
    
    # Carrega a imagem dos players
    per_image_player_1 = mt.carrega_imagem(personagem_1)
    per_image_player_2 = mt.carrega_imagem(personagem_2)
    
    # Define a nova escala para as imagens
    per_image_player_1 = mt.escala_imagem(4, per_image_player_1)
    per_image_player_2 = mt.escala_imagem(4, per_image_player_2)
    
    # Aleatoria os valores para multiplos 
    x_player_1 = fmg.arredonda_para_multiplos(rd.randint(100, 1500))
    y_player_1 = fmg.arredonda_para_multiplos(rd.randint(100, 800))
    
    x_player_2 = fmg.arredonda_para_multiplos(rd.randint(100, 1500))
    y_player_2 = fmg.arredonda_para_multiplos(rd.randint(100, 800))
    
    # Carrega a posição da imagem dos players
    per_rect_player_1 = mt.posicoes_elemento(x_player_1, y_player_1, 0, 0)
    per_rect_player_2 = mt.posicoes_elemento(x_player_2, y_player_2, 0, 0)
    
    # Carrega a imagem do NPC
    npc_image = mt.carrega_imagem("img/personagens/npc.png")
    npc_image = mt.escala_imagem(4, npc_image)
    
    # Aleatoria os valores para multiplos 
    x_npc = fmg.arredonda_para_multiplos(rd.randint(100, 1500))
    y_npc = fmg.arredonda_para_multiplos(rd.randint(100, 800))
    
    # Carrega a posição da imagem do NPC
    npc_rect = mt.posicoes_elemento(x_npc, y_npc, 0, 0)
    
    # Printa a posição dos jogadores e do NPC
    print(per_rect_player_1)
    print(per_rect_player_2)
    print(npc_rect)
    
    """
        São criadas duas instâncias de uma classe "Personagem" e uma instância de uma classe "Npc". A primeira instância da classe "Personagem", chamada "player_1", é criada passando como argumento 
        a variável "escolha_player_1". A segunda instância da classe "Personagem", chamada "player_2", é criada passando como argumento a variável "escolha_player_2". Por fim, é criada uma instância 
        da classe "Npc", chamada "npc".
    """
    # Instancia os bonecos
    player_1 = Personagem(escolha_player_1, "", 0, 0, 0, 0, 0, 0)
    player_2 = Personagem(escolha_player_2, "", 0, 0, 0, 0, 0, 0)
    npc = Npc()
    
    # Printa cada classe
    print("Player 1:\n")
    fmg.print_classe(player_1) 
    print("\n\n")
    
    print("Player 2:\n")
    fmg.print_classe(player_2) 
    print("\n\n")

    print("NPC:\n")
    fmg.print_classe(npc) 
    print("\n\n")


    """
        A função "determina_turno" é chamada com três argumentos: "player_1", "player_2" e "npc". Esta função retorna dois valores: "turn_valores" e "turn_nomes". "turn_valores" contém valores que 
        indicam a ordem de turnos dos personagens, enquanto "turn_nomes" contém o nome dos personagens em ordem de turno. Estas variáveis são então usadas em algum outro ponto do código para determinar 
        a ordem de jogadas dos personagens.
    """
    # Define o turno dos personagens
    turn_valores, turn_nomes = fmg.determina_turno(player_1, player_2, npc)
    
    # Printa a ordem dos turnos
    print("Ordem dos turnos: ", turn_nomes)   

    """
        Adicionar e armazenar as informações de HP (pontos de vida) e CA (Classe de Armadura) dos personagens "player_1", "player_2" e "npc". Os valores são obtidos através de acesso às propriedades 
        "pv" e "ca" dos objetos desses personagens, respectivamente. Estas variáveis serão usadas posteriormente na representação gráfica das informações de HP e CA dos personagens.
    """
    # Adiciona a variável que representa o HP do personagem/NPC
    hp_value_personagem_player_1 = player_1.pv
    hp_value_personagem_player_2 = player_2.pv
    hp_value_npc = npc.pv
    
    # Adiciona a variável que representa o HP do personagem/NPC
    ca_value_personagem_player_1 = player_1.ca
    ca_value_personagem_player_2 = player_2.ca
    ca_value_npc = npc.ca

    """
        Este trecho de código parece definir três variáveis booleanas, key_pressed_player_1, key_pressed_player_2 e key_pressed_bot, todas inicializadas como False. Essas variáveis podem ser usadas para 
        controlar se uma determinada tecla foi pressionada pelo jogador 1, jogador 2 ou pelo bot. Quando a tecla é pressionada, a variável correspondente é alterada para True, indicando que a tecla foi 
        pressionada e assim ele não podera clicar novamente até que seu turno recomece.
    """
    key_pressed_player_1 = False
    key_pressed_player_2 = False
    key_pressed_bot = False
    
    turn = 1
    
    player_1_vivo = True
    player_2_vivo = True
    npc_vivo = True
    
    # Variaveis para o npc
    quantidade_cura_npc = 3   # Vezes que o elemental pode rodar uma cura
    ocioso = 0                # Quantidade de turnos, quando >= 3, ele recupera 1 de cura
    npc_estado = 1            # Determina o estado que o boneco está
     
    # Loop de jogo
    running = True
        
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                    
            elif event.type == pygame.KEYDOWN:

                """ Está parte é responsável por gerenciar o turno de jogada dos jogadores em uma partida de jogo de RPG. A partir de uma lista chamada "turn_nomes" que contém o nome dos jogadores em ordem 
                    aleatória (Player_1, Player_2 e Bot), cada jogador é chamado uma vez e seu movimento é executado. Por exemplo, na primeira iteração da lista, se o primeiro elemento for "Player_1", a função 
                    "movimentacao_player_1" é chamada para movimentar o personagem do jogador 1 na tela. Da mesma forma, se o próximo elemento na lista for "Player_2", a função "movimentacao_player_2" é chamada 
                    para movimentar o personagem do jogador 2. Se o próximo elemento na lista for "Elemental", a função "movimentacao_npc" é chamada para movimentar o Bot. Antes de cada jogada, é verificado se a 
                    jogada já foi realizada usando variáveis booleanas (key_pressed_player_1, key_pressed_player_2, key_pressed_bot), e se a jogada já foi realizada, o jogador não é chamado para uma nova jogada. 
                    Além disso, as informações de vida dos personagens são passadas como argumentos para as funções de movimentação. Temos uma combinação de 6 possibilidades do turn_name ter aleatorizado, sendo elas:
                    
                    Player_1, Player_2, Elemental
                    Player_1, Elemental, Player_2
                    
                    Player_2, Player_1, Elemental
                    Player_2, Elemental, Player_1
                    
                    Elemental, Player_1, Player_2
                    Elemental, Player_2, Player_1"""
                
                # Teste para o turn_nomes[0]
                if turn_nomes[0] == name_personagem_1 and key_pressed_player_1 != True:
                    key_pressed_player_1, hp_value_npc, hp_value_personagem_player_1 = mv.movimentacao_player_1(event, screen, mapa, per_rect_player_1, font, hp_value_personagem_player_1, key_pressed_player_1,
                                                                                  npc_rect, player_1, npc, hp_value_npc)
                    
                    if(key_pressed_player_1 == True):
                        turn += 1
                    
                elif turn_nomes[0] == name_personagem_2 and key_pressed_player_2 != True:
                    key_pressed_player_2, hp_value_npc, hp_value_personagem_player_2 = mv.movimentacao_player_2(event, screen, mapa, per_rect_player_2, font, hp_value_personagem_player_2, key_pressed_player_2,
                                                                                                  npc_rect, player_2, npc, hp_value_npc)

                    if(key_pressed_player_2 == True):
                        turn += 1

                elif turn_nomes[0] == "Elemental" and key_pressed_bot != True:
                    key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, quantidade_cura_npc, ocioso = mv.movimentacao_npc(event, screen, mapa, npc_rect, font, 
                                                                                                                                            hp_value_npc, key_pressed_bot,
                                                                                                                                            player_1, player_2, npc, 
                                                                                                                                            hp_value_personagem_player_1, hp_value_personagem_player_2,
                                                                                                                                            per_rect_player_1, per_rect_player_2, 
                                                                                                                                            player_1_vivo, player_2_vivo,
                                                                                                                                            quantidade_cura_npc, ocioso, npc_estado)
                    
                    if(key_pressed_bot == True):
                        turn += 1
                    
                # Teste para o turn_nomes[1]    
                elif turn_nomes[1] == name_personagem_1 and key_pressed_player_1 != True:
                    key_pressed_player_1, hp_value_npc, hp_value_personagem_player_1 = mv.movimentacao_player_1(event, screen, mapa, per_rect_player_1, font, hp_value_personagem_player_1, key_pressed_player_1,
                                                                                                  npc_rect, player_1, npc, hp_value_npc)
                
                    if(key_pressed_player_1 == True):
                        turn += 1
                    
                elif turn_nomes[1] == name_personagem_2 and key_pressed_player_2 != True:
                    key_pressed_player_2, hp_value_npc, hp_value_personagem_player_2 = mv.movimentacao_player_2(event, screen, mapa, per_rect_player_2, font, hp_value_personagem_player_2, key_pressed_player_2,
                                                                                                    npc_rect, player_2, npc, hp_value_npc)
                
                    if(key_pressed_player_2 == True):
                        turn += 1
                    
                elif turn_nomes[1] == "Elemental" and key_pressed_bot != True:
                    key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, quantidade_cura_npc, ocioso = mv.movimentacao_npc(event, screen, mapa, npc_rect, font, 
                                                                                                                                            hp_value_npc, key_pressed_bot,
                                                                                                                                            player_1, player_2, npc, 
                                                                                                                                            hp_value_personagem_player_1, hp_value_personagem_player_2,
                                                                                                                                            per_rect_player_1, per_rect_player_2, 
                                                                                                                                            player_1_vivo, player_2_vivo,
                                                                                                                                            quantidade_cura_npc, ocioso, npc_estado)
                   
                    if(key_pressed_bot == True):
                        turn += 1 
                    
                # Teste para o turn_nomes[2]   
                elif turn_nomes[2] == name_personagem_1 and key_pressed_player_1 != True:
                    key_pressed_player_1, hp_value_npc, hp_value_personagem_player_1 = mv.movimentacao_player_1(event, screen, mapa, per_rect_player_1, font, hp_value_personagem_player_1, key_pressed_player_1,
                                                                                                  npc_rect, player_1, npc, hp_value_npc)
                    
                    if(key_pressed_player_1 == True):
                        turn += 1
                    
                elif turn_nomes[2] == name_personagem_2 and key_pressed_player_2 != True:
                    key_pressed_player_2, hp_value_npc, hp_value_personagem_player_2 = mv.movimentacao_player_2(event, screen, mapa, per_rect_player_2, font, hp_value_personagem_player_2, key_pressed_player_2,
                                                                                                  npc_rect, player_2, npc, hp_value_npc)
                    
                    if(key_pressed_player_2 == True):
                        turn += 1
                    
                elif turn_nomes[2] == "Elemental" and key_pressed_bot != True:
                    key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, quantidade_cura_npc, ocioso = mv.movimentacao_npc(event, screen, mapa, npc_rect, font, 
                                                                                                                                            hp_value_npc, key_pressed_bot,
                                                                                                                                            player_1, player_2, npc, 
                                                                                                                                            hp_value_personagem_player_1, hp_value_personagem_player_2,
                                                                                                                                            per_rect_player_1, per_rect_player_2, 
                                                                                                                                            player_1_vivo, player_2_vivo,
                                                                                                                                            quantidade_cura_npc, ocioso, npc_estado)
                    
                    if(key_pressed_bot == True):
                        turn += 1
        
        """
            Este trecho de código é parte do RPG, sendo uma das mais importantes parte da renderização dos elementos na tela do jogo é feita aqui todas as vezes que o loop passa por aqui. Primeiro, são redesenhados 
            três elementos na tela (personagem 1, personagem 2 e um personagem NPC), utilizando a função "elementos_tela()". Em seguida, são chamadas as funções "barra_HP" e "barra_CA" para desenhar as barras de vida 
            e de CA (proteção) dos personagens. Depois, é verificada a vida dos personagens com a função "testa_vida", que finaliza o jogo caso a vida de algum personagem seja menor que 0. Em seguida, é impresso na tela 
            a ordem de turnos com a função "turn_order". Finalmente, é verificado o sistema de turnos, onde se três ações tiverem sido realizadas, a função "verifica_botoes_precionados" é chamada para resetar o sistema. 
            Por fim, a tela é atualizada e um pequeno delay é adicionado antes de começar o próximo loop de jogo.
        """                       
        # Chama a função barra_HP ao final do loop de jogo
        fmg.barra_HP(per_rect_player_1, screen, hp_value_personagem_player_1, font_hp_ca)
        fmg.barra_HP(per_rect_player_2, screen, hp_value_personagem_player_2, font_hp_ca)
        fmg.barra_HP(npc_rect, screen, hp_value_npc, font_hp_ca)
        
        # Chama a função barra_CA ao final do loop de jogo
        fmg.barra_CA(per_rect_player_1, screen, ca_value_personagem_player_1, font_hp_ca)
        fmg.barra_CA(per_rect_player_2, screen, ca_value_personagem_player_2, font_hp_ca)
        fmg.barra_CA(npc_rect, screen, ca_value_npc, font_hp_ca)

        # Atualiza a tela
        pygame.display.update()

        # Printa os turnos
        fmg.turn_order(screen, turn_nomes, turn, font_turns, font)
        
        # Verifia o sistema de turnos
        if((key_pressed_player_1 == True) and (key_pressed_player_2 == True) and (key_pressed_bot == True)):
            key_pressed_player_1, key_pressed_player_2, key_pressed_bot = fmg.verifica_botoes_precionados(key_pressed_player_1, key_pressed_player_2, key_pressed_bot)
        
        # Testa se o player está morto
        player_1_vivo, player_2_vivo, npc_vivo, per_image_player_1, per_image_player_2, npc_image = fmg.vivo_morto(hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc,
                                                                                                        player_1_vivo, player_2_vivo, npc_vivo,
                                                                                                        per_image_player_1, per_image_player_2, npc_image,
                                                                                                        personagem_1_dead, personagem_2_dead)
        
        # Testa a vida dos personagens, se caso for < 0, finaliza o jogo
        fmg.testa_vida(player_1_vivo, player_2_vivo, npc_vivo, screen)
        
        # Determina a orderm que será printado os turnos na tela, no caso server para que o turno que for, o nome fique em roxo
        if turn > 3:
            turn = 1
        
        
        # Atualiza a tela
        mt.update_tela()
        
        # Desenha o personagem 1 na tela
        mt.elementos_tela(screen, per_image_player_1, per_rect_player_1)
        
        # Desenha o personagem 2 na tela
        mt.elementos_tela(screen, per_image_player_2, per_rect_player_2)
        
        # Desenha o personagem NPC na tela
        mt.elementos_tela(screen, npc_image, npc_rect)
        
        # Define um delay para o proximo movimento
        mt.delay(70)
        
        # Altera uma configuração para náo bugar a proxima entrada
        mt.display_flip()


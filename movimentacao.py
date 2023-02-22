import manipulacao_tela as mt
import manipulacao_gameplay as mg
import funcoes_manipulacao_gameplay as fmg
import dados as d
import pygame
import random as rd
import math
 
# Define quantos pixels, o movimento de qualque boneco, poderá realizar
movimentacao = 100

# Define a distancia de engajamento entre os bonecos
distancia_engajamento = 100

""" Estas funções determinão a movimentação de cada player, chamados nas suas respectivas vezes na ordem dost urnos, aqui qualquer movimentação e ataque será realizado a atualizado no mapa, 
    podemos nos movimentar utilizando as setinhas do teclado, no rpg de mesa existe a movimentação na diagonal, mas por efeito de simplicidade, aqui apenas pode ir para os 4 pontos sendo 
    para a esquerda, direita, cima e baixo. Com o botão "z" podemos realizar um ataque ao oponente apenas se estiverem "engajados" (quando os dois bonecos estão perto um do outro). Apertando 
    o botão 9, o turno passara para o próximo da lista de "turn_nomes[n], e alem disse temos o botão 0 para finalizar o jogo, fechando-o"
"""
def movimentacao_player_1(event, screen, mapa, per_rect_player_1, font, hp_value_personagem_player_1, key_pressed_player_1,
                          npc_rect, player_1, npc, hp_value_npc):
    
    
    
    if hp_value_personagem_player_1 <= 0:
        print("Player 1 já está morto")
        key_pressed_player_1 = True
        return key_pressed_player_1, hp_value_npc, hp_value_personagem_player_1
    
    
    elif event.key == pygame.K_LEFT:
        mt.atualizacao_movimentacao(screen, mapa, per_rect_player_1)
        per_rect_player_1.x -= movimentacao
        key_pressed_player_1 = True

    elif event.key == pygame.K_RIGHT:
        mt.atualizacao_movimentacao(screen, mapa, per_rect_player_1)
        per_rect_player_1.x += movimentacao
        key_pressed_player_1 = True

    elif event.key == pygame.K_UP:
        mt.atualizacao_movimentacao(screen, mapa, per_rect_player_1)
        per_rect_player_1.y -= movimentacao
        key_pressed_player_1 = True

    elif event.key == pygame.K_DOWN:
        mt.atualizacao_movimentacao(screen, mapa, per_rect_player_1)
        per_rect_player_1.y += movimentacao
        key_pressed_player_1 = True

    elif event.key == pygame.K_z:
        mt.atualiza_texto(screen, mapa)
        
        # Verifica se é possivel realizar um golpe, caso sim, ele ataca, caso não, o comando realizado não é efetivado e a chave key não é mudada
        hp_value_npc, key_pressed_player_1 = fmg.realiza_golpe(per_rect_player_1, npc_rect, distancia_engajamento,
                                                            player_1, npc, hp_value_npc, key_pressed_player_1, screen, font)

    elif event.key == pygame.K_9:
        key_pressed_player_1 = True
        print("Turno do player 1 passou")
        
    elif event.key == pygame.K_0:
        mt.finaliza_pygame()

    return key_pressed_player_1, hp_value_npc, hp_value_personagem_player_1
 
def movimentacao_player_2(event, screen, mapa, per_rect_player_2, font, hp_value_personagem_player_2, key_pressed_player_2,
                          npc_rect, player_2, npc, hp_value_npc):
    
    if hp_value_personagem_player_2 <= 0:
        print("Player 2 já está morto")
        key_pressed_player_2 = True
        return key_pressed_player_2, hp_value_npc, hp_value_personagem_player_2
    
    elif event.key == pygame.K_LEFT:
        mt.atualizacao_movimentacao(screen, mapa, per_rect_player_2)
        per_rect_player_2.x -= movimentacao
        key_pressed_player_2 = True
                            
    elif event.key == pygame.K_RIGHT:
        mt.atualizacao_movimentacao(screen, mapa, per_rect_player_2)
        per_rect_player_2.x += movimentacao
        key_pressed_player_2 = True
                            
    elif event.key == pygame.K_UP:
        mt.atualizacao_movimentacao(screen, mapa, per_rect_player_2)
        per_rect_player_2.y -= movimentacao
        key_pressed_player_2 = True
                            
    elif event.key == pygame.K_DOWN:
        mt.atualizacao_movimentacao(screen, mapa, per_rect_player_2)
        per_rect_player_2.y += movimentacao
        key_pressed_player_2 = True
                        
    elif event.key == pygame.K_z:
        mt.atualiza_texto(screen, mapa)
        
        # Verifica se é possivel realizar um golpe, caso sim, ele ataca, caso não, o comando realizado não é efetivado e a chave key não é mudada
        hp_value_npc, key_pressed_player_2 = fmg.realiza_golpe(per_rect_player_2, npc_rect, distancia_engajamento, 
                                                           player_2, npc, hp_value_npc, key_pressed_player_2, screen, font)
        
    elif event.key == pygame.K_9:
        key_pressed_player_2 = True
        print("Turno do player 2 passou")
                          
    elif event.key == pygame.K_0:
        # Saida do game
        mt.finaliza_pygame()
        
    return key_pressed_player_2, hp_value_npc, hp_value_personagem_player_2

def movimentacao_npc(event, screen, mapa, npc_rect, font, 
                     hp_value_npc, key_pressed_bot,
                     player_1, player_2, npc, 
                     hp_value_personagem_player_1, hp_value_personagem_player_2,
                     per_rect_player_1, per_rect_player_2, 
                     player_1_vivo, player_2_vivo,
                     quantidade_cura_npc, ocioso, npc_estado):
    
    distancia_player_1 = fmg.verifica_distancia(per_rect_player_1, npc_rect)
    distancia_player_2 = fmg.verifica_distancia(per_rect_player_2, npc_rect)
        
    print("Distancia player_1 = ", distancia_player_1)
    print("Distancia player_2 = ", distancia_player_2)
    print("Quantidade de cura: ", quantidade_cura_npc)
    print("Npc ocioso: ", ocioso)
    
    if hp_value_npc <= 0:
        print("Elemental já está morto")
        key_pressed_bot = True
        return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, quantidade_cura_npc, ocioso
    
    elif event.key == pygame.K_8:
        key_pressed_bot = True
        print("Turno do bot passou")
    
    elif event.key == pygame.K_9:
        
        """
            Essa é uma máquina de estado que controla o comportamento de um NPC (personagem não-jogador) em um jogo. A máquina recebe informações sobre a posição dos jogadores e do NPC, assim como 
            seus pontos de vida, para decidir o que o NPC deve fazer.

            Aqui está o que cada seção da máquina de estado faz:

            - Se ambos os jogadores estiverem vivos e distantes o suficiente do NPC, o NPC vai entrar em modo ocioso, onde ele simplesmente fica parado e não faz nada. A função fmg.turn_pass_bot() 
            é chamada para atualizar o estado do NPC. Se a saúde do NPC estiver abaixo de 30% de seu valor máximo e ele ainda tiver curas disponíveis, ele vai entrar no modo de cura (estado 5), o 
            que o levará a curar-se. A função fmg.realiza_cura_npc() é chamada para executar a cura.

            - Se o jogador 2 estiver vivo e distante o suficiente do NPC, mas o jogador 1 estiver morto e perto o suficiente para entrar em combate, o NPC entrará no modo ocioso. Se a saúde do NPC 
            estiver abaixo de 30% de seu valor máximo e ele ainda tiver curas disponíveis, ele vai entrar no modo de cura (estado 5), o que o levará a curar-se. A função fmg.realiza_cura_npc() é 
            chamada para executar a cura.

            - Se o jogador 1 estiver vivo e distante o suficiente do NPC, mas o jogador 2 estiver morto e perto o suficiente para entrar em combate, o NPC entrará no modo ocioso. Se a saúde do NPC 
            estiver abaixo de 30% de seu valor máximo e ele ainda tiver curas disponíveis, ele vai entrar no modo de cura (estado 5), o que o levará a curar-se. A função fmg.realiza_cura_npc() é 
            chamada para executar a cura.

            - Se o jogador 1 estiver vivo, perto o suficiente do NPC e sua saúde estiver acima de 30% de seu valor máximo, o NPC entrará no modo de perseguir o jogador 1 (estado 2). A função 
            fmg.movimento_perseguindo() é chamada para movimentar o NPC em direção ao jogador 1.

            - Se o jogador 1 estiver vivo, perto o suficiente do NPC e sua saúde estiver abaixo de 30% de seu valor máximo, e o NPC não tiver curas disponíveis, o NPC entrará no modo de fuga (estado 6). 
            A função fmg.movimento_fugir() é chamada para movimentar o NPC para longe do jogador 1.

            - Se o jogador 2 estiver vivo, perto o suficiente do NPC e sua saúde estiver acima de 30% de seu valor máximo, o NPC entrará no modo de perseguir o jogador 2 (estado 2). A função fmg.movimento_perseguindo() 
            é chamada para movimentar o NPC em direção ao jogador 2.

            - Se o jogador 2 estiver vivo, perto o suficiente do NPC e sua saúde estiver abaixo de 30% de seu valor máximo, e o NPC não tiver curas disponíveis, o NPC entrará no modo de fuga (estado 6). A função 
            `fmg.movimento_fugir
        """
        
        if (distancia_player_1 > distancia_engajamento*2) and (distancia_player_2 > distancia_engajamento*2):
            # caso os dois player estajao vivos e longe
            key_pressed_bot, npc_estado, ocioso, quantidade_cura_npc = fmg.turn_pass_bot(key_pressed_bot, npc_estado, ocioso, quantidade_cura_npc)
            
            if (hp_value_npc <= (npc.pv * 0.3)) and (quantidade_cura_npc > 0):
                npc_estado = 5 #cura
                print("Npc esta curando")
                mt.atualiza_texto(screen, mapa)
                key_pressed_bot, hp_value_npc = fmg.realiza_cura_npc(npc, screen, font, hp_value_npc)
                quantidade_cura_npc -= 1
            
        elif (distancia_player_2 > distancia_engajamento*2) and (distancia_player_1 <= distancia_engajamento*2) and (player_1_vivo == False):
            key_pressed_bot, npc_estado, ocioso, quantidade_cura_npc = fmg.turn_pass_bot(key_pressed_bot, npc_estado, ocioso, quantidade_cura_npc)
                
            if (hp_value_npc <= (npc.pv * 0.3)) and (quantidade_cura_npc > 0):
                npc_estado = 5 #cura
                print("Npc esta curando")
                mt.atualiza_texto(screen, mapa)
                key_pressed_bot, hp_value_npc = fmg.realiza_cura_npc(npc, screen, font, hp_value_npc)
                quantidade_cura_npc -= 1
        
        elif (distancia_player_1 > distancia_engajamento*2) and (distancia_player_2 <= distancia_engajamento*2) and (player_2_vivo == False):
            key_pressed_bot, npc_estado, ocioso, quantidade_cura_npc = fmg.turn_pass_bot(key_pressed_bot, npc_estado, ocioso, quantidade_cura_npc)
            
            if (hp_value_npc <= (npc.pv * 0.3)) and (quantidade_cura_npc > 0):
                npc_estado = 5 #cura
                print("npc esta curando")
                mt.atualiza_texto(screen, mapa)
                key_pressed_bot, hp_value_npc = fmg.realiza_cura_npc(npc, screen, font, hp_value_npc)
                quantidade_cura_npc -= 1
                            
        elif (distancia_player_1 <= distancia_engajamento*2) and (distancia_player_1 > distancia_engajamento) and (hp_value_npc > (npc.pv * 0.3)) and (player_1_vivo == True):
            npc_estado = 2 #perseguindo player
            print("O Elemental ta perseguindo o player 1")
            key_pressed_bot = fmg.movimento_perseguindo(per_rect_player_1, npc_rect, screen, mapa, key_pressed_bot)
            
            return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, quantidade_cura_npc, ocioso
        
        elif (distancia_player_1 <= distancia_engajamento*2) and (hp_value_npc <= (npc.pv * 0.3)) and (player_1_vivo == True) and (quantidade_cura_npc == 0):
            npc_estado = 6 #fugir
        
            print("O Elemental está fujindo player 1")
            key_pressed_bot = fmg.movimento_fugir(per_rect_player_1, npc_rect, screen, mapa, key_pressed_bot)
            
            return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, quantidade_cura_npc, ocioso

        elif (distancia_player_2 <= distancia_engajamento*2) and (distancia_player_2 > distancia_engajamento) and (hp_value_npc > (npc.pv * 0.3)) and (player_2_vivo == True):
            npc_estado = 2 #perseguindo player
            print("O Elemental ta perseguindo do player 2")
            key_pressed_bot = fmg.movimento_perseguindo(per_rect_player_2, npc_rect, screen, mapa, key_pressed_bot)
            
            return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, quantidade_cura_npc, ocioso
                
        elif (distancia_player_2 <= distancia_engajamento*2) and (hp_value_npc <= (npc.pv * 0.3)) and (player_2_vivo == True) and (quantidade_cura_npc == 0):
            npc_estado = 6 #fugir

            print("O Elemental está fujindo do player 2")

            key_pressed_bot = fmg.movimento_fugir(per_rect_player_2, npc_rect, screen, mapa, key_pressed_bot)
            
            return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, quantidade_cura_npc, ocioso
        
        elif (distancia_player_1 <= distancia_engajamento) and (player_1_vivo == True):
            npc_estado = 3 #em combate
            print("O Elemental esta em combate com o player 1")
            
            if (hp_value_npc > (npc.pv * 0.3)):
                npc_estado = 4 #ataque
                print("Golpe no player 1")
                mt.atualiza_texto(screen, mapa)
                
                # Verifica se é possivel realizar um golpe, caso sim, ele ataca, caso não, o comando realizado não é efetivado e a chave key não é mudada
                hp_value_personagem_player_1, key_pressed_bot = fmg.realiza_golpe(npc_rect, per_rect_player_1, distancia_engajamento, 
                                                                                npc, player_1, hp_value_personagem_player_1, key_pressed_bot, screen, font)


            elif (hp_value_npc <= (npc.pv * 0.3)) and (quantidade_cura_npc > 0):
                npc_estado = 5 #cura
                print("Npc esta curando")
                mt.atualiza_texto(screen, mapa)
                key_pressed_bot, hp_value_npc = fmg.realiza_cura_npc(npc, screen, font, hp_value_npc)
                quantidade_cura_npc -= 1


            elif (hp_value_npc <= (npc.pv * 0.3)) and (quantidade_cura_npc == 0):
                npc_estado = 6 #fugir
                
                key_pressed_bot = fmg.movimento_fugir(per_rect_player_1, npc_rect, screen, mapa, key_pressed_bot)     
                     
        elif (distancia_player_2 <= distancia_engajamento) and (player_2_vivo == True):
            npc_estado = 3 #em combate
            print("O Elemental esta em combate com o player 2")
            
            if (hp_value_npc > (npc.pv * 0.3)):
                npc_estado = 4 #ataque
                mt.atualiza_texto(screen, mapa)
                print("Golpe no player 2")
                # Verifica se é possivel realizar um golpe, caso sim, ele ataca, caso não, o comando realizado não é efetivado e a chave key não é mudada
                hp_value_personagem_player_2, key_pressed_bot = fmg.realiza_golpe(npc_rect, per_rect_player_2, distancia_engajamento, 
                                                                                  npc, player_2, hp_value_personagem_player_2, key_pressed_bot, screen, font)


            elif (hp_value_npc <= (npc.pv * 0.3)) and (quantidade_cura_npc > 0):
                npc_estado = 5 #cura
                print("npc esta curando")
                mt.atualiza_texto(screen, mapa)
                key_pressed_bot, hp_value_npc = fmg.realiza_cura_npc(npc, screen, font, hp_value_npc)
                quantidade_cura_npc -= 1

            elif (hp_value_npc <= (npc.pv * 0.3)) and (quantidade_cura_npc == 0):
                npc_estado = 6 #fugir
                
                key_pressed_bot = fmg.movimento_fugir(per_rect_player_2, npc_rect, screen, mapa, key_pressed_bot)  
        
        elif (distancia_player_1 <= distancia_engajamento*2):
    
            key_pressed_bot = fmg.movimento_fugir(per_rect_player_1, npc_rect, screen, mapa, key_pressed_bot)

        elif (distancia_player_2 <= distancia_engajamento*2):

            key_pressed_bot = fmg.movimento_fugir(per_rect_player_2, npc_rect, screen, mapa, key_pressed_bot)
                  
        elif (distancia_player_1 > distancia_engajamento*2) and (distancia_player_2 > distancia_engajamento*2):
            npc_estado = 1 #ocioso
            ocioso += 1
            
            if (hp_value_npc <= (npc.pv * 0.3)) and (quantidade_cura_npc > 0):
                npc_estado = 5 #cura
                print("Npc esta curando")
                mt.atualiza_texto(screen, mapa)
                key_pressed_bot, hp_value_npc = fmg.realiza_cura_npc(npc, screen, font, hp_value_npc)
                quantidade_cura_npc -= 1
                             
    elif event.key == pygame.K_0:
        # Saida do game
        mt.finaliza_pygame()
        
    return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, quantidade_cura_npc, ocioso


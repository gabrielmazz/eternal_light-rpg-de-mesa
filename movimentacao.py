import manipulacao_tela as mt
import manipulacao_gameplay as mg
import funcoes_manipulacao_gameplay as fmg
import pygame
import estado as es
 
# Define quantos pixels, o movimento de qualque boneco, poderá realizar
movimentacao = 100

# Define a distancia de engajamento entre os bonecos
distancia_engajamento = 100



""" Estas funções determinão a movimentação de cada player, chamados nas suas respectivas vezes na ordem ddos
    turnos, aqui qualquer movimentação e ataque será realizado a atualizado no mapa, podemos nos movimentar utilizando
    as setinhas do teclado, no rpg de mesa existe a movimentação na diagonal, mas por efeito de simplicidade, aqui apenas
    pode ir para os 4 pontos sendo para a esquerda, direita, cima e baixo. Com o botão "z" podemos realizar um ataque ao
    oponente apenas se estiverem "engajados" (quando os dois bonecos estão perto um do outro). Apertando o botão 9, o turno
    passara para o próximo da lista de "turn_nomes[n], e alem disse temos o botão 0 para finalizar o jogo, fechando-o"
"""
def movimentacao_player_1(event, screen, mapa, per_rect_player_1, font, hp_value_personagem_player_1, key_pressed_player_1,
                          npc_rect, player_1, npc, hp_value_npc):
    
    if hp_value_personagem_player_1 <= 0:
        print("Player 1 já está morto")
        key_pressed_player_1 = True
        return key_pressed_player_1, hp_value_npc

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

    return key_pressed_player_1, hp_value_npc
 
def movimentacao_player_2(event, screen, mapa, per_rect_player_2, font, hp_value_personagem_player_2, key_pressed_player_2,
                          npc_rect, player_2, npc, hp_value_npc):
    
    if hp_value_personagem_player_2 <= 0:
        print("Player 2 já está morto")
        key_pressed_player_2 = True
        return key_pressed_player_2, hp_value_npc
    
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
        
    return key_pressed_player_2, hp_value_npc

def movimentacao_npc(event, screen, mapa, npc_rect, font, hp_value_npc, key_pressed_bot,
                     player_1, player_2, npc, hp_value_personagem_player_1, hp_value_personagem_player_2,
                     per_rect_player_1, per_rect_player_2, quantide_cura_npc, ocioso, npc_estado):
    
    if hp_value_personagem_player_1 <= 0:
        print("Elemental já está morto")
        key_pressed_bot = True
        return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2
    
    elif event.key == pygame.K_9:
        distancia_player_1 = fmg.verifica_engajamento_estado(npc_rect, per_rect_player_1)
        distancia_player_2 = fmg.verifica_engajamento_estado(npc_rect, per_rect_player_2)
        
        print("player_1: ", distancia_player_1)
        print("player_2: ", distancia_player_2)
        
        key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, quantide_cura_npc, ocioso, npc_estado = es.estado(npc_rect, distancia_player_1, distancia_player_2, distancia_engajamento*2, 
                                                                                                distancia_engajamento, per_rect_player_1, per_rect_player_2, hp_value_npc, npc.pv, hp_value_personagem_player_1, hp_value_personagem_player_2,
                                                                                                player_1, player_2, npc, screen, font, mapa, key_pressed_bot, quantide_cura_npc, ocioso, npc_estado)
        
        
        
    return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, quantide_cura_npc, ocioso, npc_estado

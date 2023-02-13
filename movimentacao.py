import manipulacao_tela as mt
import manipulacao_gameplay as mg
import dados as d
import pygame
import random as rd
import math
 
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
        hp_value_npc, key_pressed_player_1 = realiza_golpe(per_rect_player_1, npc_rect, distancia_engajamento,
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
        hp_value_npc, key_pressed_player_2 = realiza_golpe(per_rect_player_2, npc_rect, distancia_engajamento, 
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
                     per_rect_player_1, per_rect_player_2):
    
    if hp_value_personagem_player_1 <= 0:
        print("Elemental já está morto")
        key_pressed_bot = True
        return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2
    
    elif event.key == pygame.K_LEFT:
        mt.atualizacao_movimentacao(screen, mapa, npc_rect)
        npc_rect.x -= movimentacao
        key_pressed_bot = True
                            
    elif event.key == pygame.K_RIGHT:
        mt.atualizacao_movimentacao(screen, mapa, npc_rect)
        npc_rect.x += movimentacao
        key_pressed_bot = True
                            
    elif event.key == pygame.K_UP:
        mt.atualizacao_movimentacao(screen, mapa, npc_rect)
        npc_rect.y -= movimentacao
        key_pressed_bot = True
                            
    elif event.key == pygame.K_DOWN:
        mt.atualizacao_movimentacao(screen, mapa, npc_rect)
        npc_rect.y += movimentacao
        key_pressed_bot = True
                        
    # COMO AINDA NÃO EXISTE A IA DE FATO, USA-SE O BOTÃO Z PARA ATACAR O PLAYER 1
    elif event.key == pygame.K_z:
        mt.atualiza_texto(screen, mapa)
        
        # Verifica se é possivel realizar um golpe, caso sim, ele ataca, caso não, o comando realizado não é efetivado e a chave key não é mudada
        hp_value_personagem_player_1, key_pressed_bot = realiza_golpe(npc_rect, per_rect_player_1, distancia_engajamento, 
                                                                      player_1, npc, hp_value_personagem_player_1, key_pressed_bot, screen, font)
        
      
      
    # COMO AINDA NÃO EXISTE A IA DE FATO, USA-SE O BOTÃO X PARA ATACAR O PLAYER 2  
    elif event.key == pygame.K_x:
        mt.atualiza_texto(screen, mapa)
        
        # Verifica se é possivel realizar um golpe, caso sim, ele ataca, caso não, o comando realizado não é efetivado e a chave key não é mudada
        hp_value_personagem_player_2, key_pressed_bot = realiza_golpe(npc_rect, per_rect_player_2, distancia_engajamento, 
                                                                      player_2, npc, hp_value_personagem_player_2, key_pressed_bot, screen, font)
          
    elif event.key == pygame.K_9:
        key_pressed_bot = True
        print("Turno do bot passou")
                            
    elif event.key == pygame.K_0:
        # Saida do game
        mt.finaliza_pygame()
        
    return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2


"""
    Este código implementa duas funções, a primeira função "verifica_engajamento" é responsável por verificar se dois retângulos estão engajados. Isso é feito pela verificação da distância 
    entre os centros dos dois retângulos. Se a distância for menor ou igual à distância de engajamento, a função retorna "True", caso contrário retorna "False". A segunda função "realiza_golpe" 
    verifica se o jogador 1 está engajado com o jogador 2. Isso é feito chamando a função "verifica_engajamento". Se o jogador 1 não estiver engajado, a função imprime "Você não está engajado" 
    e retorna o valor de hp_value e key_pressed. Se o jogador 1 estiver engajado, então ele rola os dados usando a função "d.rolagem_20_separados" e verifica se o resultado é igual a 20 ou se 
    é maior ou igual ao CA (Classe de Armadura) do jogador 2. Se for, então a vida do jogador 2 é decrementada pelo valor de dice_roll_proficiencia e a função "mg.draw_dice_roll" é chamada para 
    desenhar os resultados dos dados na tela. Caso contrário, a função imprime "Você não acertou" e a função "mg.draw_dice_roll" é chamada para desenhar os resultados dos dados na tela. Em ambos 
    os casos, a função retorna o valor de hp_value e key_pressed.
"""
def verifica_engajamento(per_rect, per_rect_2, distancia_engajamento):
    print("Você está engajado")
    x1, y1, z1, a1 = per_rect
    x2, y2, z2, a2 = per_rect_2
    
    # Distancia entre os centros dos retangulos
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if distancia <= distancia_engajamento:
        return True
    else:
        return False

def realiza_golpe(per_rect, per_rect_2, distancia_engajamento, player_1, player_2, hp_value, key_pressed, screen, font):
    if not verifica_engajamento(per_rect, per_rect_2, distancia_engajamento):
        print("Você não está engajado")
        return hp_value, key_pressed
    
    dice_roll, dice_roll_proficiencia = d.rolagem_20_separados(1, (player_1.destreza + player_1.arma))
    key_pressed = True

    if ((dice_roll == 20) or (dice_roll >= player_2.ca)):
        hp_value -= dice_roll_proficiencia
        print(hp_value)
        mg.draw_dice_roll(screen, font, dice_roll, dice_roll_proficiencia, (player_1.destreza + player_1.arma))
        return hp_value, key_pressed

    else:
        print("Você não acertou")
        mg.draw_dice_roll(screen, font, dice_roll, dice_roll_proficiencia, (player_1.destreza + player_1.arma))
        return hp_value, key_pressed
    
    
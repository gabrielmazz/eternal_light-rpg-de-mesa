import dados as d
import funcoes_manipulacao_gameplay as fmg
import manipulacao_tela as mt



# Define quantos pixels, o movimento de qualque boneco, poderá realizar
movimentacao = 100



def movimento_perseguindo(per_rect_player, npc_rect, screen, mapa, key_pressed_bot):
    
    # Calcula as diferenças de posição entre o jogador e o NPC em cada direção
    diff_left = per_rect_player.x - npc_rect.x
    diff_right = npc_rect.x - per_rect_player.x
    diff_up = per_rect_player.y - npc_rect.y
    diff_down = npc_rect.y - per_rect_player.y
    
    # Escolhe a direção de movimento mais adequada com base nas diferenças de posição
    if diff_left > 0 and diff_left >= max(diff_right, diff_up, diff_down):
        # Move o NPC para a esquerda
        npc_rect.x += movimentacao
        key_pressed_bot = True
        print("ana")
        
    elif diff_right > 0 and diff_right > max(diff_left, diff_up, diff_down):
        # Move o NPC para a direita
        npc_rect.x -= movimentacao
        key_pressed_bot = True
        print("danieli")
        
    elif diff_up > 0 and diff_up >= max(diff_left, diff_right, diff_down):
        # Move o NPC para cima
        npc_rect.y += movimentacao
        key_pressed_bot = True
        print("laurinha")
        
    elif diff_down > 0 and diff_down > max(diff_left, diff_right, diff_up):
        # Move o NPC para baixo
        npc_rect.y -= movimentacao
        key_pressed_bot = True
        print("cassia")
    
    # Atualiza a tela
    mt.atualizacao_movimentacao(screen, mapa, npc_rect)
       
    return key_pressed_bot


def movimento_fugir(per_rect_player, npc_rect, screen, mapa, key_pressed_bot):
    # Cima
    if(abs(per_rect_player.x - npc_rect.x)) > (abs(per_rect_player.y - npc_rect.y)):
        if(per_rect_player.y > npc_rect.y):
            mt.atualizacao_movimentacao(screen, mapa, npc_rect)
            npc_rect.y -= movimentacao
            key_pressed_bot = True
                
    # Baixo
    elif(abs(per_rect_player.x - npc_rect.x)) > (abs(per_rect_player.y - npc_rect.y)):
        if(per_rect_player.y < npc_rect.y):
            mt.atualizacao_movimentacao(screen, mapa, npc_rect)
            npc_rect.y += movimentacao
            key_pressed_bot = True
                
    # Direita
    elif(abs(per_rect_player.x - npc_rect.x)) < (abs(per_rect_player.y - npc_rect.y)):
        if(per_rect_player.x < npc_rect.x):
            mt.atualizacao_movimentacao(screen, mapa, npc_rect)
            npc_rect.x += movimentacao
            key_pressed_bot = True
        
    # Esquerda       
    elif(abs(per_rect_player.x - npc_rect.x)) < (abs(per_rect_player.y - npc_rect.y)):
        if(per_rect_player.x > npc_rect.x):
            mt.atualizacao_movimentacao(screen, mapa, npc_rect)
            npc_rect.x -= movimentacao
            key_pressed_bot = True

    return key_pressed_bot


def estado (npc_rect, distancia_player_1, distancia_player_2, distancia_engajamento, distancia_ataque, 
            per_rect_player_1, per_rect_player_2, hp_value_npc, npc_rect_maxhp, hp_value_personagem_player_1, hp_value_personagem_player_2,
            player_1, player_2, npc, screen, font, mapa, key_pressed_bot, quantide_cura_npc, ocioso, npc_estado):

    
    #testa para saber se não está engajado com nenhum player
    if (distancia_player_1 > distancia_engajamento) and (distancia_player_2 > distancia_engajamento):
        key_pressed_bot = True
        print("Turno do bot passou")
      
        npc_estado = 1 #ocioso
        ocioso += 1
        
        if (ocioso >= 3) and (cura < 3):
            cura += 1
            ocioso = 0
        
            

    #testa para saber se esta engajado com algum player e se vai perseguir ou fugir
    if (distancia_player_1 <= distancia_engajamento) and (hp_value_npc > (npc_rect_maxhp * 0.3)) and (npc_estado==1):
        npc_estado = 2 #perseguindo player
        print("o capeta ta perseguindo o player 1")
        
        key_pressed_bot = movimento_perseguindo(per_rect_player_1, npc_rect, screen, mapa, key_pressed_bot)
        
        return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, quantide_cura_npc, ocioso, npc_estado
        
                
        
    elif (distancia_player_1 <= distancia_engajamento) and (hp_value_npc <= (npc_rect_maxhp * 0.3)) and (npc_estado==1):
        npc_estado = 6 #fugir
        
        print("o capeta fico fujao player_1")
        key_pressed_bot = movimento_fugir(per_rect_player_1, npc_rect, screen, mapa, key_pressed_bot)
        
        return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, quantide_cura_npc, ocioso, npc_estado
        
        
        
        

    if (distancia_player_2 <= distancia_engajamento) and (hp_value_npc > (npc_rect_maxhp * 0.3)) and (npc_estado==1):
        npc_estado = 2 #perseguindo player
        
        print("o capeta ta perseguindo o player 2")
        
        key_pressed_bot = movimento_perseguindo(per_rect_player_2, npc_rect, screen, mapa, key_pressed_bot)
        
        return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, quantide_cura_npc, ocioso, npc_estado
        
   
                
                

    elif (distancia_player_2 <= distancia_engajamento) and (hp_value_npc <= (npc_rect_maxhp * 0.3)) and (npc_estado==1):
        npc_estado = 6 #fugir

        print("o capeta fico fujao player 2")

        key_pressed_bot = movimento_fugir(per_rect_player_2, npc_rect, screen, mapa, key_pressed_bot)
        
        return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, quantide_cura_npc, ocioso, npc_estado
        
        


    #se entrar em combate com player 1 decide o que fazer
    if (distancia_player_1 <= distancia_ataque) and (npc_estado==2):
        npc_estado = 3 #em combate


        if (hp_value_npc > (npc_rect_maxhp*0.3)) and (cura > 0):
            npc_estado = 4 #ataque
            # Verifica se é possivel realizar um golpe, caso sim, ele ataca, caso não, o comando realizado não é efetivado e a chave key não é mudada
            hp_value_personagem_player_1, key_pressed_bot = fmg.realiza_golpe(npc_rect, per_rect_player_1, distancia_engajamento, 
                                                                              player_1, npc, hp_value_personagem_player_1, key_pressed_bot, screen, font)


        elif (hp_value_npc <= (npc_rect_maxhp*0.3)) and (cura > 0):
            npc_estado = 5 #cura
            key_pressed_bot, hp_value_npc = fmg.realiza_cura_npc(npc, screen, font, hp_value_npc)
            cura -= 1


        elif (hp_value_npc <= (npc_rect_maxhp*0.3)) and (cura == 0):
            npc_estado = 6 #fugir
            
            key_pressed_bot = movimento_fugir(per_rect_player_1, npc_rect, screen, mapa, key_pressed_bot) 




    #se entrar em combate com o player 2 decide o que fazer
    if (distancia_player_2 <= distancia_ataque) and (npc_estado==2):
        npc_estado = 3 #em combate

        if (hp_value_npc > (npc_rect_maxhp*0.3)) and (cura > 0):
            npc_estado = 4 #ataque
            # Verifica se é possivel realizar um golpe, caso sim, ele ataca, caso não, o comando realizado não é efetivado e a chave key não é mudada
            hp_value_personagem_player_2, key_pressed_bot = fmg.realiza_golpe(npc_rect, per_rect_player_2, distancia_engajamento, 
                                                                              player_2, npc, hp_value_personagem_player_2, key_pressed_bot, screen, font)

        elif (hp_value_npc <= (npc_rect_maxhp*0.3)) and (cura > 0):
            npc_estado = 5 #cura
            key_pressed_bot, hp_value_npc = fmg.realiza_cura_npc(npc, screen, font, hp_value_npc, key_pressed_bot)
            cura -= 1

        elif (hp_value_npc <= (npc_rect_maxhp*0.3)) and (cura == 0):
            npc_estado = 6 #fugir
            
            key_pressed_bot = movimento_fugir(per_rect_player_2, npc_rect, screen, mapa, key_pressed_bot)
            
            
            
            
            

    #testa pra saber se boss precisa continuar fugindo ou entrou em estado ocioso
    if (npc_estado==6):
        if (distancia_player_1 <= distancia_engajamento):
            npc_estado = 6 #fugir
            
            key_pressed_bot = movimento_fugir(per_rect_player_1, npc_rect, screen, mapa, key_pressed_bot)
            
            

        if (distancia_player_2 <= distancia_engajamento):
            npc_estado = 6 #fugir
            
            key_pressed_bot = movimento_fugir(per_rect_player_2, npc_rect, screen, mapa, key_pressed_bot)
            

    elif (distancia_player_1 > distancia_engajamento) and (distancia_player_2 > distancia_engajamento):
        npc_estado = 1 #ocioso
        ocioso += 1


    return key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2, quantide_cura_npc, ocioso, npc_estado
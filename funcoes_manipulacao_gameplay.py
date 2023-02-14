import time
import dados as d
import manipulacao_tela as mt


"""
    Este trecho de código é uma função que tem como objetivo imprimir na tela as informações da classe do jogador. A função recebe como parâmetro um objeto do tipo "player", que é 
    uma classe definida em algum lugar do código. A função usa o método "print" para exibir na tela as informações da classe do jogador, que são o nome da classe, força, destreza, 
    constituição, pontos de vida (PV), Class Armor (CA) e arma. Cada informação é acessada através dos atributos do objeto "player". A string que será impressa é formatada usando o 
    método f"{}".
"""
def print_classe(player):
    print(f"Classe: {player.nome} \n   Força: {player.forca} \n   Destreza: {player.destreza} \n   Constituição: {player.constituicao} \n   PV: {player.pv} \n   Class Armor: {player.ca} \n   Arma: {player.arma}")

"""
    O código é uma função em Python que desenha a barra de HP em uma tela (representada pelo argumento "screen"). A função começa criando uma fonte de texto através da 
    chamada da função "criacao_texto" da biblioteca "mt". Em seguida, é renderizado um texto com o valor atual de HP, usando essa fonte. O texto é posicionado com relação a uma área 
    retangular fornecida como argumento ("per_rect"), no caso na parte de baixo dos tokens. Finalmente, o texto é desenhado na tela através da chamada de "screen.blit".
"""
def barra_HP(per_rect, screen, hp_value, font_hp_ca):
    # Desenha a barra de HP
    text = font_hp_ca.render(f"HP: {hp_value}", True, (255, 255, 255))
    text_rect = mt.rederiza_textos(per_rect.x + 30, per_rect.y + 80, text)
    mt.elementos_tela(screen, text, text_rect)
    
"""
    Este trecho de código define a função "barra_CA", que desenha uma barra de Class Armadura (CA) na tela. Ele usa a função "mt.criacao_texto" para criar uma fonte com tamanho 12, 
    e depois usa a fonte para renderizar o texto "CA: [valor de CA]" com a cor branca. Em seguida, ele cria um retângulo ao redor do texto e o posiciona na tela, abaixo do retângulo 
    da barra de HP. Por fim, a função usa "screen.blit" para desenhar o texto na tela.
"""
def barra_CA(per_rect, screen, ca_value, font_hp_ca):
    # Desenha a barra de CA
    text = font_hp_ca.render(f"CA: {ca_value}", True, (255, 255, 255))
    text_rect = mt.rederiza_textos(per_rect.x + 30, per_rect.y + 100, text)
    mt.elementos_tela(screen, text, text_rect)
    
"""
    Este trecho de código é uma função "testa_vida" que verifica a vida dos personagens em um jogo. A função recebe três argumentos: "hp_value_personagem_1", "hp_value_personagem_2" 
    e "hp_value_npc". A função verifica se o valor de vida de ambos os personagens é menor ou igual a 0, se for verdadeiro, a mensagem "NPC venceu o jogo" é exibida e a função 
    "finaliza_pygame" alem que mostrara por cerca de 6 segundos a imagem da vitória do NPC. Se não for verdadeiro, a função verifica se o valor de vida do NPC é menor ou igual a 0. 
    Se for verdadeiro, a mensagem "O jogador venceu o jogo" e tambem é mostrada uma imagem da vitória é exibida e a função "finaliza_pygame" é chamada.
"""
def testa_vida(hp_value_personagem_1, hp_value_personagem_2, hp_value_npc, screen):
    # Testa a vida dos personagens
    #print("teste")
    if ((hp_value_personagem_1 <= 0) and (hp_value_personagem_2 <= 0)):
        print("NPC venceu o jogo")
        imagem_vitoria = mt.carrega_imagem("img/geral/elemental.png")
        mt.tela_fundo(screen, imagem_vitoria)
        mt.update_tela()
        time.sleep(6)
        mt.finaliza_pygame()
        
    elif hp_value_npc <= 0:
        print("Os jogadores venceram o jogo")
        imagem_vitoria = mt.carrega_imagem("img/geral/jogadores.png")
        mt.tela_fundo(screen, imagem_vitoria)
        mt.update_tela()
        time.sleep(6)
        mt.finaliza_pygame()

"""
    A função define a função "draw_dice_roll", que desenha na tela o resultado do rolamento de um dado, incluindo o valor do dado rolado e a proficiência adicionada. Ele usa a biblioteca
    de renderização de texto da biblioteca Pygame para desenhar o texto na tela, com as coordenadas (10, screen.get_height() - 80). O texto mostrado é formato com o resultado do rolamento 
    do dado, juntamente com a proficiência adicionada a esse resultado.
"""
def draw_dice_roll(screen, font, dice_roll, dice_roll_proficiencia, proficiencia):
    # Printa na tela o dado rodado
    text = font.render(f"Dice Roll = {dice_roll} + {proficiencia} = {dice_roll_proficiencia}", True, (255, 255, 255))
    screen.blit(text, (10, screen.get_height() - 80))
    
"""
    Este trecho de código é uma função que determina o turno de três personagens, player_1, player_2 e npc, em uma batalha ou jogo de RPG. A função começa rolando o dado para cada um dos 
    três personagens com uma chamada à função d.rolagem_20(), que possivelmente rola um dado de 20 faces com uma modificação baseada na destreza dos personagens. Em seguida, a função cria 
    duas listas: fila_posições, que contém os nomes dos personagens, e fila_valores, que contém os resultados das rolagens de dados. Finalmente, a função chama uma outra função chamada 
    "ordena" que ordena as duas listas de acordo com os resultados das rolagens de dados em fila_valores. A função retorna as duas listas ordenadas, fila_valores e fila_posicoes.
"""
def determina_turno(player_1, player_2, npc):
    # Determina a rolagem dos bonecos
    rolagem_personagem = d.rolagem_20(1, player_1.destreza)
    rolagem_personagem_2 = d.rolagem_20(1, player_2.destreza)
    rolagem_npc = d.rolagem_20(1, npc.destreza)

    # Define a ordem de turno
    fila_posicoes = [player_1.nome, player_2.nome, npc.nome]
    fila_valores = [rolagem_personagem, rolagem_personagem_2, rolagem_npc]
    
    # Chama a função de ordenação
    fila_valores, fila_posicoes = ordena(fila_valores, fila_posicoes)
    
    return fila_valores, fila_posicoes

"""
    Este trecho de código é uma função chamada "ordena" que recebe duas listas como parâmetros: "fila_valores" e "fila_posicoes". A função tem como objetivo ordenar ambas as listas de acordo 
    com a ordem dos valores da primeira lista "fila_valores". Inicialmente, é atribuído à variáveis x e y os valores de fila_valores e fila_posicoes, respectivamente. Em seguida, a função gera 
    uma lista chamada "indices" com todos os índices de x. Então, os índices são ordenados com base nos valores correspondentes em x, usando a função "sort" e uma função anônima (lambda) que 
    indica a ordem de comparação como sendo o valor em x. A ordem dos índices é feita em ordem decrescente. Por fim, são criadas duas novas listas "new_x" e "new_y", com base na ordem dos índices 
    obtidos na etapa anterior. Ambas as listas são retornadas pela função.
"""
def ordena(fila_valores, fila_posicoes):
    #https://pt.stackoverflow.com/questions/507769/ordenar-duas-listas-com-base-na-ordem-da-primeira
    
    x = fila_valores
    y = fila_posicoes

    # Ordene os índices em vez dos elementos em si
    indices = list(range(len(x)))
    
    # Ordene os índices com relação ao seu respectivo valor em x
    indices.sort(key=lambda i: x[i], reverse=True) 

    # Crie as listas baseado na ordem dos índices
    new_x = [x[i] for i in indices]
    new_y = [y[i] for i in indices]

    return new_x, new_y

"""
    A função "turn_order" desenha na tela (screen) a ordem de turnos de jogadores (turn_nomes). A função começa definindo duas fontes de texto, uma com tamanho 18 e outra com tamanho 14. Depois, 
    é renderizado na tela um título "Turn Order" na posição (1400, 400) usando a fonte font_title. Em seguida, os três primeiros nomes dos jogadores na lista "turn_nomes" são renderizados na tela, 
    um por vez, na posição (1400, 450), (1400, 500) e (1400, 550), respectivamente, usando a fonte font. Na tela mostrará em roxo qual personagem pode agir no turno, sendo controlado pela variavel
    turn que se altera quando alguem termina de realizar algum turno
"""  
def turn_order(screen, turn_nomes, turn, font_turns, font):
    
    text_title = mt.cria_textos(font, "Turn Order", (255, 255, 255))
    mt.elementos_tela(screen, text_title, (1400, 400))
    
    if turn == 1:
        text_turn_1 = mt.cria_textos(font_turns, turn_nomes[0], (62, 0, 255))
        mt.elementos_tela(screen, text_turn_1, (1400, 450))
    else:
        text_turn_1 = mt.cria_textos(font_turns, turn_nomes[0], (255, 255, 255))
        mt.elementos_tela(screen, text_turn_1, (1400, 450))
            
    if turn == 2:
        text_turn_2 = mt.cria_textos(font_turns, turn_nomes[1], (62, 0, 255))
        mt.elementos_tela(screen, text_turn_2, (1400, 500)) 
    else:
        text_turn_2 = mt.cria_textos(font_turns, turn_nomes[1], (255, 255, 255))
        mt.elementos_tela(screen, text_turn_2, (1400, 500))

    if turn == 3:
        text_turn_3 = mt.cria_textos(font_turns, turn_nomes[2], (62, 0, 255))
        mt.elementos_tela(screen, text_turn_3, (1400, 550))
    else:
        text_turn_3 = mt.cria_textos(font_turns, turn_nomes[2], (255, 255, 255))
        mt.elementos_tela(screen, text_turn_3, (1400, 550))  
        
    mt.update_tela()
    
    
"""
    Esse trecho de código define uma função "verifica_botoes_precionados". A função recebe três parâmetros: "key_pressed_player_1", "key_pressed_player_2" e "key_pressed_bot". A função verifica se 
    os três valores são "True". Se for, a função atribui "False" aos três valores. Por fim, a função retorna os três valores atualizados.
"""         
def verifica_botoes_precionados(key_pressed_player_1, key_pressed_player_2, key_pressed_bot):
    if ((key_pressed_player_1 == True) and (key_pressed_player_2 == True) and (key_pressed_bot == True)):
        key_pressed_player_1 = False
        key_pressed_player_2 = False
        key_pressed_bot = False

    return key_pressed_player_1, key_pressed_player_2, key_pressed_bot   
    
    
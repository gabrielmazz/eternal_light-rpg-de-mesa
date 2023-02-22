import time
import dados as d
import manipulacao_tela as mt
import math

# Define quantos pixels, o movimento de qualque boneco, poderá realizar
movimentacao = 100

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
def testa_vida(player_1_vivo, player_2_vivo, npc_vivo, screen):
    # Testa a vida dos personagens
    #print("teste")
    if (player_1_vivo == False) and (player_2_vivo == False):
        print("NPC venceu o jogo")
        imagem_vitoria = mt.carrega_imagem("img/geral/elemental.png")
        mt.tela_fundo(screen, imagem_vitoria)
        mt.update_tela()
        time.sleep(6)
        mt.finaliza_pygame()
        
    elif (npc_vivo == False):
        print("Os jogadores venceram o jogo")
        imagem_vitoria = mt.carrega_imagem("img/geral/jogadores.png")
        mt.tela_fundo(screen, imagem_vitoria)
        mt.update_tela()
        time.sleep(6)
        mt.finaliza_pygame()

"""
    Essa função recebe valores que representam a vida dos personagens de um jogo e suas respectivas imagens. A função verifica se algum personagem morreu, ou seja, se a vida dele é menor 
    ou igual a zero. Se algum personagem morreu, a imagem correspondente é substituída pela imagem de um personagem morto e a variável correspondente é alterada para False indicando que 
    o personagem está morto. A função retorna as variáveis que indicam se os personagens estão vivos ou mortos, bem como suas respectivas imagens atualizadas.
"""
def vivo_morto(hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc,
               player_1_vivo, player_2_vivo, npc_vivo,
               per_image_player_1, per_image_player_2, npc_image,
               personagem_1_dead, personagem_2_dead):
    
    # Verifica se algum player ja morreu, se caso sim a variavel fica falsa
    if(hp_value_personagem_player_1 <= 0):
        per_image_player_1 = mt.carrega_imagem(personagem_1_dead)
        per_image_player_1 = mt.escala_imagem(4, per_image_player_1)
        player_1_vivo = False

    if(hp_value_personagem_player_2 <= 0):
        per_image_player_2 = mt.carrega_imagem(personagem_2_dead)
        per_image_player_2 = mt.escala_imagem(4, per_image_player_2)
        player_2_vivo = False
            
    if(hp_value_npc <= 0):
        npc_image = mt.carrega_imagem("img/personagens/npc_dead.png")
        npc_image = mt.escala_imagem(4, npc_image)
        npc_vivo = False
        
    return player_1_vivo, player_2_vivo, npc_vivo, per_image_player_1, per_image_player_2, npc_image

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

"""
    Essa função recebe dois retângulos definidos pelas suas coordenadas (x, y, largura e altura) e calcula a distância entre seus centros utilizando a fórmula de distância euclidiana. 
    Essa distância é retornada pela função. A função pode ser usada para verificar a proximidade entre dois objetos retangulares em um jogo ou em outras aplicações que envolvam geometria.
"""   
def verifica_distancia(per_rect, per_rect_2):
    x1, y1, z1, a1 = per_rect
    x2, y2, z2, a2 = per_rect_2
    
    # Distancia entre os centros dos retangulos
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distancia

"""
    A função realiza_golpe recebe as informações de dois jogadores (player_1 e player_2) e as suas respectivas posições (per_rect e per_rect_2) em um jogo. A função verifica se o jogador 1 
    está engajado com o jogador 2 e, caso contrário, retorna as informações originais de pontos de vida e teclas pressionadas.

    Se estiverem engajados, a função realiza uma rolagem de dados para determinar se o ataque foi bem sucedido ou não. Em seguida, ela subtrai a quantidade de pontos de vida que o jogador 2 
    perdeu devido ao ataque do jogador 1, caso o ataque tenha sido bem sucedido. A quantidade de pontos de vida atualizada e o estado das teclas pressionadas são retornados pela função.
"""
def realiza_golpe(per_rect, per_rect_2, distancia_engajamento, player_1, player_2, hp_value, key_pressed, screen, font):
    if not verifica_engajamento(per_rect, per_rect_2, distancia_engajamento):
        print("Você não está engajado")
        return hp_value, key_pressed
    
    dice_roll, dice_roll_proficiencia = d.rolagem_20_separados(1, (player_1.destreza + player_1.arma))
    
    draw_dice_roll(screen, font, dice_roll, dice_roll_proficiencia, (player_1.destreza + player_1.arma))
    
    key_pressed = True

    if ((dice_roll == 20) or (dice_roll >= player_2.ca)):
        hp_value -= dice_roll_proficiencia
        print(hp_value)
        return hp_value, key_pressed

    else:
        print("Você não acertou")
        return hp_value, key_pressed

"""
    A subida na encosta simples (ou hill climbing) é um algoritmo de busca local em que o objetivo é encontrar o máximo (ou mínimo) local de uma função de avaliação heurística. A busca começa em 
    um estado inicial aleatório e, em cada iteração, tenta encontrar um estado vizinho que seja melhor em termos de valor da função heurística. Se um estado vizinho melhor for encontrado, a busca 
    se move para ele e repete o processo até que um máximo (ou mínimo) local seja alcançado.
    
    A subida na encosta simples é uma abordagem simples e rápida, mas pode facilmente ficar presa em um máximo (ou mínimo) local. Isso ocorre porque a busca não explora outras regiões do espaço de 
    estados além daquela em que se encontra. Para superar essa limitação, existem variações do algoritmo que permitem uma certa quantidade de movimento "ruim" para evitar ficar preso em ótimos locais. 
    Essas variações incluem a subida na encosta com reinicialização aleatória e a subida na encosta com perturbação aleatória.
"""   

"""
    Essas funções são responsáveis por mover um personagem não jogável (NPC) em um jogo, baseado na posição do jogador. A função "movimento_perseguindo" move o NPC em direção ao jogador, escolhendo a 
    direção mais adequada com base nas diferenças de posição entre o jogador e o NPC em cada direção. A função "movimento_fugir" move o NPC em direção oposta ao jogador, ou seja, fugindo dele. Ambas as 
    funções atualizam a tela e retornam um valor que indica se alguma tecla do botão do NPC foi pressionada durante o movimento.
"""   
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
        print("NPC se movimentou para a esquerda")
        
    elif diff_right > 0 and diff_right >= max(diff_left, diff_up, diff_down):
        # Move o NPC para a direita
        npc_rect.x -= movimentacao
        key_pressed_bot = True
        print("NPC se movimentou para a direita")
        
    elif diff_up > 0 and diff_up >= max(diff_left, diff_right, diff_down):
        # Move o NPC para cima
        npc_rect.y += movimentacao
        key_pressed_bot = True
        print("NPC se movimentou para cima")
        
    elif diff_down > 0 and diff_down >= max(diff_left, diff_right, diff_up):
        # Move o NPC para baixo
        npc_rect.y -= movimentacao
        key_pressed_bot = True
        print("NPC se movimentou para baixo")
    
    # Atualiza a tela
    mt.atualizacao_movimentacao(screen, mapa, npc_rect)
       
    return key_pressed_bot

def movimento_fugir(per_rect_player, npc_rect, screen, mapa, key_pressed_bot):
    # Calcula as diferenças de posição entre o jogador e o NPC em cada direção
    diff_left = per_rect_player.x - npc_rect.x
    diff_right = npc_rect.x - per_rect_player.x
    diff_up = per_rect_player.y - npc_rect.y
    diff_down = npc_rect.y - per_rect_player.y
    
    # Escolhe a direção de movimento mais adequada com base nas diferenças de posição
    if diff_left > 0 and diff_left >= max(diff_right, diff_up, diff_down):
        # Move o NPC para a esquerda
        npc_rect.x -= movimentacao
        key_pressed_bot = True
        print("NPC se movimentou para a esquerda")
        
    elif diff_right > 0 and diff_right >= max(diff_left, diff_up, diff_down):
        # Move o NPC para a direita
        npc_rect.x += movimentacao
        key_pressed_bot = True
        print("NPC se movimentou para a direita")
        
    elif diff_up > 0 and diff_up >= max(diff_left, diff_right, diff_down):
        # Move o NPC para cima
        npc_rect.y -= movimentacao
        key_pressed_bot = True
        print("NPC se movimentou para cima")
        
    elif diff_down > 0 and diff_down >= max(diff_left, diff_right, diff_up):
        # Move o NPC para baixo
        npc_rect.y += movimentacao
        key_pressed_bot = True
        print("NPC se movimentou para baixo")
    
    # Atualiza a tela
    mt.atualizacao_movimentacao(screen, mapa, npc_rect)
       
    return key_pressed_bot

"""
    Nessa função, um NPC realiza a cura em si mesmo usando uma poção. Primeiramente, é realizada a rolagem de dois dados de oito faces mais o valor de Constituição do NPC. O resultado é exibido na tela 
    por meio da função "draw_dice_roll". Em seguida, o valor obtido é adicionado à vida atual do NPC, e a variável "key_pressed" é definida como verdadeira. Por fim, a função retorna as variáveis 
    "key_pressed" e "hp_value_npc".
"""
def realiza_cura_npc(npc, screen, font, hp_value_npc):
    # Roda a poção de cura do npc sendo 2d8 + CONS
    dice_roll, dice_roll_proficiencia = d.rolagem_8_separados(2, npc.constituicao)
    
    # Printa na tela o dado de vida rodado
    draw_dice_roll(screen, font, dice_roll, dice_roll_proficiencia, npc.constituicao)
    
    # Faz a cura do boneco
    hp_value_npc += dice_roll_proficiencia
    
    key_pressed = True
    
    return key_pressed, hp_value_npc

"""
    A função "turn_pass_bot" representa a passagem do turno do personagem não-jogador (NPC). Ao receber alguns parâmetros, como o estado atual do NPC e a quantidade de vezes que ele ficou ocioso, a 
    função atualiza o estado do NPC para ocioso, aumenta a quantidade de vezes que o NPC se cura após ficar ocioso por um determinado número de turnos e retorna alguns valores atualizados para serem 
    usados em outras partes do código. A variável "key_pressed_bot" é definida como verdadeira, indicando que uma tecla foi pressionada pelo NPC.
"""
def turn_pass_bot(key_pressed_bot, npc_estado, ocioso, quantidade_cura_npc):
    key_pressed_bot = True
    print("Turno do bot passou")
        
    npc_estado = 1 #ocioso
    ocioso += 1
                
    if (ocioso >= 3) and (quantidade_cura_npc < 3):
        quantidade_cura_npc += 1
        ocioso = 0
        
    return key_pressed_bot, npc_estado, ocioso, quantidade_cura_npc

def arredonda_para_multiplos(num):
    return round(num, -2) // 100 * 100
import pygame
import time
import manipulacao_tela as mt
import random as rd
import dados as d
import movimentacao as mv
from personagem import *
from npc import *

"""
    Este trecho de código é uma função em Python que usa a biblioteca Pygame para carregar e redimensionar uma imagem de um personagem. A função recebe 
    como parâmetro uma string "personagem" que representa o caminho da imagem do personagem. Em seguida, a imagem é carregada usando a função "pygame.image.load(personagem)". 
    Em seguida, a imagem é redimensionada usando a função "pygame.transform.scale(per_image, (per_image.get_width() // 4, per_image.get_height() // 4))", o que divide o 
    tamanho da imagem original por 4, redimensionando-a para 1/4 do seu tamanho original.
"""
def personagem_image(personagem):
    # Define a imagem do personagem
    per_image = pygame.image.load(personagem)
    per_image = pygame.transform.scale(per_image, (per_image.get_width() // 4, per_image.get_height() // 4))
    
    return per_image
 
"""
    Define uma função "personagem_image_rect" que retorna um objeto "rect" a partir de uma imagem de um personagem. O objeto "rect" é utilizado para representar o retângulo que 
    envolve a imagem do personagem, e é usado com frequência na biblioteca Pygame para detectar colisões, desenhar imagens na tela, entre outras aplicações. A função recebe como 
    parâmetros a imagem do personagem e as coordenadas x e y que definem a posição da imagem na tela. A função cria um objeto "rect" a partir da imagem do personagem usando o 
    método "get_rect". Em seguida, as posições x e y são definidas para o objeto "rect" usando os atributos "x" e "y". Finalmente, a função retorna o objeto "rect".
"""  
def personagem_image_rect(personagem_image, x, y):
    per_rect = personagem_image.get_rect()
    
    # Define a posição do personagem no mapa 1
    per_rect.x = x
    per_rect.y = y  
    
    return per_rect

"""
    Este trecho de código é uma função que tem como objetivo imprimir na tela as informações da classe do jogador. A função recebe como parâmetro um objeto do tipo "player", que é 
    uma classe definida em algum lugar do código. A função usa o método "print" para exibir na tela as informações da classe do jogador, que são o nome da classe, força, destreza, 
    constituição, pontos de vida (PV), Class Armor (CA) e arma. Cada informação é acessada através dos atributos do objeto "player". A string que será impressa é formatada usando o 
    método f"{}".
"""
def print_classe(player):
    print(f"Classe: {player.nome} \n   Força: {player.forca} \n   Destreza: {player.destreza} \n   Constituição: {player.constituicao} \n   PV: {player.pv} \n   Class Armor: {player.ca} \n   Arma: {player.arma}")

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
    O código é uma função em Python que desenha a barra de HP em uma tela (representada pelo argumento "screen"). A função começa criando uma fonte de texto através da 
    chamada da função "criacao_texto" da biblioteca "mt". Em seguida, é renderizado um texto com o valor atual de HP, usando essa fonte. O texto é posicionado com relação a uma área 
    retangular fornecida como argumento ("per_rect"), no caso na parte de baixo dos tokens. Finalmente, o texto é desenhado na tela através da chamada de "screen.blit".
"""
def barra_HP(per_rect, screen, hp_value):
    # Desenha a barra de HP
    font_hp = mt.criacao_texto("font/font1_elementary.ttf", 12)
    text = font_hp.render(f"HP: {hp_value}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = per_rect.x
    text_rect.y = per_rect.y + per_rect.height + 10
    screen.blit(text, text_rect)
    
    
"""
    Este trecho de código define a função "barra_CA", que desenha uma barra de Class Armadura (CA) na tela. Ele usa a função "mt.criacao_texto" para criar uma fonte com tamanho 12, 
    e depois usa a fonte para renderizar o texto "CA: [valor de CA]" com a cor branca. Em seguida, ele cria um retângulo ao redor do texto e o posiciona na tela, abaixo do retângulo 
    da barra de HP. Por fim, a função usa "screen.blit" para desenhar o texto na tela.
"""
def barra_CA(per_rect, screen, ca_value):
    # Desenha a barra de CA
    font_ca = mt.criacao_texto("font/font1_elementary.ttf", 12)
    text = font_ca.render(f"CA: {ca_value}", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.x = per_rect.x
    text_rect.y = per_rect.y + per_rect.height + 30
    screen.blit(text, text_rect)

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
def turn_order(screen, turn_nomes, turn):
    font_title = mt.criacao_texto("font/font1_elementary.ttf", 18)
    font = mt.criacao_texto("font/font1_elementary.ttf", 14)
    
    text_title = font_title.render("Turn Order", True, (255, 255, 255))
    screen.blit(text_title, (1400, 400))
    
    if turn == 1:
        text_turn_1 = font.render(turn_nomes[0], True, (62, 0, 255))
        screen.blit(text_turn_1, (1400, 450))
    else:
        text_turn_1 = font.render(turn_nomes[0], True, (255, 255, 255))
        screen.blit(text_turn_1, (1400, 450))
            
    if turn == 2:
        text_turn_2 = font.render(turn_nomes[1], True, (62, 0, 255))
        screen.blit(text_turn_2, (1400, 500))  
    else:
        text_turn_2 = font.render(turn_nomes[1], True, (255, 255, 255))
        screen.blit(text_turn_2, (1400, 500))

    if turn == 3:
        text_turn_3 = font.render(turn_nomes[2], True, (62, 0, 255))
        screen.blit(text_turn_3, (1400, 550))
    else:
        text_turn_3 = font.render(turn_nomes[2], True, (255, 255, 255))
        screen.blit(text_turn_3, (1400, 550))    
        
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

def gameplay(personagem_1, personagem_2, screen, mapa, name_personagem_1, name_personagem_2, escolha_player_1, escolha_player_2):
    
    """
        Faz a inicialização e preparação para desenhar a tela do jogo. A primeira coisa que é feita é a definição da fonte que será usada na tela. Em seguida, o fundo do mapa 
        é desenhado na tela. Depois disso, todos os eventos que ocorrerão são zerados. Em seguida, as imagens dos personagens e do NPC são carregadas e suas posições na tela são definidas.
    """
    # Define a font que será usada
    font = mt.criacao_texto("font/font1_elementary.ttf", 18)

    # Desenha o mapa na screen
    mt.tela_fundo(screen, mapa)
        
    # Zera todos os eventos que ocorrerão
    mt.zera_eventos()
    
    # Carrega a imagem do personagem player 1
    per_image_player_1 = personagem_image(personagem_1)
    
    # Carrega a posição da imagem do personagem player 1
    per_rect_player_1 = personagem_image_rect(per_image_player_1, 100, 100)
    
    # Carrega a imagem do personagem player 2
    per_image_player_2 = personagem_image(personagem_2)
    
    # Carrega a posição da imagem do personagem player 2
    per_rect_player_2 = personagem_image_rect(per_image_player_2, 300, 100)
    
    # Carrega a imagem do NPC
    npc_image = personagem_image("img/personagens/npc.png")
    
    # Carrega a posição da imagem do NPC
    npc_rect = personagem_image_rect(npc_image, 200, 100)
    
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
    print_classe(player_1) 
    print("\n\n")
    
    print("Player 2:\n")
    print_classe(player_2) 
    print("\n\n")

    print("NPC:\n")
    print_classe(npc) 
    print("\n\n")


    """
        A função "determina_turno" é chamada com três argumentos: "player_1", "player_2" e "npc". Esta função retorna dois valores: "turn_valores" e "turn_nomes". "turn_valores" contém valores que 
        indicam a ordem de turnos dos personagens, enquanto "turn_nomes" contém o nome dos personagens em ordem de turno. Estas variáveis são então usadas em algum outro ponto do código para determinar 
        a ordem de jogadas dos personagens.
    """
    # Define o turno dos personagens
    turn_valores, turn_nomes = determina_turno(player_1, player_2, npc)
    
    # Printa a ordem dos turnos
    print(turn_nomes)    

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
                    key_pressed_player_1, hp_value_npc = mv.movimentacao_player_1(event, screen, mapa, per_rect_player_1, font, hp_value_personagem_player_1, key_pressed_player_1,
                                                                                  npc_rect, player_1, npc, hp_value_npc)
                    
                    turn += 1
                    
                elif turn_nomes[0] == name_personagem_2 and key_pressed_player_2 != True:
                    key_pressed_player_2, hp_value_npc = mv.movimentacao_player_2(event, screen, mapa, per_rect_player_2, font, hp_value_personagem_player_2, key_pressed_player_2,
                                                                                                  npc_rect, player_2, npc, hp_value_npc)

                    turn += 1

                elif turn_nomes[0] == "Elemental" and key_pressed_bot != True:
                    key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2 = mv.movimentacao_npc(event, screen, mapa, npc_rect, font, hp_value_npc, key_pressed_bot,
                                                                        player_1, player_2, npc, hp_value_personagem_player_1, hp_value_personagem_player_2,
                                                                        per_rect_player_1, per_rect_player_2)
                    
                    turn += 1
                    
                # Teste para o turn_nomes[1]    
                elif turn_nomes[1] == name_personagem_1 and key_pressed_player_1 != True:
                    key_pressed_player_1, hp_value_npc = mv.movimentacao_player_1(event, screen, mapa, per_rect_player_1, font, hp_value_personagem_player_1, key_pressed_player_1,
                                                                                                  npc_rect, player_1, npc, hp_value_npc)
                
                    turn += 1
                    
                elif turn_nomes[1] == name_personagem_2 and key_pressed_player_2 != True:
                    key_pressed_player_2, hp_value_npc = mv.movimentacao_player_2(event, screen, mapa, per_rect_player_2, font, hp_value_personagem_player_2, key_pressed_player_2,
                                                                                                    npc_rect, player_2, npc, hp_value_npc)
                
                    turn += 1
                    
                elif turn_nomes[1] == "Elemental" and key_pressed_bot != True:
                    key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2 = mv.movimentacao_npc(event, screen, mapa, npc_rect, font, hp_value_npc, key_pressed_bot,
                                                                        player_1, player_2, npc, hp_value_personagem_player_1, hp_value_personagem_player_2,
                                                                        per_rect_player_1, per_rect_player_2)
                   
                    turn += 1 
                    
                # Teste para o turn_nomes[2]   
                elif turn_nomes[2] == name_personagem_1 and key_pressed_player_1 != True:
                    key_pressed_player_1, hp_value_personagem_player_1 = mv.movimentacao_player_1(event, screen, mapa, per_rect_player_1, font, hp_value_personagem_player_1, key_pressed_player_1,
                                                                                                  npc_rect, player_1, npc, hp_value_npc)
                    
                    turn += 1
                    
                elif turn_nomes[2] == name_personagem_2 and key_pressed_player_2 != True:
                    key_pressed_player_2, hp_value_personagem_player_2 = mv.movimentacao_player_2(event, screen, mapa, per_rect_player_2, font, hp_value_personagem_player_2, key_pressed_player_2,
                                                                                                  npc_rect, player_2, npc, hp_value_npc)
                    
                    turn += 1
                    
                elif turn_nomes[2] == "Elemental" and key_pressed_bot != True:
                    key_pressed_bot, hp_value_personagem_player_1, hp_value_personagem_player_2 = mv.movimentacao_npc(event, screen, mapa, npc_rect, font, hp_value_npc, key_pressed_bot,
                                                                            player_1, player_2, npc, hp_value_personagem_player_1, hp_value_personagem_player_2,
                                                                            per_rect_player_1, per_rect_player_2)
                    
                    turn += 1
        
        """
            Este trecho de código é parte do RPG, sendo uma das mais importantes parte da renderização dos elementos na tela do jogo é feita aqui todas as vezes que o loop passa por aqui. Primeiro, são redesenhados 
            três elementos na tela (personagem 1, personagem 2 e um personagem NPC), utilizando a função "elementos_tela()". Em seguida, são chamadas as funções "barra_HP" e "barra_CA" para desenhar as barras de vida 
            e de CA (proteção) dos personagens. Depois, é verificada a vida dos personagens com a função "testa_vida", que finaliza o jogo caso a vida de algum personagem seja menor que 0. Em seguida, é impresso na tela 
            a ordem de turnos com a função "turn_order". Finalmente, é verificado o sistema de turnos, onde se três ações tiverem sido realizadas, a função "verifica_botoes_precionados" é chamada para resetar o sistema. 
            Por fim, a tela é atualizada e um pequeno delay é adicionado antes de começar o próximo loop de jogo.
        """                       
        # Desenha o personagem 1 na tela
        mt.elementos_tela(screen, per_image_player_1, per_rect_player_1)
        
        # Desenha o personagem 2 na tela
        mt.elementos_tela(screen, per_image_player_2, per_rect_player_2)
        
        # Desenha o personagem NPC na tela
        mt.elementos_tela(screen, npc_image, npc_rect)
        
        # Chama a função barra_HP ao final do loop de jogo
        barra_HP(per_rect_player_1, screen, hp_value_personagem_player_1)
        barra_HP(per_rect_player_2, screen, hp_value_personagem_player_2)
        barra_HP(npc_rect, screen, hp_value_npc)
        
        # Chama a função barra_CA ao final do loop de jogo
        barra_CA(per_rect_player_1, screen, ca_value_personagem_player_1)
        barra_CA(per_rect_player_2, screen, ca_value_personagem_player_2)
        barra_CA(npc_rect, screen, ca_value_npc)

        # Atualiza a tela
        pygame.display.update()
            
        # Testa a vida dos personagens, se caso for < 0, finaliza o jogo
        testa_vida(hp_value_personagem_player_1, hp_value_personagem_player_2, hp_value_npc, screen)
        
        # Printa os turnos
        turn_order(screen, turn_nomes, turn)
        
        # Verifia o sistema de turnos
        if((key_pressed_player_1 == True) and (key_pressed_player_2 == True) and (key_pressed_bot == True)):
            key_pressed_player_1, key_pressed_player_2, key_pressed_bot = verifica_botoes_precionados(key_pressed_player_1, key_pressed_player_2, key_pressed_bot)
        
        if turn > 3:
            turn = 1
        
        # Atualiza a tela
        pygame.display.update()
        
        pygame.time.delay(70)
        pygame.display.flip()

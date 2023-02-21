import pygame
import manipulacao_gameplay as mg

"""
    A função "pygame.init()" é usada para iniciar todos os módulos Pygame. Isso é necessário antes de qualquer outro comando Pygame ser usado.
"""
def inicia_pygame():
    pygame.init()
    
"""
    A função pygame.quit() é usada para encerrar o pygame e liberar os recursos alocados. Isso é importante para evitar vazamentos de memória e garantir que o jogo seja fechado corretamente
"""
def finaliza_pygame():
    pygame.quit()
   
"""
    Esta função define o tamanho da tela do jogo. Ela aceita dois parâmetros, width e height, que representam a largura e altura da tela, respectivamente. A função usa o método set_mode do Pygame 
    para definir o tamanho da tela e retorna o objeto que representa a tela.
""" 
def define_tamanho_tela(width, height):
    return pygame.display.set_mode((width, height))

"""
    A função recebe como parâmetro o nome que será dado à janela e, em seguida, utiliza o método "set_caption" da classe "display" da biblioteca Pygame para definir o nome da janela como o valor 
    passado como parâmetro.
"""
def define_nome_janela(name):
    pygame.display.set_caption(name)
    
    
def define_icone(icon):
    pygame.display.set_icon(icon) 
        
"""
    Essa função "carrega_imagem" está sendo usada para carregar uma imagem específica (especificada pelo parâmetro "imagem") utilizando a biblioteca Pygame. O método pygame.image.load é usado para 
    carregar a imagem e armazená-la na variável "image_carregada". Em seguida, a função retorna a imagem carregada.
"""
def carrega_imagem(imagem):
    image_carregada = pygame.image.load(imagem)
    return image_carregada

def escala_imagem(scale, imagem):
    imagem = pygame.transform.scale(imagem, (imagem.get_width() // scale, imagem.get_height() // scale))
    return imagem


"""
    A função update_tela atualiza a tela do jogo. É usada para redesenhar a tela com qualquer nova informação ou mudança de estado. A função pygame.display.update é uma função da biblioteca Pygame 
    que atualiza a tela inteira ou parte da tela, dependendo dos argumentos passados para ela. Isso é usado para fazer as atualizações visuais na tela de jogo.
"""
def update_tela():
    pygame.display.update()
  
"""
    Essa função atualiza a fila de eventos do Pygame. A função pygame.event.pump() é usada para processar todos os eventos pendentes no buffer de eventos. Isso é importante para garantir que todos os 
    eventos na fila sejam processados, incluindo eventos de teclado, mouse, etc. Além disso, essa função também atualiza o estado interno do Pygame, o que é importante para garantir que o jogo continue 
    a funcionar corretamente.
"""  
def update_fila_eventos():
    pygame.event.pump()
   
"""
    Esse trecho de código define uma função chamada captura_mouse que retorna a posição atual do cursor do mouse. A função usa a biblioteca Pygame e sua função pygame.mouse.get_pos(), que retorna uma tupla 
    com as coordenadas x e y do cursor do mouse na tela. Então a função captura_mouse é uma forma simplificada de obter a posição do cursor do mouse.
"""  
def captura_mouse():
    return pygame.mouse.get_pos()

"""
    Este trecho de código limpa a fila de eventos do pygame. O método clear() remove todos os eventos armazenados na fila de eventos do pygame. Isso é útil para evitar que eventos antigos afetem o comportamento 
    atual da aplicação. A fila de eventos armazena eventos como cliques do mouse, teclas pressionadas, entre outros, que são gerados pelo usuário ou pelo sistema. Quando esses eventos são processados, eles são 
    retirados da fila. Se a fila não for limpa, eventos antigos ainda poderão estar presentes e afetar o comportamento da aplicação de forma indesejada. A função zera_eventos é usada para garantir que a fila de 
    eventos seja limpa antes de começar a processar novos eventos.
"""
def zera_eventos():
    pygame.event.clear()
  
"""
    Este trecho de código define uma função chamada "criacao_texto". A função recebe dois argumentos: "font_text" e "tam". O argumento "font_text" é o nome da fonte que será usada para o texto, enquanto o argumento 
    "tam" é o tamanho do texto.
"""  
def criacao_font(font_text, tam):
    font = pygame.font.Font(font_text, tam)
    return font

def cria_textos(font, p_text, cor):
    # Cria o texto que ira aparecer conforme oque foi passado no "text"
    text = font.render(p_text, True, cor)
    return text

def rederiza_textos(x, y, text):
    text_rect = text.get_rect()  
    text_rect.center = (x, y) 
    return text_rect

def posicoes_elemento(x, y, z, NA):
    map_rect = pygame.Rect(x, y, z, NA)
    return map_rect

def desenha_borda(screen):
    pygame.draw.rect(screen, (255, 255, 255), posicoes_elemento(0, 0, 1600, 900), 10)

"""
    Este trecho de código está definindo uma função "limpa_tela", que recebe como parâmetro "screen". Dentro da função, o comando "screen.fill" é usado para preencher a tela inteira com a cor preta (0, 0, 0). 
    Em outras palavras, a função "limpa_tela" está limpando a tela preenchendo-a com a cor preta.
"""
def limpa_tela(screen):
    screen.fill((0, 0, 0))
    
"""
    Este trecho de código está definindo uma função chamada "exclui_imagem". A função recebe dois argumentos, "screen" e "imagem_rect". O objetivo da função é "preencher" a área especificada por "imagem_rect" 
    com a cor branca (255, 255, 255). Isso essencialmente apaga a imagem que anteriormente estava na tela na área especificada por "imagem_rect".
"""
def exclui_imagem(screen, imagem_rect):
    screen.fill((255, 255, 255), imagem_rect)
 
"""
    A função define "tela_fundo" que recebe dois parâmetros: "screen" e "image". A função usa o método "blit" da biblioteca Pygame para desenhar a imagem "image" na tela "screen" na posição (0, 0), sendo basicamente
    o plano de fundo da screen. O método "blit" desenha uma imagem em uma superfície (neste caso, a tela "screen").
"""   
def tela_fundo(screen, image):
    screen.blit(image, (0, 0))

"""
    Esta função chamada "elementos_tela" tem como objetivo desenhar na tela do jogo (representada pelo parâmetro "screen") uma imagem "image" em uma posição específica representada pelo objeto "image_rect".
"""
def elementos_tela(screen, image, image_rect):
    screen.blit(image, image_rect)
 
"""
    Este trecho de código é uma função de atualização de movimentação. Ela tem como entrada a tela (screen) e o retângulo do personagem (personagem_rect) e o mapa de fundo (mapa_fundo). A função exclui a 
    imagem do personagem na tela, apagando-a na tela atual. Em seguida, a função coloca o mapa de fundo na tela, atualizando a imagem da tela com o mapa de fundo.
"""   
def atualizacao_movimentacao(screen, mapa_fundo, personagem_rect):
    exclui_imagem(screen, personagem_rect)
    tela_fundo(screen, mapa_fundo)
 
"""
    Este trecho de código está definindo uma função chamada "atualiza_texto", que tem dois parâmetros: "screen" e "mapa_fundo". A função é usada para atualizar o texto na tela, colocando o "mapa_fundo" como 
    fundo na tela especificada pelo parâmetro "screen". A função "tela_fundo" é chamada para aplicar o "mapa_fundo" na tela.
"""   
def atualiza_texto(screen, mapa_fundo):
    tela_fundo(screen, mapa_fundo)
    
def delay(num):
    pygame.time.delay(num)
    
def display_flip():
    pygame.display.flip()    
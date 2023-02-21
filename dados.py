import random as rd

"""
    Este trecho de código contém funções para rolar dados virtuais para jogos de RPG. Cada função é responsável por rolar uma quantidade diferente de dados (4, 8, 10, 12, ou 20 lados) com 
    uma proficiência específica. As funções rolam um determinado número de dados (especificado pelo argumento "dados") e retornam o valor total da rolagem. A função "rolagem_20_separados" 
    é diferente, pois ela rola apenas 1 dado de 20 lados e retorna o valor do dado e o valor da proficiência (valor do dado + proficiência). Além disso, verifica se o valor do dado é 20 e, 
    se for, duplica o valor da proficiência, este valor da proficiência na verdade é o dano que o personagem poderá receber.
"""

def rolagem_4(dados, proficiencia):
    valor = 0
    while dados > 0:
        valor += (rd.randint(1, 4) + proficiencia)
        dados = dados - 1
    return valor

def rolagem_8(dados, proficiencia):
    valor = 0
    while dados > 0:
        valor += (rd.randint(1, 8) + proficiencia)
        dados = dados - 1
    return valor

def rolagem_8_separados(dados, proficiencia):
    valor = 0
    while dados > 0:
        valor_d8 = (rd.randint(1, 8))
        valor_d8_proficiencia = valor_d8 + proficiencia
        dados = dados - 1
        
    return valor_d8, valor_d8_proficiencia

def rolagem_10(dados, proficiencia):
    valor = 0
    while dados > 0:
        valor += (rd.randint(1, 10) + proficiencia)
        dados = dados - 1
    return valor

def rolagem_12(dados, proficiencia):
    valor = 0
    while dados > 0:
        valor += (rd.randint(1, 12) + proficiencia)
        dados = dados - 1
    return valor

def rolagem_20(dados, proficiencia):
    valor = 0
    while dados > 0:
        valor += (rd.randint(1, 20) + proficiencia)
        dados = dados - 1
    return valor

def rolagem_20_separados(dados, proficiencia):
    valor = 0
    while dados > 0:
        valor_d20 = (rd.randint(1, 20))
        valor_d20_proficiencia = valor_d20 + proficiencia
        dados = dados - 1
        
    # Verifica se o dado foi 20, se sim, duplica o dano
    if valor_d20 == 20:
        valor_d20_proficiencia *= 2
        
    return valor_d20, valor_d20_proficiencia
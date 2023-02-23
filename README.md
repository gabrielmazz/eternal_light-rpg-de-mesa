# RPG de Mesa com Inteligência Artificial

Este programa tem como objetivo simular um RPG de Mesa, como o Roll20 e o Dnd 5e, utilizando técnicas de inteligência artificial com máquina de estado.

![](https://i.imgur.com/seAEaHC.png)

O programa irá permitir que os jogadores possam **controlar seus personagens e realizar ações em turnos, assim como em um jogo de RPG tradicional**. Além disso, o programa será capaz de rolar dados e calcular as consequências das ações dos personagens, como ataques e defesas, utilizando algoritmos de *inteligência artificial para garantir a fair-play e uma experiência de jogo enriquecedora.*

## Como usar

1.  Faça o download do projeto
2.  Abra o terminal e vá para o diretório do projeto
3.  Execute o comando `python3 main.py` para iniciar o programa
4.  Siga as instruções na tela para jogar

## Funcionalidades

-   Escolha de personagens com atributos e habilidades únicas
-   Ações de combate, como ataque, com cálculo de danos e efeitos
-   Rolagem de dados com diferentes tipos e quantidades de dados, baseados dos dados de RPG, sendo ``D20, D12, D10, D8, D6, D4``
-   Sistema de turnos para  garantir a ordem de turnos dos jogadores
-   Inteligência artificial para garantir fair-play e uma experiência de jogo imersiva utilizando **maquina de estados e a subida na encosta simples (ou hill climbing)**

<img src="https://i.pinimg.com/originals/df/54/d4/df54d411305571ca5d82371db65a97ea.gif">

## Entrada de dados

No loop principal do jogo, a variável ``"screen_mode"`` controla qual tela está sendo mostrada (tela de ``escolha do personagem do jogador 1``, tela de ``escolha do personagem do jogador 2`` ou próxima fase). O loop também trata eventos e atualiza a tela usando as funções "desenha_elementos" e "update_tela". Para escolher o personagem, é verificado se uma tecla foi pressionada e a escolha é armazenada em variáveis. A tecla 0 finaliza o jogo., No final ele levará para a tela de ``escolha de mapas`` nos mesmo moldes da escolha de personagem.

<img src="https://blogger.googleusercontent.com/img/a/AVvXsEjCXyJAXYLDgI8EXnORZTgugnc0UCRM3uf3-RZVx5NIkJtury4ZHn0_xhon4vT4oI-rbqtZmQ-zo2KRelxDH26jRwa23Unv5WOaBSmRcMkCjudsfv_cVtJM2FtcpNplbthggCTRKlbQZ_NLZYVzWmhIC8SIOjd4PoGqCm8CCDnNAzx9KlpDMUg" >

## Gameplay

O *objetivo do jogo é simular um RPG de mesa*, onde os jogadores podem controlar seus personagens e realizar ações em turnos. A ordem dos turnos é determinada pela função ``"determina_turno"``, que retorna uma lista com os nomes dos jogadores em ordem aleatória.

A partir da lista de ordem de turnos, cada jogador é chamado uma vez e seu movimento é executado, utilizando as funções ``"movimentacao_player_1"``, ``"movimentacao_player_2"`` e ``"movimentacao_npc"`` para mover os personagens. Antes de cada jogada, é verificado se a jogada já foi realizada, utilizando variáveis booleanas.

A renderização dos elementos na tela é feita na função ``"renderiza_tela"``, que redesenha os elementos na tela a cada loop do jogo, como os personagens, barras de vida e proteção, e a ordem de turnos. A função ``"testa_vida"`` verifica a vida dos personagens, finalizando o jogo caso a vida de algum personagem seja menor que 0. O sistema de turnos é verificado na função ``"verifica_botoes_precionados"``, que reseta o sistema após três ações terem sido realizadas.

Em resumo, o gameplay consiste em movimentar os personagens e realizar ações em turnos, seguindo a ordem determinada aleatoriamente. O objetivo é derrotar os oponentes e vencer a partida de RPG.

<img src="https://media.tenor.com/YYZIGDYagm0AAAAM/gumball-dn-d.gif" width="50%">

## Classes dos Personagens:

O código apresenta *duas classes para modelar personagens em um jogo ou RPG: "Personagem" e "Npc"*.

A classe ``"Personagem"`` tem sete atributos: ``"escolha", "nome", "pv", "força", "destreza", "constituição" e "ca"``. Ela é baseada em três tipos diferentes de personagens: ``"Warrior", "Shielder" e "Berserker"``. O método "init" é usado para inicializar os atributos quando uma nova instância da classe é criada. Dependendo do valor de ``"escolha"``, o nome, as habilidades e a quantidade de pontos de vida serão atribuídos ao personagem de forma diferente.

A **classe "Npc" é usada para modelar personagens não-jogáveis no jogo**. Ela tem os mesmos atributos que a classe "Personagem", mas não tem opções de escolha, pois é um personagem controlado pelo computador. Os valores dos atributos são pré-definidos.

As funções "rolagem_10(4, 0)", "rolagem_12(4, 0)" e "rolagem_8(4, 0)" são importadas de um arquivo chamado "dados" e realizam uma rolagem de dados para determinar a quantidade de pontos de vida do personagem. A CA (Classe de Armadura) é calculada como 12 mais a destreza.

<img src="https://i.pinimg.com/originals/37/8a/cb/378acb0dfedf589333608b2c75ca1701.gif">

## Movimentação dos Players

Estas *funções determinam a movimentação de cada player durante os seus respectivos turnos* no jogo. É possível *movimentar os players utilizando as setinhas do teclado* para ``cima, baixo, esquerda e direita.`` No entanto, **não é possível realizar movimentos na diagonal.**

Ao apertar o ``botão "z"``, o player realiza um ataque no oponente, desde que estejam engajados. Isso significa que ambos os personagens estão próximos um do outro e é possível realizar o ataque. Além disso, o ``botão "9"`` é utilizado para passar o turno para o próximo jogador da lista, enquanto o ``botão "0"`` é utilizado para finalizar o jogo e sair do programa.

<img src="https://i.pinimg.com/originals/2e/05/ba/2e05bad274268ae2c9ed1126bbcb78ac.gif">

## Movimentação do NPC

A função `movimentacao_npc()` é *responsável por controlar o comportamento do NPC (personagem não-jogador) durante o jogo.* Ela **Recebe informações sobre a posição dos jogadores e do NPC, assim como seus pontos de vida, para decidir o que o NPC deve fazer.**

Se o NPC já estiver morto, a função retorna um valor que indica que o turno do NPC já passou. Caso contrário, a função verifica se o botão `8` foi pressionado, indicando que o turno do jogador já passou. Se for esse o caso, a função retorna um valor que indica que o turno do jogador ainda não acabou.

Se o botão `9` for pressionado, a função entra na máquina de estados que controla o comportamento do NPC. O primeiro passo é verificar a distância entre o NPC e os jogadores. Se ambos os jogadores estiverem longe, a função verifica se o NPC precisa se curar. Se o NPC estiver com menos de 30% de seus pontos de vida e ainda tiver itens de cura, a função escolhe o estado de cura e chama a função `realiza_cura_npc()` para atualizar a quantidade de pontos de vida do NPC.

Se apenas um dos jogadores estiver perto, a função escolhe entre os estados de perseguir ou fugir. Se o jogador estiver a uma distância entre `distancia_engajamento` e `distancia_engajamento * 2` do NPC, e o NPC tiver mais de 30% de seus pontos de vida, a função escolhe o estado de perseguir e chama a função `movimento_perseguindo()` para atualizar a posição do NPC. Se o NPC tiver menos de 30% de seus pontos de vida e não tiver mais itens de cura, a função escolhe o estado de fugir e chama a função `movimento_fugir()` para atualizar a posição do NPC.

Se ambos os jogadores estiverem perto, a função escolhe entre perseguir ou atacar um dos jogadores. Se o jogador estiver a uma distância menor ou igual a `distancia_engajamento` do NPC, a função chama a função `ataque_npc()` para causar dano no jogador. Caso contrário, a função escolhe o estado de perseguir e chama a função `movimento_perseguindo()` para atualizar a posição do NPC.

A função retorna valores que indicam se o turno do jogador já passou, o novo valor dos pontos de vida do NPC e dos jogadores, a nova posição do NPC e a quantidade de itens de cura que ele ainda tem.

<img src="https://i.pinimg.com/originals/db/0f/b3/db0fb38d2ba4aa0a4d6a08959afced9a.gif">

## Funções da Tela

As funções da tela são responsáveis por controlar aspectos visuais do jogo, como tamanho da tela, nome da janela, ícone, carregamento de imagens, redimensionamento de imagens, atualização da tela, limpeza da fila de eventos, entre outros.

<img src="https://i.pinimg.com/originals/0c/96/a2/0c96a2b838576941a9342a704bf574f5.gif" width="50%">

## Dados:

Este trecho de código contém funções para rolar dados virtuais para jogos de RPG. Cada função é responsável por rolar uma quantidade diferente de dados (4, 8, 10, 12, ou 20 lados) com uma proficiência específica. As funções rolam um determinado número de dados (especificado pelo argumento "dados") e retornam o valor total da rolagem. A função "rolagem_20_separados" é diferente, pois ela rola apenas 1 dado de 20 lados e retorna o valor do dado e o valor da proficiência (valor do dado + proficiência). Além disso, verifica se o valor do dado é 20 e, se for, aumenta o valor da proficiência em 10, este valor da proficiência na verdade é o dano que o personagem poderá receber.

<img src="https://64.media.tumblr.com/2ae2d17fab0ac24129ef1e96f0b61159/tumblr_obisnmUjrQ1s2wio8o1_500.gif">

## Tecnologias utilizadas

-   Python 3
-   Máquina de estado
-   Algoritmos de inteligência artificial

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para reportar bugs ou propor melhorias no programa. Se quiser contribuir com código, faça um fork do projeto, faça as modificações e abra um pull request.

![](https://media.tenor.com/gOCEHYul7PAAAAAi/dnd-dungeons-and-dragons.gif)

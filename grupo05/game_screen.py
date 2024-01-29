import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, BLUE, RED
from assets import *
dicionario_de_arquivos = carrega_arquivos
from random import *

def colisao_entre_retangulos(x1, y1, largura1, altura1, x2, y2, largura2, altura2):
    if (x1 < x2 + largura2 and x1 + largura1 > x2 and y1 < y2 + altura2 and y1 + altura1 > y2):
        return True
    else:
        return False
    
def quantidade_imagens(X):
    imagem_sorteada = ['cherries', 'flower', 'fruit-tree', 'ladybug', 'tree']
    retorno = []
    
    img_sorteadas = random.sample(imagem_sorteada, X)

    for imagem in imagem_sorteada:
        qnt_sorteada = random.randint(5,10+1)

        for i in range(qnt_sorteada):
            retorno.append({"image": dicionario_de_arquivos[imagem_sorteada],
                        "x": random.randint(60,840),
                        "y": random.randint(60,640),
                        "tipo": imagem_sorteada})
    
    return retorno

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    tela = 'azul'
    tempo_da_ultima_mudanca = pygame.time.get_ticks()

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        # Lógica para alternar as cores
        agora = pygame.time.get_ticks()
        if agora - tempo_da_ultima_mudanca > 2000:
            tempo_da_ultima_mudanca = agora
            if tela == 'azul':
                tela = 'vermelha'
            else:
                tela = 'azul'

        if tela == 'azul':
            window.fill(BLUE)
        else:
            window.fill(RED)
        window.blit(dicionario_de_arquivos[CHERRIES], (0,0))

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state

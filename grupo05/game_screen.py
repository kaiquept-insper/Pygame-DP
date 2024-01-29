import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, BLUE, RED
from assets import *
import random

def colisao_entre_retangulos(x1, y1, largura1, altura1, x2, y2, largura2, altura2):
    if (x1 < x2 + largura2 and x1 + largura1 > x2 and y1 < y2 + altura2 and y1 + altura1 > y2):
        return True
    else:
        return False

def verifica_colisao(quadrado, list_quadrados):
    for quadrado2 in list_quadrados:
        if colisao_entre_retangulos(quadrado["x"], quadrado["y"], 60, 60, quadrado2["x"], quadrado2["y"], 60, 60):
            return True
    return False
        

def quantidade_imagens(X,dicionario_de_arquivos):
    imagem_sorteada = ['cherries', 'flower', 'fruit-tree', 'ladybug', 'tree']
    retorno = []
    
    img_sorteadas = random.sample(imagem_sorteada, X)

    for imagem in img_sorteadas:
        qnt_sorteada = random.randint(5,10+1)

        for i in range(qnt_sorteada):
            verificando_quadrado = {"image": dicionario_de_arquivos[imagem],
                        "x": random.randint(60,840),
                        "y": random.randint(60,640),
                        "tipo": imagem_sorteada}
            
            while verifica_colisao(verificando_quadrado,retorno):
                verificando_quadrado = {"image": dicionario_de_arquivos[imagem],
                        "x": random.randint(60,840),
                        "y": random.randint(60,640),
                        "tipo": imagem_sorteada}
            
            retorno.append(verificando_quadrado)

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
    lista_imagens = quantidade_imagens(1,dicionario_de_arquivos)
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor preto
        # Lógica para alternar as cores
        agora = pygame.time.get_ticks()
        if agora - tempo_da_ultima_mudanca > 4000:
            tempo_da_ultima_mudanca = agora
            if tela == 'azul':
                tela = 'vermelha'
            else:
                tela = 'azul'

        if tela == 'azul':

            window.fill(BLUE)
        else:
            window.fill(RED)

        for objeto in lista_imagens:
            window.blit(objeto["image"], (objeto["x"],objeto["y"]))

        pygame.display.update()  # Mostra o novo frame para o jogador

    return state

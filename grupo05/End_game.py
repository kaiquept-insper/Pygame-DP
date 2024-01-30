import pygame
from config import FPS, QUIT, WIDTH, HEIGHT, BLACK, BLUE, RED, WHITE, YELLOW
from assets import *
import random
from game_screen import *

def end_game(window, pontos):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    base_font = pygame.font.Font(None, 75)

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(BLACK)
        final = base_font.render("Pontuação:", True, YELLOW)
        window.blit(final, (WIDTH/2-200, HEIGHT/2 - 200))
        pontuacao = base_font.render(str(pontos), True, YELLOW)
        window.blit(pontuacao, (WIDTH/2-170, HEIGHT/2-100))


        pygame.display.update()  # Mostra o novo frame para o jogador

    return state

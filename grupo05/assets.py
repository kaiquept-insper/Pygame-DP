import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR

CHERRIES = 'cherries'
FLOWER = 'flower'
FRUIT = 'fruit-tree'
LADYBUG='ladybug'
TREE = 'tree'
HEART = 'heart'
VIDAS = 3



def carrega_arquivos():
    dicionario_de_arquivos = {}
    dicionario_de_arquivos['btn'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1.png')).convert()
    largura_img = 60
    altura_img =  60
    
    dicionario_de_arquivos[CHERRIES] = pygame.image.load(os.path.join(IMG_DIR, 'cherries.png')).convert_alpha()
    dicionario_de_arquivos[CHERRIES] = pygame.transform.scale(dicionario_de_arquivos[CHERRIES], (largura_img, altura_img))
        
    dicionario_de_arquivos[FLOWER] = pygame.image.load(os.path.join(IMG_DIR, 'flower.png')).convert_alpha()
    dicionario_de_arquivos[FLOWER] = pygame.transform.scale(dicionario_de_arquivos[FLOWER], (largura_img, altura_img))

    dicionario_de_arquivos[FRUIT] = pygame.image.load(os.path.join(IMG_DIR, 'fruit-tree.png')).convert_alpha()
    dicionario_de_arquivos[FRUIT] = pygame.transform.scale(dicionario_de_arquivos[FRUIT], (largura_img, altura_img))
    
    dicionario_de_arquivos[LADYBUG] = pygame.image.load(os.path.join(IMG_DIR, 'ladybug.png')).convert_alpha()
    dicionario_de_arquivos[LADYBUG] = pygame.transform.scale(dicionario_de_arquivos[LADYBUG], (largura_img, altura_img))
 
    dicionario_de_arquivos[TREE] = pygame.image.load(os.path.join(IMG_DIR, 'cherries.png')).convert_alpha()
    dicionario_de_arquivos[TREE] = pygame.transform.scale(dicionario_de_arquivos[TREE], (largura_img, altura_img))
     
    dicionario_de_arquivos[HEART] = pygame.image.load(os.path.join(IMG_DIR, 'heart.png')).convert_alpha()
    dicionario_de_arquivos[HEART] = pygame.transform.scale(dicionario_de_arquivos[HEART], (40, 40))

    #Musicas

    dicionario_de_arquivos['success_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'success.wav'))
    dicionario_de_arquivos['failure_sound'] = pygame.mixer.Sound(os.path.join(SND_DIR, 'wah-wah.wav'))

    #mudando tamanho das imagens
    largura = dicionario_de_arquivos['btn'].get_rect().width * .25
    altura = dicionario_de_arquivos['btn'].get_rect().height * .25
    dicionario_de_arquivos['btn'] = pygame.transform.scale(dicionario_de_arquivos['btn'], (largura, altura))

    dicionario_de_arquivos['btn_hover'] = pygame.image.load(os.path.join(IMG_DIR, 'btn1_hover.png')).convert()
    dicionario_de_arquivos['btn_hover'] = pygame.transform.scale(dicionario_de_arquivos['btn_hover'], (largura, altura))


    #carregando Fonte
    dicionario_de_arquivos['font'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 22)
    dicionario_de_arquivos['font_media'] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 30)
    return dicionario_de_arquivos

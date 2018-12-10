# noinspection PyUnresolvedReferences
import pygame
#entrada
pygame.init()

#processamento
pygame.mixer.music.load('arquivo.mp3')

#saída
pygame.mixer.music.play()
pygame.event.wait()

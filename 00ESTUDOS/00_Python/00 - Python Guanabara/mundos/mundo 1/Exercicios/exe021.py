##EXERCICIO 21  # Faça um programa em python que abra e reproduza o audio de um arquivo mp3 

import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
input()
pygame.event.wait()


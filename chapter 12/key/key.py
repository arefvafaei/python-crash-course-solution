import pygame
import sys
pygame.display.set_mode((1200,800))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print("hello")


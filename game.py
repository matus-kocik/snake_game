import pygame
import sys
from config import config

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode(config.GAME_RES)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys,exit()
        pygame.display.update()

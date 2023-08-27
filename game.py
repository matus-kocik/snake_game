import pygame
import sys
from config import config

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(config.GAME_RES)
    snake = [config.GAME_RES[0] // 2, config.GAME_RES[1] // 2]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys,exit()
                
        pygame.draw.rect(window, config.BODY_COLOR, pygame.Rect(snake[0], snake[1], config.SNAKE_SIZE, config.SNAKE_SIZE))
        
        pygame.display.update()
        clock.tick(config.GAME_FPS)

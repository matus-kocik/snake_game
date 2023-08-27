import pygame
import sys
from config import config

def update_position(snake, direction, step):
    if direction == "UP":
        snake = [snake[0], snake[1] - step]
    if direction == "DOWN":
        snake = [snake[0], snake[1] + step]
    if direction == "LEFT":
        snake = [snake[0] - step, snake[1]]
    if direction == "RIGHT":
        snake = [snake[0] + step, snake[1]]
    return snake

if __name__ == "__main__":
    
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(config.GAME_RES)
    snake = [config.GAME_RES[0] // 2, config.GAME_RES[1] // 2]
    direction = "UP"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys,exit()
        
        snake = update_position(snake, direction, config.SNAKE_SIZE)        
        pygame.draw.rect(window, config.BODY_COLOR, pygame.Rect(snake[0], snake[1], config.SNAKE_SIZE, config.SNAKE_SIZE))
        
        pygame.display.update()
        window.fill(config.BACKGROUND_COLOR)
        clock.tick(config.GAME_FPS)

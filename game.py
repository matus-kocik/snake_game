import pygame
import random
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

def update_direction(direction, keys):
    if keys[pygame.K_LEFT]:
        return "LEFT" if direction != "RIGHT" else direction
    if keys[pygame.K_RIGHT]:
        return "RIGHT" if direction != "LEFT" else direction
    if keys[pygame.K_UP]:
        return "UP" if direction != "DOWN" else direction
    if keys[pygame.K_DOWN]:
        return "DOWN" if direction != "UP" else direction
    return direction

def is_out(snake, game_res):
    if snake[0] < 0 or snake[1] < 0 or snake[0] > game_res[0] or snake[1] > game_res [1]:
        return True
    return False

def end_game(window):
    print("GAME OVER!!!")
    window.fill(config.BACKGROUND_COLOR)
    pygame.quit()
    sys.exit()
    
def generate_apple(game_res, snake_size):
    x = random.choice(range(0, game_res[0] - snake_size + 1, snake_size))
    y = random.choice(range(0, game_res[1] - snake_size + 1, snake_size))
    
def is_collision(snake_head, apple):
    if snake_head[0] == apple[0] and snake_head[1] == apple [1]:
        return True
    return False
    
if __name__ == "__main__":
    
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode(config.GAME_RES)
    snake = [config.GAME_RES[0] // 2, config.GAME_RES[1] // 2]
    direction = "UP"
    apple = generate_apple(config.GAME_RES, config.SNAKE_SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys,exit()
        
        keys = pygame.key.get_pressed()
        direction = update_direction(direction, keys)
        
        snake = update_position(snake, direction, config.SNAKE_SIZE)   
        
        if is_collision(snake, apple):
            print("Collision") 
            apple = generate_apple(config.GAME_RES, config.SNAKE_SIZE)

        if is_out(snake, config.GAME_RES):
            end_game(window)
            
        pygame.draw.rect(window, config.BODY_COLOR, pygame.Rect(snake[0], snake[1], config.SNAKE_SIZE, config.SNAKE_SIZE))
        pygame.draw.rect(window, config.APPLE_COLOR, pygame.Rect(apple[0], apple[1], config.APPLE_COLOR, config.APPLE_COLOR))
        
        pygame.display.update()
        
        window.fill(config.BACKGROUND_COLOR)
        clock.tick(config.GAME_FPS)

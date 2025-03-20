import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 600
screen_height = 400

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
yellow = (255, 255, 0)
gray = (169, 169, 169)

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game with Power-Ups and Obstacles")

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)

def message(msg, color, position):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, position)

def gameLoop():
    game_over = False
    game_close = False

    x1 = screen_width / 2
    y1 = screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

    powerupx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    powerupy = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
    powerup_active = True

    obstacles = [(random.randint(0, screen_width//10)*10, random.randint(0, screen_height//10)*10) for _ in range(5)]

    while not game_over:

        while game_close:
            screen.fill(blue)
            message("Game Over! Press Q to Quit or C to Play Again", red, (screen_width / 6, screen_height / 3))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)

        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])

        if powerup_active:
            pygame.draw.rect(screen, yellow, [powerupx, powerupy, snake_block, snake_block])

        for obs in obstacles:
            pygame.draw.rect(screen, gray, [obs[0], obs[1], snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        for segment in snake_List:
            pygame.draw.rect(screen, white, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        if powerup_active and x1 == powerupx and y1 == powerupy:
            global snake_speed
            powerup_active = False
            snake_speed += 5
            time.sleep(2)
            snake_speed -= 5
            powerupx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            powerupy = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            powerup_active = True

        if (x1, y1) in obstacles:
            game_close = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
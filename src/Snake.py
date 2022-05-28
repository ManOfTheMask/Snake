#add pygame boilerplate code
import pygame
import time
import random

pygame.init()

#Global Variables
IsOpen = True
window_width = 800
window_height = 600
direction = 'RIGHT'
change_to = direction

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


#create a window
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake Game by Dr.Mask')

class Snake:
    def __init__(self):
        self.snake_head = [100, 50]
        self.snake_body = [[100, 50]]

    def snakeMovement(self):
        global IsOpen, change_to, direction
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                IsOpen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'

    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
 
    # Moving the snake
        if direction == 'UP':
            self.snake_head[1] -= 10
        if direction == 'DOWN':
            self.snake_head[1] += 10
        if direction == 'LEFT':
            self.snake_head[0] -= 10
        if direction == 'RIGHT':
            self.snake_head[0] += 10

        self.snake_body[0][0] = self.snake_head[0]
        self.snake_body[0][1] = self.snake_head[1]

    def renderSnake(self):
        global screen, green
        for pos in self.snake_body:
            pygame.draw.rect(screen, green, [pos[0], pos[1], 10, 10])
    
class Fruit:
    def __init__(self):
        global window_width, window_height
        self.foodx = random.randrange(1, (window_width//10)) * 10
        self.foody = random.randrange(1, (window_height//10)) * 10
    
    def fruit_render(self):
        global screen, red
        pygame.draw.rect(screen, red, [self.foodx, self.foody, 10, 10])

snake = Snake()
fruit = Fruit()
#render function
def Render():
    screen.fill((0,0,0))
    snake.renderSnake()
    fruit.fruit_render()
    pygame.display.update()
    clock.tick(20)

#game loop
while IsOpen:
    snake.snakeMovement()
    Render()

pygame.quit()
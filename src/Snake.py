#add pygame boilerplate code
import pygame
import time
import random

pygame.init()

#Global Variables
IsOpen = True
window_width = 800
window_height = 600

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
        self.snakeposition = [100, 50]
        self.snakebody = [[100, 50]]

    def snakeMovement(self):
        global IsOpen
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                IsOpen = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.snakeposition[0] -= 10
                if event.key == pygame.K_RIGHT:
                    self.snakeposition[0] += 10
                if event.key == pygame.K_UP:
                    self.snakeposition[1] -= 10
                if event.key == pygame.K_DOWN:
                    self.snakeposition[1] += 10
        self.snakebody[0][0] = self.snakeposition[0]
        self.snakebody[0][1] = self.snakeposition[1]

    def renderSnake(self):
        global screen, green
        for pos in self.snakebody:
            pygame.draw.rect(screen, green, [pos[0], pos[1], 10, 10])
        

snake = Snake()



#render function
def Render():
    screen.fill((0,0,0))
    snake.renderSnake()
    pygame.display.update()
    clock.tick(60)

#game loop
while IsOpen:
    snake.snakeMovement()
    Render()

pygame.quit()
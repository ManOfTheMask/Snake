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
fruit_spawn = True
score = 0
block_size = 10

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

#snake class
class Snake:
    def __init__(self):
        self.snake_head = [100, 50]
        self.snake_body = [[100, 50], [90, 50]]

    #controls the snake
    def snakeMovement(self):
        global IsOpen, change_to, direction
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                IsOpen = False

            #arrow key controls
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
    # will prevent the snake from moving in the 
    # opposite direction it is facing

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
            self.snake_head[1] -= block_size
        if direction == 'DOWN':
            self.snake_head[1] += block_size
        if direction == 'LEFT':
            self.snake_head[0] -= block_size
        if direction == 'RIGHT':
            self.snake_head[0] += block_size

        for x in self.snake_body[1:]:
            if x == self.snake_head:
                IsOpen = False
    
    #wall and body collision detection
    def collision(self):
        global IsOpen
        for x in self.snake_body[1:]:
            if x == self.snake_head:
                game_over()
        if self.snake_head[0] > window_width or self.snake_head[0] < 0:
            game_over()
        if self.snake_head[1] > window_height or self.snake_head[1] < 0:
            game_over()

    #renders the snake
    def renderSnake(self):
        global screen, green
        for pos in self.snake_body:
            pygame.draw.rect(screen, green, [pos[0], pos[1], block_size, block_size])

#fruit class
class Fruit:
    def __init__(self):
        global window_width, window_height
        self.foodx = random.randrange(1, (window_width//block_size)) * block_size
        self.foody = random.randrange(1, (window_height//block_size)) * block_size

    #renders fruit
    def fruit_render(self):
        global screen, red
        pygame.draw.rect(screen, red, [self.foodx, self.foody, block_size, block_size])
    
#init objects
snake = Snake()
fruit = Fruit()

#game over function
def game_over():
    global IsOpen
    font = pygame.font.SysFont('monaco', 72)
    text = font.render('Game Over', True, white)
    text_rect = text.get_rect()
    text_rect.center = (window_width/2, window_height/2)
    screen.blit(text, text_rect)
    pygame.display.update()
    time.sleep(2)
    IsOpen = False

#show the score
def show_score(score):
    global screen, white
    scorestr = str(score)
    font = pygame.font.SysFont('times new roman', 24)
    scoretext = font.render(f"Your score is: {scorestr}", True, white)
    scoretext_rect = scoretext.get_rect()
    scoretext_rect.center = (90, 20)
    screen.blit(scoretext, scoretext_rect)

#render function
def Render():
    screen.fill((0,0,0))
    snake.renderSnake()
    fruit.fruit_render()
    clock.tick(16)

#snake and fruit collision detection function
def fruit_eaten():
    global fruit_spawn, score
    snake.snake_body.insert(0, list(snake.snake_head))

    if snake.snake_head[0] == fruit.foodx and snake.snake_head[1] == fruit.foody:
        score += 10
        show_score(score)
        fruit.foodx = random.randrange(1, (window_width//block_size)) * block_size
        fruit.foody = random.randrange(1, (window_height//block_size)) * block_size
    else:
        snake.snake_body.pop()

#game loop
while IsOpen:
    snake.snakeMovement()
    fruit_eaten()
    snake.collision()
    Render()
    show_score(score)
    pygame.display.update()
pygame.quit()
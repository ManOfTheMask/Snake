#add pygame boilerplate code
import pygame

pygame.init()

#Global Variables
IsOpen = True

#game window size
window_width = 800
window_height = 600


#create a window
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()


def Events():
    global IsOpen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsOpen = False


def Render():
    screen.fill((0,0,0))
    pygame.display.update()
    clock.tick(60)


while IsOpen:
    Events()
    Render()
pygame.quit()
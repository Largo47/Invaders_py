import pygame
import random

#global vars
w = 1366
h = 768
playerXY = [int(w * 0.45), int(h * 0.7)]
V = [0,0,1]

enemyXY = [int(w * 0.45), int(h * 0.2)]
eV = [0,0,2]

#Global methods
def Player(x,y):
    screen.blit(pIMG,(x,y))
def Enemy(x,y):
    screen.blit(eIMG,(x,y))

#initialize pygame
pygame.init()
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

# Loading assets
icon = pygame.image.load('CASCA.png')
pIMG = pygame.image.load('tr1ck6.png')
eIMG = pygame.image.load('ufo.png')

# Setup
pygame.display.set_caption("Space Invader")
pygame.display.set_icon(icon)

#Game loop
gameOn = True
while gameOn:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                V[0] = -V[2]
            elif event.key == pygame.K_RIGHT:
                V[0] = V[2]
            elif event.key == pygame.K_UP:
                V[1] = -V[2]
            elif event.key == pygame.K_DOWN:
                V[1] = V[2]
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                V[0] = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                V[1] = 0

    #Limit player to screen
    if playerXY[0] < 1:
        playerXY[0] = 1
    if playerXY[0] > w - 73:
        playerXY[0] = w - 73
    if playerXY[1] < 1:
        playerXY[1] = 1
    if playerXY[1] > h-144:
        playerXY[1] = h-144


    screen.fill((12,15,17))  #RGB
    playerXY = [playerXY[0]+V[0]*dt,playerXY[1]+V[1]*dt]
    Player(playerXY[0],playerXY[1])
    Enemy(enemyXY[0], enemyXY[1])

    pygame.display.update()

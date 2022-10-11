#PYGAME INITIALIZATION
import pygame, sys, os

from pygame import *
pygame.init()
mixer.init()

fps = 255
fpsClock = pygame.time.Clock()

#COLOURS
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)

#BALL VARIABLES
ballx = 640
bally = 475
radius = 15

dx = 1
dy = 2

#PADDLE VARIABLES
paddle_length = 20
paddle_width = 120

player1 = 415
player2 = 415

player1x = 40
player2x = 1220

#SCORE & BACKGROUND VARIABLES
LENGTH = 20
WIDTH = 950

score1 = 0
score2 = 0

font = pygame.font.SysFont("Arial Rounded MT Bold", 100, True, False)

#SETTING WINDOW PROPERTIES
SCREENWIDTH, SCREENHEIGHT = 1280, 950

os.environ['SDL_VIDEO_CENTERED'] = '1'
window = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Pong Game")


while True:#Main Program Loop
    for event in pygame.event.get():#Loop Through Each Event
        if event.type == QUIT:#Exit Program When the user Closes the Window
            pygame.quit()
            sys.exit()

    #BACKGROUND
    window.fill(black)

    pygame.draw.rect(window, blue, (0, 0, LENGTH, WIDTH), 0)#Player 1 Goal
    pygame.draw.rect(window, red, (1260, 0, LENGTH, WIDTH), 0)#Player 2 Goal

    pygame.draw.rect(window, white, (630, 0, LENGTH, WIDTH), 0)#Middle Line

    ##SCORE
    #PLAYER 1
    score_player1 = font.render(str(score1), True, (white))
    window.blit(score_player1, (100, 10))

    #PLAYER 2
    score_player2 = font.render(str(score2), True, (white))
    window.blit(score_player2, (1130, 10))
    
    ##PADDLE
    #PLAYER 1
    pygame.draw.rect(window, white, (40, player1, paddle_length, paddle_width), 0)
        
    #PLAYER 2
    pygame.draw.rect(window, white, (1220, player2, paddle_length, paddle_width), 0)


    ##PADDLE PHYSICS
    #PLAYER 1
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        player1 -= 1.2

    if keys[pygame.K_s]:
        player1 += 1.2

    if player1 < 0:
        player1 = 0
    elif player1 + paddle_width > SCREENHEIGHT:
        player1 = SCREENHEIGHT - paddle_width

    #PLAYER 2
    if keys[pygame.K_UP]:
        player2 -= 1.2

    if keys[pygame.K_DOWN]:
        player2 += 1.2

    if player2 < 0:
        player2 = 0
    elif player2 + paddle_width > SCREENHEIGHT:
        player2 = SCREENHEIGHT - paddle_width
    

    #BALL
    pygame.draw.circle(window, green,(ballx, bally), radius, 0)

    ballx += dx
    bally += dy

    #BALL CONSTRAINTS
    if ballx < 0 or ballx + radius > SCREENWIDTH:
        dx *= -1
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Hit Wall.wav'))

    if bally < 0 or bally + radius > SCREENHEIGHT:
        dy *= -1
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('Hit Wall.wav'))
        

    ##BALL TO PADDLE CONSTRAINTS
    #PLAYER 1
    if ballx == player1x + 20:
        if bally >= player1 and bally <= player1 + paddle_width:
            dx *= -1
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Ball Hit Paddle.wav'))

    #PLAYER 2
    if ballx == player2x:
        if bally >= player2 and bally <= player2 + paddle_width:
            dx *= -1
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('Ball Hit Paddle.wav'))

    ##SCORE
    #PLAYER 1
    if ballx >= 1260:
        score1 += 1

        pygame.mixer.Channel(2).play(pygame.mixer.Sound('Point.wav'))

        #Resetting Positions
        player1 = 415
        player2 = 415

        ballx = 640
        bally = 475
        
            
    #PLAYER 2
    if ballx <= 20:
        score2 += 1

        pygame.mixer.Channel(2).play(pygame.mixer.Sound('Point.wav'))

        #Resetting Positions
        player1 = 415
        player2 = 415

        ballx = 640
        bally = 475
        
    
    fpsClock.tick(fps)
    pygame.display.update()#Redraw the Screen











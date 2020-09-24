import pygame
import random
import time
pygame.init() # init

screen = pygame.display.set_mode((800,600)) # setting screen
#title + logo

pygame.display.set_caption("HorseRacePY")
programIcon = pygame.image.load('photos/horse.png')

pygame.display.set_icon(programIcon)
#logo = pygame.image.load("horse.png")

#player
player1Img = pygame.image.load("photos/Black.png")
player1X = 0
Player1Y = 0

def player1() :
    screen.blit(player1Img,(player1X,Player1Y))

player2Img = pygame.image.load("photos/Blue.png")
player2X = 0
Player2Y = 100

def player2() :
    screen.blit(player2Img,(player2X,Player2Y))

player3Img = pygame.image.load("photos/Green.png")
player3X = 0
Player3Y = 200

def player3() :
    screen.blit(player3Img,(player3X,Player3Y))


player4Img = pygame.image.load("photos/Purp.png")
player4X = 0
Player4Y = 300

def player4() :
    screen.blit(player4Img,(player4X,Player4Y))

player5Img = pygame.image.load("photos/Yellow.png")
player5X = 0
Player5Y = 400
def player5() :
    screen.blit(player5Img,(player5X,Player5Y))

player6Img = pygame.image.load("photos/horse.png")
player6X = 0
Player6Y = 500
def player6() :
    screen.blit(player6Img,(player6X,Player6Y))






player1speed = 0
half1 = False
player2speed = 0
half2 = False
player3speed = 0
half3 = False
player4speed = 0
half4 = False
player5speed = 0
half5 = False
player6speed = 0
half6 = False

won = False
winner = "None"

font = pygame.font.Font("freesansbold.ttf",32)
textX = 525
textY = 550
def show_winner(x,y) :
    score = font.render(f"Winner is {winner}",True,(0,0,0))
    screen.blit(score,(x,y))


#game loop
running = True
while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
    screen.fill((229, 206, 232))
    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_SPACE :
            player1speed = random.uniform(0.2,0.45)
            player2speed = random.uniform(0.2,0.45)
            player3speed = random.uniform(0.2,0.45)
            player4speed = random.uniform(0.2,0.45)
            player5speed = random.uniform(0.2,0.45)
            player6speed = random.uniform(0.2,0.45)
        if event.key == pygame.K_LSHIFT :
            player1X = 0
            player2X = 0
            player3X = 0
            player4X = 0
            player5X = 0
            player6X = 0
            player1speed = 0
            player2speed = 0
            player3speed = 0
            player4speed = 0
            player5speed = 0
            player6speed = 0
            half1 = False
            half2 = False
            half3 = False
            half4 = False
            half5 = False
            half6 = False
            won = False
            winner = "None"

    player1()
    player2()
    player3()
    player4()
    player5()
    player6()
    show_winner(textX,textY)

    if player1X > 720 :
        player1speed = 0
    elif player1X > 360 and half1 == False :
        half1 = True
        player1speed = random.random()
    elif player1X > 719 and won == False :
        winner = "Black"
        won = True
    player1X += player1speed 

    if player2X > 720 :
        player2speed = 0
    elif player2X > 360 and half2 == False :
        half2 = True
        player2speed = random.random()
    elif player2X > 719 and won == False :
        winner = "Blue"
        won = True
    player2X += player2speed

    if player3X > 720 :
        player3speed = 0
    elif player3X > 360 and half3 == False :
        half3 = True
        player3speed = random.random()
    elif player3X > 719 and won == False :
        winner = "green"
        won = True
    player3X += player3speed 

    if player4X > 720 :
        player4speed = 0
    elif player4X > 360 and half4 == False :
        half4 = True
        player4speed = random.random()
    elif player4X > 719 and won == False :
        winner = "Purple"
        won = True
    player4X += player4speed 

    if player5X > 720 :
        player5speed = 0
    elif player5X > 360 and half5 == False :
        half5 = True
        player5speed = random.random()
    elif player5X > 719 and won == False :
        winner = "Yellow"
        won = True
    player5X += player5speed 

    if player6X > 720 :
        player6speed = 0
    elif player6X > 360 and half6 == False :
        half6 = True
        player6speed = random.random()
    elif player6X > 719 and won == False :
        winner = "Orange"
        won = True
    player6X += player6speed 
    pygame.display.update() # önemli


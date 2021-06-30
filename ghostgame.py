import pygame
import random
import math
from pygame import mixer # adding background and handle all type of music in game as loading music or repeated music

pygame.init()

window_width = 800
window_height = 650

# def main():
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("GHOST GAME")
# background image
image = pygame.image.load('G:/graveyard_3875248_835x547-m.jpg')

#background sound
mixer.music.load('G:/GHOST8B.mp3')
mixer.music.play(-1) #-1 for play in loop mean wanna play backgnd music all time  so -1

pygame.display.flip()  # update contents of entire display of above image

# player
# x cordinate is width and y coordinate is height
player_img = pygame.image.load('G:\ghost.png')
# x,y axis coordinate
playerX = 30  # x value is 800 in this we are placing player at 30 value of x axis i.e horizontally x axis-starting 0 last 800
playerY = 480  # if we reduce it will go upwards y axis in this starting 650 and upwards or last is 0
playerX_change = 0  # signify change in x value i.e 30-0.5(speed of the palyer in X coordinate) if left 30+0.5 if ri8

# ENEMY
# creating multiple enemy by using list
enemy_img = []
enemyX = []  # empty list
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8

for i in range(num_of_enemies):  # we use for loop to insert value in list
    # enemy_img = pygame.image.load('G:\enemy.png')
    enemy_img.append(pygame.image.load('G:\enemy.png'))  # add value in a list we use append
    enemyX.append(random.randint(0, 800))  # 370#(x value decreased) 0 min 800 width max
    enemyY.append(random.randint(50, 150))# 48 #if we reduce this it will go upwards
    # when enemy hit boundary for that
    enemyX_change.append(4)
    enemyY_change.append(40)  # moves downwards along y axis when it hits the boundary

# blade or bullet
# ready-we cant see the blade on screen
# fire-blade is currently moving
bullet_img = pygame.image.load('G:/blade.png')
bulletX = 0  # 370#(x value decreased)
bulletY = 480  # same as player becz player will handle blade ,jo v value player ka hoga wahi value blade ka hoga always
bulletX_change = 0  # blade is not moving in x axis so 0 as it is useless
bulletY_change = 10  # moves y axis
bullet_state = "ready"

#score = 0
score_value=0
font=pygame.font.Font('freesansbold.ttf',32) #ttt is extension freesansbold is style format in pygame
textX=10 # x coordinate of 10 pixel in top left corner
textY=10

def show_score(X,Y):
    score=font.render("score:"+str(score_value),True,(255,255,255)) #255,255,255 is for white color
    window.blit(score,(X,Y)) #blit draw tha score on screen
#render means show the text on screen

def player(X, Y):
    window.blit(player_img, (X, Y))  # blit means drawing the img on window.# x,y are  coordinates


def enemy(X, Y, i):
    window.blit(enemy_img[i], (X, Y))


def fire_bullet(X, Y):
    global bullet_state
    bullet_state = "fire"

    window.blit(bullet_img, (X, Y))


def iscollision( enemyX , enemyY , bulletX , bulletY ):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# any keystroke pressed in a keyboard is an event
# event is any kind of input control in a game
x=0
# GAME LOOP
running = True
while running:
    window.fill((0, 0, 0))  # RGB important roll play
    window.blit(image, (0, 0))  # width and height of image we can adjust here. #for background purpose.



    # playerX+=0.1 #instead of 0.1 if we write 5or 3 img run very fastly....so we choose 0.1 ,+ means move in ri8 side
    # playerY+=0.1 #move towards up direction
    for event in pygame.event.get():  # every event is locked in pygame.event.get e.g.
        if event.type == pygame.QUIT :
            running = False
        # if keystroke is pressed check whether it is ri8 or left
        if event.type == pygame.KEYDOWN:  # chk any keystroke is pressed by keyboard
            if event.key == pygame.K_LEFT:  # check whether key pressed is left arrow or not
                playerX_change = -2 # -0.3 is too slow af inserting background image so we change 0.3 to 5 #left means we have to decrease so it move towards left
                # -5 is movement which will decrease evey time with player's width
                # print("LEFT arrow is pressed")
            if event.key == pygame.K_RIGHT:  # check whether key pressed is left arrow or not
                playerX_change = 2  # ri8 means we have to increase and move in ri8
                # ("right arrow is pressed")
            if event.key == pygame.K_SPACE:  # when we press space we are calling fire bullet function
                if bullet_state =="ready":
                    bulletX = playerX  # give the current x coordinate of player
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:  # keystroke has been released means
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # to stop the movement of player when keystroke is released  and
                # if we wri8 other than 0 player will move continously that we dont want
                # print("keystroke has been released")

    playerX += playerX_change  # 5=5+(-0.1)  or 5=5+0.1#whether it is - or + work according to that
    # setting boundary means player jo h woh boundary ke baad gayab ho jata h  so to stop we r going to use this loop
    if playerX <= 0:  # x coordinate becomes less than 0
        playerX = 0  # change value of playerX to 0
    elif playerX >= 736:  # 736 mean==window_width-png size of ghost pixel=800-64
        playerX = 736  # whenever it goes beyond 736 we want it to back to 736 X coordinate

    # enemy movement continously
    # further we are adding [i] due to creation of multiple enemies.
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]  # 5=5+(-0.1)  or 5=5+0.1#whether it is - or + work according to that
        # setting boundary means player jo h woh boundary ke baad gayab ho jata h  so to stop we r going to use this loop
        if enemyX[i] <= 0:
            enemyX_change[
                i] = 1  # when enemy hit boundary of x axis in ri8 it go left to hit and again same thing repeat
            enemyY[i] += enemyY_change[i]  # enemy hitting the boundary then it go one step down of x axis
        elif enemyX[i] >= 736:  # 736 mean==window_width-img pixel in png=800-64
            enemyX_change[i] = -1 # controlling speed of enemy in left direction
            enemyY[i] += enemyY_change[i]

        # collision
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:  # when collision occur we do
            bulletY = 480  # reset the bullet
            bullet_state = "ready"
            score_value += 1
            #print(score)
            enemyX[i] = random.randint( 0, 735)  # respond to enemy means to kill the enemy and create a new enemy
            enemyY[i] = random.randint(50, 150)  # "

        enemy(enemyX[i], enemyY[i], i)
    ##################################################above for creation of multiple enmies movement###############
    # bullet releasing multiples times
    if bulletY <= 0:
        bulletY = 480  # reset value of bullet
        bullet_state = "ready"

        # bullet movement
    if bullet_state =="fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # collision
    collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
    if collision:  # when collision occur we do
        bulletY = 480  # reset the bullet
        bullet_state = "ready"
        score_value += 1
        #print(score)
        enemyX[i] = random.randint(0, 735)  # respond to enemy means to kill the enemy and create a new enemy
        enemyY[i] = random.randint(50, 150)  # "

    player(playerX, playerY)  # calling player method
    # enemy(enemyX,enemyY)
    show_score(textX,textY)
    pygame.display.update()  # allows to update a portion on screen,instead of the entire area of screen

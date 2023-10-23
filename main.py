import pygame
import random
import math

#Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

#Create Background
background = pygame.image.load("5558636.jpg")

#Caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

#Bullet
#ready: you can't see the bullet on the screen
#fire: - The bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

#score
score_value = 0
#if you wnat to use other font text, go to www.dafont.com,download the font you want, copy that .ttf file to pythonProject(main folder)
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))
def player(x,y):
    #draw the screen by this picture, and the position of the picture on the screen
    screen.blit(playerImg,(x,y))

def enemy(x, y, i):
    screen.blit(enemyImg[i],(x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y + 10))

#Check distance between two points and the midpoint(googla)
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) +(math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False
#Game loop
running = True
while running:
    # RGB -Red- Green-Blue, color screen by this color and you should place this code on top so this become background color
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background,(0,0))

   # playerX += 0.1  # move the picture to the right hand
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:  # KEYDOWN: press the keyboard
            if event.key == pygame.K_LEFT:  #K_LEFT: press the left_arrow key
                playerX_change = -1
            if event.key == pygame.K_RIGHT:  #K_RIGHT: press the right_arrow key
                playerX_change = 1
            if event.key == pygame.K_SPACE:  #K_SPACE: press the space key
                if bullet_state == "ready":
                    # get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:  #KEYUP: release the keyboard
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #player movement
    playerX += playerX_change

    # checking for boundaries of the spaceship so it doesn't go out of bounds
    if playerX <=0:
        playerX= 0
    elif playerX >= 736:
        playerX = 736




    # checking for boundaries of the enemy, so it doesn't go out of bounds
    for i in range(num_of_enemies):
        # enemy movement
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = - 1
            enemyY[i] += enemyY_change[i]
        # Collistion
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # invoke this function above update() method so pygame will display.update() all the setting above
    player(playerX,playerY)

    show_score(textX,textY)
    pygame.display.update()



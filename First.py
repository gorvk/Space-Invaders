import pygame
import random
pygame.init()

class Player:
    def __init__(self, xPlayer, yPlayer):
        self.img = pygame.image.load('./images/player.png')
        self.xPlayer = xPlayer
        self.yPlayer = yPlayer
        self.playerSpeed = 7

class Enemy:
    def __init__(self, xEnemy, yEnemy):
        self.img = pygame.image.load('./images/enemy.png')
        self.xEnemy = xEnemy
        self.yEnemy = yEnemy
        self.enemySpeed = 0.4
        
class Bullet:
    def __init__(self, xBullet, yBullet):
        self.img = pygame.image.load('./images/bullet.png')
        self.xBullet = xBullet
        self.yBullet = yBullet
        self.bulletSpeed = 15
    
def check_events(): #Checks all the events happening 'in-canvas'.
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            return False
    return True

def player_movement(xPlayer, playerSpeed):  #Player movement using Keyboard.
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            if xPlayer > 0 :
                xPlayer -= playerSpeed
                return  xPlayer
        if key[pygame.K_d]:
            if xPlayer < 737 :
                xPlayer += playerSpeed
                return  xPlayer
        return xPlayer

def enemy_movement(yEnemy, enemySpeed):  #Enemy movement using Keyboard.
    yEnemy += enemySpeed
    return yEnemy

def bullet_movement(img, xBullet, yBullet, bulletSpeed, xPlayer):
    if pygame.mouse.get_pressed() == (1, 0, 0) and bullet.yBullet == 500:
        xBullet = xPlayer+24
    if pygame.mouse.get_pressed() == (1, 0, 0):
        canvas.blit(img, (xBullet, yBullet))
        yBullet -= bulletSpeed
        if yBullet < 0:
            yBullet = 500
        return xBullet, yBullet
    elif pygame.mouse.get_pressed() == (0, 0, 0) and yBullet < 500:
        canvas.blit(img, (xBullet, yBullet))
        yBullet -= bulletSpeed
        if yBullet < 0:
            yBullet = 500
        return xBullet, yBullet
    return xBullet, yBullet

if __name__ == '__main__':
    canvas = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Space Invader')
    showCanvas = True
    background = pygame.image.load('./images/background.png')
    player = Player(370, 510)
    flag = 0
    bullet = Bullet(500, 500)

    enemies = [Enemy(random.randint(0, 200), random.randint(0, 300)),
               Enemy(random.randint(250, 500), random.randint(0, 300)),
               Enemy(random.randint(550, 700), random.randint(0, 300))]
    
    while showCanvas:
        #Building and Giving Movement to all objects in game.
        canvas.fill((0, 0, 0))
        canvas.blit(background, (0, 0))
        canvas.blit(player.img, (player.xPlayer, player.yPlayer))
        for enemy in enemies:
            canvas.blit(enemy.img, (enemy.xEnemy, enemy.yEnemy))
            enemy.yEnemy = enemy_movement(enemy.yEnemy, enemy.enemySpeed)        
        player.xPlayer = player_movement(player.xPlayer, player.playerSpeed)
        bullet.xBullet, bullet.yBullet = bullet_movement(bullet.img, 
                                                         bullet.xBullet, 
                                                         bullet.yBullet, 
                                                         bullet.bulletSpeed, 
                                                         player.xPlayer)
        #Checking Events and Updating Canvas
        showCanvas = check_events()
        pygame.display.update()
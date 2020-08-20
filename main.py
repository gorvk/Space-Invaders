import pygame
import random
pygame.init()

class Player:
    def __init__(self, xPlayer, yPlayer):
        self.img = pygame.image.load('./images/player.png')
        self.xPlayer = xPlayer
        self.yPlayer = yPlayer
        self.playerSpeed = 7

class Enemy(pygame.sprite.Sprite):
    def __init__(self, xEnemy, yEnemy):
        super().__init__()
        self.image = pygame.image.load('./images/enemy.png')
        self.rect = self.image.get_rect()
        self.xEnemy = xEnemy
        self.yEnemy = yEnemy
        self.enemySpeed = 0.4
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, xBullet, yBullet):
        super().__init__()
        self.image = pygame.image.load('./images/bullet.png')
        self.rect = self.image.get_rect()
        self.xBullet = xBullet
        self.yBullet = yBullet
        self.bulletSpeed = 10
    
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
        yBullet -= bulletSpeed
        if yBullet < 0:
            yBullet = 500
        return xBullet, yBullet
    elif pygame.mouse.get_pressed() == (0, 0, 0) and yBullet < 500:
        yBullet -= bulletSpeed
        if yBullet < 0:
            yBullet = 500
        return xBullet, yBullet
    return xPlayer+24, yBullet

if __name__ == '__main__':
    canvas = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Space Invader')
    showCanvas = True
    background = pygame.image.load('./images/background.png')
    player = Player(370, 510)
    bullet = Bullet(500, 500)
    flag = 0
    score = 0
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    enemies = [Enemy(random.randint(0, 200), random.randint(0, 300)),
               Enemy(random.randint(250, 500), random.randint(0, 300)),
               Enemy(random.randint(550, 700), random.randint(0, 300))]
    block_list.add(enemies)
    all_sprites_list.add(enemies)
    while showCanvas:
        canvas.fill((0, 0, 0))
        canvas.blit(background, (0, 0))
        canvas.blit(player.img, (player.xPlayer, player.yPlayer))
        for enemy in enemies:
            enemy.yEnemy = enemy_movement(enemy.yEnemy, enemy.enemySpeed)        
            enemy.rect.y = enemy.yEnemy
            enemy.rect.x = enemy.xEnemy
        player.xPlayer = player_movement(player.xPlayer, player.playerSpeed)
        bullet.xBullet, bullet.yBullet = bullet_movement(bullet.image, 
                                                         bullet.xBullet, 
                                                         bullet.yBullet, 
                                                         bullet.bulletSpeed, 
                                                         player.xPlayer)
        bullet.rect.x = bullet.xBullet
        bullet.rect.y = bullet.yBullet
        all_sprites_list.add(bullet)
        blocks_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        for block in blocks_hit_list:
            score +=1 
            flag = 1
            print(score)
        if flag == 1:
            bullet.yBullet = 500
            flag = 0
        all_sprites_list.draw(canvas)

        #Checking Events and Updating Canvas
        showCanvas = check_events()
        pygame.display.update()
import pygame
import random
pygame.init()

class Player:
    def __init__(self, xPlayer, yPlayer):
        self.img = pygame.image.load('./images/player.png')
        self.xPlayer = xPlayer
        self.yPlayer = yPlayer
        self.playerSpeed = 11

class Enemy(pygame.sprite.Sprite):
    def __init__(self, xEnemy, yEnemy):
        super().__init__()
        self.image = pygame.image.load('./images/enemy.png')
        self.rect = self.image.get_rect()
        self.xEnemy = xEnemy
        self.yEnemy = yEnemy
        self.enemySpeed = 1
        
class Bullet(pygame.sprite.Sprite):
    def __init__(self, xBullet, yBullet):
        super().__init__()
        self.image = pygame.image.load('./images/bullet.png')
        self.rect = self.image.get_rect()
        self.rect.x = xBullet
        self.rect.y = yBullet
        self.bulletSpeed = 14
    
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
    if pygame.mouse.get_pressed() == (1, 0, 0) and yBullet == 530:
        xBullet = xPlayer+24
    if pygame.mouse.get_pressed() == (1, 0, 0):
        yBullet -= bulletSpeed
        if yBullet < 0:
            yBullet = 530
            xBullet = xPlayer+24
        return xBullet, yBullet
    elif pygame.mouse.get_pressed() == (0, 0, 0) and yBullet < 530:
        yBullet -= bulletSpeed
        if yBullet < 0:
            yBullet = 530
            xBullet = xPlayer+24
        return xBullet, yBullet
    return xPlayer+24, yBullet

if __name__ == '__main__':
    canvas = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Space Invader')
    showCanvas = True
    background = pygame.image.load('./images/background.png')
    player = Player(370, 510)
    bullet = Bullet(500, 530)
    gameFlag = 0
    score = 0
    enemies = [Enemy(random.randint(0, 100), random.randint(0, 100)),
               Enemy(random.randint(0, 300), random.randint(0, 100)),
               Enemy(random.randint(0, 400), random.randint(0, 100)),
               Enemy(random.randint(0, 600), random.randint(0, 100)),
               Enemy(random.randint(0, 700), random.randint(0, 100))]
    enemySprites = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()
    enemySprites.add(enemies)
    allSprites.add(enemies, bullet)
    scoreFont = pygame.font.Font("./font/font.ttf", 20)
    gameOverFont = pygame.font.Font("./font/font.ttf", 50)
    while showCanvas:
        if gameFlag == 0:
            canvas.fill((0, 0, 0))
            canvas.blit(background, (0, 0))
            scoreImg = scoreFont.render(f"SCORE : {str(score)}", True, (0,255,0))
            canvas.blit(scoreImg, (20, 20))
            for enemy in enemies:
                enemy.yEnemy = enemy_movement(enemy.yEnemy, enemy.enemySpeed)        
                enemy.rect.y = enemy.yEnemy
                enemy.rect.x = enemy.xEnemy
                if enemy.rect.y >= 420:
                    gameFlag = 1
            player.xPlayer = player_movement(player.xPlayer, player.playerSpeed)
            bullet.rect.x, bullet.rect.y = bullet_movement(bullet.image, bullet.rect.x, bullet.rect.y, bullet.bulletSpeed, player.xPlayer)
            allSprites.draw(canvas)
            canvas.blit(player.img, (player.xPlayer, player.yPlayer))
            blocks_hit_list = pygame.sprite.spritecollide(bullet, enemySprites, False)
            for block in blocks_hit_list:
                score +=1
                block.xEnemy = random.randint(0, 700)
                block.yEnemy = random.randint(0, 200)
                bullet.rect.y = 530
                hitFlag = 0
        elif gameFlag == 1:
            gameOverImg = gameOverFont.render("GAME OVER", True, (0,255,0))
            canvas.blit(background, (0, 0))
            allSprites.draw(canvas)
            canvas.blit(player.img, (player.xPlayer, player.yPlayer))
            canvas.blit(gameOverImg, (350/2, 300/2))
            canvas.blit(scoreImg, (600/2, 500/2))
            
        #Checking Events and Updating Canvas
        showCanvas = check_events() 
        pygame.display.update()
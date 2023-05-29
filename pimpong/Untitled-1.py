from pygame import *

win = display.set_mode((700,500))
display.set_caption('pin-pong')

class GameSprite(sprite.Sprite):
    def __init__(self,pic,speed,x,y,size):
        self.image = transform.scale(image.load(pic),size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.xspeed = speed
        self.yspeed = speed
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        global finish
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.y >= 475 or self.rect.y <= 0:
            self.yspeed *= -1
        if self.rect.x >= 700 or self.rect.x <= -25:
            finish = True
    def collide(self,recte):
        return self.rect.colliderect(recte)
class Player1(GameSprite):
    def update(self):
        keypressed = key.get_pressed()
        if keypressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keypressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
class Player2(GameSprite):
    def update(self):
        keypressed = key.get_pressed()
        if keypressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keypressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
background = transform.scale(image.load('fon.jpg'),(700,500))
game = True
finish = False
clock = time.Clock()
player1 = Player1('player1.png',5,0,225,(20,100))
player2 = Player2('player2.png',5,680,225,(20,100))
ball = GameSprite('ball.png',5,325,225,(25,25))

mixer.init()
mixer.music.load('relax.mp3')
mixer.music.play(-1)
collisionsound = mixer.Sound('collision.mp3')

font.init()
font = font.Font(None,70)
wintext = font.render('Player 1 Won!',True,(0,0,255))
losetext = font.render('Player 2 Won!',True,(255,0,0))

while game:
    win.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()
        if ball.collide(player1):
            ball.xspeed *= -1
            collisionsound.play()
        elif ball.collide(player2):
            ball.xspeed *= -1
            collisionsound.play()
    else:
        if ball.rect.x >= 700:
            win.blit(wintext,(220,200))
        elif ball.rect.x <= -25:
            win.blit(losetext,(220,200))
    clock.tick(60)
    display.update()
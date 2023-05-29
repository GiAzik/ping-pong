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
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
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
class Ball(GameSprite):
    def __init__(self,pic,speed,x,y):
        super.__init__(pic,speed,x,y,(25,25))
        self.xspeed = speed
        self.yspeed = speed
    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        if self.rect.y >= 475 or self.rect.y <= 0:
            self.yspeed *= -1
background = transform.scale(image.load('fon.jpg'),(700,500))
game = True
clock = time.Clock()
player1 = Player1('player1.png',5,0,225,(20,100))
player2 = Player2('player2.png',5,680,225,(20,100))
ball = Ball('ball.png',5,325,225)
while game:
    win.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    player1.update()
    player1.reset()
    player2.update()
    player2.reset()
    clock.tick(60)
    display.update()
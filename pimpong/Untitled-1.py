from pygame import *
from random import randint

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
        self.x2speed = speed
        self.yspeed = speed
        self.plusspeed = 0
        self.qw = 1
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        global finish
        self.yspeed += self.plusspeed
        self.rect.x += randint(self.x2speed,self.xspeed)*self.qw
        self.rect.y += self.yspeed
        if self.rect.y >= 475 or self.rect.y <= 0:
            if self.yspeed > 0:
                self.yspeed = self.speed
                self.rect.y = 476
            else:
                self.rect.y = 1
                self.yspeed = -self.speed
            self.yspeed *= -1
            self.plusspeed *= -1
        print(self.yspeed)
        if self.rect.x >= 700 or self.rect.x <= -25:
            finish = True
    def collide(self,recte):
        return self.rect.colliderect(recte)
    def collide1(self,x,y):
        return self.rect.collidepoint(x,y)
class Player1(GameSprite):
    def update1(self,ball,pt):
        if pt == 1:
            keypressed = key.get_pressed()
            if keypressed[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            elif keypressed[K_s] and self.rect.y < 400:
                self.rect.y += self.speed
        elif pt == 0:
            if ball.rect.x -self.rect.x <= 220:
                if self.rect.y < ball.rect.y:
                    self.rect.y += self.yspeed
                elif self.rect.y > ball.rect.y:
                    self.rect.y -= self.speed
            else:
                self.rect.y += randint(self.speed - 3,self.speed)*self.qw
                if self.xspeed == 0:
                    self.qw = randint(-1,1)
                    self.xspeed = randint(7,30)
                else:
                    self.xspeed -= 1
            if self.rect.y > 400:
                self.rect.y = 400
            elif self.rect.y < 0:
                self.rect.y = 0
class Player2(GameSprite):
    def update1(self,ball,pt):
        if pt == 1:
            keypressed = key.get_pressed()
            if keypressed[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            elif keypressed[K_DOWN] and self.rect.y < 400:
                self.rect.y += self.speed
        elif pt == 0:
            if self.rect.x -ball.rect.x <= 220:
                if self.rect.y < ball.rect.y:
                    self.rect.y += self.yspeed
                elif self.rect.y > ball.rect.y:
                    self.rect.y -= self.speed
            else:
                self.rect.y += randint(self.speed - 3,self.speed)*self.qw
                if self.xspeed == 0:
                    self.qw = randint(-1,1)
                    self.xspeed = randint(7,30)
                else:
                    self.xspeed -= 1
            if self.rect.y > 400:
                self.rect.y = 400
            elif self.rect.y < 0:
                self.rect.y = 0
background = transform.scale(image.load('fon.jpg'),(700,500))
game = True
finish = False
clock = time.Clock()
player1 = Player1('player1.png',5,0,225,(20,100))
player2 = Player2('player2.png',5,680,225,(20,100))
ball = GameSprite('ball.png',5,325,225,(25,25))

buttonStart = GameSprite('buttonStart.png',5,250,100,(200,95))
buttonEasy = GameSprite('buttonEasy.png',5,50,100,(100,95))
buttonHard = GameSprite('buttonHard.png',5,550,100,(100,95))
buttonP1 = GameSprite('buttonP1.png',5,50,375,(75,70))
buttonP2 = GameSprite('buttonP2.png',5,450,375,(75,70))
buttonPC1 = GameSprite('buttonPC1.png',5,175,375,(75,70))
buttonPC2 = GameSprite('buttonPC2.png',5,575,375,(75,70))
butlist = list()
butlist.append(buttonStart)
butlist.append(buttonEasy)
butlist.append(buttonHard)
butlist.append(buttonP1)
butlist.append(buttonPC1)
butlist.append(buttonP2)
butlist.append(buttonPC2)

mixer.init()
mixer.music.load('relax.mp3')
mixer.music.play(-1)
collisionsound = mixer.Sound('collision.mp3')
clicksound = mixer.Sound('click.mp3')

font.init()
font = font.Font(None,70)
wintext = font.render('Player 1 Wins!',True,(0,0,255))
losetext = font.render('Player 2 Wins!',True,(255,0,0))

a = 0
level = 0
pt1 = 1
pt2 = 0

while game:
    win.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1 and a ==0:
            xg,yg = e.pos
            for i in butlist:
                if i.collide1(xg,yg):
                    if i == buttonStart:
                        a = 1
                        finish = False
                        ball.rect.x = 340
                        clicksound.play()
                    elif i == buttonEasy:
                        ball.x2speed = ball.speed
                        ball.xspeed = ball.speed
                        ball.plusspeed = 0
                        clicksound.play()
                    elif i == buttonHard:
                        ball.x2speed = 0
                        ball.xspeed = 20
                        ball.plusspeed = 1
                        clicksound.play()
                    elif i == buttonP1:
                        pt1 = 1
                        clicksound.play()
                    elif i == buttonP2:
                        pt2 = 1
                        clicksound.play()
                    elif i == buttonPC1:
                        pt1 = 0
                        clicksound.play()
                    elif i == buttonPC2:
                        pt2 = 0
                        clicksound.play()
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                a = 0

    if a == 0:
        buttonStart.reset()
        buttonEasy.reset()
        buttonHard.reset()
        buttonP1.reset()
        buttonP2.reset()
        buttonPC1.reset()
        buttonPC2.reset()
    if not finish and a == 1:
        player1.reset()
        player2.reset()
        ball.update()
        ball.reset()
        player1.update1(ball,pt1)
        player2.update1(ball,pt2)
        if ball.collide(player1):
            ball.qw *= -1
            ball.rect.x = player1.rect.x + 25
            collisionsound.play()
        elif ball.collide(player2):
            ball.qw *= -1
            ball.rect.x = player2.rect.x - 25
            collisionsound.play()
    else:
        if ball.rect.x >= 680:
            win.blit(wintext,(220,220))
        elif ball.rect.x <= -5:
            win.blit(losetext,(220,220))
    clock.tick(60)
    display.update()
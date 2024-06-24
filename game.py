import pygame as pg
from bird import bird
import sys,time
class Game:
    def __init__(self):
        self.width=450
        self.height=650
        self.multiplier=1.5
        self.win=pg.display.set_mode((self.width,self.height))   # Make a Window 
        self.mov_speed=250
        self.clock=pg.time.Clock()
        self.bird=bird()
        self.isEnterPressed=False

        self.setupGroundAndBg()
        self.GameLoop()
    
    def GameLoop(self):
        lastTime=time.time()
        while True:
            # Calculating delta time
            newTime=time.time()
            dt=newTime-lastTime                       # last frame se curr frame me aane ka time
            lastTime=newTime
            for event in pg.event.get():            # Ek frame k andar jitne Event hue hai   frame-> ek baar loop run krna   pg.event.get()->return List type object
                if event.type==pg.QUIT:             # Check if the event type is QUIT
                    pg.quit()        # pygame se quit ho gya
                    sys.exit()    # Loop se exit ho jae or sare resources bhi memory se hat jae
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.isEnterPressed = True
                    if event.key==pg.K_SPACE and self.isEnterPressed:
                        self.bird.flap(dt)
            
            self.updateEverything(dt)
            self.drawEveryThing()
            pg.display.update()
            self.clock.tick(60)           # Ek   sec me 60 frame hi run hoenge



    def updateEverything(self,dt):
        if self.isEnterPressed:
            self.ground1_rect.x -= self.mov_speed * dt
            self.ground2_rect.x -= self.mov_speed * dt

            if self.ground1_rect.right < 0:
                self.ground1_rect.left = self.ground2_rect.right
            elif self.ground2_rect.right < 0:
                self.ground2_rect.left = self.ground1_rect.right
            
            self.bird.update(dt)
        

    def drawEveryThing(self):
        self.win.blit(self.bg_img,(0,-350))                   # Agr kuch bhi window pe dikhana hai to
        self.win.blit(self.ground1_img,self.ground1_rect)
        self.win.blit(self.ground2_img,self.ground2_rect)
        self.win.blit(self.bird.birdImg,self.bird.bird_rect)


    def setupGroundAndBg(self):
        self.bg_img=pg.transform.scale_by(pg.image.load("Assets/bg.png").convert(),self.multiplier)

        self.ground1_img=pg.transform.scale_by(pg.image.load("Assets/ground.png").convert(),self.multiplier)
        self.ground2_img=pg.transform.scale_by(pg.image.load("Assets/ground.png").convert(),self.multiplier)

        self.ground1_rect=self.ground1_img.get_rect()
        self.ground2_rect=self.ground2_img.get_rect()

        self.ground1_rect.x=0
        self.ground2_rect.x=self.ground1_rect.right
        self.ground1_rect.y=500
        self.ground2_rect.y=500



game =Game()
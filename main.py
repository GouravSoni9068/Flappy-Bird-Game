import pygame as pg
from bird import bird
from pipe import pipe
import sys,time
class Game:
    def __init__(self):
        pg.font.init()
        self.width=450
        self.height=650
        self.multiplier=1.5
        self.win=pg.display.set_mode((self.width,self.height))   # Make a Window 
        self.mov_speed=250
        self.clock=pg.time.Clock()
        self.bird=bird()
        self.isEnterPressed=False
        self.font=pg.font.Font("Assets/font.ttf",22)
        self.score_text=self.font.render("Score: 0 ",True,(0,0,0))
        self.score_text_rect=self.score_text.get_rect(center=(90,20))
        self.gameover_text=self.font.render("gameover",True,(0,0,0))
        self.gameover_text_rect=self.gameover_text.get_rect(center=(225,600))
        # self.Pipe=pipe(self.multiplier,self.mov_speed)
        self.allPipes=[]
        self.pipeCounter=71
        self.start_monetring=False
        self.score=0
        self.isGameStart=True

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
                if event.type == pg.KEYDOWN and self.isGameStart:
                    if event.key == pg.K_RETURN:
                        self.isEnterPressed = True
                        self.bird.update_on=True
                    if event.key==pg.K_SPACE and self.isEnterPressed:
                        self.bird.flap(dt)
                    
            
            self.updateEverything(dt)
            self.drawEveryThing()
            self.checkCollision()
            self.checkScore()
            pg.display.update()
            self.clock.tick(60)           # Ek   sec me 60 frame hi run hoenge

    def checkCollision(self):
        if len(self.allPipes)!=0:
            if( self.bird.bird_rect.bottom>=495):
                self.bird.update_on=False
                self.isEnterPressed=False
                self.isGameStart=False
            if(self.bird.bird_rect.colliderect(self.allPipes[0].pipeUp_rect) or self.bird.bird_rect.colliderect(self.allPipes[0].pipeDown_rect)):
                self.isEnterPressed=False
                self.isGameStart=False
            
    # def restartGame(self):
    #     self.score=0
    #     self.score_text=self.font.render("Score: 0 ",True,(0,0,0))


    def checkScore(self):
        if(len(self.allPipes)!=0):
            if (self.bird.bird_rect.left>self.allPipes[0].pipeUp_rect.left and 
                self.bird.bird_rect.right<self.allPipes[0].pipeUp_rect.right and
                self.start_monetring==False):
                self.start_monetring=True
            if(self.bird.bird_rect.right>self.allPipes[0].pipeUp_rect.right and
                self.start_monetring==True):
                self.start_monetring=False
                self.score+=1

                if(self.score==5):
                    self.mov_speed=300
                if(self.score==10):
                    self.mov_speed=350
                if(self.score==15):
                    self.mov_speed=450
                self.score_text=self.font.render(f"Score:{self.score} ",True,(0,0,0))


    def updateEverything(self,dt):

        if self.isEnterPressed:
            self.ground1_rect.x -= self.mov_speed * dt
            self.ground2_rect.x -= self.mov_speed * dt

            if self.ground1_rect.right < 0:
                self.ground1_rect.left = self.ground2_rect.right
            elif self.ground2_rect.right < 0:
                self.ground2_rect.left = self.ground1_rect.right
            
            if(self.pipeCounter>=75):
                self.allPipes.append(pipe(self.multiplier,self.mov_speed))
                print("Pipe Created")
                self.pipeCounter=0
            self.pipeCounter+=1
            for Pipe in self.allPipes:
                Pipe.update(dt)
            
            if len(self.allPipes)!=0:
                if self.allPipes[0].pipeUp_rect.right<0:
                    self.allPipes.pop(0)
                    print("Pipe Removed")
        self.bird.update(dt)


    def drawEveryThing(self):
        self.win.blit(self.bg_img,(0,-350))  
        for Pipe in self.allPipes:
            Pipe.drawPipe(self.win)
        self.win.blit(self.ground1_img,self.ground1_rect)
        self.win.blit(self.ground2_img,self.ground2_rect)
        self.win.blit(self.bird.birdImg,self.bird.bird_rect)
        self.win.blit(self.score_text,self.score_text_rect)
        if not self.isGameStart:
            self.win.blit(self.gameover_text,self.gameover_text_rect)

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
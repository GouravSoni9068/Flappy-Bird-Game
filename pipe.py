import pygame as pg
from random import randint

class pipe:
    def __init__(self,multiplier,mov_speed):
        self.pipeDown=pg.transform.scale_by(pg.image.load("Assets/pipedown.png").convert_alpha(),multiplier)
        self.pipeUp=pg.transform.scale_by(pg.image.load("Assets/pipeup.png").convert_alpha(),multiplier)
        self.pipeDown_rect=self.pipeDown.get_rect()
        self.pipeUp_rect=self.pipeUp.get_rect()
        self.gap=300
        self.mov_speed=mov_speed
        self.pipeUp_rect.y=randint(150,450)
        self.pipeUp_rect.x=450
        self.pipeDown_rect.x=self.pipeUp_rect.x
        self.pipeDown_rect.y=self.pipeUp_rect.y-self.gap-320
    
    def drawPipe(self,win):
        win.blit(self.pipeUp,self.pipeUp_rect)
        win.blit(self.pipeDown,self.pipeDown_rect)


    def update(self,dt):
        self.pipeUp_rect.x-=self.mov_speed*dt
        self.pipeDown_rect.x-=self.mov_speed*dt


import pygame as pg

class bird(pg.sprite.Sprite):                  # sprite class help krti hai vo entities jinhe hum move krna chahte hai
    def __init__(self):
        super(bird,self).__init__()
        self.bird_list=[pg.image.load("Assets/birdup.png").convert_alpha(),
                        pg.image.load("Assets/birddown.png").convert_alpha()]
        self.bird_idx=0
        self.birdImg=self.bird_list[self.bird_idx]
        self.bird_rect=self.birdImg.get_rect(center=(100,100))
        self.velocity_y=0
        self.gravity=10
        self.flapSpeed=250
        self.counter=0


    def update(self,dt):
        self.applyGravity(dt)
        self.updateImg()
        if(self.bird_rect.y<=0 and self.flapSpeed==250):
            self.bird_rect.y=0
            self.flapSpeed=0
            self.velocity_y=0
        elif(self.bird_rect.y>0 ):
            self.flapSpeed=250

    def applyGravity(self,dt):
        self.velocity_y+=self.gravity*dt
        self.bird_rect.y+=self.velocity_y

    def flap(self,dt):
        self.velocity_y=-self.flapSpeed*dt
    
    def updateImg(self):
        if self.counter==5:
            if self.bird_idx==0:
                self.bird_idx=1
            else:
                self.bird_idx=0

            self.birdImg=self.bird_list[self.bird_idx]
            self.counter=0
        self.counter+=1



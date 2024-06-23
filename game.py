import pygame as pg
import sys;
class Game:
    def __init__(self):
        self.height=725
        self.width=600
        self.win=pg.display.set_mode((self.width,self.height))   # Make a Window 
        self.bg_img=pg.transform.scale(pg.image.load("Assets/bg.png").convert(),(600,1066))
        self.GameLoop()
    
    def GameLoop(self):
        while True:
            for event in pg.event.get():            # Ek frame a andar jitne Event hue hai   frame-> ek baar loop run krna   pg.event.get()->return List type object
                if event.type==pg.QUIT:             # Check if the event type is QUIT
                    pg.quit()        # pygame se quit ho gya
                    sys.exit()    # Loop se exit ho jae or sare resources bhi memory se hat jae

            self.win.blit(self.bg_img,(0,-300))                   # Agr kuch bhi window pe dikhana hai to
            pg.display.update()

game =Game()
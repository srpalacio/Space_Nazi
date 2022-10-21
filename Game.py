from Sky import Sky
import pygame
import random

class Game:
    
    def __init__(self):
        
        self.width= 400
        self.heigth= 400
        
        self.mySky= Sky(self.width, self.heigth, 50)
        
        self.screen= pygame.display.set_mode((self.width, self.heigth))
        self.clock= pygame.time.Clock()
        self.fps= 60
        #Cargar la hoja de imágenes
        
        self.sprites= pygame.image.load("sprites.png")
        
    def run(self):
        
        pygame.init()
        
        control=True
        while control:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
            
            self.screen.fill((0,0,0))
            
            #Show the Sky
            
            for star in self.mySky.stars:
                r= random.randint(0, 255)
                g= random.randint(0, 255)
                b= random.randint(0, 255)
                pygame.draw.circle(self.screen,(r,g,b), star, 1)
                
            self.mySky.move()
                
            pygame.display.flip()
            
            self.clock.tick(self.fps)
            
myGame=Game()
myGame.run()
            
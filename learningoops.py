import pygame
import random

reso_x=840
reso_y=640
FPS=30
class Game(object):
    def main(self,screen):
        clock=pygame.time.Clock()
        image = pygame.image.load('background.png')
        sprites=pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        self.player=Player(sprites)
        for i in range(4):
            self.m=Mob(sprites)
            
        image_x=0
        image_y=0
        while 1:
            dt=clock.tick(FPS)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    return
            ''''key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                image1_x -=10
            if key[pygame.K_RIGHT]:
                image1_x +=10
            if key[pygame.K_UP]:
                image1_y -=10
            if key[pygame.K_DOWN]:
                image1_y +=10'''
            #screen.fill((200,200,200))
            sprites.update(dt/1000.,self)
            screen.blit(image,(0,0))
            #screen.blit(image,(image_x,image_y))
            sprites.draw(screen)
            #screen.blit(image1,(image1_x,image1_y))
            pygame.display.flip()
class Player(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(Player,self).__init__(*groups)
        self.image = pygame.image.load('python.png')
        self.rect = pygame.rect.Rect((120,280),self.image.get_size())
        self.resting = False
        self.dy = 0

    def update(self,dt,game):
        #last=self.rect.copy() #For gravity
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -=300*dt
        elif key[pygame.K_RIGHT]:
            self.rect.x += 300*dt
        elif key[pygame.K_UP]:
            self.rect.y -= 300*dt
        elif key[pygame.K_DOWN]:
            self.rect.y +=300*dt
        if (self.rect.x<140):
            self.rect.x=140
        if (self.rect.x > 670):
            self.rect.x=670
        if (self.rect.top<0):
            self.rect.top=0
        if (self.rect.bottom>reso_y):
            self.rect.bottom=reso_y

        #if key[pygame.K_SPACE]:
         #   self.dy = -400
        #self.dy = min(100,self.dy + 10)

        #self.rect.y +=self.dy * dt
        #new = self.rect
        #self.resting = False  #Gravity
class Mob(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(Mob,self).__init__(*groups)
        self.image = pygame.image.load('obst.png')
        self.rect = pygame.rect.Rect((random.randrange(140,670),random.randrange(-100,-40)),self.image.get_size())
        self.dy = 0
        self.speedy = random.randrange(10,15)

    def update(self,dt,game):
        self.rect.y += self.speedy
        if self.rect.top > reso_y + 10 :
            self.rect.x = random.randrange(140,670)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(10,15)
 
if __name__=='__main__':
    pygame.init()
    pygame.mixer.init()
    screen=pygame.display.set_mode((reso_x,reso_y))
    pygame.display.set_caption("###THE GAME CHANGERS###")
    Game().main(screen)

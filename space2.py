import pygame
from moviepy.editor import VideoFileClip,CompositeVideoClip,concatenate_videoclips,TextClip#For Gameover Video

import random
import os,sys
from os import path#For image loading path

img_dir = path.join(path.dirname(__file__),'img')

reso_x=1000
reso_y=750
FPS=30
class Game(object):
    def main(self,screen):
        clock=pygame.time.Clock()
        image = pygame.image.load(path.join(img_dir,'stars.png')).convert()#Background
        sprites=pygame.sprite.Group()#All sprites which are drawn 
        mobs = pygame.sprite.Group()#All sprites which disappear after hitting bullets

        boss = pygame.sprite.Group()# all BOss Class sprites
        bullet = pygame.sprite.Group()#all bullet sprites
#Same as Space.py
        self.player=Player(sprites)
        resume = pygame.image.load(path.join(img_dir,'resume.png')).convert_alpha()
        #font_name = pygame.font.match_font('arial')
        def draw_text(surf,text,size,x,y):
            font = pygame.font.Font('kenvector_future.ttf',size)
            text_surface = font.render(text,True,(255,255,255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            surf.blit(text_surface,text_rect)
        for i in range(3):
            self.m=Mob(path.join(img_dir,'alien2.png'),sprites,mobs)
            self.n=Mob(path.join(img_dir,'alien3.png'),sprites,mobs)
            self.o=Mob(path.join(img_dir,'alien4.png'),sprites,mobs)
        self.boss1= Boss(250,-40,path.join(img_dir,'boss1.png'),sprites,boss)
        self.boss2= Boss(500,-20,path.join(img_dir,'boss2.png'),sprites,boss)
        self.boss3= Boss(750,-40,path.join(img_dir,'boss3.png'),sprites,boss)
        running=True
        image_x=0
        image_y=0
        score=0
        run = True
        button1 = pygame.draw.rect(screen, (255, 0, 0),(285, 355, 130, 80))
        button2 = pygame.draw.rect(screen, (255, 0, 0),(590, 360, 110, 75))

        def shoot(player):
            bullet1=Bullets(player.rect.left+14,player.rect.top,sprites,bullet)
            bullet2=Bullets(player.rect.right-14,player.rect.top,sprites,bullet)
        run = True
        count = 0
        while running:
            dt=clock.tick(FPS)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if button2.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                        run = True
                    if button1.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                        pygame.quit()
                key = pygame.key.get_pressed() 
                if key[pygame.K_SPACE]:
                    shoot(self.player)
            if run == True:
                #screen.fill((200,200,200))
                sprites.update(dt/1000.,self)
                hits = pygame.sprite.groupcollide(mobs,bullet,True,True)
                for hit in hits:
                    score += 1

                if count < 300:
                    hits = pygame.sprite.groupcollide(boss,bullet,False,True)
                    for hit in hits:
                        score+=2
                    count+=1
                else:
                    hits = pygame.sprite.groupcollide(boss,bullet,True,True)
                    for hit in hits:
                        score +=5
                if score > 90 :#Boss defeating Condition 
                    running = False


                hits = pygame.sprite.spritecollide(self.player,mobs,False,pygame.sprite.collide_circle)
                if hits:
                    clip5 = VideoFileClip('./mp4/planet.mp4')
                    video =clip5.resize((1000,700))
                    video.preview()
                    pygame.quit()

            screen.blit(image,(0,0))
            #screen.blit(image,(image_x,image_y))
            sprites.draw(screen)
            draw_text(screen,"Score : "+str(score),18,900,20)
            #screen.blit(image1,(image1_x,image1_y))
            if run == False:
                resume_rect=resume.get_rect()
                resume_rect.center=(reso_x/2,reso_y/2)
                screen.blit(resume,resume_rect)

            pygame.display.flip()
class Player(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(Player,self).__init__(*groups)
        self.image = pygame.image.load(path.join(img_dir,'fighter.png'))
        self.rect = pygame.rect.Rect((430,580),self.image.get_size())
        self.radius = 35
        self.resting = False
        self.dy = 0
        #last=self.rect.copy() #For gravity
    def update(self,dt,game):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -=300*dt
        elif key[pygame.K_RIGHT]:
            self.rect.x += 300*dt
        elif key[pygame.K_UP]:
            self.rect.y -= 300*dt
        elif key[pygame.K_DOWN]:
            self.rect.y +=300*dt
        if (self.rect.left<0):
            self.rect.left=0
        if (self.rect.right > reso_x):
            self.rect.right=reso_x
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
    def __init__(self,image,*groups):
        super(Mob,self).__init__(*groups)
        self.image_orig = pygame.image.load(image)
        self.image = self.image_orig.copy()
        self.rect = pygame.rect.Rect((random.randrange(50,950),random.randrange(-100,-40)),self.image.get_size())
        self.radius = 25
        self.dy = 0
        self.speedy = random.randrange(10,15)
        self.speedx = random.randrange(-10,10)
    def update(self,dt,game):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > reso_y + 10  :
            self.rect.x = random.randrange(140,670)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(10,15)
class Boss(pygame.sprite.Sprite):
    def __init__(self,x,y,image,*groups):
        super(Boss,self).__init__(*groups)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.speedy = 10
    def update(self,dt,game):
        self.rect.y += self.speedy
        if self.rect.top > 0 :
            self.speedy = 0
            self.rect.top =0
            

class Bullets(pygame.sprite.Sprite):
    def __init__(self,x,y,*groups):
        super(Bullets,self).__init__(*groups)
        self.image = pygame.image.load(path.join(img_dir,'laserRed.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -40
    def update(self,dt,game):
        self.rect.y += self.speedy
        if self.rect.bottom < 0 :
            self.kill()


 
if __name__=='__main__':
    pygame.init()
    pygame.mixer.init()
    screen=pygame.display.set_mode((reso_x,reso_y))
    pygame.display.set_caption("###THE GAME CHANGERS###")
    Game().main(screen)

import pygame
from moviepy.editor import VideoFileClip,CompositeVideoClip,concatenate_videoclips
import random
import os,sys
from os import path
img_dir = path.join(path.dirname(__file__),'img')

reso_x=840
reso_y=640
FPS=30
class Game(object):
    def __init__(self):
        self.score =0
    def main(self,screen):
        clock=pygame.time.Clock()
        image = pygame.image.load(path.join(img_dir,'background.png'))
        sprites=pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        self.player=Player(sprites)
        resume = pygame.image.load(path.join(img_dir,'resume.png')).convert_alpha()
        #font_name = pygame.font.match_font('arial')
        def draw_text(surf,text,size,x,y):
            font = pygame.font.Font('kenvector_future.ttf',size)
            text_surface = font.render(text,True,(0,255,0))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            surf.blit(text_surface,text_rect)

        for i in range(2):
            self.m=Mob(path.join(img_dir,'obst1.png'),sprites,mobs)
            self.n=Mob(path.join(img_dir,'obst2.png'),sprites,mobs)
        running=True
        image_x=0
        image_y=0
        times_last=pygame.time.get_ticks()
        self.score=0
        run = True
        button1 = pygame.draw.rect(screen, (255, 0, 0),(205, 265, 130, 80))
        button2 = pygame.draw.rect(screen, (255, 0, 0),(510, 300, 110, 75))

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
            if run == True:
                times=pygame.time.get_ticks()
                if times - times_last >1000:
                    times_last = times
                    self.score+=1
                sprites.update(dt/1000.,self)
                hits = pygame.sprite.spritecollide(self.player,mobs,False)
                if hits:
                    clip5 = VideoFileClip('./mp4/planet.mp4')
                    video =clip5.resize((1000,700))
                    video.preview()
                    pygame.quit()

            screen.blit(image,(0,0))
            #screen.blit(image,(image_x,image_y))
            sprites.draw(screen)
            draw_text(screen,"Score : "+str(self.score),18,780,20)
            if self.score > 20:
                running = False
            if run == False:
                resume_rect=resume.get_rect()
                resume_rect.center=(reso_x/2,reso_y/2)
                screen.blit(resume,resume_rect)
            #screen.blit(image1,(image1_x,image1_y))
            pygame.display.flip()
        #pygame.quit()
class Player(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(Player,self).__init__(*groups)
        self.image = pygame.image.load(path.join(img_dir,'python.png'))
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
    def __init__(self,image,*groups):
        super(Mob,self).__init__(*groups)
        self.image = pygame.image.load(image)
        self.rect = pygame.rect.Rect((random.randrange(140,670),random.randrange(-100,-40)),self.image.get_size())
        self.dy = 0
        self.speedy = random.randrange(10,11)

    def update(self,dt,game):
        self.rect.y += self.speedy
        if self.rect.top > reso_y + 10 :
            self.rect.x = random.randrange(140,670)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(10,11)

 
if __name__=='__main__':
    pygame.init()
    pygame.mixer.init()
    screen=pygame.display.set_mode((reso_x,reso_y))
    pygame.display.set_caption("###THE GAME CHANGERS###")
    Game().main(screen)

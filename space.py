from moviepy.editor import VideoFileClip,CompositeVideoClip,concatenate_videoclips#For Gameover Video
import pygame
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
        bullet = pygame.sprite.Group()#all bullet sprites
        self.player=Player(sprites)
        resume = pygame.image.load(path.join(img_dir,'resume.png')).convert_alpha()#Resume screen
        #font_name = pygame.font.match_font('arial')
        def draw_text(surf,text,size,x,y):#For writing text on screen
            font = pygame.font.Font('kenvector_future.ttf',size)
            text_surface = font.render(text,True,(255,255,255))
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            surf.blit(text_surface,text_rect)
        for i in range(6):
            self.m=Mob(sprites,mobs)
        running=True
        image_x=0
        image_y=0
        score=0
        def shoot(player):
            bullet1=Bullets(player.rect.left+14,player.rect.top,sprites,bullet)
            bullet2=Bullets(player.rect.right-14,player.rect.top,sprites,bullet)
        run = True
        button1 = pygame.draw.rect(screen, (255, 0, 0),(285, 355, 130, 80))#Mouse Buttons positions
        button2 = pygame.draw.rect(screen, (255, 0, 0),(590, 360, 110, 75))

        while running:
            dt=clock.tick(FPS)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if event.type == pygame.MOUSEBUTTONDOWN: # Mouse buttons action
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
                hits = pygame.sprite.groupcollide(mobs,bullet,True,True)# bullets action
                for hit in hits:
                    score += 1 # Score updation
                    self.m=Mob(sprites,mobs)
                hits = pygame.sprite.spritecollide(self.player,mobs,False,pygame.sprite.collide_circle)
                if hits:#Gameover Screen
                    clip5 = VideoFileClip('./mp4/planet.mp4')
                    video =clip5.resize((1000,700))
                    video.preview()
                    pygame.quit()
            if score > 35 :#For moving onto next game
                running = False
            screen.blit(image,(0,0))
            #screen.blit(image,(image_x,image_y))
            sprites.draw(screen)# for drawing sprites
            draw_text(screen,"Score : "+str(score),18,900,20) #for displaying text
            #screen.blit(image1,(image1_x,image1_y))
            if run == False:# resume screen
                resume_rect=resume.get_rect()
                resume_rect.center=(reso_x/2,reso_y/2)
                screen.blit(resume,resume_rect)

            pygame.display.flip()
class Player(pygame.sprite.Sprite):#This class contains player sprite properties
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
class Mob(pygame.sprite.Sprite):#This contains Enemy sprite properties
    def __init__(self,*groups):
        super(Mob,self).__init__(*groups)
        self.image_orig = pygame.image.load(path.join(img_dir,'asteroid.png'))
        self.image = self.image_orig.copy()
        self.rect = pygame.rect.Rect((random.randrange(50,950),random.randrange(-100,-40)),self.image.get_size())
        self.radius = 25
        self.dy = 0
        self.speedy = random.randrange(10,15)
        self.speedx = random.randrange(-10,10)
        self.rot=0
        self.rot_speed = random.randrange(-20,20)
        self.last_update = pygame.time.get_ticks()
    def rotate(self): #For rotating asteroid 50ms 1 degree
        now = pygame.time.get_ticks()
        if now - self.last_update > 50 :
            self.last_update = now
            self.rot = (self.rot + self.rot_speed)%360
            new_image = pygame.transform.rotate(self.image_orig,self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center= old_center
    def update(self,dt,game):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > reso_y + 10  :
            self.rect.x = random.randrange(140,670)
            self.rect.y = random.randrange(-100,-40)#for spawwing above screen
            self.speedy = random.randrange(10,15)
class Bullets(pygame.sprite.Sprite): # Bullet properties
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


 
if __name__=='__main__': # FOr running single name
    pygame.init()
    pygame.mixer.init()
    screen=pygame.display.set_mode((reso_x,reso_y))
    pygame.display.set_caption("###THE GAME CHANGERS###")
    Game().main(screen)

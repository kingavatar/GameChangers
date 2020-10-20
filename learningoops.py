import pygame
import tmx

reso_x=1024
reso_y=768
class Game(object):
    def main(self,screen):
        clock=pygame.time.Clock()
        reso_y=720
        image = pygame.image.load('python.jpg')
        sprites=pygame.sprite.Group()
        self.player=Player(sprites)
        self.walls=pygame.sprite.Group()
        tree=pygame.image.load('python.png')
        image_x=0
        image_y=0
        for x in range(0,reso_x,80):
            for y in range(0,reso_y,80):
                if x in (0,reso_x-80) or y in (0,reso_y-80):
                    wall=pygame.sprite.Sprite(self.walls)
                    wall.image=tree
                    wall.rect=pygame.rect.Rect((x,y),tree.get_size())
        #sprites.add(self.walls)'''
        while 1:
            dt=clock.tick(30)

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    return
            #image_y-=1
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
        sprites.add(self.walls)
class Player(pygame.sprite.Sprite):
    def __init__(self,*groups):
        super(Player,self).__init__(*groups)
        self.image = pygame.image.load('python.png')
        self.rect = pygame.rect.Rect((120,480),self.image.get_size())
        self.resting = False
        self.dy = 0

    def update(self,dt,game):
        last=self.rect.copy()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -=300*dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300*dt
        '''if key[pygame.K_UP]:
            self.rect.y -= 300*dt
        if key[pygame.K_DOWN]:
            self.rect.y +=300*dt'''
        if self.resting and key[pygame.K_SPACE]:
            self.dy = -400
        self.dy = min(100,self.dy + 10)

        self.rect.y +=self.dy * dt
        new = self.rect
        self.resting = False
        for cell in pygame.sprite.spritecollide(self,game.walls,False):
    #    self.rect=last
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left :
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right :
                new.left = cell.right
            if last.bottom <= cell.top and new.bottom > cell.top :
                self.resting = True
                new.bottom = cell.top
                self.dy =0
            if last.top >= cell.bottom and new.top < cell.bottom :
                new.top = cell.bottom
                self.dy =0
if __name__=='__main__':
    pygame.init()
    screen=pygame.display.set_mode((reso_x,reso_y))
    Game().main(screen)

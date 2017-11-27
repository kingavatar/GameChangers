from moviepy.editor import VideoFileClip,CompositeVideoClip,concatenate_videoclips,TextClip
import car as car
import space as space
import space2 as space2
import pygame
import os,sys
from os import path
img_dir = path.join(path.dirname(__file__),'img')

pygame.init()
pygame.mixer.init()
FPS=30

pygame.display.set_caption("###THE GAME CHANGERS###")
running = True
run = False
reso_x=1131
reso_y=707
screen=pygame.display.set_mode((reso_x,reso_y))
play=pygame.image.load(path.join(img_dir,'play.png'))
play_rect=pygame.rect.Rect((460,570),play.get_size())
button1 = pygame.draw.rect(screen, (255, 0, 0),play_rect)
img=pygame.image.load(path.join(img_dir,'awesome.jpg'))
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
def draw_text(surf,text,size,x,y):
    font = pygame.font.Font('kenvector_future.ttf',size)
    text_surface = font.render(text,True,(255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if button1.collidepoint(pos) and pygame.mouse.get_pressed()[0]:
                run = True
                running = False
    screen.blit(img,(0,0))
    draw_text(screen,"THE GAME CHANGERS",40,550,25)
    screen.blit(play,play_rect)
    pygame.display.flip()



if run == True:
    clip1 = VideoFileClip('./mp4/logo.mp4')
    video =clip1.resize((1280,720))
    video.preview()
    clip2 = VideoFileClip('./mp4/coming.mp4')
    clip2= concatenate_videoclips([clip2,clip2])
    video =clip2.resize((1280,720))
    video.preview()
    clip3 = VideoFileClip('./mp4/earth.mp4')
    video =clip3.resize((1280,720))
    video.preview()
    clip4 = VideoFileClip('./mp4/lightning.mp4')
    clip4= concatenate_videoclips([clip4,clip4])
    video =clip4.resize((1280,720))
    video.preview()
    '''clip5 = VideoFileClip('./mp4/sunflare2.mp4')
    clip5= concatenate_videoclips([clip5,clip5,clip5])
    video =clip5.resize((1280,720))
    video.preview()'''
    clip6 = VideoFileClip('./mp4/road.mp4')
    clip6= concatenate_videoclips([clip6,clip6,clip6])
    video =clip6.resize((1280,720))
    video.preview()
    reso_x=840
    reso_y=650
    screen=pygame.display.set_mode((reso_x,reso_y))
    screen.fill((0,0,0))
    car.Game().main(screen)

    clip1 = VideoFileClip('./mp4/chaos.mp4')
    video =clip1.resize((1280,720))
    video.preview()

    clip1 = VideoFileClip('./mp4/chaos2.mp4')
    video =clip1.resize((1280,720))
    video.preview()

    clip1 = VideoFileClip('./mp4/rain.mp4')
    clip1= concatenate_videoclips([clip1,clip1,clip1,clip1])
    video =clip1.resize((1280,720))
    video.preview()

    clip1 = VideoFileClip('./mp4/cabin.mp4')
    clip1= concatenate_videoclips([clip1,clip1,clip1])
    video =clip1.resize((1280,720))
    video.preview()

    clip1 = VideoFileClip('./mp4/bluelight.mp4')
    clip1= concatenate_videoclips([clip1,clip1,clip1])
    video =clip1.resize((1280,720))
    video.preview()


    clip1 = VideoFileClip('./mp4/warpspeed.mp4')
    clip1= concatenate_videoclips([clip1,clip1,clip1,clip1])
    video =clip1.resize((1280,720))
    video.preview()
    reso_x=1000
    reso_y=750
    screen=pygame.display.set_mode((reso_x,reso_y))
    space.Game().main(screen)

    clip1 = VideoFileClip('./mp4/landing.mp4')
    clip1= concatenate_videoclips([clip1,clip1])
    video =clip1.resize((800,800))
    video.preview()


    clip1 = VideoFileClip('./mp4/aliean.mp4')
    clip1= concatenate_videoclips([clip1,clip1])
    video =clip1.resize((1280,720))
    video.preview()

    clip1 = VideoFileClip('./mp4/lock.mp4')
    video =clip1.resize((1280,720))
    video.preview()

    reso_x=1000
    reso_y=750
    screen=pygame.display.set_mode((reso_x,reso_y))
    space2.Game().main(screen)


    clip1 = VideoFileClip('./mp4/blackhole.mp4')
    video =clip1.resize((1280,720))
    video.preview()

    clip1 = VideoFileClip('./mp4/warp.mp4')
    clip1= concatenate_videoclips([clip1,clip1,clip1,clip1])
    video =clip1.resize((1280,720))
    video.preview()
    
    clip1 = VideoFileClip('./mp4/ending.mp4')
    video =clip1.resize((1000,900))
    video.preview()


pygame.quit()

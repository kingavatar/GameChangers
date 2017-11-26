from moviepy.editor import VideoFileClip,CompositeVideoClip
import pygame
pygame.display.set_mode((1000,1000))
pygame.display.set_caption('My video!')
clip1 = VideoFileClip('./mp4/planet.mp4')
clip2 = VideoFileClip('./mp4/planet.mp4')
clip3 = VideoFileClip('./mp4/planet.mp4')
video = CompositeVideoClip([clip1,clip2.set_start(3),clip3.set_start(6)], size=(720,460))

video.preview()
pygame.quit()

import pygame
import os
import math
o = 50

width, height = 1200,800
f_width, f_height = 1100,700
D_yposition = 177.5
G_yposition = 252.5
D_r_xposition = 875
G_r_xposition = 1025
thickness = 6.25
D_width = 112.5
D_length = 345
G_width = 37.5
G_length = 195

win = pygame.display.set_mode((width,height))
FPS = 60
green = (0,255,0)
white = (255,255,255)
border_c = pygame.Rect(width/2 - thickness/2 + 1, o , thickness , height - 2*o)
border_fl = pygame.Rect(o , o , thickness , height - 2*o)
border_fr = pygame.Rect(f_width + o + 1 - thickness , o , thickness , height - 100)
border_fu = pygame.Rect(o , o , width - 2*o , thickness)
border_fd = pygame.Rect(o , f_height + o + 1 - thickness , width - 2*o , thickness)
goall_1_u = pygame.Rect(o , o + D_yposition , D_width , thickness)
goall_1_d = pygame.Rect(o , o + D_length + D_yposition , D_width , thickness)
goall_1_l = pygame.Rect(o + D_width , o + D_yposition , thickness , D_length+thickness )
goall_2_u = pygame.Rect(o , o + G_yposition, G_width , thickness)
goall_2_d = pygame.Rect(o , o + G_yposition + G_length , G_width , thickness)
goall_2_l = pygame.Rect(o + G_width , o + G_yposition , thickness , G_length + thickness)
goalr_1_u = pygame.Rect(o + D_width + D_r_xposition, o + D_yposition , D_width , thickness)
goalr_1_d = pygame.Rect(o + D_width + D_r_xposition, o + D_length + D_yposition , D_width , thickness)
goalr_1_l = pygame.Rect(o + D_width + D_r_xposition, o + D_yposition , thickness , D_length + thickness )
goalr_2_u = pygame.Rect(o + G_width + G_r_xposition , o + G_yposition , G_width , thickness)
goalr_2_d = pygame.Rect(o + G_width + G_r_xposition , o + G_yposition + G_length , G_width , thickness)
goalr_2_l = pygame.Rect(o + G_width + G_r_xposition , o + G_yposition , thickness , G_length + thickness)


def draw_window():
    win.fill(green)
    pygame.draw.rect(win,white,border_c)
    pygame.draw.rect(win,white,border_fl)
    pygame.draw.rect(win,white,border_fr)
    pygame.draw.rect(win,white,border_fu)
    pygame.draw.rect(win,white,border_fd)
    pygame.draw.circle(win, white, (600, 400), 50 , 6)
    pygame.draw.circle(win, white, (600, 400), 6)
    pygame.draw.circle(win, white, (230, 400), 6)
    pygame.draw.circle(win, white, (970, 400), 6)
    pygame.draw.arc(win, white, pygame.Rect(o - 37 , o - 37 , 74 , 74), math.radians(270), math.radians(360), 6)
    pygame.draw.arc(win, white, pygame.Rect(o + f_width - 37 , o - 37 , 74 , 74), math.radians(180), math.radians(270), 6)
    pygame.draw.arc(win, white, pygame.Rect(o - 37 , o + f_height - 37 , 74 , 74), math.radians(0), math.radians(90), 6)
    pygame.draw.arc(win, white, pygame.Rect(o + f_width - 37 , o +f_height - 37 , 74 , 74), math.radians(90), math.radians(180), 6)
    pygame.draw.rect(win,white, goall_1_u)
    pygame.draw.rect(win,white, goall_1_d)
    pygame.draw.rect(win,white, goall_1_l)
    pygame.draw.rect(win,white, goall_2_u)
    pygame.draw.rect(win,white, goall_2_d)
    pygame.draw.rect(win,white, goall_2_l)
    pygame.draw.rect(win,white, goalr_1_u)
    pygame.draw.rect(win,white, goalr_1_d)
    pygame.draw.rect(win,white, goalr_1_l)
    pygame.draw.rect(win,white, goalr_2_u)
    pygame.draw.rect(win,white, goalr_2_d)
    pygame.draw.rect(win,white, goalr_2_l)
    
    

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()


if (__name__ == '__main__'):
    main()
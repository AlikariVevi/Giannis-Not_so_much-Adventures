# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame as pg

pg.init()


###Screen Resolution
screen_width=800
screen_height=600
GameResolution={screen_width,screen_height}

###Flag Options
#0             no flags
#FULLSCREEN    create a fullscreen display (default)
#DOUBLEBUF     recommended for HWSURFACE or OPENGL
#HWSURFACE     hardware accelerated, only in FULLSCREEN
#OPENGL        create an OpenGL-renderable display
#RESIZABLE     display window should be sizeable
#NOFRAME       display window will have no border or controls

ScreenFlags=0

### Color Depth
# not passing the argument default to the best and fastest color depth for the system
#NumberofBitstoUseforColor=0

gameDisplay=pg.display.det_mode(resolution=GameResolution,flags=ScreenFlags)

### Title of the game Window
pg.display.set_captions("Hello World")

###Game Clock
clock=pg.time.clock()

crashed=Flase
while not crashed:
    #list of events per frame per second
    for event in pg.event.get():
        #QUIT--> X botton
        if event.type == pg.QUIT:
            crashed = True
        print(event)
    pg.display.update()
    #frame per second
    FramesPerSecond=60
    clock.tick(FramesPerSecond)
    
pg.quit()
quit()
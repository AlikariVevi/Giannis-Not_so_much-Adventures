# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame as pg


pg.init()


###Screen Resolution
screen_width=800
screen_height=400
GameResolution=[screen_width,screen_height]

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

gameDisplay=pg.display.set_mode(GameResolution,ScreenFlags)

### Title of the game Window
pg.display.set_caption('Hello World!')


###Game Clock
clock=pg.time.Clock()

###Colors RGB code 0-255

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)


colors={0:red,
        1:white
        }

tilemap=[[red,green,red,green,red,green,red,green],
         [white,blue,white,blue,white,blue,white,blue],
         [red,green,red,green,red,green,red,green],
         [white,blue,white,blue,white,blue,white,blue],
         [red,green,red,green,red,green,red,green],
         [white,blue,white,blue,white,blue,white,blue]
        ]

tilemap2=[[red,green,red,green,red,green,red,green],
         [white,blue,white,blue,white,blue,white,blue],
         [red,green,red,green,red,green,red,green],
         [white,blue,white,blue,white,blue,white,blue],
         [red,green,red,green,red,green,red,green],
         [white,blue,white,blue,white,blue,white,blue],
         [white,blue,white,blue,white,blue,white,blue],
         [red,green,red,green,red,green,red,green],
         [white,blue,white,blue,white,blue,white,blue]
        ]
tilesize=100
mapwidth=int(screen_width/tilesize)
print(mapwidth)
mapheight=int(screen_height/tilesize)
print(mapheight)
GameResolutionWithTiles=[mapwidth*tilesize,mapheight*tilesize]
gameDisplay=pg.display.set_mode(GameResolutionWithTiles,ScreenFlags)

#pg.display.update()

crashed= False
while not crashed:
    #list of events per frame per second
    
    #Quiting the game
    for event in pg.event.get():
        #X buttom mouse clicking --> Quit
        if event.type == pg.QUIT:
            crashed = True
        # presing key event
        if event.type == pg.KEYDOWN:
            # ESCAPE --> Quit
            if event.key == pg.K_ESCAPE:
                crashed = True
            # CTRL+Q -->Quit
            if pg.key.get_mods() and pg.KMOD_CTRL and event.key == pg.K_q:
                crashed = True
    
    for row in range(mapwidth):
        for column in range(mapheight):
            position=(row*tilesize,column*tilesize, tilesize,tilesize)
            pg.draw.rect(gameDisplay,tilemap2[row][column],position)
    ## shapes on thw screen 
    ## Rectangural
    positon=(100,50,20,20)
    width=50
    pg.draw.rect(gameDisplay,black,positon,width)
    
    positon=(50,300,200,20)
    width=0
    pg.draw.rect(gameDisplay,black,positon,width)
    
    positon=(500,60,100,100)
    width=0
    pg.draw.rect(gameDisplay,black,positon,width)
    #Cicle
    center=(500,500)
    width=0
    radius=100
    pg.draw.circle(gameDisplay,black,center,radius,width)
    
    
    
    pg.display.update()
    #frame per second
    FramesPerSecond=60
    clock.tick(FramesPerSecond)
    
pg.quit()
quit()
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame as pg


pg.init()


###Screen Resolution
screen_width=1000
screen_height=550
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

## MOSAIC

tilesize=10
mapwidth=int(screen_width/tilesize)
print(mapwidth)
mapheight=int(screen_height/tilesize)
print(mapheight)
GameResolutionWithTiles=[mapwidth*tilesize,mapheight*tilesize]
gameDisplay=pg.display.set_mode(GameResolutionWithTiles,ScreenFlags)


#border_tiles_H=[0,1,5,6,mapheight-7,mapheight-6,mapheight-2,mapheight-1]
#border_tiles_V=[0,1,5,6,mapwidth-7,mapwidth-6,mapwidth-2,mapwidth-1]

border_tiles_H=[0,1,mapheight-2,mapheight-1]
border_tiles_V=[0,1,mapwidth-2,mapwidth-1]


tilemap=[[red for y in range(mapheight)] for x in range(mapwidth)]

for row in range(mapwidth):
    for column in range(mapheight):
        if row in border_tiles_V:
            tilemap[row][column]=red
        elif column in border_tiles_H:
            tilemap[row][column]=red
        else:
            tilemap[row][column]=green
        

## Palyer's Avatar
#load image
DDbaby=pg.image.load("shrek1.png").convert_alpha()
#resizing palyer's image
DDbaby=pg.transform.scale(DDbaby,(50,50))
#initial potision
DDposition=[2,2]        
        
crashed= False
while not crashed:
    #list of events per frame per second
    
    ### MAP
    for row in range(mapwidth):
        for column in range(mapheight):
            position=(row*tilesize,column*tilesize, tilesize,tilesize)
            pg.draw.rect(gameDisplay,tilemap[row][column],position)        
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
    center=(600,400)
    width=0
    radius=100
    pg.draw.circle(gameDisplay,black,center,radius,width)
    
    ## Palyer's Avatar
    #dispaly on game's surface
    gameDisplay.blit(DDbaby,(DDposition[0]*tilesize,DDposition[1]*tilesize)) 
    
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
                
            # moving to the right until the end of map
            if event.key == pg.K_RIGHT and DDposition[0]<mapwidth-tilesize/2-2:
                DDposition[0]+=1
            # moving to the left until the end of map
            if event.key == pg.K_LEFT and DDposition[0]>2:
                DDposition[0]-=1
            # moving to the up until the end of map
            if event.key == pg.K_UP and DDposition[1]>2:
                DDposition[1]-=1
            # moving to the down until the end of map
            if event.key == pg.K_DOWN and DDposition[1]<mapheight-tilesize/2-2:
                DDposition[1]+=1

                
    gameDisplay.blit(DDbaby,(DDposition[0]*tilesize,DDposition[1]*tilesize))
    
    pg.display.update()
    #frame per second
    FramesPerSecond=100
    clock.tick(FramesPerSecond)
    

    
pg.quit()
quit()
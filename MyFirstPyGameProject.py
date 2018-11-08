# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame as pg
import os


pg.init()



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

###Screen Resolution/Game Surface
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


## MOSAIC

tilesize=10
mapwidth=int(screen_width/tilesize)
#print(mapwidth)
mapheight=int(screen_height/tilesize)
#print(mapheight)
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
            tilemap[row][column]=pink
        

## Palyer's Avatar
            
#Avatar parameters and starting position
Avatar_x=250
Avatar_y=250
#initial potision
Avatar_position=[Avatar_x,Avatar_y]   
#Avatar size
Avatar_width=64
Avatar_height=64
#Avatar speed
Avatar_speed=2

Jumping= False
Jump_step_max=10
Jump_step=Jump_step_max

### Avatar Image
image_path="Giannis"

##Walking

Right_images=["sprite_Giannis00","sprite_Giannis01","sprite_Giannis02",
              "sprite_Giannis03","sprite_Giannis04","sprite_Giannis05",
              "sprite_Giannis06","sprite_Giannis07","sprite_Giannis08",
              "sprite_Giannis09","sprite_Giannis10","sprite_Giannis11",
              "sprite_Giannis12","sprite_Giannis13","sprite_Giannis14",
              "sprite_Giannis15","sprite_Giannis16","sprite_Giannis17",
              "sprite_Giannis18","sprite_Giannis19","sprite_Giannis20",
              "sprite_Giannis21","sprite_Giannis22","sprite_Giannis23",
              "sprite_Giannis24","sprite_Giannis25","sprite_Giannis26",
              "sprite_Giannis27","sprite_Giannis28","sprite_Giannis29",
              "sprite_Giannis30"]

Walking_images_path=os.path.join(image_path,"GiannisWalking")
Right_images_path=[os.path.join(Walking_images_path,i+".png") for i in Right_images]

Walking_Right=[pg.image.load(i) for i in Right_images_path]
Walking_Left=[pg.transform.flip(i,True,False) for i in Walking_Right]


Left=False
Right=False
Frond=False
Back=False
WalkCount=0

##Waving
## One Hand
Waving_images=["sprite_GiannisWaving0","sprite_GiannisWaving1",
               "sprite_GiannisWaving2","sprite_GiannisWaving3",
               "sprite_GiannisWaving4",
               "sprite_GiannisWaving5","sprite_GiannisWaving6"]

Waving_images_folder_path=os.path.join(image_path,"GiannisWaving")
Waving_images_path=[os.path.join(Waving_images_folder_path,i+".png") for i in Waving_images]
Waving=[pg.image.load(i) for i in Waving_images_path]
## Two Hand
Waving_2Hands_images=["sprite_GiannisWavingBothHAnds0",
                       "sprite_GiannisWavingBothHAnds1",
                       "sprite_GiannisWavingBothHAnds2",
                       "sprite_GiannisWavingBothHAnds3",
                       "sprite_GiannisWavingBothHAnds4",
                       "sprite_GiannisWavingBothHAnds5",
                       "sprite_GiannisWavingBothHAnds6",
                       "sprite_GiannisWavingBothHAnds7",
                       "sprite_GiannisWavingBothHAnds8"]

Waving_2Hands_images_folder_path=os.path.join(image_path,"GiannisWavingBOthHAnds")
Waving_2Hands_images_path=[os.path.join(Waving_2Hands_images_folder_path,i+".png") for i in Waving_2Hands_images]
Waving_2Hands=[pg.image.load(i) for i in Waving_2Hands_images_path]

## Avatar Frond
Frond_images=["GiannisStanding"]
Frond_images_folder_path=os.path.join(image_path,"GiannisFrond")
Frond_images_path=[os.path.join(Frond_images_folder_path,i+".png") for i in Frond_images]
Face=[pg.image.load(i) for i in Frond_images_path]

## Avatar Back
Back_images=["GiannisBack"]
Back_images_folder_path=os.path.join(image_path,"GiannisBack")
Back_images_path=[os.path.join(Back_images_folder_path,i+".png") for i in Back_images]
BackHead=[pg.image.load(i) for i in Back_images_path]


def redrawGameWindow():
    global WalkCount  
    if WalkCount+1>31:
        WalkCount=0
    if Right:
        gameDisplay.blit(Walking_Right[WalkCount],(Avatar_position[0],Avatar_position[1]))
        WalkCount+=1
    elif Left:
        gameDisplay.blit(Walking_Left[WalkCount],(Avatar_position[0],Avatar_position[1]))
        WalkCount+=1
    elif Back:
        gameDisplay.blit(BackHead[0],(Avatar_position[0],Avatar_position[1]))    
    else:
        gameDisplay.blit(Face[0],(Avatar_position[0],Avatar_position[1]))
    pg.display.update()


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
    

    
    #Quiting the game
    for event in pg.event.get():
        
        #### QUITING GAME
        
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
                
    ### Moving the avatar
    ## Moving Keys
    moving_keys=pg.key.get_pressed()
    # moving left and right
    if moving_keys[pg.K_RIGHT] and Avatar_position[0]<screen_width-Avatar_speed-50:
        Avatar_position[0]+=Avatar_speed
        Left=False
        Right=True
        Frond=False
        Back=False
    elif moving_keys[pg.K_LEFT] and Avatar_position[0]>Avatar_speed:
        Avatar_position[0]-=Avatar_speed
        Left=True
        Right=False
        Frond=False
        Back=False
    else:
        Left=False
        Right=False
        Frond=True
        Back=False
        
        
        
    #moving up and down and jumping
    if not Jumping:
        if moving_keys[pg.K_UP] and Avatar_position[1]>0:
            Avatar_position[1]-=Avatar_speed
            Left=False
            Right=False
            Frond=False
            Back=True
        if moving_keys[pg.K_DOWN] and Avatar_position[1]<(screen_height-Avatar_height-Avatar_speed):
            Avatar_position[1]+=Avatar_speed
            Left=False
            Right=False
            Frond=True
            Back=False
        if moving_keys[pg.K_SPACE] and Avatar_position[1]>2*Jump_step_max**2:
            Jumping = True
            Left=False
            Right=False
            Frond=True
            Back=False
    if Jumping:
        counter=1
        if Jump_step>=-Jump_step_max :
            direction=1
            if Jump_step<0:
                direction=-1
            Avatar_position[1]-=(Jump_step**2)*0.5*direction
            Jump_step-=1
            counter+=1
        else:
            Jumping=False
            Jump_step=Jump_step_max


            

    
    #dispaly on game's surface           
    
    #frame per second
    FramesPerSecond=100
    clock.tick(FramesPerSecond)
    
    redrawGameWindow()
    
pg.quit()
quit()
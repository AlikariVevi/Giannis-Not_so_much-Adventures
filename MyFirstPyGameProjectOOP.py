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

#gameDisplay=pg.display.set_mode(GameResolution,ScreenFlags)

### Title of the game Window
pg.display.set_caption('Hello World!')


###Game Clock
clock=pg.time.Clock()


###############################################################################
###############           Background Images         ###########################
###############################################################################
tilesize=10
mapwidth=int(screen_width/tilesize)
#print(mapwidth)
mapheight=int(screen_height/tilesize)
#print(mapheight)pg.time.Clock
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
        


###############################################################################
###################           Avatar Images         ###########################
###############################################################################
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

###############################################################################
######################                               ##########################
######################             CLASSES           ##########################
######################                               ##########################
###############################################################################

###############################################################################
#######################            AVATARS           ##########################
###############################################################################
            
class Avatar():
    # Avatar position and size
    # The position and size are give as artibutes
    # while speed, jump, walking direction and count steps
    # are defaulted
    def __init__(self, x, y, width, height):
        #initial potision
        self.x = x
        self.y = y
        #Avatar's size
        self.width = width
        self.height = height
        #Avatar's speed
        self.speed = 2
        #Avatar's jumping parameters
        self.jumping = False
        self.jump_step_max = 8
        self.jump_step = self.jump_step_max
        #Avatar's walking parameters
        self.Free_to_move = True
        self.left = False
        self.right = False
        self.frond = False
        self.back = False
        self.WalkCount = 0
        self.StandingCount = 0
        
        self.actionTime=timeUnit()
        
    def movement(self):
        ## Moving Keys
        moving_keys=pg.key.get_pressed()
        
        # moving left and right
        if moving_keys[pg.K_RIGHT] and self.x < screen_width - self.speed - 50:
            self.x += self.speed
            self.left = False
            self.right = True
            self.frond = False
            self.back = False
        elif moving_keys[pg.K_LEFT] and self.x > self.speed:
            self.x-=self.speed
            self.left = True
            self.right = False
            self.frond = False
            self.back = False
        else:
            # Doing nothing
            self.left = False
            self.right = False
            self.frond = True
            self.back = False
            self.WalkCount=0
        #moving up and down and jumping
        if not self.jumping:
            if moving_keys[pg.K_UP] and self.y > 0:
                self.y-=self.speed
                self.left = False
                self.right = False
                self.frond = False
                self.back = True 
            if moving_keys[pg.K_DOWN] and self.y < (screen_height - self.height - self.speed):
                self.y+=self.speed
                self.left = False
                self.right = False
                self.frond = True
                self.back = False
            if moving_keys[pg.K_SPACE] and player.y > 2*player.jump_step_max**2:
                self.jumping = True
                self.left = False
                self.right = False
                self.frond = True
                self.back = False
        else:
            self.Jump()

                
    def Jump(self):
        if self.jumping == True:
            if self.jump_step >= -self.jump_step_max :
                direction = 1
                if self.jump_step < 0:
                    direction = -1
                self.y -= (self.jump_step**2)*0.5*direction
                self.jump_step -= 1
            else:
                self.jumping = False
                self.jump_step = self.jump_step_max
            
    def WaitingSequence(self):
        waiting=1000 # msec
        if self.actionTime.waitingAct(waiting):
            if self.StandingCount+1>7:
                self.StandingCount=0
            else:
                #dispalying action
                gameDisplay.blit(Waving[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1 
        elif self.actionTime.waitingAct(2*waiting):
            if self.StandingCount+1>9:
                self.StandingCount=0
            else:
                #dispalying action
                gameDisplay.blit(Waving_2Hands[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1
        elif self.actionTime.waitingAct(3*waiting):
            self.jumping = True
            if self.StandingCount+1>9:
                self.StandingCount=0
                self.jumping = False
            else:
                self.Jump()
                #dispalying action
                gameDisplay.blit(Waving_2Hands[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1
                                            
        else:
            #dispalying action
            gameDisplay.blit(Face[0],(self.x,self.y))        
            
        
    def drawAvatar(self, gameDisplay):
        #walking image number of frames
        if self.WalkCount+1>31:
            self.WalkCount=0
        # standing image number of frames
        if self.StandingCount+1>7:
            self.StandingCount=0
        if self.right:
            # count time after this action
            self.actionTime=timeUnit()
            #dispalying action
            gameDisplay.blit(Walking_Right[self.WalkCount],(self.x,self.y))
            self.WalkCount+=1
        elif self.left:
            # count time after this action
            self.actionTime=timeUnit()
            #dispalying action
            gameDisplay.blit(Walking_Left[self.WalkCount],(self.x,self.y))
            self.WalkCount+=1
        elif self.back:
            # count time after this action
            self.actionTime=timeUnit()
            #dispalying action
            gameDisplay.blit(BackHead[0],(self.x,self.y))    
        else:
            if self.jumping:
                # count time after this action
                self.actionTime=timeUnit()
                #dispalying action
                gameDisplay.blit(Face[0],(self.x,self.y))
            else:
                self.WaitingSequence()
                
                
  
    

###############################################################################
########################          WALLS             ###########################
###############################################################################

####### type_of_wall takes arguments the shapes of pygame.draw modulw
class Wall():
    
    def rectWall(self, x, y, width=10, height=10, color=black, outline=0):
        #Wall's position (top left)
        self.x = x
        self.y = y
        #Wall's size
        self.width = width
        self.height = height
        self.color = color
        self.outline = outline
            
        self.position=(self.x, self.y, self.width, self.height)
        pg.draw.rect(gameDisplay, self.color, self.position, self.outline)
                
    def CircleWall(self, center_x, center_y, radius=1, color=black, outline=0):
        #Wall's position (top left)
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        #Wall's size
        self.color = color
        self.outline = outline
        
        self.position=(self.center_x, self.center_y)
        pg.draw.circle(gameDisplay, self.color, self.position, self.radius, self.outline)
            
###############################################################################
#######################           Time Unit           #########################
###############################################################################            
            
class timeUnit():
    def __init__(self ):
        self.last = pg.time.get_ticks()

    def waitingAct(self, waiting = 3000):
        stop = 3*waiting
        now = pg.time.get_ticks()
        if now - self.last >= waiting and now - self.last <stop:
            return True
        else:
            return False

###############################################################################
###############################################################################
######################3###        FUNCTIONS         ###########################
###############################################################################
###############################################################################
                
###############################################################################
##################         Draw Avatar on Surface       #######################
###############################################################################
  
def redrawGameWindow(avatar):
        avatar.drawAvatar(gameDisplay)
        pg.display.update()
        
###############################################################################
#######################         Quit the Game         #########################
###############################################################################
        
def quitGame(crashed=False):
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
    return crashed         

###############################################################################
##########################          Background          #######################
###############################################################################

def drawBackground():
        ### MAP
    for row in range(mapwidth):
        for column in range(mapheight):
            position=(row*tilesize,column*tilesize, tilesize,tilesize)
            pg.draw.rect(gameDisplay,tilemap[row][column],position)        
    ## shapes on thw screen 
    ## Rectangural
    walls=[]
    walls.append(Wall().rectWall(100, 50, 20, 20, black, 50))
    
    Wall().rectWall(50,300,200,20, black)
    
    Wall().rectWall(500,60,100,100, black)
    #Cicle
    Wall().CircleWall(center_x=600,center_y=400,radius=100)
    
###############################################################################
##########################          Collision           #######################
###############################################################################

def Collision(object1,object2):
    for w in object2:
        if object1.x == object2[x].x:
            return False
        else:
            return True
        
###############################################################################
#######################                                 #######################
#######################              PLAYER             #######################
#######################                                 #######################
###############################################################################
player = Avatar(250,250,32,32)

###############################################################################
#######################                                 #######################
#######################         Games Main Loop         #######################
#######################                                 #######################
###############################################################################
while not quitGame():
    quitGame()
    
    #Background
    drawBackground()
    ### Moving the avatar
    
    player.movement()
    
    #frame per second
    FramesPerSecond=100
    clock.tick(FramesPerSecond)
    
    redrawGameWindow(player)
    
pg.quit()
quit()
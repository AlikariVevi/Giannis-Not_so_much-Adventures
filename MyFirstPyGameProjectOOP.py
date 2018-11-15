# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pygame as pg
import os


pg.init()


font = pg.font.SysFont("comicsansms", 24)
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

earth=0
grass=1

ground={
        earth : pg.image.load("Ground Sprite Pack\ground3.png"),
        #grass : pg.image.load("Ground Sprite Pack\\LGrass2.png")
        }

gallery = pg.image.load("Ground Sprite Pack\gallery.png")

tilemap=[[earth for y in range(mapheight)] for x in range(mapwidth)]

#
#for row in range(mapwidth):
#    for column in range(mapheight):
#        if row in border_tiles_V:
#            tilemap[row][column]=red
#        elif column in border_tiles_H:
#            tilemap[row][column]=red
#        else:
#            tilemap[row][column]=pink

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
            
class Avatar(pg.sprite.Sprite):
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
        self.stand = False
        self.WalkCount = 0
        self.StandingCount = 0
    
        ## Avatar is inside buildins
        self.inside = False
      
        
        self.actionTime=timeUnit()
        #Avatar's boundaries
        # the have to be renew in every movement
        # intire image of avatar
#       self.hitbox=pg.Rect((self.x+4), self.y, 20, 32)
        # just the legs
        self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
        
        
    def DoNothing(self):
        self.left = False
        self.right = False
        self.frond = False
        self.back = False
        self.stand = True
        self.WalkCount=0
        self.Free_to_move = True
    def DoRight(self):
        self.left = False
        self.right = True
        self.frond = False
        self.back = False
        self.stand = False
        self.Free_to_move = True
    def DoLeft(self):
        self.left = True
        self.right = False
        self.frond = False
        self.back = False
        self.stand = False
        self.Free_to_move = True
    def DoBack(self):
        self.left = False
        self.right = False
        self.frond = False
        self.back = True
        self.stand = False
        self.Free_to_move = True
    def DoFace(self):
        self.left = False
        self.right = False
        self.frond = True
        self.back = False 
        self.stand = False
        
        
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
        waiting=6000 # msec
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
            else:
                self.Jump()
                #dispalying action
                gameDisplay.blit(Waving_2Hands[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1
                                            
        else:
            #dispalying action
            gameDisplay.blit(Face[0],(self.x,self.y))        
            
    
        
    def movement(self):
        ## Moving Keys
        moving_keys=pg.key.get_pressed()
        #self.Free_to_move moving left and right
        if self.Free_to_move:
            if moving_keys[pg.K_RIGHT]:
                self.x += self.speed
                self.DoRight()
#                self.hitbox=pg.Rect((self.x+4), self.y, 20, 32)
                self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
            elif moving_keys[pg.K_LEFT]:
                self.x-=self.speed
#                self.hitbox=pg.Rect((self.x+4), self.y, 20, 32)
                self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                self.DoLeft()
            else:
                self.DoNothing()
           
            #moving up and down and jumping
            if not self.jumping:
                if moving_keys[pg.K_UP]:
                    self.y-=self.speed
#                    self.hitbox=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                    self.DoBack()
                if moving_keys[pg.K_DOWN]:
                    self.y+=self.speed
#                    self.hitbox=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                    self.DoFace()
                if moving_keys[pg.K_SPACE] and player.y > 2*player.jump_step_max**2:
#                    self.hitbox=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                    self.jumping = True
                    self.DoFace()
            else:
                self.Jump()

               
           ################################
           ###    Checking for Walls    ###
           ################################
            for wall in walls:
                if self.hitbox.colliderect(wall):
                    self.Free_to_move = False
                    if moving_keys[pg.K_RIGHT]:
                        self.Free_to_move = False
                        self.TextMessage("I can't go there", self.x, self.y)
                        self.DoNothing()
                        clock.tick(2000)
                    if moving_keys[pg.K_LEFT]:
                        self.Free_to_move = False
                        self.TextMessage("I can't go there", self.x, self.y)
                        self.DoNothing()
                        clock.tick(2000)
                    if moving_keys[pg.K_UP]:
                        self.Free_to_move = False
                        self.TextMessage("I can't go there", self.x, self.y)
                        self.DoNothing()
                        clock.tick(2000)
                    if moving_keys[pg.K_DOWN]:
                        self.Free_to_move = False
                        self.TextMessage("I can't go there", self.x, self.y)
                        self.DoNothing()
                        clock.tick(2000)
#            draw avatar's hitbox            
#            pg.draw.rect(gameDisplay, red, self.hitbox,2)      
            
           ####################################
           ###    Checking for Buildings    ###
           ####################################
            for building in BuildingsSurface:
                    if self.hitbox.colliderect(building):
                        self.jumping = False
                        self.inside = True
                    else:
                        self.inside = False
                        

    def drawAvatar(self, gameDisplay):
        #walking image number of frames
        if self.WalkCount+1>31:
            self.WalkCount=0
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
        elif self.frond:
                # count time after this action
            self.actionTime=timeUnit()
                #dispalying action
            gameDisplay.blit(Face[0],(self.x,self.y))
        else:
            self.WaitingSequence()
        #Avatar's boundaries
#        self.hitbox=(self.x+4, self.y, 20, 32)
#        pg.draw.rect(gameDisplay,black, self.hitbox,2)
                
    def TextMessage(self, message, x, y,color = black):
        self.message = message
        self.color = color
        self.text = font.render(self.message, True, self.color)
        self.box=pg.Rect(self.x, self.y-self.text.get_height(),self.text.get_width(),self.text.get_height())
        pg.draw.rect(gameDisplay, white, self.box)
        gameDisplay.blit(self.text,(x,y-self.text.get_height()))
        gameDisplay.blit(Face[0],(self.x,self.y))
        pg.display.flip()
        
        
            ###############################################################
    ##############      Action inside Buildings       #############
    ###############################################################
    

                
            

###############################################################################
########################          WALLS             ###########################
###############################################################################

####### type_of_wall takes arguments the shapes of pygame.draw modulw
class Wall(pg.Rect):
    
    def __init__(self, x, y, width, height):
        pg.Rect.__init__(self, x, y, width, height)
        #Wall's position (top left)
        self.x = x
        self.y = y
        #Wall's size
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        walls.append(self)
        
class rectWall(Wall):
    def __init__(self, x, y, width, height):
        Wall.__init__ (self, x, y, width, height)
        self.hitbox = self.rect
                
class CircleWall(Wall):
    def __init__(self, x, y, radius=10, width=10, height=10):
        Wall.__init__ (self, x, y, width=10, height=10)
        self.radius = radius
        self.hitbox=pg.Rect(self.x, self.y, 2*self.radius, 2*self.radius)
        self.center = (self.x + self.radius, self.y + self.radius) 
        walls.append(self.hitbox)
#        pg.draw.rect(gameDisplay, red, self.hitbox,2)


class Door(pg.Rect):
    
    def __init__(self, x, y, width, length):
        self.width = width
        self.length = length
        if self.width < self.length:
            pg.Rect.__init__(self, x, y, self.width, self.length)
            self.hitbox = pg.Rect(self.x, self.y, self.width, self.length)
        else:
            pg.Rect.__init__(self, x, y, self.length, self.width)
            self.hitbox = pg.Rect(self.x, self.y, self.length, self.width)
        doors.append(self)
    
class Building(pg.Rect):
    
    def __init__(self, x_begin, y_begin, x_end, y_end, door):
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin
        self.y_end = y_end
        self.width = x_end - x_begin
        self.height = y_end - y_begin
        pg.Rect.__init__(self, x_begin, y_begin, self.width, self.height)
        self.WallWidth = 10
        self.door = door
        self.buildingWalls=[]
        
        paintingBuilding=pg.Rect(x_begin, y_begin, self.width, self.height)
        BuildingsSurface.append(paintingBuilding)
        
        
        ### The Door is on the LEft side
        if self.door.x == self.x_begin:
            DoorWallLenght1 = self.door.y - self.y_begin
            DoorWallLenght2 = self.y_end - (self.door.y + self.door.length)
            #Left
            rectWall(self.x_begin, self.y_begin, self.WallWidth,  DoorWallLenght1)
            rectWall(self.x_begin, self.door.y + self.door.length , self.WallWidth, DoorWallLenght2)
            #Τop
            rectWall(self.x_begin, self.y_begin, self.width, self.WallWidth)
            #Bottom
            rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
            #Right
            rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)

        
        
                ### The Door is on the Right side
        if self.door.x == (self.x_end - self.WallWidth):
            DoorWallLenght1 = self.door.y - self.y_begin
            DoorWallLenght2 = self.y_end - (self.door.y + self.door.length)
            #Left
            rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
            #Τop
            rectWall(self.x_begin, self.y_begin, self.width, self.WallWidth)
            #Bottom
            rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
            #Right
            rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, DoorWallLenght1)
            rectWall(self.x_end - self.WallWidth, self.door.y + self.door.length , self.WallWidth, DoorWallLenght2)
            
                        ### The Door is on the Top side
        if self.door.y == self.y_begin:
            DoorWallLenght2 = self.x_end - (self.door.x + self.door.length)
            #Left
            rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
            #Τop
            rectWall(self.x_begin, self.y_begin , self.door.length, self.WallWidth)
            rectWall(self.door.x + self.door.length, self.y_begin, DoorWallLenght2 , self.WallWidth)
            #Bottom
            rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
            #Right
            rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)


                        ### The Door is on the Bottom side
        if self.door.y == self.y_end:
            DoorWallLenght2 = self.x_end - (self.door.x + self.door.length)
            #Left
            wall1=rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
            pg.draw.rect(gameDisplay, red, wall1.rect)
            #Τop
            wall2=rectWall(self.x_begin, self.y_begin , self.width, self.WallWidth)
            pg.draw.rect(gameDisplay, red, wall2.rect)
            #Bottom
            wall4=rectWall(self.x_begin, self.y_end, self.door.length, self.WallWidth)
            pg.draw.rect(gameDisplay, red, wall4.rect)
            wall3=rectWall(self.door.x + self.door.length, self.y_end, DoorWallLenght2 , self.WallWidth)
            pg.draw.rect(gameDisplay, red, wall3.rect)
            #Right
            wall5=rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)
            pg.draw.rect(gameDisplay, red, wall5.rect)
            

###############################################################################
#######################             HITBOX            #########################
################################  ###############################################
        
class HitBox(pg.Rect):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
           
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
#            # ESCAPE --> Quit
            if event.key == pg.K_ESCAPE:
                crashed = True
            # CTRL+Q -->Quit
            if pg.key.get_mods() and pg.KMOD_CTRL and event.key == pg.K_q:
                crashed = True
    return crashed     

###############################################################################
#########################         Quit Scene         ##########################
###############################################################################
        
def quitScene():
        #Quiting Scene
    for event in pg.event.get(): 
        if event.type == pg.KEYDOWN:
            # ESCAPE --> Back to previous scene
            if event.key ==pg.K_RETURN:
                return True
    return False

                      

###############################################################################
##########################          Background          #######################
###############################################################################
doors=[]
screenborders={}
def drawBackground():
        ### MAP
    for row in range(mapwidth):
        for column in range(mapheight):
            position=(row*tilesize,column*tilesize, tilesize,tilesize)
            gameDisplay.blit(ground[tilemap[row][column]],position)   
    
    #screen borders
    ScreenBorders()
          
    ### Painting's Gallery        
    gameDisplay.blit(gallery,(500,60))
    Building(548,108,652,202,Door(548,145,10,30))

    

def ScreenBorders(x_begin = 0, y_begin = 0, x_end = screen_width, y_end = screen_height, width = 10):
        #screen borders
    #top
    rectWall(x_begin,y_begin,x_end,width)
    screenborders["topBorder"]=rectWall(x_begin,y_begin,x_end,width)
    #right
    rectWall(x_end,y_begin,width,y_end)
    screenborders["rightBorder"]=rectWall(x_end,y_begin,width,y_end)
    #bottom
    rectWall(x_begin,y_end,x_end,width)
    screenborders["bottomBorder"]=rectWall(x_begin,y_end,x_end,width)
    #left
    rectWall(x_begin,y_begin,width,y_end)
    screenborders["leftBorder"]=rectWall(x_begin,y_begin,width,y_end)
    
    
    
###############################################################################
########################      Action inside Buildings       ###################
###############################################################################
    
def Action_Inside_Building(player):
    if player.inside == True and player.Free_to_move == False:
        return True
    else:
        return False
         
              

###############################################################################
##########################          Draw Walls          #######################
###############################################################################
walls=[]
BuildingsSurface=[]
PaintingBuildingWalls=[]


    #return walls
###############################################################################
##################             Text Message             #######################
###############################################################################   

def TextMessage(message, x, y,color = black):
    text = font.render(message, True, color)
    box=pg.Rect(x,y-text.get_height(),text.get_width(),text.get_height())
    pg.draw.rect(gameDisplay, white, box)
    gameDisplay.blit(text,(x,y-text.get_height()))
    pg.display.flip() 
    return text


###############################################################################
#######################                                 #######################
#######################              PLAYER             #######################
#######################                                 #######################
###############################################################################
player = Avatar(500,200,32,32)

###############################################################################
#######################                                 #######################
#######################         Games Main Loop         #######################
#######################                                 #######################
###############################################################################


while not quitGame():
    quitGame()
    
    if Action_Inside_Building(player):
        pg.display.flip()
        text = font.render("Hello", True,black)
        gameDisplay.fill(white)
        gameDisplay.blit(text,(320 , 240))

    else:
        #Background
        drawBackground()
        ### Moving the avatar
        
        player.movement()
        
        FramesPerSecond=100
       
        #frame per second
        
        clock.tick(FramesPerSecond)
        redrawGameWindow(player)
        
        
 
    
pg.quit()
quit()
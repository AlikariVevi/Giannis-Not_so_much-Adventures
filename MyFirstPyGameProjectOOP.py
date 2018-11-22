# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import pygame as pg
#import py2exe

import os, random


global red, green, blue, darkBlue, white, black, pink
###Screen Resolution/Game Surface
global screen_width, screen_height

screen_width=1000 
screen_height=550
###Colors RGB code 0-255
    
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
gold = (255,215,0)
saddlebrown = (139,69,19)
LoseScreenColor = (153,76,0)
HelloScreenColor = (128,128,128)


###############################################
##########    Intializing list    #############
###############################################
doors = []
screenborders = {}

walls = []
BuildingsSurface = []
PaintingBuildingWalls = []
Bullets_x = []
Bullets_y = []
Bullets = []

Vamps = []
Werewolfs = []
VampsANDWerewolfs = []

###############################################################################
#################           Buildings Images         ##########################
###############################################################################

gallery = pg.image.load("Ground Sprite Pack\gallery.png")

GiannisHome = pg.image.load("Ground Sprite Pack\GiannisHome.png")

###############################################################################
###################           Avatar Images         ###########################
###############################################################################

###############################################################################
###################              Player             ###########################
###############################################################################
image_path="Giannis"

##Walking

Right_images=["sprite_Giannis10","sprite_Giannis11",
              "sprite_Giannis12","sprite_Giannis13","sprite_Giannis14",
              "sprite_Giannis15","sprite_Giannis16","sprite_Giannis17",
              "sprite_Giannis18","sprite_Giannis19","sprite_Giannis20",
              "sprite_Giannis21","sprite_Giannis22","sprite_Giannis23",
              "sprite_Giannis24","sprite_Giannis25","sprite_Giannis26",
              "sprite_Giannis27","sprite_Giannis28","sprite_Giannis29",
              "sprite_Giannis30","sprite_Giannis00","sprite_Giannis01","sprite_Giannis02",
              "sprite_Giannis03","sprite_Giannis04","sprite_Giannis05",
              "sprite_Giannis06","sprite_Giannis07","sprite_Giannis08",
              "sprite_Giannis09"]



    
Walking_images_path=os.path.join(image_path,"GiannisWalking")
Right_images_path=[os.path.join(Walking_images_path,i+".png") for i in Right_images]

Walking_Right=[pg.image.load(i) for i in Right_images_path]
Walking_Left=[pg.transform.flip(i,True,False) for i in Walking_Right]

Bigger_Walking_Right_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Right]
Bigger_Walking_Left_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Left]

##Waving
## One Hand
Waving_images=["sprite_GiannisWaving0","sprite_GiannisWaving1",
               "sprite_GiannisWaving2","sprite_GiannisWaving3",
               "sprite_GiannisWaving4",
               "sprite_GiannisWaving5","sprite_GiannisWaving6"]


Waving_images_folder_path=os.path.join(image_path,"GiannisWaving")
Waving_images_path=[os.path.join(Waving_images_folder_path,i+".png") for i in Waving_images]
Waving=[pg.image.load(i) for i in Waving_images_path]

Bigger_Waving_400 = [pg.transform.scale(im,(400,400)) for im in Waving]
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

Bigger_Waving_2Hands_400 = [pg.transform.scale(im,(400,400)) for im in Waving_2Hands]

## Avatar Frond
Frond_images=["GiannisStanding"]
Frond_images_folder_path=os.path.join(image_path,"GiannisFrond")
Frond_images_path=[os.path.join(Frond_images_folder_path,i+".png") for i in Frond_images]
Face=[pg.image.load(i) for i in Frond_images_path]

Bigger_Frond_400 = [pg.transform.scale(im,(400,400)) for im in Face]

## Avatar Back
Back_images=["GiannisBack"]
Back_images_folder_path=os.path.join(image_path,"GiannisBack")
Back_images_path=[os.path.join(Back_images_folder_path,i+".png") for i in Back_images]
BackHead=[pg.image.load(i) for i in Back_images_path]

Bigger_BackHead_400 = [pg.transform.scale(im,(400,400)) for im in BackHead]

Falling_Down_images =["sprite_Giannis_Falling_Beaten0","sprite_Giannis_Falling_Beaten1",
                      "sprite_Giannis_Falling_Beaten2","sprite_Giannis_Falling_Beaten3",
                      "sprite_Giannis_Falling_Beaten4","sprite_Giannis_Falling_Beaten5",
                      "sprite_Giannis_Falling_Beaten6","sprite_Giannis_Falling_Beaten7",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8","sprite_Giannis_Falling_Beaten8",
                      "sprite_Giannis_Falling_Beaten8"]

Falling_Down_images_folder_path=os.path.join(image_path,"Giannis_Falling_Beaten")
Falling_Down_images_path=[os.path.join(Falling_Down_images_folder_path,i+".png") for i in Falling_Down_images]
Falling_Down=[pg.image.load(i) for i in Waving_2Hands_images_path]

Falling_Down_Left=[pg.image.load(i) for i in Falling_Down_images_path]
Falling_Down_Right=[pg.transform.flip(i,True,False) for i in Falling_Down_Left]

Bigger_Falling_Down_Left_400 = [pg.transform.scale(im,(400,400)) for im in Falling_Down_Left]
Bigger_Falling_Down_Right_400 = [pg.transform.scale(im,(400,400)) for im in Falling_Down_Right]


Dead_Images = ["sprite_Giannis_Vampire_Kill" , "sprite_Giannis_Werewolf_Kill"]

Dead_Images_path=[os.path.join(image_path,i+".png") for i in Dead_Images]

Giannis_Dead_Left = [pg.image.load(i) for i in Dead_Images_path] 
Giannis_Dead_Right = [pg.transform.flip(i,True,False) for i in Giannis_Dead_Left] 

Bigger_Giannis_Dead_Left_400 = [pg.transform.scale(im,(400,400)) for im in Giannis_Dead_Left ]
Bigger_Giannis_Dead_Right_400 = [pg.transform.scale(im,(400,400)) for im in Giannis_Dead_Right]


############## BEATEN ######################
Right_images_Beaten=["sprite_Giannis_Beaten10","sprite_Giannis_Beaten11",
              "sprite_Giannis_Beaten12","sprite_Giannis_Beaten13",
              "sprite_Giannis_Beaten14","sprite_Giannis_Beaten15","sprite_Giannis_Beaten16",
              "sprite_Giannis_Beaten17","sprite_Giannis_Beaten18","sprite_Giannis_Beaten19",
              "sprite_Giannis_Beaten20","sprite_Giannis_Beaten21","sprite_Giannis_Beaten22",
              "sprite_Giannis_Beaten23",
              "sprite_Giannis_Beaten24","sprite_Giannis_Beaten25","sprite_Giannis_Beaten26",
              "sprite_Giannis_Beaten27","sprite_Giannis_Beaten28","sprite_Giannis_Beaten29",
              "sprite_Giannis_Beaten30","sprite_Giannis_Beaten00","sprite_Giannis_Beaten01",
              "sprite_Giannis_Beaten02",
              "sprite_Giannis_Beaten03","sprite_Giannis_Beaten04","sprite_Giannis_Beaten05",
              "sprite_Giannis_Beaten06","sprite_Giannis_Beaten07","sprite_Giannis_Beaten08",
              "sprite_Giannis_Beaten09"]



    
Walking_images_Beaten_path=os.path.join(image_path,"GiannisWalking_Beaten")
Right_images_Beaten_path=[os.path.join(Walking_images_Beaten_path,i+".png") for i in Right_images_Beaten]

Walking_Right_Beaten=[pg.image.load(i) for i in Right_images_Beaten_path]
Walking_Left_Beaten=[pg.transform.flip(i,True,False) for i in Walking_Right_Beaten]

Bigger_Walking_Right_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Right_Beaten]
Bigger_Walking_Left_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Left_Beaten]

## Avatar Frond
Frond_images_Beaten=["GiannisStanding_Beaten"]
Frond_images_folder_Beaten_path=os.path.join(image_path,"GiannisFrond")
Frond_images_Beaten_path=[os.path.join(Frond_images_folder_Beaten_path,i+".png") for i in Frond_images_Beaten]
Face_Beaten=[pg.image.load(i) for i in Frond_images_Beaten_path]

Bigger_Frond_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in Face_Beaten]

## Avatar Back
Back_images_Beaten=["GiannisBack_Beaten"]
Back_images_folder_Beaten_path=os.path.join(image_path,"GiannisBack")
Back_images_Beaten_path=[os.path.join(Back_images_folder_Beaten_path,i+".png") for i in Back_images_Beaten]
BackHead_Beaten=[pg.image.load(i) for i in Back_images_Beaten_path]

Bigger_BackHead_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in BackHead_Beaten]
###############################################################################
###################              Vampire            ###########################
###############################################################################

image_path_Vamp="Vampire"

##Walking

Right_images_Vamp=["sprite_Vampire_Walking00","sprite_Vampire_Walking01",
                   "sprite_Vampire_Walking02","sprite_Vampire_Walking03",
                   "sprite_Vampire_Walking04","sprite_Vampire_Walking05",
                   "sprite_Vampire_Walking06","sprite_Vampire_Walking07",
                   "sprite_Vampire_Walking08","sprite_Vampire_Walking09",
                   "sprite_Vampire_Walking10","sprite_Vampire_Walking11",
                   "sprite_Vampire_Walking12","sprite_Vampire_Walking13",
                   "sprite_Vampire_Walking14","sprite_Vampire_Walking15",
                   "sprite_Vampire_Walking16","sprite_Vampire_Walking17",
                   "sprite_Vampire_Walking18","sprite_Vampire_Walking19",
                   "sprite_Vampire_Walking20","sprite_Vampire_Walking21",
                   "sprite_Vampire_Walking22","sprite_Vampire_Walking23",
                   "sprite_Vampire_Walking24","sprite_Vampire_Walking25",
                   "sprite_Vampire_Walking26","sprite_Vampire_Walking27"]

Walking_images_path_Vamp=os.path.join(image_path_Vamp,"VampireWalking")
Right_images_path_Vamp=[os.path.join(Walking_images_path_Vamp,i+".png") for i in Right_images_Vamp]

Walking_Right_Vamp=[pg.image.load(i) for i in Right_images_path_Vamp]
Walking_Left_Vamp=[pg.transform.flip(i,True,False) for i in Walking_Right_Vamp]

#Falling
Falling_images_Vamp=["sprite_Vampire_Falling0","sprite_Vampire_Falling1",
                   "sprite_Vampire_Falling2","sprite_Vampire_Falling3",
                   "sprite_Vampire_Falling4","sprite_Vampire_Falling5",
                   "sprite_Vampire_Falling6","sprite_Vampire_Falling7",
                   "sprite_Vampire_Falling8"]

for i in range(1000):
    Falling_images_Vamp.append("sprite_Vampire_Falling8")
Falling_images_path_Vamp=os.path.join(image_path_Vamp,"Vampire_Falling")
Falling_Right_images_path_Vamp=[os.path.join(Falling_images_path_Vamp,i+".png") for i in Falling_images_Vamp]

Falling_Right_Vamp=[pg.image.load(i) for i in Falling_Right_images_path_Vamp]
Falling_Left_Vamp=[pg.transform.flip(i,True,False) for i in Falling_Right_Vamp]


## Avatar Frond
Frond_images_Vamp=["Vampire_Frond"]
Frond_images_folder_path_Vamp=os.path.join(image_path_Vamp,"Vampire_Frond")
Frond_images_path_Vamp=[os.path.join(Frond_images_folder_path_Vamp+".png") for i in Frond_images_Vamp]
Face_Vamp=[pg.image.load(i) for i in Frond_images_path_Vamp]

Bigger_Frond_400_Vamp = [pg.transform.scale(im,(400,400)) for im in Face_Vamp]

Back_images_Vamp=["Vampire_Back"]
Back_images_folder_path_Vamp=os.path.join(image_path_Vamp,"Vampire_Back")
Back_images_path_Vamp=[os.path.join(Back_images_folder_path_Vamp+".png") for i in Back_images_Vamp]
Back_Vamp=[pg.image.load(i) for i in Back_images_path_Vamp]

Bigger_Back_400_Vamp = [pg.transform.scale(im,(400,400)) for im in Back_Vamp]

###############################################################################
###################             Werewolf            ###########################
###############################################################################

image_path_Wer="Werewolf"

##Walking

Right_images_Wer=["sprite_WereWolfWalking00","sprite_WereWolfWalking01",
                   "sprite_WereWolfWalking02","sprite_WereWolfWalking03",
                   "sprite_WereWolfWalking04","sprite_WereWolfWalking05",
                   "sprite_WereWolfWalking06","sprite_WereWolfWalking07",
                   "sprite_WereWolfWalking08","sprite_WereWolfWalking09",
                   "sprite_WereWolfWalking10","sprite_WereWolfWalking11",
                   "sprite_WereWolfWalking12","sprite_WereWolfWalking13",
                   "sprite_WereWolfWalking14","sprite_WereWolfWalking15",
                   "sprite_WereWolfWalking16","sprite_WereWolfWalking17",
                   "sprite_WereWolfWalking18","sprite_WereWolfWalking19",
                   "sprite_WereWolfWalking20","sprite_WereWolfWalking21",
                   "sprite_WereWolfWalking22","sprite_WereWolfWalking23",
                   "sprite_WereWolfWalking24","sprite_WereWolfWalking25",
                   "sprite_WereWolfWalking26","sprite_WereWolfWalking27",
                   "sprite_WereWolfWalking28","sprite_WereWolfWalking29",
                   "sprite_WereWolfWalking30"]

Walking_images_path_Wer=os.path.join(image_path_Wer,"WereWolfWalking")
Right_images_path_Wer=[os.path.join(Walking_images_path_Wer,i+".png") for i in Right_images_Wer]

Walking_Right_Wer=[pg.image.load(i) for i in Right_images_path_Wer]
Walking_Left_Wer=[pg.transform.flip(i,True,False) for i in Walking_Right_Wer]

#Falling
Falling_images_Wer=["sprite_WereWolf_Falling0","sprite_WereWolf_Falling1",
                   "sprite_WereWolf_Falling2","sprite_WereWolf_Falling3",
                   "sprite_WereWolf_Falling4","sprite_WereWolf_Falling5",
                   "sprite_WereWolf_Falling6","sprite_WereWolf_Falling7",
                   "sprite_WereWolf_Falling8"]

for i in range(1000):
    Falling_images_Wer.append("sprite_WereWolf_Falling8")

Falling_images_path_Wer=os.path.join(image_path_Wer,"sprite_WerwWolfFalling")
Falling_Right_images_path_Wer=[os.path.join(Falling_images_path_Wer,i+".png") for i in Falling_images_Wer]

Falling_Right_Wer=[pg.image.load(i) for i in Falling_Right_images_path_Wer]
Falling_Left_Wer=[pg.transform.flip(i,True,False) for i in Falling_Right_Wer]



## Avatar Frond
Frond_images_Wer=["Werewolf_Frond"]
Frond_images_folder_path_Wer = os.path.join(image_path_Wer,"Werewolf_Frond")
Frond_images_path_Wer=[os.path.join(Frond_images_folder_path_Wer+".png")]
Face_Wer=[pg.image.load(i) for i in Frond_images_path_Wer]

Bigger_Frond_400_Wer = [pg.transform.scale(im,(400,400)) for im in Face_Wer]

Back_images_Wer=["Werewolf_Back"]
Back_images_folder_path_Wer=os.path.join(image_path_Wer,"Werewolf_Back")
Back_images_path_Wer=[os.path.join(Back_images_folder_path_Wer+".png") for i in Back_images_Wer]
Back_Wer=[pg.image.load(i) for i in Back_images_path_Wer]

Bigger_Back_400_Wer = [pg.transform.scale(im,(400,400)) for im in Back_Wer]


###############################################################################
######################                               ##########################
######################             CLASSES           ##########################
######################                               ##########################
###############################################################################

###############################################################################
#######################            SCENES            ##########################
###############################################################################

class SceneBase:
    def __init__(self, flps = 10):
        self.next = self
        self.flps = flps
        self.crashed = False
    
    def ProcessInput(self, events):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

                    
        
class Introduction(SceneBase):
    def __init__(self, flps = 10):
        SceneBase.__init__(self, flps)
        
        
        
    
    def quitScene(self, event):
        if self.playButton.pushed:
            self.SwitchToScene(GameScene())

        if self.introButton.pushed:
            self.SwitchToScene(TitleScene())
            
        if self.controlsButton.pushed:
            self.SwitchToScene(Control_Keys())
            
        if self.Quit_Button.pushed:
            self.crashed = True
        
    
    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        self.screen.blit(Bigger_Frond_400[0],(600,100))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 100)
        self.text1 = self.welcomefont.render("Wellcome...", True,black)
        self.screen.blit(self.text1,(50,10))
        
        self.playButton = Button("Play...", 450, 240, black)
        self.introButton = Button("Introduction...", 450, 300,black)
        self.controlsButton = Button("Key Controls...", 450, 360, black)
        self.Quit_Button = Button("Quit...", 450, 420, black)
        
        self.playButton.DrawButton(screen)
        self.introButton.DrawButton(screen)
        self.controlsButton.DrawButton(screen)
        self.Quit_Button.DrawButton(screen)

        
class Control_Keys(SceneBase):
    def __init__(self, flps = 5):
        SceneBase.__init__(self, flps)
        
    
    def quitScene(self, event):
        if self.playButton.pushed:
            self.SwitchToScene(GameScene())

        if self.Back_Button.pushed:
            self.SwitchToScene(Introduction())
                  
    
    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        self.screen.blit(Bigger_Frond_400[0],(600,100))
        
        self.playButton = Button("Play", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        
        self.playButton.DrawButton(screen)
        self.Back_Button.DrawButton(screen)
        
        self.text1 = font.render("Right arrow : move right", True,black)
        self.text2 = font.render("Left arrow : move left", True,black)
        self.text3 = font.render("Up arrow : move up", True,black)
        self.text4 = font.render("Down arrow : move down", True,black)
        self.text5 = font.render("Space : Fire", True,black)
        self.text6 = font.render("Enter : next scene", True,black)
        
        self.texts = ((self.text1,(250,140)),(self.text2,(250,180)),(self.text3,(250,220)),
                      (self.text4,(250,260)),(self.text5,(250,300)),(self.text6,(250,340)))
        self.screen.blits(self.texts)
      
        
class TitleScene(SceneBase):
    def __init__(self, flps = 10):
        SceneBase.__init__(self, flps)
    
    def quitScene(self, event):
        if event[pg.K_RETURN] or self.Next_Button.pushed:
           self.SwitchToScene(TitleScene_2())
         
        if self.Back_Button.pushed:
            self.SwitchToScene(Introduction())
            
    
    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.Next_Button = Button("Next", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        self.Next_Button.DrawButton(screen)
        self.Back_Button.DrawButton(screen)
        

        self.text1 = font.render("Hello!!", True,black)
        self.text2 = font.render("This is Giannis,", True,black)
        self.text3 = font.render("He wants to buy a diamont ring for his girlfriend.", True,black)
        self.text4 = font.render("But he has no money", True,black)
        
        self.texts = ((self.text1,(100 , 140)),(self.text2,(100 , 180)),
                      (self.text3,(100 , 220)),(self.text4,(100,260)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Frond_400[0],(600,100))
        

class TitleScene_2(SceneBase):
    def __init__(self, flps = 10):
        SceneBase.__init__(self, flps)
    
    def quitScene(self, event):
        if event[pg.K_RETURN] or self.Next_Button.pushed:
           self.SwitchToScene(TitleScene_3())
         
        if self.Back_Button.pushed:
            self.SwitchToScene(TitleScene())
                
    
    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.Next_Button = Button("Next", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        self.Next_Button.DrawButton(screen)
        self.Back_Button.DrawButton(screen)
        
        self.text1 = font.render("He also has to cross through", True,black)
        self.text2 = font.render("an area full of ", True,black)
        self.text3 = font.render("Vampires and Werewolfs.", True,black)
        
        self.texts = ((self.text1,(100 , 140)),(self.text2,(100 , 180)),(self.text3,(100 , 220)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Frond_400[0],(600,100))
        
class TitleScene_3(SceneBase):
    def __init__(self, flps = 10):
        SceneBase.__init__(self, flps)
    
    def quitScene(self, event):
        
        if event[pg.K_RETURN] or self.Play_Button.pushed:
           self.SwitchToScene(GameScene())
         
        if self.Back_Button.pushed:
            self.SwitchToScene(TitleScene_2())

    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.Play_Button = Button("Play", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        self.Play_Button.DrawButton(screen)
        self.Back_Button.DrawButton(screen)
        
        self.text1 = font.render("Thankfully he has", True,black)
        self.text2 = font.render("a powerful stun gun", True,black)
        self.text3 = font.render("that can nock them off", True,black)
        self.text4 = font.render("for a good amount of time", True,black)
       
        self.texts = ((self.text1,(100 , 140)),(self.text2,(100 , 180)),
                      (self.text3,(100 , 220)),(self.text4,(100 , 260)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Frond_400[0],(600,100))




class BeatenScene1(SceneBase):
    def __init__(self, flps = 10):
        SceneBase.__init__(self, flps)
    
    def quitScene(self, event):
        if event[pg.K_RETURN]:
            self.SwitchToScene(GameScene())
            pg.time.delay(800)
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        self.screen = screen
        self.screen.fill(LoseScreenColor)
        if player.beaten_by_Vampire:
            self.text1 = font.render("This Vampire beat you up", True,black)
            if player.coins > 0 :
                self.text2 = font.render("and stole all of your money", True,black)
                self.texts = (self.text1,(300 , 240)),(self.text2,(300 , 280))
                self.screen.blits(self.texts)
            else:
                self.text3 = font.render("And beacause you did not have any monet", True,black)
                self.text4 = font.render("he beat you again", True,black)
                self.texts = ((self.text1,(300, 240)),(self.text3,(300, 280)),
                              (self.text4,(300 , 320)))
                self.screen.blits(self.texts)
            self.screen.blit(Bigger_Falling_Down_Left_400[8],(600,100))
            
            
        if player.beaten_by_Werewolf:
            self.text5 = font.render("This Werewolf beat you up", True,black)
            self.text6 = font.render("just for fun. He didn't care for your money", True,black)
            self.texts = (self.text5,(320 , 240)),(self.text6,(320 , 280))
            self.screen.blits(self.texts)
            self.screen.blit(Bigger_Falling_Down_Left_400[8],(600,100))
            
            
            
class GameScene(SceneBase):
    def __init__(self, flps = 100):
        SceneBase.__init__(self, flps)
        
    
    def quitScene(self, event):
        if self.Quit_Button.pushed:
           self.SwitchToScene(Introduction())
         
        if self.Pause_Button.pushed:
            pass
        
    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        drawBackground()
        
        self.Pause_Button = Button("Pause", 900, 500, gold)
        self.Quit_Button = Button("Quit", 50, 500, gold)
    
        self.Pause_Button.DrawButton(screen)
        self.Quit_Button.DrawButton(screen)
        
        player.beaten_by_Werewolf = False
        player.beaten_by_Vampire = False
       
        
        self.message = "You Have " + str(player.coins) + " coins"
        self.message_x = screen_width - 14*(len(self.message))
        self.message_y = 40
        TextMessage(self.screen,self.message,self.message_x, self.message_y, gold, saddlebrown)
            ### Moving the avatar
        player.movement(self.screen)
        if player.Beaten:
            player.Beaten = False
            player.Person_to_Beat_You.x +=300
            player.Person_to_Beat_You.speed = 2
            player.speed = 1.75
            
            self.SwitchToScene(BeatenScene1())
       
        if player.coins > 200:
            self.SwitchToScene(CongratsScene())

        
        redrawGameWindow(player)

class CongratsScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def quitScene(self, event):
        if self.Restart_Button.pushed:
            self.SwitchToScene(Introduction())
            
        if self.Quit_Button.pushed:
            self.crashed = True
    
    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        screen.fill(HelloScreenColor)
        
        self.Restart_Button = Button("New Game", 850, 500, gold)
        self.Quit_Button = Button("Quit", 50, 500, gold)
    
        self.Restart_Button.DrawButton(screen)
        self.Quit_Button.DrawButton(screen)
        
        
        # For the sake of brevity, the title scene is a blank red screen
        self.text1 = font.render("Congratulations", True,black)
        self.text2 = font.render("You manage to stole", True,black)
        self.text4 = font.render(str(player.coins) + " coins", True, black)
        
        self.texts = ((self.text1,(100 , 140)),(self.text2,(100 , 180)),(self.text4,(100,260)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Frond_400[0],(600,100))
###############################################################################
###############################################################################
#######################            AVATARS           ##########################
###############################################################################
###############################################################################
            
class Avatar(object):
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
        self.dying = False
        self.DyingCount = 0
    
        ## Avatar is inside buildins
        self.inside = False
      
        
        self.actionTime=timeUnit()
        #Avatar's boundaries
        # the have to be renew in every movement
        # intire image of avatar
        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
        # just the legs
        self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
        
        
    def DoNothing(self):
        self.left = False
        self.right = False
        self.frond = False
        self.back = False
        self.stand = True
        self.dying = False
        self.WalkCount=0
        self.Free_to_move = True
        self.moving_keys=pg.key.get_pressed()
#        if moving_Keys[pg.K_RIGHT]:
#            self.Do
    def DoRight(self):
        self.left = False
        self.right = True
        self.frond = False
        self.back = False
        self.stand = False
        self.dying = False
        self.Free_to_move = True
    def DoLeft(self):
        self.left = True
        self.right = False
        self.frond = False
        self.back = False
        self.stand = False
        self.Free_to_move = True
        self.dying = False
    def DoBack(self):
        self.left = False
        self.right = False
        self.frond = False
        self.back = True
        self.stand = False
        self.Free_to_move = True
        self.dying = False
    def DoFace(self):
        self.left = False
        self.right = False
        self.frond = True
        self.back = False 
        self.stand = False
        self.dying = False
    def DoDying(self):
        self.left = False
        self.right = False
        self.frond = False
        self.back = False 
        self.stand = False
        self.dying = True
        
    def movement(self):
            pass
                        

    def drawAvatar(self, gameDisplay):
        self.gameDisplay = gameDisplay
            
    def InsideBuildings(self, BuildingsSurface):
        self.BuildingsSurface = BuildingsSurface
        ####################################
        ###    Checking for Buildings    ###
        ####################################
        for building in BuildingsSurface:
            if self.hitbox.colliderect(building):
#                self.jumping = False
                self.inside = True
            else:
                self.inside = False
 
###############################################################################
#######################            PLAYER            ##########################
###############################################################################
       
class Player(Avatar): 
    
    def __init__(self, x, y, width, height):
        Avatar.__init__(self, x, y, width, height)
        self.speed = 3
        self.Beaten = False
        self.beaten_by_Vampire = False
        self.beaten_by_Werewolf = False 
        self.coins = 0
        self.injured = False

        
        
        
    
    def Jump(self):
        if self.jumping == True and self.inside == False:
            if self.jump_step >= -self.jump_step_max :
                direction = 1
                if self.jump_step < 0:
                    direction = -1
                self.y -= (self.jump_step**2)*0.5*direction
                self.jump_step -= 1
            else:
                self.jumping = False
                self.jump_step = self.jump_step_max    
    
    def WaitingSequence(self,screen):
        self.screen = screen
        waiting=10000 # msec
        if self.actionTime.waitingAct(waiting):
            if self.StandingCount+1>7:
                self.StandingCount=0
            else:
                #dispalying action
                self.screen.blit(Waving[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1 
        elif self.actionTime.waitingAct(2*waiting):
            if self.StandingCount+1>9:
                self.StandingCount=0
            else:
                #dispalying action
                self.screen.blit(Waving_2Hands[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1
        elif self.actionTime.waitingAct(3*waiting):
            self.jumping = True
            if self.StandingCount+1>9:
                self.StandingCount=0
            else:
                self.Jump()
                #dispalying action
                self.screen.blit(Waving_2Hands[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1
                self.actionTime=timeUnit()
                
                                            
        else:
            #dispalying action
            gameDisplay.blit(Face[0],(self.x,self.y))
            

    
    def movement(self,screen):
        ## Moving Keys
        self.screen = screen
        self.moving_keys=pg.key.get_pressed()
        self.dying = False
        if self.injured:
            self.speed = 1
        else:
            self.speed = 3
        #self.Free_to_move moving left and right
        if self.Free_to_move:
            if self.speed > 0:
                if self.moving_keys[pg.K_RIGHT]:
                    self.x += self.speed
                    self.DoRight()
                    self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                elif self.moving_keys[pg.K_LEFT]:
                    self.x-=self.speed
                    self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                    self.DoLeft()
    
               
                #moving up and down
                
                elif self.moving_keys[pg.K_UP]:
                    self.y-=self.speed
                    self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                    self.DoBack()
                elif self.moving_keys[pg.K_DOWN]:
                    self.y+=self.speed
                    self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                    self.DoFace()
    #            if moving_keys[pg.K_SPACE] and player.y > 2*player.jump_step_max**2:
    #                self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
    #                self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
    #                self.jumping = True
    #                self.DoFace()
                else:
                    self.WalkCount = 0
#                else:
#                    self.DoNothing()
            
            if self.speed < 0:
                if self.moving_keys[pg.K_LEFT]:
                    self.x += self.speed
                    self.DoLeft()
                    self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                elif self.moving_keys[pg.K_RIGHT]:
                    self.x-=self.speed
                    self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                    self.DoRight()
    
               
                #moving up and down
                
                elif self.moving_keys[pg.K_DOWN]:
                    self.y-=self.speed
                    self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                    self.DoFace()
                elif self.moving_keys[pg.K_UP]:
                    self.y+=self.speed
                    self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                    self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
                    self.DoBack()
    #            if moving_keys[pg.K_SPACE] and player.y > 2*player.jump_step_max**2:
    #                self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
    #                self.hitbox=pg.Rect((self.x+8), self.y+20, 13, 10)
    #                self.jumping = True
    #                self.DoFace()
                else:
                    self.DoNothing()
                    
        
#        else:
#            self.x +=self.speed + 15
        
        ################################
           ###    Checking for Walls    ###
           ################################
            for wall in walls:
                if self.hitbox.colliderect(wall):
                    ## moving left
                    if self.moving_keys[pg.K_RIGHT]:
                        self.hitbox.left = wall.hitbox.right
                        self.DoNothing()
                        self.x -=4
                        self.TextMessage(self.screen ,"I can't go there", self.x, self.y)
                        
                    ## moving right
                    if self.moving_keys[pg.K_LEFT]:
                        self.hitbox.right = wall.hitbox.left
                        self.DoNothing()
                        self.x +=4
                        self.TextMessage(self.screen ,"I can't go there", self.x, self.y)
                       
                    ## moving up
                    if self.moving_keys[pg.K_UP]:
                        self.hitbox.top = wall.hitbox.bottom
                        self.DoNothing()
                        self.y+=5
                        self.TextMessage(self.screen ,"I can't go there", self.x, self.y)
                        
                    ## moving up
                    if self.moving_keys[pg.K_DOWN]:
                        self.hitbox.bottom = wall.hitbox.top
                        self.DoNothing()
                        self.y-=5
                        self.TextMessage(self.screen,"I can't go there", self.x, self.y)
                        
                
#                        clock.tick(2000)
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
            
        for enemy in VampsANDWerewolfs :
            if  not enemy.unconsious:
                enemy.MoneyMoneyMoney()
                if enemy.AttackingBox.colliderect(player.hitboxBody):
                    enemy.x = self.x
                    enemy.y = self.y
                    self.speed = 0
                    self.dying = True
                    self.Person_to_Beat_You = enemy
                    self.injured = True
                    if enemy in Vamps:
                        enemy.coins += self.coins
                        self.coins = 0
                        self.beaten_by_Vampire = True
                    else:
                        self.beaten_by_Werewolf = True
            else: 
                if self.hitboxBody.colliderect(enemy.hitboxBody):
                    self.coins += enemy.coins
                    enemy.coins = 0
                    

                              

    def drawAvatar(self, screen):
        self.screen = screen
        Avatar.drawAvatar(self, self.screen)
        #walking image number of frames
        if self.x < 100 and self.y < 100:
            self.injured = False
        if self.WalkCount + 1 > 31:
            self.WalkCount = 0
        if self.DyingCount + 1 > 31:
            self.DyingCount = 0
            self.Beaten = True
        if not self.injured:
            if self.right and not self.dying:
                # count time after this action
                self.actionTime=timeUnit()
                #dispalying action
                self.screen.blit(Walking_Right[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            elif self.left and not self.dying:
                # count time after this action
                self.actionTime=timeUnit()
                #dispalying action
                self.screen.blit(Walking_Left[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            elif self.back and not self.dying:
                # count time after this action
                self.actionTime=timeUnit()
                #dispalying action
                self.screen.blit(BackHead[0],(self.x,self.y))    
            elif self.frond and not self.dying:
                    # count time after this action
                self.actionTime=timeUnit()
                    #dispalying action
                self.screen .blit(Face[0],(self.x,self.y))
            elif self.dying:
                self.actionTime=timeUnit()
                self.screen.blit(Falling_Down_Left[self.DyingCount],(self.x,self.y))
                self.DyingCount += 1
            else:
                self.WaitingSequence(self.screen)
        if self.injured:
            if self.right and not self.dying:
                # count time after this action
                self.actionTime=timeUnit()
                #dispalying action
                self.screen.blit(Walking_Right_Beaten[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            elif self.left and not self.dying:
                # count time after this action
                self.actionTime=timeUnit()
                #dispalying action
                self.screen.blit(Walking_Left_Beaten[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            elif self.back and not self.dying:
                # count time after this action
                self.actionTime=timeUnit()
                #dispalying action
                self.screen.blit(BackHead_Beaten[0],(self.x,self.y))    
            elif (self.frond  or self.stand) and not self.dying:
                    # count time after this action
                self.actionTime=timeUnit()
                    #dispalying action
                self.screen.blit(Face_Beaten[0],(self.x,self.y))
            elif self.dying:
                self.actionTime=timeUnit()
                self.screen.blit(Falling_Down_Left[self.DyingCount],(self.x,self.y))
                self.DyingCount += 1
            else:                                   
               self.screen.blit(Face_Beaten[0],(self.x,self.y))
                
           
                 
        #Avatar's boundaries
#        self.hitbox=(self.x+4, self.y, 20, 32)
#        pg.draw.rect(gameDisplay,black, self.hitbox,2)
                
    def TextMessage(self,screen, message, x, y,color = black):
        self.screen = screen
        self.message = message
        self.color = color
        if self.injured:
            self.screen.blit(Face_Beaten[0],(self.x,self.y))
        else:
            self.screen.blit(Face[0],(self.x,self.y))
        self.text = font.render(self.message, True, self.color)
        self.box=pg.Rect(self.x, self.y-self.text.get_height(),self.text.get_width(),self.text.get_height())
        pg.draw.rect(self.screen, white, self.box)
        self.screen.blit(self.text,(x,y-self.text.get_height()))
        


        
###############################################################################
#######################            Vampire            #########################
###############################################################################


class Vampire(Avatar): 
    
    def __init__(self, x, y, width, height, x_end , y_end,Buildings):
        Avatar.__init__(self, x, y, width, height)
        self.x_end = x_end
        self.y_end = y_end
        self.path_x = [self.x, self.x_end]
        self.path_y = [self.y, self.y_end]
        self.random = random.randint(0, 10)
        self.AttackingBox = pg.Rect((self.x+40), self.y, 100, 32)
        self.coins = random.randint(50, 200)
        self.unconsious = False
        self.hits = 0
        self.Buildings = Buildings
        
        
    def Hit(self):
        if self.hits == 40:
            self.hits = 0
            self.WalkCount = 0
            self.shootDown = True
            if self.hits < 1000:
                self.unconsious = True
            
    def MoneyMoneyMoney(self):
        if self.unconsious == True:
            self.coins = random.randint(50, 200)          
        
    def movement(self):
         
        self.Hit()
        if self.unconsious:
            self.Free_to_move = False
        else:
            self.Free_to_move = True
      
        if self.Free_to_move == True:
            if self.speed > 0:
                if self.random < 5:
                    if (self.x + self.speed) < self.path_x[1] :
                        self.x += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x+4), self.y-32, 100, 100)
                        self.DoRight()
#                        Attacking(self, player)
                        

                    else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-74), self.y-32, 100, 100)
                        self.DoLeft()
#                        Attacking(self, player)
                        

                else:
                     if (self.y +self.speed) < self.path_y[1]:
                        self.y += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y, 92, 92)
                        self.DoFace()
#                        Attacking(self, player)
                        
                     else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y-55, 92, 92)
                        self.DoBack()
#                        Attacking(self, player)
            else:
                if self.random < 5:
                    if  (self.x +self.speed) > self.path_x[0] :
                        self.x += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-74), self.y-32, 100, 100)
                        self.DoLeft()
#                        Attacking(self, player)
                    else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-54), self.y-32, 100, 100)
                        self.DoRight()
#                        Attacking(self, player)
                else:
                     if (self.y + self.speed) > self.path_y[0]:
                        self.y += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y-55, 92, 92)
                        self.DoBack()
#                        Attacking(self, player)
                     else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y, 92, 92)
                        self.DoFace()
#           
            if Attacking(self,player):
                self.speed = 0
                self.uncoinsious = False

            ####################################
            ###    Checking for Buildings    ###
            ####################################
            for building in BuildingsSurface:
                    if self.hitbox.colliderect(building):
                        print("VmpireBuilding")
                        self.hitboxBody.left = building.right
                        self.speed *= -1
                        self.x += self.speed*10
                        self.inside = True
        else:
            self.speed = 0
            
    def drawAvatar(self, gameDisplay):
        self.movement()
        self.gameDisplay = gameDisplay
        
                #walking image number of frames
        if self.WalkCount+1>27:
            self.WalkCount=0
        if self.StandingCount + 1 > 800:
            self.StandingCount = 0
            self.unconsious = False
        if self.speed > 0:
            if self.random < 5:
                gameDisplay.blit(Walking_Right_Vamp[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            else:
                gameDisplay.blit(Face_Vamp[0],(self.x,self.y))
                self.WalkCount+=1
        elif self.speed < 0:
            if self.random < 5:
                gameDisplay.blit(Walking_Left_Vamp[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            else:
                gameDisplay.blit(Back_Vamp[0],(self.x,self.y))
                self.WalkCount+=1
        else:
            self.WalkCount = 0
            if self.unconsious:
                gameDisplay.blit(Falling_Right_Vamp[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1
            else:
                gameDisplay.blit(Face_Vamp[0],(self.x,self.y))
                self.StandingCount=0
                self.speed = 2

            
        

###############################################################################
#######################         WereWolf             ##########################
###############################################################################


class WereWolf(Avatar): 
    
    def __init__(self, x, y, width, height, x_end, y_end):
        Avatar.__init__(self, x, y, width, height)
        self.x_end = x_end
        self.y_end = y_end
        self.path_x = [self.x, self.x_end]
        self.path_y = [self.y, self.y_end]
        self.random = random.randint(0, 10)
        self.AttackingBox = pg.Rect((self.x+40), self.y, 100, 32)
        self.coins = random.randint(10, 70)
        self.unconsious = False
        self.hits = 0

    def Hit(self):
        if self.hits == 40:
            self.hits = 0
            self.WalkCount = 0
            self.shootDown = True
            if self.hits < 1000:
                self.unconsious = True
    
    def MoneyMoneyMoney(self):
        if self.unconsious == True:
            self.coins = random.randint(10, 70)              
        
#    def Looted(self):
#        self.coins = 0 
            
    def movement(self):
        
        self.Hit()
        if self.unconsious:
            self.Free_to_move = False
        else:
            self.Free_to_move = True
        
        if self.Free_to_move == True:
            if self.speed > 0:
                if self.random < 5:
                    if (self.x + self.speed) < self.path_x[1] :
                        self.x += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x+4), self.y-32, 100, 100)
                        self.DoRight()
#                        Attacking(self, player)
                        

                    else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-74), self.y-32, 100, 100)
                        self.DoLeft()
#                        Attacking(self, player)
                        

                else:
                     if (self.y +self.speed) < self.path_y[1]:
                        self.y += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y, 92, 92)
                        self.DoFace()
#                        Attacking(self, player)
                        
                     else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y-55, 92, 92)
                        self.DoBack()
#                        Attacking(self, player)
            else:
                if self.random < 5:
                    if  (self.x +self.speed) > self.path_x[0] :
                        self.x += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-74), self.y-32, 100, 100)
                        self.DoLeft()
#                        Attacking(self, player)
                    else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-54), self.y-32, 100, 100)
                        self.DoRight()
#                        Attacking(self, player)
                else:
                     if (self.y + self.speed) > self.path_y[0]:
                        self.y += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y-55, 92, 92)
                        self.DoBack()
#                        Attacking(self, player)
                     else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y, 92, 92)
                        self.DoFace()         
            if Attacking(self,player):
                self.speed = 0

            ####################################
            ###    Checking for Buildings    ###
            ####################################
            for building in BuildingsSurface:
                    if self.hitbox.colliderect(building):
                        print("VmpireBuilding")
                        self.hitboxBody.left = building.right
                        self.speed *= -1
                        self.x += self.speed*10
                        self.inside = True
        else:
            self.speed = 0                             

    
    def drawAvatar(self, gameDisplay):
        self.gameDisplay = gameDisplay
        self.movement()
        self.gameDisplay = gameDisplay
        
                #walking image number of frames
        if self.WalkCount+1>27:
            self.WalkCount=0
        if self.StandingCount+1 > 800:
            self.StandingCount=0
            self.unconsious = False
        if self.speed > 0:
            if self.random < 5:
                gameDisplay.blit(Walking_Right_Wer[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            else:
                gameDisplay.blit(Face_Wer[0],(self.x,self.y))
                self.WalkCount+=1
        elif self.speed < 0:
            if self.random < 5:
                gameDisplay.blit(Walking_Left_Wer[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            else:
                gameDisplay.blit(Back_Wer[0],(self.x,self.y))
                self.WalkCount+=1
        else:
            self.WalkCount = 0
            if self.unconsious:
                gameDisplay.blit(Falling_Left_Wer[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1
            else:
                gameDisplay.blit(Face_Wer[0],(self.x,self.y))
                self.StandingCount=0
                self.speed = 2
                
    

 
        
            
###############################################################################
#######################          Stun Shoots         ##########################
###############################################################################
                
class StunShoots():

    def __init__(self, x, y, facing, radius = 3, color = blue):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 8*facing
        self.hitbox = pg.Rect((self.x-self.radius), self.y-self.radius , 2*self.radius,2*self.radius)

    def DrawShoot(self, gameDisplaylf):
        pg.draw.circle(gameDisplay, self.color, (self.x, self.y), self.radius)               
#        pg.draw.rect(gameDisplay,red, self.hitbox) 
                
                
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
#        pg.draw.rect(gameDisplay, red, self.rect)

                
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
        
        paintingBuilding=pg.Rect(x_begin-10, y_begin, self.width+20, self.height+10)
#        pg.draw.rect(gameDisplay, red,  paintingBuilding)
        BuildingsSurface.append(paintingBuilding)
        
        
        ### The Door is on the LEft side
        if self.door.x == self.x_begin:
            DoorWallLenght1 = self.door.y - self.y_begin
            DoorWallLenght2 = self.y_end - (self.door.y + self.door.length)
            #Left
            wall1=rectWall(self.x_begin, self.y_begin, self.WallWidth,  DoorWallLenght1)
#            pg.draw.rect(gameDisplay, red, wall1.rect)
            wall2=rectWall(self.x_begin, self.door.y + self.door.length , self.WallWidth, DoorWallLenght2)
#            pg.draw.rect(gameDisplay, red, wall2.rect)
            #Τop
            wall3=rectWall(self.x_begin, self.y_begin, self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall3.rect)
            #Bottom
            wall4=rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall4.rect)
            #Right
            wall5=rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)
#            pg.draw.rect(gameDisplay, red, wall5.rect)
        
        
                ### The Door is on the Right side
        if self.door.x == (self.x_end - self.WallWidth):
            DoorWallLenght1 = self.door.y - self.y_begin
            DoorWallLenght2 = self.y_end - (self.door.y + self.door.length)
            #Left
            wall1 = rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
#            pg.draw.rect(gameDisplay, red, wall1.rect)
            #Τop
            wall2 = rectWall(self.x_begin, self.y_begin, self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall2.rect)
            #Bottom
            wall3 =rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall3.rect)
            #Right
            wall4 = rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, DoorWallLenght1)
            pg.draw.rect(gameDisplay, red, wall4.rect)
            wall5 = rectWall(self.x_end - self.WallWidth, self.door.y + self.door.length , self.WallWidth, DoorWallLenght2)
#            pg.draw.rect(gameDisplay, red, wall5.rect)
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
            rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
#            pg.draw.rect(gameDisplay, red, wall1.rect)
            #Τop
            rectWall(self.x_begin, self.y_begin , self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall2.rect)
            #Bottom
            rectWall(self.x_begin, self.y_end, self.door.length, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall4.rect)
            rectWall(self.door.x + self.door.length, self.y_end, DoorWallLenght2 , self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall3.rect)
            #Right
            rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)
#
            

           
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
#######################            Buttons            #########################
###############################################################################

class Button():
    
    def __init__(self, message, x, y,inactive_color = red, interaction_color = pink):
        self.x = x
        self.y = y
        self.message = message
        self.interaction_color = interaction_color
        self.inactive_color = inactive_color
        self.pushed = False
        
        self.mouse_pos= pg.mouse.get_pos()
        self.click = pg.mouse.get_pressed()
        
    def DrawButton(self, screen):
        
        self.screen = screen
        self.text = font.render(self.message, True, self.inactive_color)
        self.box = pg.Rect(self.x-10,self.y-self.text.get_height(),self.text.get_width()+24,self.text.get_height())

        if self.mouse_pos[0] > self.x and self.mouse_pos[0] < self.x +self.box.width:
            if  self.mouse_pos[1] > self.y and self.mouse_pos[1] < self.y + self.box.height:
                self.text = font.render(self.message, True, self.interaction_color)
                self.screen.blit(self.text, (self.x,self.y))
                if self.click[0]:
                    self.pushed = True
        else:
            self.pushed = False
        
        self.screen.blit(self.text, (self.x,self.y))

   
    

###############################################################################
###############################################################################
######################3###        FUNCTIONS         ###########################
###############################################################################
###############################################################################
 
    
###############################################################################
###########           Initialise Game Funciton         ########################
###############################################################################    

def main():
    global screen_width, mapwidth, mapheight, tilesize, tilemap
    global clock, font, gameDisplay
    global ground
    
    font = pg.font.SysFont("comicsansms", 24)

    ###Screen Resolution/Game Surface
    GameResolution=[screen_width,screen_height]
    

    ### Title of the game Window
    pg.display.set_caption('Hello World!')
    
    
    ###Game Clock
    clock=pg.time.Clock()
    
    
    ###########################################################################
    #############           Background Images         #########################
    ###########################################################################
    tilesize=10
    mapwidth=int(screen_width/tilesize)
    #print(mapwidth)
    mapheight=int(screen_height/tilesize)
    #print(mapheight)pg.time.Clock
    GameResolutionWithTiles=[mapwidth*tilesize,mapheight*tilesize]
    gameDisplay=pg.display.set_mode(GameResolutionWithTiles)

    
    border_tiles_H=[0,1,mapheight-2,mapheight-1]
    border_tiles_V=[0,1,mapwidth-2,mapwidth-1]
    
    earth=0
    grass=1
    
    ground={
            earth : pg.image.load("Ground Sprite Pack\ground3.png"),
            #grass : pg.image.load("Ground Sprite Pack\\LGrass2.png")
            }
    

    
    tilemap=[[earth for y in range(mapheight)] for x in range(mapwidth)]
    
               
###############################################################################
##################         Draw Avatar on Surface       #######################
###############################################################################
  
def redrawGameWindow(avatar):
        avatar.drawAvatar(gameDisplay)
        for bullet in Bullets_x:
            bullet.DrawShoot(gameDisplay)
        for bullet in Bullets_y:
            bullet.DrawShoot(gameDisplay)
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
#########################     Enemies Attacking      ##########################
###############################################################################




def Attacking(enemy, player, waiting = 100, attacked = False):
    enemy.player = player
    if enemy.AttackingBox.colliderect(player.hitboxBody):
        enemy.x = player.x
        enemy.y = player.y
        attacked = True
    return attacked


                  

###############################################################################
##########################          Background          #######################
###############################################################################

def drawBackground():
        ### MAP
    for row in range(mapwidth):
        for column in range(mapheight):
            position=(row*tilesize,column*tilesize, tilesize,tilesize)
            gameDisplay.blit(ground[tilemap[row][column]],position)   
    
    #screen borders
    ScreenBorders()
          
    ### Painting's Gallery        
    gameDisplay.blit(gallery,(600,360))
    Building(648,408,752,502,Door(648,445,10,30))
    
    gameDisplay.blit(GiannisHome,(20,20))
    Building(50,40,175,160,Door(165,100,10,30))


    for vamp in Vamps:
        vamp.drawAvatar(gameDisplay)
#        pg.draw.rect(gameDisplay, white, vamp.AttackingBox,2)

    for wery in Werewolfs:
        wery.drawAvatar(gameDisplay)
#        pg.draw.rect(gameDisplay, pink, wery.AttackingBox,2)
        
        
def ScreenBorders(x_begin = 0, y_begin = 0, x_end = screen_width, y_end = screen_height, width = 10):
        #screen borders
    #top
    rectWall(x_begin,y_begin,x_end,width)
    screenborders["topBorder"]=rectWall(x_begin,y_begin,x_end,width)
    #right
    rectWall(x_end-width,y_begin,width,y_end-width)
    screenborders["rightBorder"]=rectWall(x_end,y_begin,width,y_end)

    #bottom
    rectWall(x_begin,y_end-width,x_end-width,width)
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
##################             Text Message             #######################
###############################################################################   

def TextMessage(screen,message, x, y,color = black, colorBox = white):
    text = font.render(message, True, color)
    box=pg.Rect(x-10,y-text.get_height(),text.get_width()+24,text.get_height())
    pg.draw.rect(screen, colorBox, box)
    screen.blit(text,(x,y-text.get_height()))
    pg.display.flip() 
    return text

###############################################################################
################             Random Vampire             #######################
###############################################################################
    
def CreateVampire():
    x1 = random.randint(150,1000)
    x2 = random.randint(150,1000)+x1
    y1 = random.randint(-32,500)
    y2 = random.randint(-32,500)+y1
    if abs(x1-x2)>200 and abs(y1-y2)>200:
        Vamp = Vampire (x1,y1,32,32,x2,y2,BuildingsSurface)
        for building in BuildingsSurface:
            if Vamp.hitboxBody.colliderect(building):
                return CreateVampire()
        return Vamp
    else:
        x2 = random.randint(150,1000)+x1
        y2 = random.randint(-32,500)+y1
    return CreateVampire()

###############################################################################
################             Random WereWolf            #######################
###############################################################################
    
def CreateWerewolf():
    x1 = random.randint(150,1000)
    x2 = random.randint(150,1000)+x1
    y1 = random.randint(-32,500)
    y2 = random.randint(-32,500)+y1
    if abs(x1-x2)>200 and abs(y1-y2)>200:
        Werewolf = WereWolf (x1,y1,32,32,x2,y2)
        for building in BuildingsSurface:
            if Werewolf.hitboxBody.colliderect(building):
                return CreateWerewolf()
        return Werewolf
    else:
        x2 = random.randint(150,1000)+x1
        y2 = random.randint(-32,500)+y1
    return CreateWerewolf()

###############################################################################
#######################                                 #######################
#######################              Avatars            #######################
#######################                                 #######################
###############################################################################
player = Player(50,50,32,32)



number_of_Vamps = random.randint(5,10)
for i in range(number_of_Vamps):
    Vamps.append(CreateVampire())
    VampsANDWerewolfs.extend(Vamps)




number_of_Wers = random.randint(5,10)
for i in range(number_of_Wers):
    Werewolfs.append(CreateWerewolf())
    VampsANDWerewolfs.extend(Werewolfs)



def ShootingBullets(Bullets_x, Bullets_y, avatar, key):
        
    newBullet_x = round(avatar.x + avatar.width/2)
    newBullet_y = round(avatar.y + avatar.height/3)
    
    for bullet in Bullets_x:
        if bullet.x < avatar.x + 420 and bullet.x > avatar.x - 420 :
            bullet.x += bullet.speed
            bullet.hitbox = pg.Rect((bullet.x-bullet.radius),bullet.y-bullet.radius , 2*bullet.radius,2*bullet.radius)
#               pg.draw.rect(gameDisplay, red,bullet.hitbox)
        else:
            Bullets_x.pop(Bullets_x.index(bullet))
#            Bullets.pop(Bullets.index(bullet))
    
    for bullet in Bullets_y:
        if bullet.y < avatar.y + 400 and bullet.y > avatar.y - 400:
            bullet.y += bullet.speed
            bullet.hitbox = pg.Rect((bullet.x-bullet.radius),bullet.y-bullet.radius , 2*bullet.radius,2*bullet.radius)
#               pg.draw.rect(gameDisplay, red,bullet.hitbox)
        else:
            Bullets_y.pop(Bullets_y.index(bullet))
#            Bullets.pop(Bullets.index(bullet))

    
    if avatar.right:
        facing_x = 1
        facing_y = 0
    if avatar.frond:
        facing_y = 1
        facing_x = 0
    if avatar.left:
        facing_x = -1
        facing_y = 0
    if avatar.back:
        facing_y = -1
        facing_x = 0
    if key[pg.K_SPACE]:
        if len(Bullets_x) < 60:
            if avatar.right:
                newBullet_x = round(avatar.x + avatar.width)
                newBullet_y = round(avatar.y + avatar.height/3)
            if avatar.left:
                newBullet_x = round(avatar.x)
                newBullet_y = round(avatar.y + avatar.height/3)
            if facing_x != 0:
                Bullets_x.append(StunShoots(newBullet_x,newBullet_y,facing_x))
                Bullets.extend(Bullets_x)
        if len(Bullets_y) < 60:
            if key[pg.K_UP]:
                newBullet_x = round(avatar.x + avatar.width/2)
                newBullet_y = round(avatar.y + avatar.height/3)
            if key[pg.K_DOWN]:
                newBullet_x = round(avatar.x + avatar.width/2)
                newBullet_y = round(avatar.y + avatar.height/3)
            if facing_y !=0:
                Bullets_y.append(StunShoots(newBullet_x,newBullet_y,facing_y))
                Bullets.extend(Bullets_y) 
        pg.time.delay(5)            


    
    
  
    for enemy in VampsANDWerewolfs:
        BeingShoot(enemy, Bullets) 

def BeingShoot(enemy, Bullets):
    for bullet in Bullets:
        if enemy.hitboxBody.colliderect(bullet.hitbox):
            Bullets.pop(Bullets.index(bullet))
            enemy.hits += 1
            enemy.Hit()
            print (enemy.hits)
            
###############################################################################
#######################                                 #######################
#######################         Games Main Loop         #######################
#######################                                 #######################
###############################################################################

def run_game(starting_scene):
    pg.init()
    crashed = False
    main()
    active_scene = starting_scene
    while not crashed:
        key=pg.key.get_pressed()
        
        ShootingBullets(Bullets_x, Bullets_y,player,key)

        
        
        active_scene.Update()
        active_scene.Render(gameDisplay)
        active_scene.quitScene(key)
        pg.display.flip()
        active_scene = active_scene.next
        
        if quitGame() or active_scene.crashed:
            crashed = True
     
        clock.tick(active_scene.flps)
    pg.quit()
run_game(GameScene())
quit()
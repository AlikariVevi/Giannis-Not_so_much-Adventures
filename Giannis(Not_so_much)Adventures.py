# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import pygame as pg
import os, random

pg.init()

global red, green, blue, darkBlue, white, black, pink
###Screen Resolution/Game Surface
global screen_width, screen_height, music_playing

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
#################           Sounds and Mysic         ##########################
##############################################################################

pg.mixer.music.load("Music_Sounds\Dungeon_Boss.ogg")
#pg.mixer.music.load("Music_Sounds\Dungeon_Level.ogg")






pg.mixer.music.play(-1)

music_playing = True

shootingSound = pg.mixer.Sound("Music_Sounds\Shoot3.wav")
#shootingSound = pg.mixer.Sound("Music_Sounds\Shoot5.wav")

pg.mixer.music.set_volume(0.35)
###############################################################################
#################           Buildings Images         ##########################
###############################################################################

gallery = pg.image.load("Ground Sprite Pack\gallery.png")

GiannisHome = pg.image.load("Ground Sprite Pack\GiannisHome.png")

ClothShop = pg.image.load("Ground Sprite Pack\clothshop.png")

###############################################################################
#################           Cloths Images         ##########################
###############################################################################

Fancy_Shocks = pg.image.load("Cloths\Fancy_Shocks.png")

Black_Coat = pg.image.load("Cloths\Black_Coat.png")

Werewolf_Wig = pg.image.load("Cloths\Werewolf_Wig.png")

########################################################################
#############                   Resizing             ###################
########################################################################

Fancy_Shocks_200 = pg.transform.scale(Fancy_Shocks,(200,200))

Black_Coat_200 = pg.transform.scale(Black_Coat,(200,200))

Werewolf_Wig_200 = pg.transform.scale(Werewolf_Wig,(200,200))

Fancy_Shocks_100 = pg.transform.scale(Fancy_Shocks,(100,100))

Black_Coat_100 = pg.transform.scale(Black_Coat,(100,100))

Werewolf_Wig_100 = pg.transform.scale(Werewolf_Wig,(100,100))

Black_Coat_30 = pg.transform.scale(Black_Coat,(30,30))

Fancy_Shocks_200 = pg.transform.scale(Fancy_Shocks,(200,200))
###############################################################################
###################           Avatar Images         ###########################
###############################################################################

###############################################################################
###################              Player             ###########################
###############################################################################
image_path="Giannis"

Giannis_in_Jail = pg.image.load("Giannis\GiannisFrond\Giannis_in_Jail.png")
########################################################################
#############                   Resizing             ###################
########################################################################

Giannis_in_Jail_400 = pg.transform.scale(Giannis_in_Jail,(400,400))

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

########################################################################
#############                   Resizing             ###################
########################################################################
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

Bigger_Waving_300 = [pg.transform.scale(im,(300,300)) for im in Waving]
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

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Waving_2Hands_400 = [pg.transform.scale(im,(400,400)) for im in Waving_2Hands]

## Avatar Frond
Frond_images=["GiannisStanding"]
Frond_images_folder_path=os.path.join(image_path,"GiannisFrond")
Frond_images_path=[os.path.join(Frond_images_folder_path,i+".png") for i in Frond_images]
Face=[pg.image.load(i) for i in Frond_images_path]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Frond_400 = [pg.transform.scale(im,(400,400)) for im in Face]
Bigger_Frond_300 = [pg.transform.scale(im,(300,300)) for im in Face]
Bigger_Frond_200 = [pg.transform.scale(im,(200,200)) for im in Face]
Bigger_Frond_100 = [pg.transform.scale(im,(100,100)) for im in Face]


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

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Falling_Down_Left_400 = [pg.transform.scale(im,(400,400)) for im in Falling_Down_Left]
Bigger_Falling_Down_Right_400 = [pg.transform.scale(im,(400,400)) for im in Falling_Down_Right]


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

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Walking_Right_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Right_Beaten]
Bigger_Walking_Left_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Left_Beaten]

## Avatar Frond
Frond_images_Beaten=["GiannisStanding_Beaten"]
Frond_images_folder_Beaten_path=os.path.join(image_path,"GiannisFrond")
Frond_images_Beaten_path=[os.path.join(Frond_images_folder_Beaten_path,i+".png") for i in Frond_images_Beaten]
Face_Beaten=[pg.image.load(i) for i in Frond_images_Beaten_path]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Frond_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in Face_Beaten]

## Avatar Back
Back_images_Beaten=["GiannisBack_Beaten"]
Back_images_folder_Beaten_path=os.path.join(image_path,"GiannisBack")
Back_images_Beaten_path=[os.path.join(Back_images_folder_Beaten_path,i+".png") for i in Back_images_Beaten]
BackHead_Beaten=[pg.image.load(i) for i in Back_images_Beaten_path]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_BackHead_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in BackHead_Beaten]

#############################################################
############## BEATEN with new Shocks  ######################
#############################################################
Right_images_Beaten_NewShocks=["sprite_GiannisWalking_Beaten_NewShocks10",
                     "sprite_GiannisWalking_Beaten_NewShocks11",
                     "sprite_GiannisWalking_Beaten_NewShocks12",
                     "sprite_GiannisWalking_Beaten_NewShocks13",
                     "sprite_GiannisWalking_Beaten_NewShocks14",
                     "sprite_GiannisWalking_Beaten_NewShocks15",
                     "sprite_GiannisWalking_Beaten_NewShocks16",
                     "sprite_GiannisWalking_Beaten_NewShocks17",
                     "sprite_GiannisWalking_Beaten_NewShocks18",
                     "sprite_GiannisWalking_Beaten_NewShocks19",
                     "sprite_GiannisWalking_Beaten_NewShocks20",
                     "sprite_GiannisWalking_Beaten_NewShocks21",
                     "sprite_GiannisWalking_Beaten_NewShocks22",
                     "sprite_GiannisWalking_Beaten_NewShocks23",
                     "sprite_GiannisWalking_Beaten_NewShocks24",
                     "sprite_GiannisWalking_Beaten_NewShocks25",
                     "sprite_GiannisWalking_Beaten_NewShocks26",
                     "sprite_GiannisWalking_Beaten_NewShocks27",
                     "sprite_GiannisWalking_Beaten_NewShocks28",
                     "sprite_GiannisWalking_Beaten_NewShocks29",
                     "sprite_GiannisWalking_Beaten_NewShocks30",
                     "sprite_GiannisWalking_Beaten_NewShocks00",
                     "sprite_GiannisWalking_Beaten_NewShocks01",
                     "sprite_GiannisWalking_Beaten_NewShocks02",
                     "sprite_GiannisWalking_Beaten_NewShocks03",
                     "sprite_GiannisWalking_Beaten_NewShocks04",
                     "sprite_GiannisWalking_Beaten_NewShocks05",
                     "sprite_GiannisWalking_Beaten_NewShocks06",
                     "sprite_GiannisWalking_Beaten_NewShocks07",
                     "sprite_GiannisWalking_Beaten_NewShocks08",
                     "sprite_GiannisWalking_Beaten_NewShocks09"]



    
Walking_images_Beaten_NewShocks_path=os.path.join(image_path,"GiannisWalking_Beaten_NewShocks")
Right_images_Beaten_NewShocks_path=[os.path.join(Walking_images_Beaten_NewShocks_path,i+".png") for i in Right_images_Beaten_NewShocks]

Walking_Right_Beaten_NewShocks=[pg.image.load(i) for i in Right_images_Beaten_NewShocks_path]
Walking_Left_Beaten_NewShocks=[pg.transform.flip(i,True,False) for i in Walking_Right_Beaten_NewShocks]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Walking_Right_Beaten_NewShocks_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Right_Beaten_NewShocks]
Bigger_Walking_Left_Beaten_NewShocks_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Left_Beaten_NewShocks]

## Avatar Frond
Frond_images_Beaten_NewShocks=["GiannisStanding_Beaten_NewShocks"]
Frond_images_folder_Beaten_NewShocks_path=os.path.join(image_path,"GiannisFrond")
Frond_images_Beaten_NewShocks_path=[os.path.join(Frond_images_folder_Beaten_NewShocks_path,i+".png") for i in Frond_images_Beaten_NewShocks]
Face_Beaten_NewShocks=[pg.image.load(i) for i in Frond_images_Beaten_NewShocks_path]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Frond_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in Face_Beaten]

## Avatar Back
Back_images_Beaten_NewShocks=["GiannisBack_Beaten_NewShocks"]
Back_images_folder_Beaten_NewShocks_path=os.path.join(image_path,"GiannisBack")
Back_images_Beaten_NewShocks_path=[os.path.join(Back_images_folder_Beaten_NewShocks_path,i+".png") for i in Back_images_Beaten_NewShocks]
BackHead_Beaten_NewShocks=[pg.image.load(i) for i in Back_images_Beaten_NewShocks_path]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_BackHead_Beaten_400 = [pg.transform.scale(im,(400,400)) for im in BackHead_Beaten]


############## Dressed as a Vampire ######################
Right_images_Vamp_Giannis=[
        "sprite_Vamp_GiannisWalking10","sprite_Vamp_GiannisWalking11",
        "sprite_Vamp_GiannisWalking12","sprite_Vamp_GiannisWalking13",
        "sprite_Vamp_GiannisWalking14","sprite_Vamp_GiannisWalking15",
        "sprite_Vamp_GiannisWalking16","sprite_Vamp_GiannisWalking17",
        "sprite_Vamp_GiannisWalking18","sprite_Vamp_GiannisWalking19",
        "sprite_Vamp_GiannisWalking20","sprite_Vamp_GiannisWalking21",
        "sprite_Vamp_GiannisWalking22","sprite_Vamp_GiannisWalking23",
        "sprite_Vamp_GiannisWalking24","sprite_Vamp_GiannisWalking25",
        "sprite_Vamp_GiannisWalking26","sprite_Vamp_GiannisWalking27",
        "sprite_Vamp_GiannisWalking00",
        "sprite_Vamp_GiannisWalking01","sprite_Vamp_GiannisWalking02",
        "sprite_Vamp_GiannisWalking03","sprite_Vamp_GiannisWalking04",
        "sprite_Vamp_GiannisWalking05","sprite_Vamp_GiannisWalking06",
        "sprite_Vamp_GiannisWalking07","sprite_Vamp_GiannisWalking08",
        "sprite_Vamp_GiannisWalking09"]



    
Walking_images_Vamp_Giannis_path=os.path.join(image_path,"Vamp_Giannis_Walking")
Right_images_Vamp_Giannis_path=[os.path.join(Walking_images_Vamp_Giannis_path,i+".png") for i in Right_images_Vamp_Giannis]

Walking_Right_Vamp_Giannis=[pg.image.load(i) for i in Right_images_Vamp_Giannis_path]
Walking_Left_Vamp_Giannis=[pg.transform.flip(i,True,False) for i in Walking_Right_Vamp_Giannis]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Walking_Right_Vamp_Giannis_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Right_Vamp_Giannis]
Bigger_Walking_Left_Vamp_Giannis_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Left_Vamp_Giannis]

## Avatar Frond
Frond_images_Vamp_Giannis=["Vamp_Giannis_Frond"]
Frond_images_folder_Vamp_Giannis_path=os.path.join(image_path,"GiannisFrond")
Frond_images_Vamp_Giannis_path=[os.path.join(Frond_images_folder_Vamp_Giannis_path,i+".png") for i in Frond_images_Vamp_Giannis]
Face_Vamp_Giannis=[pg.image.load(i) for i in Frond_images_Vamp_Giannis_path]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Frond_Vamp_Giannis_400 = [pg.transform.scale(im,(400,400)) for im in Face_Vamp_Giannis]

## Avatar Back
Back_images_Vamp_Giannis=["Vamp_Giannis_Back"]
Back_images_folder_Vamp_Giannis_path=os.path.join(image_path,"GiannisBack")
Back_images_Vamp_Giannis_path=[os.path.join(Back_images_folder_Vamp_Giannis_path,i+".png") for i in Back_images_Vamp_Giannis]
BackHead_Vamp_Giannis=[pg.image.load(i) for i in Back_images_Vamp_Giannis_path]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_BackHead_Vamp_Giannis_400 = [pg.transform.scale(im,(400,400)) for im in BackHead_Vamp_Giannis]

#Falling
Falling_images_Vamp_Giannis=["sprite_Vamp_Giannis_Falling0","sprite_Vamp_Giannis_Falling1",
                   "sprite_Vamp_Giannis_Falling2","sprite_Vamp_Giannis_Falling3",
                   "sprite_Vamp_Giannis_Falling4","sprite_Vamp_Giannis_Falling5",
                   "sprite_Vamp_Giannis_Falling6","sprite_Vamp_Giannis_Falling7",
                   "sprite_Vamp_Giannis_Falling8"]

for i in range(500):
    Falling_images_Vamp_Giannis.append("sprite_Vamp_Giannis_Falling8")
Falling_images_path_Vamp_Giannis=os.path.join(image_path,"Vamp_Giannis_Falling")
Falling_Right_images_path_Vamp_Giannis=[os.path.join(Falling_images_path_Vamp_Giannis,i+".png") for i in Falling_images_Vamp_Giannis]

Falling_Right_Vamp_Giannis=[pg.image.load(i) for i in Falling_Right_images_path_Vamp_Giannis]
Falling_Left_Vamp_Giannis=[pg.transform.flip(i,True,False) for i in Falling_Right_Vamp_Giannis]

############## Dressed as a Werewolf ######################
Right_images_Wery_Giannis=[
        "sprite_Wery_Giannis_Walking10","sprite_Wery_Giannis_Walking11",
        "sprite_Wery_Giannis_Walking12","sprite_Wery_Giannis_Walking13",
        "sprite_Wery_Giannis_Walking14","sprite_Wery_Giannis_Walking15",
        "sprite_Wery_Giannis_Walking16","sprite_Wery_Giannis_Walking17",
        "sprite_Wery_Giannis_Walking18","sprite_Wery_Giannis_Walking19",
        "sprite_Wery_Giannis_Walking20","sprite_Wery_Giannis_Walking21",
        "sprite_Wery_Giannis_Walking22","sprite_Wery_Giannis_Walking23",
        "sprite_Wery_Giannis_Walking24","sprite_Wery_Giannis_Walking25",
        "sprite_Wery_Giannis_Walking26","sprite_Wery_Giannis_Walking27",
        "sprite_Wery_Giannis_Walking00",
        "sprite_Wery_Giannis_Walking01","sprite_Wery_Giannis_Walking02",
        "sprite_Wery_Giannis_Walking03","sprite_Wery_Giannis_Walking04",
        "sprite_Wery_Giannis_Walking05","sprite_Wery_Giannis_Walking06",
        "sprite_Wery_Giannis_Walking07","sprite_Wery_Giannis_Walking08",
        "sprite_Wery_Giannis_Walking09"]



    
Walking_images_Wery_Giannis_path=os.path.join(image_path,"Wery_Giannis_Walking")
Right_images_Wery_Giannis_path=[os.path.join(Walking_images_Wery_Giannis_path,i+".png") for i in Right_images_Wery_Giannis]

Walking_Right_Wery_Giannis=[pg.image.load(i) for i in Right_images_Wery_Giannis_path]
Walking_Left_Wery_Giannis=[pg.transform.flip(i,True,False) for i in Walking_Right_Wery_Giannis]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Walking_Right_Wery_Giannis_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Right_Wery_Giannis]
Bigger_Walking_Left_Wery_Giannis_400 = [pg.transform.scale(im,(400,400)) for im in Walking_Left_Wery_Giannis]

## Avatar Frond
Frond_images_Wery_Giannis=["Wery_Giannis_Frond"]
Frond_images_folder_Wery_Giannis_path=os.path.join(image_path,"GiannisFrond")
Frond_images_Wery_Giannis_path=[os.path.join(Frond_images_folder_Wery_Giannis_path,i+".png") for i in Frond_images_Wery_Giannis]
Face_Wery_Giannis=[pg.image.load(i) for i in Frond_images_Wery_Giannis_path]

Bigger_Frond_Wery_Giannis_400 = [pg.transform.scale(im,(400,400)) for im in Face_Wery_Giannis]

## Avatar Back
Back_images_Wery_Giannis=["Wery_Giannis_Back"]
Back_images_folder_Wery_Giannis_path=os.path.join(image_path,"GiannisBack")
Back_images_Wery_Giannis_path=[os.path.join(Back_images_folder_Wery_Giannis_path,i+".png") for i in Back_images_Wery_Giannis]
BackHead_Wery_Giannis=[pg.image.load(i) for i in Back_images_Wery_Giannis_path]

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_BackHead_Wery_Giannis_400 = [pg.transform.scale(im,(400,400)) for im in BackHead_Wery_Giannis]

#Falling
Falling_images_Wery_Giannis=["sprite_Wery_Giannis_Falling0","sprite_Wery_Giannis_Falling1",
                   "sprite_Wery_Giannis_Falling2","sprite_Wery_Giannis_Falling3",
                   "sprite_Wery_Giannis_Falling4","sprite_Wery_Giannis_Falling5",
                   "sprite_Wery_Giannis_Falling6","sprite_Wery_Giannis_Falling7",
                   "sprite_Wery_Giannis_Falling8"]

for i in range(500):
    Falling_images_Wery_Giannis.append("sprite_Wery_Giannis_Falling8")
Falling_images_path_Wery_Giannis=os.path.join(image_path,"Wery_Giannis_Falling")
Falling_Right_images_path_Wery_Giannis=[os.path.join(Falling_images_path_Wery_Giannis,i+".png") for i in Falling_images_Wery_Giannis]

Falling_Right_Wery_Giannis=[pg.image.load(i) for i in Falling_Right_images_path_Wery_Giannis]
Falling_Left_Wery_Giannis=[pg.transform.flip(i,True,False) for i in Falling_Right_Wery_Giannis]


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

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Walking_Left_Vamp_100 =[pg.transform.scale(im,(100,100)) for im in Walking_Right_Vamp]
Bigger_Walking_Right_Vamp_100 =[pg.transform.scale(im,(100,100)) for im in Walking_Left_Vamp]
#Falling
Falling_images_Vamp=["sprite_Vampire_Falling0","sprite_Vampire_Falling1",
                   "sprite_Vampire_Falling2","sprite_Vampire_Falling3",
                   "sprite_Vampire_Falling4","sprite_Vampire_Falling5",
                   "sprite_Vampire_Falling6","sprite_Vampire_Falling7",
                   "sprite_Vampire_Falling8"]

for i in range(500):
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

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Frond_400_Vamp = [pg.transform.scale(im,(400,400)) for im in Face_Vamp]

Vampire_gallery_image=["Vampire_Gallery"]
Vampire_gallery_images_folder_path=os.path.join(image_path_Vamp,"Vampire_Gallery")
Vampire_gallery__images_path=[os.path.join(Vampire_gallery_images_folder_path+".png") for i in Vampire_gallery_image]
Vampire_Gallery=[pg.image.load(i) for i in Vampire_gallery__images_path]

Bigger_Frond_400_Vamp = [pg.transform.scale(im,(400,400)) for im in Face_Vamp]


Back_images_Vamp=["Vampire_Back"]
Back_images_folder_path_Vamp=os.path.join(image_path_Vamp,"Vampire_Back")
Back_images_path_Vamp=[os.path.join(Back_images_folder_path_Vamp+".png") for i in Back_images_Vamp]
Back_Vamp=[pg.image.load(i) for i in Back_images_path_Vamp]

########################################################################
#############                   Resizing             ###################
########################################################################

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

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Walking_Left_Wer_100 =[pg.transform.scale(im,(100,100)) for im in Walking_Right_Wer]
Bigger_Walking_Right_Wer_100 =[pg.transform.scale(im,(100,100)) for im in Walking_Left_Wer]

#Falling
Falling_images_Wer=["sprite_WereWolf_Falling0","sprite_WereWolf_Falling1",
                   "sprite_WereWolf_Falling2","sprite_WereWolf_Falling3",
                   "sprite_WereWolf_Falling4","sprite_WereWolf_Falling5",
                   "sprite_WereWolf_Falling6","sprite_WereWolf_Falling7",
                   "sprite_WereWolf_Falling8"]

for i in range(500):
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

########################################################################
#############                   Resizing             ###################
########################################################################

Bigger_Frond_400_Wer = [pg.transform.scale(im,(400,400)) for im in Face_Wer]
Bigger_Frond_300_Wer = [pg.transform.scale(im,(300,300)) for im in Face_Wer]

Werewolf_Facion_image= ["Werewolf_Facion"]
Frond_images_path_Werewolf_Facion_folder_path = os.path.join(image_path_Wer,"Werewolf_Facion")
Frond_images_path_Werewolf_Facion=[os.path.join(Frond_images_path_Werewolf_Facion_folder_path+".png")]
Werewolf_Facion=[pg.image.load(i) for i in Frond_images_path_Werewolf_Facion]

########################################################################
#############                   Resizing             ###################
########################################################################
Bigger_Werewolf_Facion_300 = [pg.transform.scale(im,(300,300)) for im in Werewolf_Facion]
Bigger_Werewolf_Facion_200 = [pg.transform.scale(im,(200,200)) for im in Werewolf_Facion]
Bigger_Werewolf_Facion_100 = [pg.transform.scale(im,(100,100)) for im in Werewolf_Facion]


Back_images_Wer=["Werewolf_Back"]
Back_images_folder_path_Wer=os.path.join(image_path_Wer,"Werewolf_Back")
Back_images_path_Wer=[os.path.join(Back_images_folder_path_Wer+".png") for i in Back_images_Wer]
Back_Wer=[pg.image.load(i) for i in Back_images_path_Wer]

########################################################################
#############                   Resizing             ###################
########################################################################

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
    def __init__(self,player, flps = 10):
        self.next = self
        self.flps = flps
        self.player = player
        self.crashed = False
        
    
    def quitScene(self, events):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)

###############################################################################
###############################################################################
###############################################################################
###########################                           #########################
###########################       Opening Scenes      #########################
###########################                           #########################
###############################################################################
###############################################################################
###############################################################################                  
        
class Introduction(SceneBase):
    def __init__(self, player,flps = 10):
        SceneBase.__init__(self, player,flps)
        self.music_playing = True

    def quitScene(self):

        if self.playButton.pushed:
            self.new_player = Player(70,70,32,32)
            run_game(GameScene(self.new_player))

        if self.introButton.pushed:
            self.SwitchToScene(TitleScene(self.player))
            
        if self.Resume_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.controlsButton.pushed:
            self.SwitchToScene(Control_Keys(self.player))
         
        if self.Sound_Button.pushed:
            if self.music_playing:
                pg.mixer.music.pause()
                self.music_playing = False
            else:
                pg.mixer.music.unpause()
                self.music_playing = True
            
        if self.Quit_Button.pushed:
            self.crashed = True
            
        if self.My_Stuff_Button.pushed:
            self.SwitchToScene(Giannis_Stuff(self.player))
   
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        
        self.welcomefont = pg.font.SysFont("comicsansms", 100)
        self.text1 = self.welcomefont.render("Welcome...", True,black)
        self.screen.blit(self.text1,(50,10))
        
        self.playButton = Button("New Game...", 450, 180, black)
        self.Resume_Button = Button("Resume Game...", 150, 300, black)
        self.introButton = Button("Introduction...", 450, 240,black)
        self.Sound_Button = Button("Sound", 450, 300, black)
        self.controlsButton = Button("Control Keys...", 450, 360, black)
        self.Quit_Button = Button("Quit", 450, 420, black)
        self.My_Stuff_Button = Button("Personal Storage (aka Giannis Stuff)", 550, 500, black, gold)
        
        self.playButton.DrawButton(self.screen)
        self.introButton.DrawButton(self.screen)
        self.Sound_Button.DrawButton(self.screen)
        self.controlsButton.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.My_Stuff_Button.DrawButton(self.screen)
        self.Resume_Button.DrawButton(self.screen)
        
        if self.player.ability_to_be_invisible:
            if self.player.invisible:
                self.Invisible_Button = Button("Invisibility Cloak On/Off", 655, 50, pink, gold)
                self.Invisible_Button.DrawButton(self.screen)
                if self.Invisible_Button.pushed:
                    self.player.invisible = False
            else:
                self.Invisible_Button = Button("Invisibility Cloak On/Off", 655, 50, black, gold)
                self.Invisible_Button.DrawButton(self.screen)
                self.screen.blit(Bigger_Frond_400[0],(600,100))
                if self.Invisible_Button.pushed:
                    self.player.invisible = True
        else:
            self.screen.blit(Bigger_Frond_400[0],(600,100))

###############################################################################
            
class Control_Keys(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Play_Button.pushed:
            self.SwitchToScene(GameScene(self.player))

        if self.Back_Button.pushed:
            self.SwitchToScene(Introduction(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        self.screen.blit(Bigger_Frond_400[0],(600,100))
        
        self.Play_Button = Button("Play", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        
        self.Play_Button.DrawButton(self.screen)
        self.Back_Button.DrawButton(self.screen)
        
        self.text1 = font.render("Right arrow : move right", True,black)
        self.text2 = font.render("Left arrow : move left", True,black)
        self.text3 = font.render("Up arrow : move up", True,black)
        self.text4 = font.render("Down arrow : move down", True,black)
        self.text5 = font.render("Space : Fire", True,black)
        self.text6 = font.render("Enter : next scene", True,black)
        
        self.texts = ((self.text1,(250,140)),(self.text2,(250,180)),(self.text3,(250,220)),
                      (self.text4,(250,260)),(self.text5,(250,300)),(self.text6,(250,340)))
        self.screen.blits(self.texts)
###############################################################################

class Giannis_Stuff(SceneBase):
    def __init__(self, player,flps = 10):
        SceneBase.__init__(self, player,flps)
        
    def quitScene(self):

        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))

        if self.Back_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
   
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Personal Storage Unit", True,black)
        self.screen.blit(self.text1,(50,10))
        
        self.Go_Button = Button("Go", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        self.Go_Button.DrawButton(self.screen)
        self.Back_Button.DrawButton(self.screen)
        
        self.message = "You Have " + str(self.player.coins) + " coins"
        self.message_x = screen_width - 15*(len(self.message))
        self.message_y = 60
        TextMessage(self.screen,self.message,self.message_x, self.message_y, gold, HelloScreenColor)
      
        self.box = pg.Rect(600,100,400,400)
        pg.draw.rect(self.screen, HelloScreenColor, self.box)
        self.screen.blit(Bigger_Frond_400[0],(600,100))
        
        
        if self.player.ability_to_be_invisible:
            if self.player.invisible:
                self.Invisible_Button = Button("Invisibility Cloak On/Off", 300, 180, pink, gold)
                self.Invisible_Button.DrawButton(self.screen)
                pg.draw.rect(self.screen, HelloScreenColor, self.box)
                if self.Invisible_Button.pushed:
                    self.player.invisible = False
                self.player.VampireLook_on = False
                self.player.WerewolfLook_on = False
            else:
                self.Invisible_Button = Button("Invisibility Cloak On/Off", 300, 180, black, gold)
                self.Invisible_Button.DrawButton(self.screen)
                self.screen.blit(Bigger_Frond_400[0],(600,100))
                if self.Invisible_Button.pushed:
                    self.player.invisible = True
        
        
        if self.player.VampireLook and not self.player.injured:
            self.screen.blit(Black_Coat_30,(253,245))
            if self.player.VampireLook_on:
                self.Black_Coat_Button = Button("Vampire Look On/Off", 300, 240, pink, gold)
                self.Black_Coat_Button.DrawButton(self.screen)
                self.screen.blit(Bigger_Frond_Vamp_Giannis_400[0],(600,100))
                if self.Black_Coat_Button.pushed:
                    self.player.VampireLook_on= False
                self.player.WerewolfLook_on = False
                self.player.invisible = False
            else:
                self.Black_Coat_Button = Button("Vampire Look On/Off", 300, 240, black, gold)
                self.Black_Coat_Button.DrawButton(self.screen)
    #               self.screen.blit(Bigger_Frond_400[0],(600,100))
                if self.Black_Coat_Button.pushed:
                    self.player.VampireLook_on = True
                         
        if self.player.WerewolfLook and not self.player.injured:
            self.screen.blit(Werewolf_Wig_100,(220,275))
            if self.player.WerewolfLook_on:
                self.Wig_Button = Button("Werewolf Look On/Off", 300, 300, pink, gold)
                self.Wig_Button.DrawButton(self.screen)
                self.screen.blit(Bigger_Frond_Wery_Giannis_400[0],(600,100))
                if self.Wig_Button.pushed:
                    self.player.WerewolfLook_on = False
                self.player.invisible = False
                self.player.VampireLook_on = False
            else:
                self.Wig_Button = Button("Werewolf Look On/Off", 300, 300, black, gold)
                self.Wig_Button.DrawButton(self.screen)
    #               self.screen.blit(Bigger_Frond_400[0],(600,100))
                if self.Wig_Button.pushed:
                    self.player.WerewolfLook_on = True
        
        if self.player.injured:
            self.text4 = font.render("You are injured", True, red)
            self.screen.blit(self.text4,(300,420))
            self.text5 = font.render("Go Home", True, red)
            self.screen.blit(self.text5,(300,480))
            self.text6 = font.render("Vampire Look On/Off", True, black)
            self.screen.blit(self.text6,(300,240))
            self.text7 = font.render("Werewolf Look On/Off", True, black)
            self.screen.blit(self.text7,(300,300))
                     
                     
        if self.player.number_of_shocks > 0:
            self.screen.blit(Fancy_Shocks,(250,360))
            self.text3 = font.render("You have " + str(self.player.number_of_shocks)+" fancy shocks", True,black)
            self.screen.blit(self.text3,(300,360))
                     
        if not self.player.WerewolfLook:
            if not self.player.VampireLook:
                if not self.player.ability_to_be_invisible:
                    if self.player.number_of_shocks == 0:
#                        self.screen.blit(Bigger_Frond_400[0],(600,100))
                        self.text3 = font.render("You have has nothing... yet", True,black)
                        self.screen.blit(self.text3,(250,250))

       
        
###############################################################################
###############################################################################
###############################################################################
###########################                           #########################
###########################    Story- intro Scenes    #########################
###########################                           #########################
###############################################################################
###############################################################################
###############################################################################
        
class TitleScene(SceneBase):
    def __init__(self, player,flps = 10):
        SceneBase.__init__(self, player,flps)
    
    def quitScene(self):
        self.event=pg.key.get_pressed()
        if self.event[pg.K_RETURN] or self.Next_Button.pushed:
           self.SwitchToScene(TitleScene_2(self.player))
         
        if self.Back_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
            
    
    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.Next_Button = Button("Next", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        self.Next_Button.DrawButton(self.screen)
        self.Back_Button.DrawButton(self.screen)
        
        self.font = pg.font.SysFont("comicsansms", 20)
        self.text1 = font.render("Hello!!", True,black)
        self.text2 = self.font.render("This is Giannis. Giannis lives in a non rotating planet. In a Galaxy far far away...", True,black)
        self.text3 = self.font.render("Once inhabited by humans but not anymore.", True,black)
        self.text4 = self.font.render("On this planet there are now two  dominated species...", True,black)
        self.text5 = self.font.render("Vampires and Werewolfs.", True,black)
        self.text6 = self.font.render("After millenias of conflict between them they finally reach a peaceful", True,black)
        self.text7 = self.font.render("coexistence. The areas of the planet that are neither day", True,black)
        self.text8 = self.font.render("nor night are inhabited by both species.", True,black)
        
        self.texts = ((self.text1,(80 , 100)),(self.text2,(80 , 160)),
                      (self.text3,(80 , 190)),(self.text4,(80 , 220)),
                      (self.text5,(80 , 250)),(self.text6,(80 , 280)),
                      (self.text7,(80 , 310)),(self.text8,(80 , 340)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Frond_400[0],(700,100))
        

class TitleScene_2(SceneBase):
    def __init__(self,player,flps = 10):
        SceneBase.__init__(self,player, flps)
    
    def quitScene(self):
        self.event=pg.key.get_pressed()
        if self.event[pg.K_RETURN] or self.Next_Button.pushed:
           self.SwitchToScene(TitleScene_3(self.player))
         
        if self.Back_Button.pushed:
            self.SwitchToScene(TitleScene(self.player))

    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.Next_Button = Button("Next", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        self.Next_Button.DrawButton(self.screen)
        self.Back_Button.DrawButton(self.screen)
        
        self.font = pg.font.SysFont("comicsansms", 20)
        self.text2 = self.font.render("The called those areas the 'Peace and Friendship' zones", True,black)
        self.text3 = self.font.render("Some hundreds years after their establishment", True,black)
        self.text4 = self.font.render("Their local government went a step further and invested to biological", True,black)
        self.text5 = self.font.render("experiments for creating a mixed-race species.", True,black)
        self.text6 = self.font.render("The optimists said that the goal was the complete union", True,black)
        self.text7 = self.font.render("The others that they were trying to build the perfect soldier to", True,black)
        self.text8 = self.font.render("conquer the rest of the world. Very few know the truth.", True,black)
        
        self.texts = ((self.text2,(80 , 160)),
                      (self.text3,(80 , 190)),(self.text4,(80 , 220)),
                      (self.text5,(80 , 250)),(self.text6,(80 , 280)),
                      (self.text7,(80 , 310)),(self.text8,(80 , 340)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Frond_400[0],(700,100))
        
class TitleScene_3(SceneBase):
    def __init__(self, player,flps = 10):
        SceneBase.__init__(self, player,flps)
    
    def quitScene(self):
        self.event=pg.key.get_pressed()
        if self.event[pg.K_RETURN] or self.Next_Button.pushed:
           self.SwitchToScene(TitleScene_4(self.player))
         
        if self.Back_Button.pushed:
            self.SwitchToScene(TitleScene_2(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.Next_Button = Button("Next", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        self.Next_Button.DrawButton(self.screen)
        self.Back_Button.DrawButton(self.screen)
        
        self.font = pg.font.SysFont("comicsansms", 20)
        self.text2 = self.font.render("What everybody knows is that Giannis is the first successful", True,black)
        self.text3 = self.font.render("'product' of those experiments.", True,black)
        self.text4 = self.font.render("His parents seeking for easy money donated their genetic material.", True,black)
        self.text5 = self.font.render("The excitement of the success had the scientist focusing on making more", True,black)
        self.text6 = self.font.render("The official announcement said that the child was faster than both species", True,black)
        self.text7 = self.font.render("but lacked in strength and he could feed both with meat and blood.", True,black)
        
        
        self.texts = ((self.text2,(80 , 160)),
                      (self.text3,(80 , 190)),(self.text4,(80 , 220)),
                      (self.text5,(80 , 250)),(self.text6,(80 , 280)),
                      (self.text7,(80 , 310)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Frond_400[0],(700,100))


class TitleScene_4(SceneBase):
    def __init__(self,player,flps = 10):
        SceneBase.__init__(self,player, flps)
    
    def quitScene(self):
        self.event=pg.key.get_pressed()
        if self.event[pg.K_RETURN] or self.Next_Button.pushed:
           self.SwitchToScene(TitleScene_5(self.player))
         
        if self.Back_Button.pushed:
            self.SwitchToScene(TitleScene_3(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.Next_Button = Button("Next", 900, 500)
        self.Back_Button = Button("Back", 50, 500)
    
        self.Next_Button.DrawButton(self.screen)
        self.Back_Button.DrawButton(self.screen)
        
        self.font = pg.font.SysFont("comicsansms", 20)
        self.text2 = self.font.render("We do not really know much about his childhood", True,black)
        self.text3 = self.font.render("but we are certain that no one cared for the moral growth", True,black)
        self.text4 = self.font.render("of the child. He received basic education, mostly because", True,black)
        self.text5 = self.font.render("the activists made a fuss about it.", True,black)
        self.text6 = self.font.render("After reaching adulthood he was sent away with a few coins.", True,black)
        self.text7 = self.font.render("he is currently living somewhere in the Peace and Friendship Zone", True,black)
        self.text8 = font.render("And Generally he is too lazy to work", True,black)
        
        self.texts = ((self.text2,(80 , 160)),
                      (self.text3,(80 , 190)),(self.text4,(80 , 220)),
                      (self.text5,(80 , 250)),(self.text6,(80 , 280)),
                      (self.text7,(80 , 310)),(self.text8,(80 , 340)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Frond_400[0],(700,100))
        

class TitleScene_5(SceneBase):
    def __init__(self,player,flps = 10):
        SceneBase.__init__(self,player, flps)
    
    def quitScene(self):
        self.event=pg.key.get_pressed()
        if self.event[pg.K_RETURN] or self.Play_Button.pushed:
           self.SwitchToScene(GameScene(self.player))
         
        if self.Back_Button.pushed:
            self.SwitchToScene(TitleScene_3(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.Play_Button = Button("Play", 900, 50, gold)
        self.Back_Button = Button("Back", 50, 50, gold)
    
        self.Play_Button.DrawButton(self.screen)
        self.Back_Button.DrawButton(self.screen)
        
        self.font = pg.font.SysFont("comicsansms", 20)
        self.text2 = font.render("And he has a stun-Gun", True,black)
        self.text3 = self.font.render("(How he came to possess a bio-lock high technology weapon", True,black)
        self.text4 = self.font.render("is a very interesting story", True,black)
        self.text5 = self.font.render("for another time)", True,black)
        
        self.texts = ((self.text2,(100 , 160)),
                      (self.text3,(80 , 250)),(self.text4,(80 , 280)),
                      (self.text5,(80 , 310)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Frond_400[0],(700,100))
        


class BeatenScene1(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
    
    def quitScene(self):
        self.event=pg.key.get_pressed()
        if self.event[pg.K_RETURN]:
            self.SwitchToScene(GameScene(self.player))
            pg.time.delay(800)

    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        self.screen = screen
        self.screen.fill(LoseScreenColor)
        
        if self.player.beaten_by_Vampire:
            self.text1 = font.render("This Vampire beat you up", True,black)
            if player.coins > 0 :
                self.text2 = font.render("and stole all of your money", True,black)
                self.texts = (self.text1,(300 , 240)),(self.text2,(300 , 280))
                self.screen.blits(self.texts)
            else:
                self.text3 = font.render("And beacause you had no money", True,black)
                self.text4 = font.render("he beat you up again", True,black)
                self.texts = ((self.text1,(300, 240)),(self.text3,(300, 280)),
                              (self.text4,(300 , 320)))
                self.screen.blits(self.texts)
            self.screen.blit(Bigger_Falling_Down_Left_400[8],(600,100))
            
            
        if self.player.beaten_by_Werewolf:
            self.text5 = font.render("This Werewolf beat you up", True,black)
            self.text6 = font.render("just for fun. He didn't care about your money", True,black)
            self.texts = (self.text5,(320 , 240)),(self.text6,(320 , 280))
            self.screen.blits(self.texts)
            self.screen.blit(Bigger_Falling_Down_Left_400[8],(600,100))
            
class BeatenScene2(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
    
    def quitScene(self):
        self.event=pg.key.get_pressed()
        if self.event[pg.K_RETURN]:
            self.SwitchToScene(GameScene(self.player))
            pg.time.delay(800)

    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        self.screen = screen
        self.screen.fill(LoseScreenColor)
        
        if player.beaten_by_Vampire:
            self.text1 = font.render("This Vampire beat you a little bit", True,black)
            self.text2 = font.render("and stole your money", True,black)
            self.texts = (self.text1,(300 , 240)),(self.text2,(300 , 280))
            self.screen.blits(self.texts)
            self.screen.blit(Bigger_Frond_Wery_Giannis_400[0],(600,100))
            
            
        if player.beaten_by_Werewolf:
            self.text5 = font.render("This Werewolf beat you a little bit", True,black)
            self.text6 = font.render("He didn't care about your money", True,black)
            self.texts = (self.text5,(320 , 240)),(self.text6,(320 , 280))
            self.screen.blits(self.texts)
            self.screen.blit(Bigger_Frond_Vamp_Giannis_400[0],(600,100))          
            

###############################################################################
###############################################################################
###############################################################################
###########################                           #########################
###########################     Cloths Shop Scenes    #########################
###########################                           #########################
###############################################################################
###############################################################################
###############################################################################
            
            
##########################################################33

class LookAround(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.message = "You Have " + str(self.player.coins) + " coins"
        self.message_x = screen_width/2 - 5*(len(self.message))
        self.message_y = 515
        TextMessage(self.screen,self.message,self.message_x, self.message_y, black, HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.screen.blit(Bigger_Werewolf_Facion_200 [0],(800,300))
        
        self.screen.blit(Black_Coat_100,(270,200))
        self.BlackCoat_Button = Button("800 coins", 267, 300, black, gold)
                
        self.screen.blit(Werewolf_Wig_200,(420,200))
        self.Wig_Button = Button("200 coins", 460, 350, black, gold)
        
        self.screen.blit(Fancy_Shocks_100,(620,200))
        self.Shocks_Button = Button("20 coins", 640, 300, black, gold)
        
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
    
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        
        self.BlackCoat_Button.DrawButton(self.screen)
        self.Wig_Button.DrawButton(self.screen)
        self.Shocks_Button.DrawButton(self.screen)
        
                
        if self.BlackCoat_Button.pushed:
            if not self.player.VampireLook:           
                self.SwitchToScene(LookAround_Buying_BlackCoat(self.player))
            else:
                self.SwitchToScene(Do_not_waste_my_time(self.player))
                
        if self.Wig_Button.pushed:
            if not self.player.WerewolfLook:           
                self.SwitchToScene(LookAround_Buying_Wig(self.player))
            else:
                self.SwitchToScene(Do_not_waste_my_time(self.player))
        
        if self.Shocks_Button.pushed:
            self.SwitchToScene(LookAround_Buying_Shocks(self.player))
##########################################################33

class LookAround_Buying_BlackCoat(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Back_Button.pushed:
            self.SwitchToScene(LookAround(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.message = "You Have " + str(self.player.coins) + " coins"
        self.message_x = screen_width/2 - 5*(len(self.message))
        self.message_y = 515
        TextMessage(self.screen,self.message,self.message_x, self.message_y, black, HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.screen.blit(Bigger_Werewolf_Facion_200 [0],(800,300))
        
        self.screen.blit(Black_Coat_100,(270,200))
        self.BlackCoat_Button = Button("800 coins", 267, 300, black, gold)
                
        self.screen.blit(Werewolf_Wig_200,(420,200))
        self.Wig_Button = Button("200 coins", 460, 350, black, gold)
        
        self.screen.blit(Fancy_Shocks_100,(620,200))
        self.Shocks_Button = Button("20 coins", 640, 300, black, gold)
        
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
    
        self.Back_Button = Button("Back to shopping", 790, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Back_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        
        self.BlackCoat_Button.DrawButton(self.screen)
        self.Wig_Button.DrawButton(self.screen)
        self.Shocks_Button.DrawButton(self.screen)

        if not self.player.VampireLook:
            if self.player.coins  >= 800:
                self.text2 = font.render("It is yours, enjoy!", True,black)
                self.player.coins -= 800
                self.player.VampireLook = True
            else:
               self.SwitchToScene(Do_not_waste_my_time(self.player))
       
        self.screen.blit(self.text2,(770,220)) 

##########################################################33

class LookAround_Buying_Wig(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Back_Button.pushed:
            self.SwitchToScene(LookAround(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.message = "You Have " + str(self.player.coins) + " coins"
        self.message_x = screen_width/2 - 5*(len(self.message))
        self.message_y = 515
        TextMessage(self.screen,self.message,self.message_x, self.message_y, black, HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.screen.blit(Bigger_Werewolf_Facion_200 [0],(800,300))
        
        self.screen.blit(Black_Coat_100,(270,200))
        self.BlackCoat_Button = Button("800 coins", 267, 300, black, gold)
                
        self.screen.blit(Werewolf_Wig_200,(420,200))
        self.Wig_Button = Button("200 coins", 460, 350, black, gold)
        
        self.screen.blit(Fancy_Shocks_100,(620,200))
        self.Shocks_Button = Button("20 coins", 640, 300, black, gold)
        
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
    
        self.Back_Button = Button("Back to shopping", 790, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Back_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        
        self.BlackCoat_Button.DrawButton(self.screen)
        self.Wig_Button.DrawButton(self.screen)
        self.Shocks_Button.DrawButton(self.screen)

        if not self.player.WerewolfLook:
            if self.player.coins  >= 200:
                self.text2 = font.render("It is yours, enjoy!", True,black)
                self.player.coins -= 200
                self.player.WerewolfLook = True
            else:
               self.SwitchToScene(Do_not_waste_my_time(self.player))
       
        self.screen.blit(self.text2,(770,220)) 
##########################################################
class I_am_not_selling_you_more_shocks(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Back_Button.pushed:
            self.SwitchToScene(LookAround(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
    
        self.message = "You Have " + str(self.player.coins) + " coins"
        self.message_x = screen_width/2 - 5*(len(self.message))
        self.message_y = 515
        TextMessage(self.screen,self.message,self.message_x, self.message_y, black, HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.screen.blit(Bigger_Werewolf_Facion_200 [0],(800,300))
        
        self.screen.blit(Black_Coat_100,(270,200))
        self.BlackCoat_Button = Button("800 coins", 267, 300, black, gold)
                
        self.screen.blit(Werewolf_Wig_200,(420,200))
        self.Wig_Button = Button("200 coins", 460, 350, black, gold)
        
        self.screen.blit(Fancy_Shocks_100,(620,200))
        self.Shocks_Button = Button("20 coins", 640, 300, black, gold)
        
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
    
        self.Back_Button = Button("Back to shopping", 790, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Back_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        
        self.BlackCoat_Button.DrawButton(self.screen)
        self.Wig_Button.DrawButton(self.screen)
        self.Shocks_Button.DrawButton(self.screen)

        self.text2 = font.render("I am not selling", True,black)
        self.screen.blit(self.text2 ,(770,220)) 
        self.text3 = font.render("you more shocks", True,black)
        self.screen.blit(self.text3 ,(770,250))        

##########################################################33

class LookAround_Buying_Shocks(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Back_Button.pushed:
            self.SwitchToScene(LookAround(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.message = "You Have " + str(self.player.coins) + " coins"
        self.message_x = screen_width/2 - 5*(len(self.message))
        self.message_y = 515
        TextMessage(self.screen,self.message,self.message_x, self.message_y, black, HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.screen.blit(Bigger_Werewolf_Facion_200 [0],(800,300))
        
        self.screen.blit(Black_Coat_100,(270,200))
        self.BlackCoat_Button = Button("800 coins", 267, 300, black, gold)
                
        self.screen.blit(Werewolf_Wig_200,(420,200))
        self.Wig_Button = Button("200 coins", 460, 350, black, gold)
        
        self.screen.blit(Fancy_Shocks_100,(620,200))
        self.Shocks_Button = Button("20 coins", 640, 300, black, gold)
        
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
    
        self.Back_Button = Button("Back to shopping", 790, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Back_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        
        self.BlackCoat_Button.DrawButton(self.screen)
        self.Wig_Button.DrawButton(self.screen)
        self.Shocks_Button.DrawButton(self.screen)

        if self.player.number_of_shocks < 5:
            if self.player.coins  >= 20:
                self.player.coins -= 20
                self.SwitchToScene(shocks_Congrats_Scene(self.player))
                
        else:
            self.SwitchToScene(I_am_not_selling_you_more_shocks(self.player)) 
##########################################################

class Do_not_waste_my_time(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Back_Button.pushed:
            self.SwitchToScene(LookAround(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.message = "You Have " + str(self.player.coins) + " coins"
        self.message_x = screen_width/2 - 5*(len(self.message))
        self.message_y = 515
        TextMessage(self.screen,self.message,self.message_x, self.message_y, black, HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_200[0],(0,300))
        self.screen.blit(Bigger_Werewolf_Facion_200 [0],(800,300))
        
        self.screen.blit(Black_Coat_100,(270,200))
        self.BlackCoat_Button = Button("800 coins", 267, 300, black, gold)
                
        self.screen.blit(Werewolf_Wig_200,(420,200))
        self.Wig_Button = Button("200 coins", 460, 350, black, gold)
        
        self.screen.blit(Fancy_Shocks_100,(620,200))
        self.Shocks_Button = Button("20 coins", 640, 300, black, gold)
        
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
    
        self.Back_Button = Button("Back to shopping", 790, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Back_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        
        self.BlackCoat_Button.DrawButton(self.screen)
        self.Wig_Button.DrawButton(self.screen)
        self.Shocks_Button.DrawButton(self.screen)

        self.text2 = font.render("Do not waste my time", True,black)
        self.screen.blit(self.text2,(770,220)) 
##########################################################33

class InvisibilityClothScene_1(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        self.event=pg.key.get_pressed()
        if self.event[pg.K_RETURN]:
            self.SwitchToScene(GameScene(self.player))
            pg.time.delay(800)
        
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        
        if self.Talk_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_Talk(self.player))
        
        if self.View_Button.pushed:
            self.SwitchToScene(LookAround(self.player))


    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300 [0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Talk_Button = Button("Talk to the guy", 300, 240, black)
        self.View_Button = Button("View Store", 300, 280, black)
        
        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.Talk_Button.DrawButton(self.screen)
        self.View_Button.DrawButton(self.screen)

##########################################################33
            

class InvisibilityClothScene_Talk(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        
        if self.Hi_Button.pushed:
            self.SwitchToScene(Hello(self.player))
        
        if self.Question1_Button.pushed:
            self.SwitchToScene(What_is_selling(self.player))
            
        if self.Insullt_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_Talk_insult1(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300 [0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Hi_Button = Button("Hi there Fiernd...", 210, 240, black)
        self.Question1_Button = Button("What are you selling?", 210, 280, black)
        self.Insullt_Button = Button("You Werewolfs are all stinky", 210, 320, black)
        
        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.Hi_Button.DrawButton(self.screen)
        self.Question1_Button.DrawButton(self.screen)
        self.Insullt_Button.DrawButton(self.screen)


##########################################################33

class YouLookLovely(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))

        
        if self.Question1_Button.pushed:
            self.SwitchToScene(What_is_selling(self.player))
            
        if self.Insullt_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_Talk_insult3(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.text3 = font.render("What do you want?", True,black)
        self.screen.blit(self.text3,(600,150))

        
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        
        self.Question1_Button = Button("What are you selling?", 210, 280, black)
        self.Insullt_Button = Button("You stink ...", 210, 320, black)
        
        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.Question1_Button.DrawButton(self.screen)
        self.Insullt_Button.DrawButton(self.screen)

class Hello(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        
        if self.Hi_Button.pushed:
            self.SwitchToScene(YouLookLovely(self.player))
        
        if self.Question1_Button.pushed:
            self.SwitchToScene(What_is_selling(self.player))
            
        if self.Insullt_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_Talk_insult1(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.text3 = font.render("Hi......", True,black)
        self.screen.blit(self.text3,(600,150))

        
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Hi_Button = Button("You look lovely today", 210, 240, black)
        self.Question1_Button = Button("What are you selling?", 210, 280, black)
        self.Insullt_Button = Button("You Werewolfs are all stinky", 210, 320, black)
        
        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.Hi_Button.DrawButton(self.screen)
        self.Question1_Button.DrawButton(self.screen)
        self.Insullt_Button.DrawButton(self.screen)


##########################################################33

class InvisibilityClothScene_Talk_insult1(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        
        
        if self.Question1_Button.pushed:
            self.SwitchToScene(What_is_selling(self.player))
            
        if self.Insullt_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_Talk_insult3(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.text3 = font.render("I have been called worse ", True,black)
        self.screen.blit(self.text3,(500,150))
        self.text2 = font.render("things by better people", True,black)
        self.screen.blit(self.text2,(500,180))
        
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Question1_Button = Button("What are you selling?", 210, 280, black)
        self.Insullt_Button = Button("Seriously!! Every time I meet one of you ", 210, 320, black)
        self.Insullt_Button2 = Button("I have to fart to make you smell better.", 210, 338, black)

        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.Question1_Button.DrawButton(self.screen)
        self.Insullt_Button.DrawButton(self.screen)
        self.Insullt_Button2.DrawButton(self.screen)
        

##########################################################33
        
class What_is_selling(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        
        
        if self.Question1_Button.pushed:
            self.SwitchToScene(SomethingRallyReallyGood(self.player))
        
        if self.Ok_Button.pushed:
            self.SwitchToScene(LookAround(self.player))
            
        if self.Insullt_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_Talk_insult3(self.player))
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.text3 = font.render("Cloths", True,black)
        self.screen.blit(self.text3,(600,150))

        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Question1_Button = Button("Do you have anything really, really, really good?", 210, 240, black)
        self.Ok_Button = Button("Ok! I will look around then.", 210, 280, black)
        self.Insullt_Button = Button("Seriously!! Every time I meet one of you ", 210, 320, black)
        self.Insullt_Button2 = Button("I have to fart to make you smell better.", 210, 338, black)

        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.Question1_Button.DrawButton(self.screen)
        self.Ok_Button.DrawButton(self.screen)
        self.Insullt_Button.DrawButton(self.screen)
        self.Insullt_Button2.DrawButton(self.screen)

##########################################################33
        
class SomethingRallyReallyGood(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        
        
        if self.Question1_Button.pushed:
            self.SwitchToScene(Invisibility(self.player))
            
        if self.Insullt_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_Talk_insult3(self.player))
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.text3 = font.render("With the proper", True,black)
        self.screen.blit(self.text3,(600,150))
        self.text2 = font.render("amount of coins...", True,black)
        self.screen.blit(self.text2,(600,180))

        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Question1_Button = Button("How much and what?", 210, 280, black)
        self.Insullt_Button = Button("Seriously!! Every time I meet one of you ", 210, 320, black)
        self.Insullt_Button2 = Button("I have to fart to make you smell better.", 210, 338, black)

        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.Question1_Button.DrawButton(self.screen)
        self.Insullt_Button.DrawButton(self.screen)
        self.Insullt_Button2.DrawButton(self.screen)

##########################################################33

class Invisibility(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        
        
        if self.Question1_Button.pushed:
            self.SwitchToScene(BuyCloak(self.player))
            
        if self.Insullt_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_Talk_insult3(self.player))
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.text3 = font.render("For 1500 coins I can get", True,black)
        self.screen.blit(self.text3,(500,150))
        self.text2 = font.render(" you an invisibility cloak...", True,black)
        self.screen.blit(self.text2,(500,180))

        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Question1_Button = Button("I want it...", 210, 280, black)
        self.Insullt_Button = Button("Seriously!! Every time I meet one of you ", 210, 320, black)
        self.Insullt_Button2 = Button("I have to fart to make you smell better.", 210, 338, black)

        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.Question1_Button.DrawButton(self.screen)
        self.Insullt_Button.DrawButton(self.screen)
        self.Insullt_Button2.DrawButton(self.screen)

###############################################################################
        
class BuyCloak(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Menu_Button.pushed:
            self.SwitchToScene(Introduction(self.player))


    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Menu_Button = Button("Menu", 50, 50, gold)
        
        self.Yes_Button = Button("Yes!!! Yes!!", 200, 210, black)
        self.No_Button = Button("No. Thanks", 200, 240, black)
        
        self.Go_Button.DrawButton(self.screen)
        self.Menu_Button.DrawButton(self.screen)

        if self.player.coins < 1500:
            self.text5 = font.render("That is not enough money", True,black)
            self.screen.blit(self.text5,(500,150))
            self.text6 = font.render("Do you want sothning else?", True,black)
            self.screen.blit(self.text6,(500,180))
            self.text7 = font.render("We have nice socks", True,black)
            self.screen.blit(self.text7,(500,210))
            self.text8 = font.render("with 20 coins", True,black)
            self.screen.blit(self.text8,(500,240))
                    
            self.Yes_Button.DrawButton(self.screen)
            self.No_Button.DrawButton(self.screen)
            if self.Yes_Button.pushed:
                if self.player.coins >= 20:
                    self.player.coins -= 20
                    self.player.number_of_shocks +=1
                    self.SwitchToScene(shocks_Congrats_Scene(self.player))
                if self.player.coins < 20:
                    self.SwitchToScene(InvisibilityClothScene_GoAway(self.player))  
            if self.No_Button.pushed:
                self.SwitchToScene(InvisibilityClothScene_GoAway(self.player))
        else:
            self.player.coins -= 1500 
            self.SwitchToScene(BuyCloak_2(self.player))
            
##############################################################################
class BuyCloak_2(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Menu_Button.pushed:
            self.SwitchToScene(Introduction(self.player))


    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Menu_Button = Button("Menu", 50, 50, gold)
        
        self.Yes_Button = Button("Yes!!! Yes!!", 200, 210, black)
        self.No_Button = Button("No. Thanks", 200, 240, black)
        
        self.Go_Button.DrawButton(self.screen)
        self.Menu_Button.DrawButton(self.screen)

   
        self.player.ability_to_be_invisible = True
        self.text3 = font.render("Nice doing bussines with you", True,black)
        self.screen.blit(self.text3,(500,150))
        self.text2 = font.render("Please come again", True,black)
        self.screen.blit(self.text2,(500,180))
        self.text1 = font.render("We have beatiful cloths", True,black)
        self.screen.blit(self.text1,(500,210))
                   
            
##############################################################3
                
                
class InvisibilityClothScene_Talk_insult3(SceneBase):
    def __init__(self,player, flps = 10):
        SceneBase.__init__(self,player, flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_GoAway(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        
        if self.Hi_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_GoAway(self.player))
        
        if self.Question1_Button.pushed:
            self.SwitchToScene(InvisibilityClothScene_GoAway(self.player))

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.text3 = font.render("Stop trying to be a smart", True,black)
        self.screen.blit(self.text3,(500,150))
        self.text3 = font.render(" ass, you're just an ass", True,black)
        self.screen.blit(self.text3,(500,180))
        self.text2 = font.render("Go away...", True,black)
        self.screen.blit(self.text2,(500,230))
        
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        
        self.Hi_Button = Button("Hi there Fiernd...", 210, 240, black)
        self.Question1_Button = Button("What are you selling?", 210, 280, black)
        

        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        self.Question1_Button.DrawButton(self.screen)
        self.Hi_Button.DrawButton(self.screen)

##########################################################33
        
class InvisibilityClothScene_GoAway(SceneBase):
    def __init__(self,player ,flps = 10):
        SceneBase.__init__(self, player,flps)
        
    
    def quitScene(self):
        if self.Go_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        

    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.text2 = font.render("Go away", True,black)
        self.screen.blit(self.text2,(600,150))
        
        self.Go_Button = Button("Go", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Go_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)

##########################################################33
        
class shocks_Congrats_Scene(SceneBase):
    def __init__(self,player ,flps = 10):
        SceneBase.__init__(self, player,flps)
        self.player.number_of_shocks += 1
        
    
    def quitScene(self):
        if self.Back_Button.pushed:
            self.SwitchToScene(LookAround(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
        
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_300[0],(0,150))
        self.screen.blit(Bigger_Werewolf_Facion_300[0],(700,150))
        
        self.welcomefont = pg.font.SysFont("comicsansms", 60)
        self.text1 = self.welcomefont.render("Self Presentation store", True,black)
        self.screen.blit(self.text1,(165,50))
        
        self.text2 = font.render("Congratulations!!!! ", True,black)
        self.text3 = font.render("You no have a new pair", True,black)
        self.text4 = font.render(" of  fancy shocks", True,black)
        self.screen.blit(self.text2,(450,150))
        self.screen.blit(self.text3,(450,180))
        self.screen.blit(self.text4,(450,210))
        
        
        self.Back_Button = Button("Back to shopping", 790, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
        
        self.Back_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)




###############################################################################
###############################################################################
###############################################################################
###########################                           #########################
###########################       Galery Scenes      #########################
###########################                           #########################
###############################################################################
###############################################################################
###############################################################################


###########################################################################3333
        
class PauseScene(SceneBase):
    def __init__(self,player , flps = 10):
        SceneBase.__init__(self, player,flps)
        
    
    def quitScene(self):
        if self.Play_Button.pushed:
            self.SwitchToScene(GameScene(self.player))
            
        if self.Quit_Button.pushed:
            self.SwitchToScene(Introduction(self.player))

    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        self.screen.fill(HelloScreenColor)

        self.screen.blit(Bigger_Waving_300[3],(0,200))
        self.screen.blit(Bigger_Walking_Left_Wer_100[18],(200,390))
        self.screen.blit(Bigger_Walking_Right_Vamp_100[0],(300,390))
        self.screen.blit(Bigger_Walking_Left_Wer_100[1],(400,390))
        self.screen.blit(Bigger_Walking_Right_Vamp_100[15],(500,390))
        self.screen.blit(Bigger_Walking_Left_Vamp_100[25],(700,390))
        self.screen.blit(Bigger_Walking_Right_Wer_100[11],(900,390))
        
        
        

        
        self.welcomefont = pg.font.SysFont("comicsansms", 100)
        self.text1 = self.welcomefont.render("Game Paused", True,black)
        self.screen.blit(self.text1,(200,150))
        
        self.Play_Button = Button("Play", 900, 50, gold)
        self.Quit_Button = Button("Quit", 50, 50, gold)
    
        
        self.Play_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)

######################################################

class Lets_steal_all_the_shocks(SceneBase):
    def __init__(self,player, flps = 50):
        SceneBase.__init__(self, player,flps)

    def quitScene(self):
        if self.Back_Button.pushed:
           self.SwitchToScene(GameScene(self.player))
         
        if self.Go_Button.pushed:
            self.player.steal_shocks = True
            self.player.number_of_shocks = random.randint(30,50)
            self.SwitchToScene(GameScene(self.player))
        
    
    def Render(self, screen):
        
        self.screen = screen
        screen.fill(HelloScreenColor)
        
        self.Go_Button = Button("Go to get the shocks", 700, 500, gold)
        self.Back_Button = Button("Back to just shooting", 50, 500, gold)
    
        self.Go_Button.DrawButton(self.screen)
        self.Back_Button.DrawButton(self.screen)
        
        self.text1 = font.render("I am bored", True,black)
        self.text2 = font.render("Let's go steal ", True,black)
        self.text3 = font.render("some shocks", True,black)


        self.texts = ((self.text1,(100 , 140)),(self.text2,(100 , 180)),
                      (self.text3,(100 , 220)))
        self.screen.blits(self.texts) 
        
        
        self.screen.blit(Bigger_Frond_400[0],(600,100))        
#####################################################

class Congrats_for_the_shocks(SceneBase):
    def __init__(self,player, flps = 50):
        SceneBase.__init__(self, player,flps)

    def quitScene(self):
        if self.Back_Button.pushed:
           self.SwitchToScene(End_Game_2(self.player))
         
       
        
    
    def Render(self, screen):
        
        self.screen = screen
        screen.fill(HelloScreenColor)
        
        self.screen.blit(Bigger_Frond_400[0],(600,100))
        
        self.screen.blit(Fancy_Shocks,(310,260))
        self.screen.blit(Fancy_Shocks,(231,465))
        self.screen.blit(Fancy_Shocks,(601,165))
        self.screen.blit(Fancy_Shocks,(901,505))
        self.screen.blit(Fancy_Shocks,(400,40))
        self.screen.blit(Fancy_Shocks_100,(250,360))
        self.screen.blit(Fancy_Shocks_100,(50,50))
        self.screen.blit(Fancy_Shocks_100,(856,25))
        self.screen.blit(Fancy_Shocks_200,(500,340))
        
        self.text1 = font.render("Congratulations!!!!!!!!!!!", True,black)
        self.text2 = font.render("on your ability to steal.......", True,black)
        self.text3 = font.render("You now have", True,black)
        self.text4 = font.render(str(player.number_of_shocks) + " fancy shocks", True, black)


        self.texts = ((self.text1,(100 , 140)),(self.text2,(100 , 180)),
                      (self.text3,(100 , 220)),(self.text4,(120 , 260)))
        self.screen.blits(self.texts)   
        
        
        self.Back_Button = Button("Back to just shooting", 50, 400, gold)
    
        self.Back_Button.DrawButton(self.screen)
#####################################################3

class End_Scene_1(SceneBase):
    def __init__(self,player , flps = 10):
        SceneBase.__init__(self, player,flps)
        
    
    def quitScene(self):
        if self.Restart_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
            
        if self.Quit_Button.pushed:
            self.crashed = True
    
    def Update(self):
        pass
    
    def Render(self, screen):
        
        self.screen = screen
        screen.fill(HelloScreenColor)
        
        self.Restart_Button = Button("New Game", 850, 500, gold)
        self.Quit_Button = Button("Quit", 50, 500, gold)
    
        self.Restart_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        
        self.welcomefont = pg.font.SysFont("comicsansms", 50)
        self.text1 = self.welcomefont.render("Game Ended", True,black)
        self.screen.blit(self.text1,(350,20))
        # For the sake of brevity, the title scene is a blank red screen
        self.text1 = font.render("Congratulations!!!!!!!!!!!", True,black)
        self.text2 = font.render("on your ability to steal.......", True,black)
        self.text3 = font.render("Your total loot is", True,black)
        self.text4 = font.render(str(player.total_stolen_coins) + " coins", True, black)
        self.text5 = font.render("Unfortunately high rate of stealing", True,black)
        self.text6 = font.render("has initiate investigation", True,black)
        self.text7 = font.render("You decide to stay low", True,black)
        self.text8 = font.render("See you next time", True,black)
        
        
        self.texts = ((self.text1,(100 , 140)),(self.text2,(100 , 180)),
                      (self.text3,(100 , 220)),(self.text4,(140 , 260)),
                      (self.text5,(100 , 300)),(self.text6,(100 , 340)),
                      (self.text7,(100 , 380)),(self.text8,(160 , 420)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Bigger_Walking_Right_400[10],(600,100))

###################################################################

class End_Game_2(SceneBase):
    def __init__(self,player , flps = 10):
        SceneBase.__init__(self, player,flps)
        
    
    def quitScene(self):
        if self.Restart_Button.pushed:
            self.SwitchToScene(Introduction(self.player))
            
        if self.Quit_Button.pushed:
            self.crashed = True

    def Render(self, screen):
        
        self.screen = screen
        screen.fill(HelloScreenColor)
        
        self.Restart_Button = Button("New Game", 850, 500, gold)
        self.Quit_Button = Button("Quit", 50, 500, gold)
    
        self.Restart_Button.DrawButton(self.screen)
        self.Quit_Button.DrawButton(self.screen)
        
        self.welcomefont = pg.font.SysFont("comicsansms", 50)
        self.text1 = self.welcomefont.render("Game Ended", True,black)
        self.screen.blit(self.text1,(350,20))
        # For the sake of brevity, the title scene is a blank red screen
        self.text1 = font.render("Unfortunately", True,black)
        self.text2 = font.render("the shop keeper reported the thef", True,black)
        self.text3 = font.render("and informed the police", True,black)
        self.text4 = font.render("about you purchase of the", True,black)
        self.text5 = font.render("invisible cloak", True,black)
        self.text6 = font.render("They came to your house ", True,black)
        self.text7 = font.render("and found the " + str(player.number_of_shocks) + " fancy shocks", True,black)
        self.text8 = font.render("and your gun.", True,black)
        self.text9 = font.render("You are currently in jail.", True,black)
        self.text10 = font.render("See you next time", True,black)
        
        
        self.texts = ((self.text1,(100 , 100)),(self.text2,(120 , 140)),
                      (self.text3,(140 , 180)),(self.text4,(160 , 220)),
                      (self.text5,(100 , 260)),(self.text6,(120 , 300)),
                      (self.text7,(140 , 340)),(self.text8,(160 , 380)),
                      (self.text9,(100 , 420)),(self.text10,(140 , 460)))
        self.screen.blits(self.texts)
        
        self.screen.blit(Giannis_in_Jail_400,(600,100))

                
####################################################3##########        
        
class GameScene(SceneBase):
    def __init__(self,player, flps = 50):
        SceneBase.__init__(self, player,flps)

    def quitScene(self):
        if self.Menu_Button.pushed:
           self.SwitchToScene(Introduction(self.player))
         
        if self.Pause_Button.pushed:
            self.SwitchToScene(PauseScene(self.player))
        
    
    def Render(self, screen):
        self.event=pg.key.get_pressed()
        self.screen = screen
        self.screen.fill(saddlebrown)
        #Vamps and Werewolfs external lists
        redrawGameWindow(self.screen, self.player, Vamps, Werewolfs)
        
        self.tailor = Tailor(895,115,32,32)
        self.tailor.MeetingPalyer(self.player)
        
        
        self.Pause_Button = Button("Pause", 900, 500, gold)
        self.Menu_Button = Button("Menu", 50, 500, gold)
    
        self.Pause_Button.DrawButton(self.screen)
        self.Menu_Button.DrawButton(self.screen)
        
        self.player.beaten_by_Werewolf = False
        self.player.beaten_by_Vampire = False
       
        
        self.message = "You Have " + str(self.player.coins) + " coins"
        self.message_x = screen_width - 14*(len(self.message))
        self.message_y = 40
        TextMessage(self.screen,self.message,self.message_x, self.message_y, gold, saddlebrown)
            ### Moving the avatar
        self.player.movement(self.screen,walls,BuildingsSurface,VampsANDWerewolfs)
        if not self.player.dying:
            ShootingBullets(Bullets_x, Bullets_y,self.player,self.event,walls)
        else:
            for bullet in Bullets_x:
                Bullets_x.pop(Bullets_x.index(bullet))
                Bullets.pop(Bullets.index(bullet))
            for bullet in Bullets_y:
                Bullets_y.pop(Bullets_y.index(bullet))
                Bullets.pop(Bullets.index(bullet))
                
        if self.player.Beaten:
            self.player.Beaten = False
            self.player.Get_Up(1000)
            if not self.player.WerewolfLook_on and not self.player.VampireLook_on:
                self.SwitchToScene(BeatenScene1(self.player))
            else:
                self.SwitchToScene(BeatenScene2(self.player))
                
        if self.player.total_stolen_coins > 8000:
            self.SwitchToScene(End_Scene_1(self.player))
            
        if self.tailor.talking:
            self.tailor.talking = False
            if self.player.steal_shocks:
                if player.invisible:
                    self.SwitchToScene(Congrats_for_the_shocks(self.player))
            else:
                self.SwitchToScene(InvisibilityClothScene_1(self.player))
                
        if self.player.ability_to_be_invisible:
            if self.player.coins > 4000:
                if self.player.number_of_shocks == 5:
                    self.SwitchToScene(Lets_steal_all_the_shocks(self.player))
            
        pg.display.update()   

     
        
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
        self.speed = 2
        #Avatar's size
        self.width = width
        self.height = height
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
        self.unconsious = False
    
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
    
    def Get_Up(self , waiting = 18000):
        self.waiting = waiting
        if self.unconsious and self.actionTime.waitingAct(self.waiting):
            self.unconsious = False
                   
    def Collision(self, obj, message = None):
        self.message = message
        self.obj = obj
        ## moving left
        if self.right:
            self.hitbox.left = self.obj.hitbox.right
            self.DoNothing()
            self.x -=6                     
        ## moving right
        if self.left:
            self.hitbox.right = self.obj.hitbox.left
            self.DoNothing()
            self.x +=6
        ## moving up
        if self.back:
            self.hitbox.top = self.obj.hitbox.bottom
            self.DoNothing()
            self.y+=5
        ## moving up
        if self.frond:
            self.hitbox.bottom = self.obj.hitbox.top
            self.DoNothing()
            self.y-=5
        if self.message != None:
                self.TextMessage(self.screen ,self.message, self.x, self.y)        


    def drawAvatar(self, gameDisplay):
        self.gameDisplay = gameDisplay
            

 
###############################################################################
#######################            PLAYER            ##########################
###############################################################################
       
class Player(Avatar): 
    
    def __init__(self, x, y, width, height):
        Avatar.__init__(self, x, y, width, height)
        self.speed = 3.5
        self.Beaten = False
        self.beaten_by_Vampire = False
        self.beaten_by_Werewolf = False 
        self.coins = 0
        self.injured = False
        self.total_stolen_coins = 0
        self.inside = []
        self.ability_to_be_invisible = False
        self.invisible = False
        self.VampireLook = False
        self.WerewolfLook = False
        self.VampireLook_on = False
        self.WerewolfLook_on = False
        self.number_of_shocks = 0
        self.steal_shocks = False
       
        

 
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
        else:
            #dispalying action
            self.screen.blit(Face[0],(self.x,self.y))

    def movement(self,screen, walls, BuildingsSurface, enemies):
        self.enemies = enemies
        self.walls = walls
        self.BuildingsSurface = BuildingsSurface
        self.screen = screen
        self.moving_keys=pg.key.get_pressed()
        self.dying = False
        if self.x < 120 and self.y < 120:
            self.injured = False
        if self.injured:
            self.speed = 2.2
        else:
            self.speed = 3.5
        if not self.dying:
            self.Free_to_move = True
        #self.Free_to_move moving left and right
        if self.Free_to_move:
            self.Enemy_Encounter(self.enemies)
            if self.speed > 0:
                # moving left and right
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
                else:
                    self.WalkCount = 0
            
            if self.speed < 0:
                #moving left and right
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
                else:
                    self.DoNothing()

            ###############################################################
            ###    Checking for Walls    ##################################
            ###############################################################
            for wall in self.walls:
                if self.hitbox.colliderect(wall):
                    self.Collision(wall,"I can't go through the wall...")
     
    ###############################################################
    ###     Meeting Hostiles     ##################################
    ###############################################################            
    def Enemy_Encounter(self, enemies):
        self.enemies = enemies
        for enemy in self.enemies:
            if not self.invisible:
                if  not enemy.unconsious:
                    if enemy.AttackingBox.colliderect(self.hitboxBody):
                        if not self.dying:
                            if not self.VampireLook_on and not self.WerewolfLook_on:
                                enemy.Attacking(self)
                                if enemy.Attacking(self):
                                    self.dying = True
                                    self.Person_to_Beat_You = enemy
                                    self.injured = True
                                    enemy.Free_to_move = True
                                    self.Free_to_move = False
                                    if enemy in Vamps:
                                        enemy.coins += self.coins
                                        self.coins = 0
                                        self.beaten_by_Vampire = True
                                    else:
                                        self.beaten_by_Werewolf = True
                                else:
                                    pass
                            elif self.VampireLook_on and enemy in Werewolfs:
                                enemy.Attacking(self)
                                if enemy.Attacking(self):
                                    self.dying = True
                                    self.Person_to_Beat_You = enemy
                                    enemy.Free_to_move = True
                                    self.Free_to_move = False
                                    self.beaten_by_Werewolf = True
                                    
                            elif self.WerewolfLook_on and enemy in Vamps:
                                enemy.Attacking(self)
                                if enemy.Attacking(self):
                                    self.dying = True
                                    self.Person_to_Beat_You = enemy
                                    enemy.Free_to_move = True
                                    self.Free_to_move = False
                                    enemy.coins += self.coins
                                    self.coins = 0
                                    self.beaten_by_Vampire = True
                            else:
                                pass
                else: 
                    if self.hitboxBody.colliderect(enemy.hitboxBody):
                        self.coins += enemy.coins
                        self.total_stolen_coins += enemy.coins
                        enemy.coins = 0
            else: 
                if enemy.unconsious:
                    if self.hitboxBody.colliderect(enemy.hitboxBody):
                        self.coins += enemy.coins
                        self.total_stolen_coins += enemy.coins
                        enemy.coins = 0
        if self.Beaten:
            self.Person_to_Beat_You.x +=300
            self.Person_to_Beat_You.attacking = False

        ####################################
        ###    Checking for Buildings    ###
        ####################################

        if self.hitboxBody.collidelist(self.BuildingsSurface) ==-1:
            self.inside = False
        else:
            self.inside = True
                
        
    def drawAvatar(self, screen):
        self.screen = screen
        Avatar.drawAvatar(self, self.screen)
        #walking image number of frames
        if self.WalkCount + 1 > 27:
            self.WalkCount = 0
        if self.DyingCount + 1 > 31:
            self.DyingCount = 0
            self.Beaten = True
        if not self.invisible:
            if not self.WerewolfLook_on:
                if not self.VampireLook_on:
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
                        if self.number_of_shocks == 0:
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
                        else:
                            if self.right and not self.dying:
                                # count time after this action
                                self.actionTime=timeUnit()
                                #dispalying action
                                self.screen.blit(Walking_Right_Beaten_NewShocks[self.WalkCount],(self.x,self.y))
                                self.WalkCount+=1
                            elif self.left and not self.dying:
                                # count time after this action
                                self.actionTime=timeUnit()
                                #dispalying action
                                self.screen.blit(Walking_Left_Beaten_NewShocks[self.WalkCount],(self.x,self.y))
                                self.WalkCount+=1
                            elif self.back and not self.dying:
                                # count time after this action
                                self.actionTime=timeUnit()
                                #dispalying action
                                self.screen.blit(BackHead_Beaten_NewShocks[0],(self.x,self.y))    
                            elif (self.frond  or self.stand) and not self.dying:
                                    # count time after this action
                                self.actionTime=timeUnit()
                                    #dispalying action
                                self.screen.blit(Face_Beaten_NewShocks[0],(self.x,self.y))
                            elif self.dying:
                                self.actionTime=timeUnit()
                                self.screen.blit(Falling_Down_Left[self.DyingCount],(self.x,self.y))
                                self.DyingCount += 1
                            else:                                   
                               self.screen.blit(Face_Beaten_NewShocks[0],(self.x,self.y))
                
                else:
                    if self.right and not self.dying:
                            # count time after this action
                        self.actionTime=timeUnit()
                        #dispalying action
                        self.screen.blit(Walking_Right_Vamp_Giannis[self.WalkCount],(self.x,self.y))
                        self.WalkCount+=1
                    elif self.left and not self.dying:
                        # count time after this action
                        self.actionTime=timeUnit()
                        #dispalying action
                        self.screen.blit(Walking_Left_Vamp_Giannis[self.WalkCount],(self.x,self.y))
                        self.WalkCount+=1
                    elif self.back and not self.dying:
                        # count time after this action
                        self.actionTime=timeUnit()
                        #dispalying action
                        self.screen.blit(BackHead_Vamp_Giannis[0],(self.x,self.y))    
                    elif (self.frond  or self.stand) and not self.dying:
                        # count time after this action
                        self.actionTime=timeUnit()
                        #dispalying action
                        self.screen.blit(Face_Vamp_Giannis[0],(self.x,self.y))
                    elif self.dying:
                        self.actionTime=timeUnit()
                        self.screen.blit(Falling_Left_Vamp_Giannis[self.DyingCount],(self.x,self.y))
                        self.DyingCount += 1
                    else:                                   
                        self.screen.blit(Face_Vamp_Giannis[0],(self.x,self.y))
            else:
                if self.right and not self.dying:
                    # count time after this action
                    self.actionTime=timeUnit()
                    #dispalying action
                    self.screen.blit(Walking_Right_Wery_Giannis[self.WalkCount],(self.x,self.y))
                    self.WalkCount+=1
                elif self.left and not self.dying:
                    # count time after this action
                    self.actionTime=timeUnit()
                    #dispalying action
                    self.screen.blit(Walking_Left_Wery_Giannis[self.WalkCount],(self.x,self.y))
                    self.WalkCount+=1
                elif self.back and not self.dying:
                    # count time after this action
                    self.actionTime=timeUnit()
                    #dispalying action
                    self.screen.blit(BackHead_Wery_Giannis[0],(self.x,self.y))    
                elif (self.frond  or self.stand) and not self.dying:
                    # count time after this action
                    self.actionTime=timeUnit()
                    #dispalying action
                    self.screen.blit(Face_Wery_Giannis[0],(self.x,self.y))
                elif self.dying:
                    self.actionTime=timeUnit()
                    self.screen.blit(Falling_Left_Wery_Giannis[self.DyingCount],(self.x,self.y))
                    self.DyingCount += 1
                else:                                   
                    self.screen.blit(Face_Wery_Giannis[0],(self.x,self.y))
                
    def TextMessage(self,screen, message, x, y,color = gold):
        self.screen = screen
        self.message = message
        self.color = color
        if not self.invisible:
            if not self.WerewolfLook_on:
                if not self.VampireLook_on:
                    if self.injured:
                        self.screen.blit(Face_Beaten[0],(self.x,self.y))
                    else:
                        self.screen.blit(Face[0],(self.x,self.y))
                else:
                    self.screen.blit(Face_Vamp_Giannis[0],(self.x,self.y))
            else:
                self.screen.blit(Face_Wery_Giannis[0],(self.x,self.y))
        self.text = font.render(self.message, True, self.color)
        self.box=pg.Rect(self.x, self.y-self.text.get_height(),self.text.get_width(),self.text.get_height())
#        pg.draw.rect(self.screen, white, self.box)
        self.screen.blit(self.text,(x,y-self.text.get_height()))



###############################################################################
#######################            Enemies            #########################
###############################################################################

class PeopleThatDislikePlayer(Avatar):
            
    def __init__(self, x, y, width, height, x_end , y_end,Buildings):
        Avatar.__init__(self, x, y, width, height)
        self.x_end = x_end
        self.y_end = y_end
        self.path_x = [self.x, self.x_end]
        self.path_y = [self.y, self.y_end]
        self.random = random.randint(0, 10)
        self.AttackingBox = pg.Rect((self.x+40), self.y, 80, 32)
        self.coins = random.randint(50, 200)
        self.unconsious = False
        self.hits = 0
        self.Buildings = Buildings

    def Hit(self):
        if self.hits == 20:
            self.hits = 0
            self.WalkCount = 0
            self.shootDown = True
            self.speed = 0
            self.unconsious = True
            self.actionTime=timeUnit()
            
    def Collision(self, obj, message = None):
        self.obj = obj
        ## moving left
        if self.right:
            self.hitboxBody.left = self.obj.right
            self.x -=4
            self.speed = (-1)*self.speed
        ## moving right
        if self.left:
            self.hitboxBody.right = self.obj.left
            self.x +=4
            self.speed = (-1)*self.speed
        ## moving up
        if self.back:
            self.hitboxBody.top = self.obj.bottom
            self.y+=5
            self.speed = (-1)*self.speed
        if self.frond:
            self.hitboxBody.bottom = self.obj.top
            self.y-=5
            self.speed = (-1)*self.speed
        
    def MoneyMoneyMoney(self):
        pass         
                
    def Attacking(self, player):
        self.player = player
        if not self.player.inside: 
            self.uncoinsious = False
            self.x = self.player.x
            self.y = self.player.y
            self.speed = 0
            self.player.speed = 0
            self.Free_to_move = False
            return True
        else:
            return False
        
    def drawAvatar(self, screen):
        self.screen = screen
        self.movement()
#        self.movement(self.BuildingsSurface)
        #walking image number of frames
        if self.WalkCount+1>27:
            self.WalkCount=0
        if self.StandingCount+1 > 800:
            self.StandingCount=0
            self.unconsious = False
    
    def movement(self):
        
        self.Hit()
        self.inside = True
        if self.unconsious:
            self.Get_Up()
            self.MoneyMoneyMoney()
            self.Free_to_move = False
        else:
            self.Free_to_move = True
            
      
        if self.Free_to_move:
            if self.speed > 0:
                if self.random < 5:
                    if (self.x + self.speed) < self.path_x[1] :
                        self.x += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x+4), self.y-32, 80, 100)
                        self.DoRight()
                    else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-74), self.y-32, 80, 100)
                        self.DoLeft()
                else:
                     if (self.y +self.speed) < self.path_y[1]:
                        self.y += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y, 72, 92)
                        self.DoFace()   
                     else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-32), self.y-55, 72, 92)
                        self.DoBack()
            else:
                if self.random < 5:
                    if  (self.x +self.speed) > self.path_x[0] :
                        self.x += self.speed
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-74), self.y-32, 100, 100)
                        self.DoLeft()
                    else:
                        self.speed = (-1)*self.speed
                        self.WalkCount = 0
                        self.random = random.randint(0, 10)
                        self.hitboxBody=pg.Rect((self.x+4), self.y, 20, 32)
                        self.AttackingBox = pg.Rect((self.x-54), self.y-32, 100, 100)
                        self.DoRight()

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


           ####################################
           ###    Checking for Buildings    ###
           ####################################
            for building in self.Buildings:
                if building.colliderect(self.hitboxBody):
                    self.inside = True
                    self.Collision(building)
                else:
                    self.inside = False

                          
                        
###############################################################################
#######################            Vampire            #########################
###############################################################################


class Vampire(PeopleThatDislikePlayer): 

    def __init__(self, x, y, width, height, x_end , y_end,Buildings):
        PeopleThatDislikePlayer.__init__(self, x, y, width, height, x_end , y_end,Buildings)
    
    def MoneyMoneyMoney(self):
        if not self.unconsious and self.coins == 0:
            self.coins = random.randint(50, 200) 
    
    def movement(self):
        PeopleThatDislikePlayer.movement(self)
        
    def drawAvatar(self, screen):
        PeopleThatDislikePlayer.drawAvatar(self, screen)
        if self.speed > 0:
            if self.random < 5:
                self.screen.blit(Walking_Right_Vamp[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            else:
                self.screen.blit(Face_Vamp[0],(self.x,self.y))
                self.WalkCount+=1
        elif self.speed < 0:
            if self.random < 5:
                self.screen.blit(Walking_Left_Vamp[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            else:
                self.screen.blit(Back_Vamp[0],(self.x,self.y))
                self.WalkCount+=1
        else:
            self.WalkCount = 0
            if self.unconsious:
                self.screen.blit(Falling_Right_Vamp[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1
            else:
                self.screen.blit(Face_Vamp[0],(self.x,self.y))
                self.StandingCount=0
                self.speed = 2

            
        

###############################################################################
#######################         WereWolf             ##########################
###############################################################################


class WereWolf(PeopleThatDislikePlayer): 

    def __init__(self, x, y, width, height, x_end , y_end,Buildings):
        PeopleThatDislikePlayer.__init__(self, x, y, width, height, x_end , y_end,Buildings)
    
    def MoneyMoneyMoney(self):
        if  not self.unconsious and self.coins == 0:
            self.coins = random.randint(10, 70) 
            
    def movement(self):
        PeopleThatDislikePlayer.movement(self)
        
    def drawAvatar(self, screen):
        PeopleThatDislikePlayer.drawAvatar(self, screen)
        #walking image number of frames
        if self.WalkCount+1>27:
            self.WalkCount=0
        if self.StandingCount+1 > 800:
            self.StandingCount=0
            self.unconsious = False
        if self.speed > 0:
            if self.random < 5:
                self.screen.blit(Walking_Right_Wer[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            else:
                self.screen.blit(Face_Wer[0],(self.x,self.y))
                self.WalkCount+=1
        elif self.speed < 0:
            if self.random < 5:
                self.screen.blit(Walking_Left_Wer[self.WalkCount],(self.x,self.y))
                self.WalkCount+=1
            else:
                self.screen.blit(Back_Wer[0],(self.x,self.y))
                self.WalkCount+=1
        else:
            self.WalkCount = 0
            if self.unconsious:
                self.screen.blit(Falling_Left_Wer[self.StandingCount],(self.x,self.y))
                self.StandingCount+=1
            else:
                self.screen.blit(Face_Wer[0],(self.x,self.y))
                self.StandingCount=0
                self.speed = 2
                
    

###############################################################################
#######################           Mechants            #########################
###############################################################################

class Mechants(Avatar):
            
    def __init__(self, x, y, width, height):
        Avatar.__init__(self, x, y, width, height)
        self.talking = False
                

    def drawAvatar(self, screen):
        self.screen = screen
        pass

    def MeetingPalyer(self,player):
        self.player = player
        if self.hitboxBody.colliderect(self.player.hitbox):
            self.talking = True         
            self.player.Collision(self)
                
            
###############################################################################
#######################           Mechants            #########################
###############################################################################

class Tailor(Mechants):
            
    def __init__(self, x, y, width, height):
        Avatar.__init__(self, x, y, width, height)
        self.talking = False
                

    def drawAvatar(self, screen):
        self.screen = screen
        self.screen.blit(Werewolf_Facion[0],(self.x,self.y))

      
###############################################################################
#######################           Gallerist           #########################
###############################################################################

class Gallerist(Mechants):
            
    def __init__(self, x, y, width, height):
        Avatar.__init__(self, x, y, width, height)
        self.talking = False
                

    def drawAvatar(self, screen):
        self.screen = screen
        self.screen.blit(Vampire_Gallery[0],(self.x,self.y))

      
         
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

    def DrawShoot(self, screen):
        self.screen = screen
        pg.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)               
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
        # append to an external list
        walls.append(self)
        
class rectWall(Wall):
    def __init__(self, x, y, width, height):
        Wall.__init__ (self, x, y, width, height)
        self.hitbox = self.rect
#        pg.draw.rect(gameDisplay, red, self.rect)

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
        # append to an external list
        doors.append(self)
    
class Building(pg.Rect):
    
    def __init__(self,x_begin, y_begin, x_end, y_end, door , BuildingsSurface):
        self.x_begin = x_begin
        self.x_end = x_end
        self.y_begin = y_begin
        self.y_end = y_end
        self.width = x_end - x_begin
        self.height = y_end - y_begin
        pg.Rect.__init__(self, x_begin, y_begin, self.width, self.height)
        self.WallWidth = 10
        self.door = door
        self.BuildingsSurface = BuildingsSurface

        
        self.paintingBuilding=pg.Rect(self.x_begin-10, self.y_begin, self.width+20, self.height+10)
#        pg.draw.rect(gameDisplay, red,  self.paintingBuilding)
        # append to an external list
        self.BuildingsSurface.append(self.paintingBuilding)
        
        
        ### The Door is on the LEft side
        if self.door.x == self.x_begin:
            self.DoorWallLenght1 = self.door.y - self.y_begin
            self. DoorWallLenght2 = self.y_end - (self.door.y + self.door.length)
            #Left
            rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.DoorWallLenght1)
#            wall1=rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.DoorWallLenght1)
#            pg.draw.rect(gameDisplay, red, wall1.rect)
            rectWall(self.x_begin, self.door.y + self.door.length , self.WallWidth, self.DoorWallLenght2)
#            wall2=rectWall(self.x_begin, self.door.y + self.door.length , self.WallWidth, self.DoorWallLenght2)
#            pg.draw.rect(gameDisplay, red, wall2.rect)
            #Τop
            rectWall(self.x_begin, self.y_begin, self.width, self.WallWidth)
#            wall3=rectWall(self.x_begin, self.y_begin, self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall3.rect)
            #Bottom
            rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
#            wall4=rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall4.rect)
            #Right
            rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)
#            wall5=rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)
#            pg.draw.rect(gameDisplay, red, wall5.rect)
        
        
                ### The Door is on the Right side
        if self.door.x == (self.x_end - self.WallWidth):
            self.DoorWallLenght1 = self.door.y - self.y_begin
            self.DoorWallLenght2 = self.y_end - (self.door.y + self.door.length)
            #Left
            rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
#            wall1 = rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
#            pg.draw.rect(gameDisplay, red, wall1.rect)
            #Τop
            rectWall(self.x_begin, self.y_begin, self.width, self.WallWidth)
#            wall2 = rectWall(self.x_begin, self.y_begin, self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall2.rect)
            #Bottom
            rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
#            wall3 =rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall3.rect)
            #Right
            rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.DoorWallLenght1)
#            wall4 = rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.DoorWallLenght1)
#            pg.draw.rect(gameDisplay, red, wall4.rect)
            rectWall(self.x_end - self.WallWidth, self.door.y + self.door.length , self.WallWidth, self.DoorWallLenght2)
#            wall5 = rectWall(self.x_end - self.WallWidth, self.door.y + self.door.length , self.WallWidth, self.DoorWallLenght2)
#            pg.draw.rect(gameDisplay, red, wall5.rect)
                        ### The Door is on the Top side
        
        if self.door.y == self.y_begin:
            self.DoorWallLenght2 = self.x_end - (self.door.x + self.door.length)
            #Left
            rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
#            wall1=rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
#            pg.draw.rect(gameDisplay, red, wall1.rect)
            #Τop
            rectWall(self.x_begin, self.y_begin , self.door.length, self.WallWidth)
#            wall2=rectWall(self.x_begin, self.y_begin , self.door.length, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall2.rect)
            rectWall(self.door.x + self.door.length, self.y_begin, self.DoorWallLenght2 , self.WallWidth)
#            wall3=rectWall(self.door.x + self.door.length, self.y_begin, self.DoorWallLenght2 , self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall3.rect)
            #Bottom
            rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
#            wall4=rectWall(self.x_begin, self.y_end, self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall4.rect)
            #Right
            rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)
#            wall5=rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)
#            pg.draw.rect(gameDisplay, red, wall5.rect)

                        ### The Door is on the Bottom side
        if self.door.y == self.y_end:
            self.DoorWallLenght1 = self.WallWidth + self.door.x + self.door.length
            self.DoorWallLenght2 = self.x_end - self.DoorWallLenght1
            #Left
            rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
#            wall1=rectWall(self.x_begin, self.y_begin, self.WallWidth,  self.height)
#            pg.draw.rect(gameDisplay, red, wall1.rect)
            #Τop
            rectWall(self.x_begin, self.y_begin , self.width, self.WallWidth)
#            wall2=rectWall(self.x_begin, self.y_begin , self.width, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall2.rect)
            #Bottom
            rectWall(self.x_begin, self.y_end, self.door.length, self.WallWidth)
#            wall4=rectWall(self.x_begin, self.y_end, self.door.length, self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall4.rect)
            rectWall(self.door.x + self.door.length, self.y_end, self.DoorWallLenght2 , self.WallWidth)
#            wall3=rectWall(self.DoorWallLenght1, self.y_end, self.DoorWallLenght2 , self.WallWidth)
#            pg.draw.rect(gameDisplay, red, wall3.rect)
            #Right
            rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)
#            wall5=rectWall(self.x_end - self.WallWidth, self.y_begin, self.WallWidth, self.height)
#            pg.draw.rect(gameDisplay, red, wall5.rect)

           
###############################################################################
#######################           Time Unit           #########################
###############################################################################            
            
class timeUnit():
    def __init__(self ):
        self.last = pg.time.get_ticks()

    def waitingAct(self, waiting = 3000):
        self.waiting = waiting
        self.stop = 3*waiting
        self.now = pg.time.get_ticks()
        if self.now - self.last >= self.waiting and self.now - self.last < self.stop:
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
    pg.display.set_caption('Giannis(Not_so_much)Adventures')
    
    
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
  
def redrawGameWindow(screen, avatar, Vamps, Werewolfs):
    ### Painting's Gallery        
    
    drawBackground()
    gameDisplay.blit(gallery,(600,360))
    Building(648,408,752,502,Door(648,445,10,30),BuildingsSurface)
    
    ###Giannis Home
    gameDisplay.blit(GiannisHome,(20,20))
    Building(50,40,175,160,Door(165,100,10,30),BuildingsSurface)
    
    
    ### Cloth shop
    gameDisplay.blit(ClothShop,(760,30))
    Building(790,60,960,160,Door(830,160,10,25),BuildingsSurface)
    
    
    gallerist.drawAvatar(screen)
    tailor.drawAvatar(screen)
    
    avatar.drawAvatar(screen)
        
        
    for bullet in Bullets_x:
        bullet.DrawShoot(screen)
    for bullet in Bullets_y:
        bullet.DrawShoot(screen)
            
    for vamp in Vamps:
        vamp.drawAvatar(screen)
#        pg.draw.rect(gameDisplay, white, vamp.AttackingBox,2)

    for wery in Werewolfs:
        wery.drawAvatar(screen)
    
        
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




def Attacking(enemy, player, waiting = 100, attacking = False):
    enemy.player = player
    if enemy.AttackingBox.colliderect(player.hitboxBody):
        enemy.x = enemy.player.x
        enemy.y = enemy.player.y
        enemy.speed = 0
        enemy,player = 0
        attacking = True
    return attacking


                  

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
    pg.Rect(x-10,y-text.get_height(),text.get_width()+24,text.get_height())
#    box=pg.Rect(x-10,y-text.get_height(),text.get_width()+24,text.get_height())
#    pg.draw.rect(screen, colorBox, box)    
    screen.blit(text,(x,y-text.get_height()))

###############################################################################
################             Random Vampire             #######################
###############################################################################
    
def CreateVampire():
    x1 = random.randint(-32,1032)
    x2 = random.randint(-32,1032)+x1
    y1 = random.randint(-32,582)
    y2 = random.randint(-32,582)+y1
    if abs(x1-x2)>200 and abs(y1-y2)>200:
        Vamp = Vampire (x1,y1,32,32,x2,y2,BuildingsSurface)
        if Vamp.hitboxBody.collidelist(BuildingsSurface) ==-1:
            return Vamp  
        else:
            return CreateVampire()
    else:
        return CreateVampire()

###############################################################################
################             Random WereWolf            #######################
###############################################################################
    
def CreateWerewolf():
    x1 = random.randint(-32,1032)
    x2 = random.randint(-32,1032)+x1
    y1 = random.randint(-32,582)
    y2 = random.randint(-32,582)+y1
    if abs(x1-x2)>200 and abs(y1-y2)>200:
        Werewolf = WereWolf (x1,y1,32,32,x2,y2,BuildingsSurface)
        if Werewolf.hitboxBody.collidelist(BuildingsSurface) ==-1:
            return Werewolf  
        else:
            return CreateWerewolf()
    else:
        return CreateWerewolf()



###############################################################################
######################                                   ######################
######################              Shooting             ######################
######################                                   ######################
###############################################################################
def ShootingBullets(Bullets_x, Bullets_y, avatar, key ,walls):
        
    newBullet_x = round(avatar.x + avatar.width/2)
    newBullet_y = round(avatar.y + avatar.height/3)
    facing_x = 0
    facing_y = 0
    for bullet in Bullets_x:
        if bullet.x < avatar.x + 220 and bullet.x > avatar.x - 220 :
            bullet.x += bullet.speed
            bullet.hitbox = pg.Rect((bullet.x-bullet.radius),bullet.y-bullet.radius , 2*bullet.radius,2*bullet.radius)
        else:
            Bullets_x.pop(Bullets_x.index(bullet))
            Bullets.pop(Bullets.index(bullet))

    for bullet in Bullets_y:
        if bullet.y < avatar.y + 200 and bullet.y > avatar.y - 200:
            bullet.y += bullet.speed
            bullet.hitbox = pg.Rect((bullet.x-bullet.radius),bullet.y-bullet.radius , 2*bullet.radius,2*bullet.radius)
        else:
            Bullets_y.pop(Bullets_y.index(bullet))
            Bullets.pop(Bullets.index(bullet))
    
    
    for building in BuildingsSurface:
        for bullet in Bullets_x:
            if building.colliderect(bullet.hitbox):
                Bullets_x.pop(Bullets_x.index(bullet))
                Bullets.pop(Bullets.index(bullet))
        for bullet in Bullets_y:
            if building.colliderect(bullet.hitbox):
                Bullets_y.pop(Bullets_y.index(bullet))
                Bullets.pop(Bullets.index(bullet))
            
    
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
        
        if len(Bullets_x) < 15:
            if avatar.right:
                newBullet_x = round(avatar.x + avatar.width)
                newBullet_y = round(avatar.y + avatar.height/3)
            if avatar.left:
                newBullet_x = round(avatar.x)
                newBullet_y = round(avatar.y + avatar.height/3)
            if facing_x != 0:
                shootingSound.play()
                Bullets_x.append(StunShoots(newBullet_x,newBullet_y,facing_x))
                Bullets.extend(Bullets_x)
                pg.time.delay(20)
        if len(Bullets_y) < 15:
            if key[pg.K_UP]:
                newBullet_x = round(avatar.x + avatar.width/2)
                newBullet_y = round(avatar.y + avatar.height/3)
            if key[pg.K_DOWN]:
                newBullet_x = round(avatar.x + avatar.width/2)
                newBullet_y = round(avatar.y + avatar.height/3)
            if facing_y !=0:
                shootingSound.play()
                Bullets_y.append(StunShoots(newBullet_x,newBullet_y,facing_y))
                Bullets.extend(Bullets_y) 
                pg.time.delay(20)            


    for enemy in VampsANDWerewolfs:
        BeingShoot(enemy, Bullets_x)
        BeingShoot(enemy, Bullets_y)
        

def BeingShoot(enemy, Bullets):
    for bullet in Bullets:
        if enemy.hitboxBody.colliderect(bullet.hitbox):
            Bullets.pop(Bullets.index(bullet))
            enemy.hits += 1
            enemy.Hit()
        

###############################################################################
#######################                                 #######################
#######################         Games Main Loop         #######################
#######################                                 #######################
###############################################################################
main()
            
def run_game(starting_scene):
    
    crashed = False
    

    active_scene = starting_scene
    while not crashed:
#        key=pg.key.get_pressed()

        
        active_scene.Render(gameDisplay)
        active_scene.quitScene()
        pg.display.flip()
        active_scene = active_scene.next
        
        if quitGame() or active_scene.crashed:
            crashed = True
     
        clock.tick(active_scene.flps)
#        drawBackground()
        pg.display.update()


###############################################################################
#######################                                 #######################
#######################             Avatars              #######################
#######################                                 #######################
###############################################################################
player = Player(60,70,32,32)

number_of_Vamps = random.randint(7,15)
for i in range(number_of_Vamps):
    Vamp = CreateVampire()
    if not Vamp.inside:
        Vamps.append(Vamp)
        VampsANDWerewolfs.extend(Vamps)
    
    
    
    
number_of_Wers = random.randint(7,15)
for i in range(number_of_Wers):
    Wery = CreateWerewolf()
    if not Wery.inside:
        Werewolfs.append(Wery)
        VampsANDWerewolfs.extend(Werewolfs)
        

tailor = Tailor(895,115,32,32)

gallerist = Gallerist(710,460,32,32)  

run_game(Introduction(player))

pg.quit()
quit()
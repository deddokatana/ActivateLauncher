__author__ = 'Jason Crockett'

import pygame,sys,os,time
from pygame.locals import *

from os.path import expanduser


WIDGETORAPPNAME = "Activate Launcher"

pygame.init()
bits = pygame.
flags = pygame.display.get_flags()
ScreenWidth = pygame.display.get_width()
ScreenHeight = pygame.display.get_height()
DISPLAYSURF = pygame.display.set_mode((ScreenWidth,ScreenHeight),flags^FULLSCREEN,bits)  # the default display, and root surface
pygame.display.set_caption(WIDGETORAPPNAME)

# Functions go here below:


def get_background_images():
    UserHome = str(expanduser("~")) # get user home folder
    # ^ works on windows and mac too. prints with no "/" on the end

    try: #try and make a Pictures folder location string.
        assert(isinstance(UserHome,str))
        PicturesFolder = UserHome + "/Pictures" #is a string
    except AssertionError:
        print("Userhome is not a string!")

    PicturesFullPathList = []

    try: # try to load images in the pictures folder string.
        for file in os.listdir(PicturesFolder):
            assert(file is type(str())) #file hopefully is a string
            PicturesFullPath = PicturesFolder + file
            PicturesFullPathList.append(PicturesFullPath)
    except TypeError:
        print("a filename in os.listdir is not a string, is it the actual file? ") # oh *uck it isnt.
    return PicturesFullPathList

def countdown(count):
    while (count >= 0):
        print ('The count is: ', count)
        count -= 1
        time.sleep(1)

def choose_background_image(FullFilePathList):
    while event.type == QUIT:
        for picture in FullFilePathList:
            countdown(10)
            return picture
            continue

def set_background(PickedBackground="./Resources/Default/Background.png"):
    if not PickedBackground:
        Image = pygame.image.load("./Resources/Default/Background.png")
    Image = pygame.image.load(PickedBackground)
    DISPLAYSURF.blit(Image,(0,0)) #put image onscreen
    # ^ at 0 horizontally and 0 vertically, down and right, from the top left corner.




PickedBackground = choose_background_image(get_background_images())
# ^ Starts an infinite picture file rotation

while True: # put game logic and functions in this loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT()
            sys.exit()
        #if event.type == KEYDOWN and event.key == K_F11: # The Keypress Boilerplate line! The Powah!
            #toggle_fullscreen() # problem lines

        #add extra events above.

    #the leave the below lines alone
    screen = pygame.display.get_surface() # problem lines
    pygame.display.update()
    #pygame.display.flip() # possibly needed.
    set_background(PickedBackground)

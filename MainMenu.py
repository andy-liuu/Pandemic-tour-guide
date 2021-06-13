from pygame import *
import writeTextBox
size=width,height = 1280,720
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)


#global variables accessed by globals()
wMap = image.load("Images/WorldMap.png").convert_alpha()
CanadaMap = image.load("Images/CanadaMap.png").convert_alpha()
IndiaMap = image.load("Images/IndiaMap.png").convert_alpha()

#each country gets an rgb value
countryDict = {"Canada" : (255, 0, 0),
               "India" : (255, 138, 0),
               "USA": (52, 100, 235),
               "Mexico": (13, 107, 21),
               "Brazil": (10,209,27),
               "Spain": (235, 231, 30),
               "South Africa": (181,5,38),
               "Ethiopia": (27, 128, 135),
               "Egypt": (225, 227, 209),
               "Saudi Arabia": (3,37,84),
               "Russia": (134, 17,17),
               "Thailand": (88,3,110),
               "China": (189, 30, 57),
               "Australia": (9, 66, 181),
               "Algeria": (60,255,0),
               "Nigeria": (204, 0, 255)}


#load image assets
menu = image.load("Images/Frontpage.png").convert_alpha()
selectedMenu = image.load("Images/Frontpage2.png").convert_alpha()
loadingPage = image.load("Images/LoadingPage.png").convert_alpha()
loadingPages = []
for i in range(4):
    loadingPages.append(image.load("Images/Loading"+str(i+1)+".png").convert_alpha())

infoOverlay = image.load("Images/InfoOverlay.png").convert_alpha()
infoOverlaySelected = image.load("Images/InfoOverlaySelected.png").convert_alpha()


infoX = 1280

inMenu = True
clickable = True

loading = False
loadingCount = 0
loadingBar = 0

launching = False

showingInfo = False
infoBox = None

buttonRect = Rect(467, 495, 346, 134)
closeButtonRect = Rect(228, 0, 123, 73)

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    mpos=mouse.get_pos()
    mb=mouse.get_pressed()

    #when the infobox for a country is displayed + animation
    if showingInfo:
        screen.blit(wMap, (0, 0))
        if closeButtonRect.collidepoint(mpos):
            screen.blit(infoOverlaySelected, (infoX, 0))
        else:
            screen.blit(infoOverlay, (infoX, 0))
        screen.blit(infoBox, (infoX+360, 0))
        if infoX>0 and not clickable:
            infoX-=10
        if infoX<=0:
            if closeButtonRect.collidepoint(mpos) and mb[0] == 1:
                    clickable = True
        if clickable:
            infoX += 10
            if infoX>=1280:
                showingInfo = False

    #regular map usage                
    elif launching:
        
        screen.blit(wMap, (0, 0))
        for country, col in countryDict.items():
            if screen.get_at(mpos) == col:

                newcountrystring = country.strip().replace(" ", "_")
                screen.blit(globals()[newcountrystring+"Map"], (0, 0))
                if clickable and mb[0] == 1:
                    clickable = False
                    showingInfo = True
                    infoBox = writeTextBox.textBox(country.lower(), 920, 720)
                    
    #"loading" screen
    elif loading:
        
        screen.blit(loadingPage, (0, 0))
        loadingBar+=1
        draw.rect(screen, (0, 255, 204), (370, 480, loadingBar, 60))
        if loadingBar >= 540:
            loading = False
            launching = True

        loadingCount+=1
        screen.blit(loadingPages[(loadingCount//110)%4], (0, 0))
        
        
        
    
    elif inMenu:
        
        screen.blit(menu, (0, 0))
        if buttonRect.collidepoint(mpos):
            if mb[0] == 0:
                screen.blit(selectedMenu, (0, 0))
            if mb[0] == 1:
                loading = True
                inMenu = False
    
    display.flip() 

quit()

from pygame import *
size=width,height = 1280,720
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

wMap = image.load("Images/WorldMap.png").convert_alpha()
CanadaMap = image.load("Images/CanadaMap.png").convert_alpha()
IndiaMap = image.load("Images/IndiaMap.png").convert_alpha()
countryDict = {"Canada" : (255, 0, 0), "India" : (255, 138, 0)}

menu = image.load("Images/Frontpage.png").convert_alpha()
selectedMenu = image.load("Images/Frontpage2.png").convert_alpha()
loadingPage = image.load("Images/LoadingPage.png").convert_alpha()
loadingPages = []
for i in range(4):
    loadingPages.append(image.load("Images/Loading"+str(i+1)+".png").convert_alpha())

inMenu = True

loading = False
loadingCount = 0
loadingBar = 0

launching = False

buttonRect = Rect(467, 495, 346, 134)

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    mpos=mouse.get_pos()
    mb=mouse.get_pressed()

    if launching:
        
        screen.blit(wMap, (0, 0))
        for country, col in countryDict.items():
            if screen.get_at(mpos) == col:
                screen.blit(globals()[country+"Map"], (0, 0))
                if clickable and mb[0] == 1:
                    clickable = False
                    print(country)

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

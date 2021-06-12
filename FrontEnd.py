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
clickable = True
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
    mpos=mouse.get_pos()
    mb=mouse.get_pressed()

    
    screen.blit(wMap, (0, 0))

    for country, col in countryDict.items():
        if screen.get_at(mpos) == col:
            screen.blit(globals()[country+"Map"], (0, 0))
            if clickable and mb[0] == 1:
                clickable = False
                print(country)        
    
    
    display.flip() 

quit()


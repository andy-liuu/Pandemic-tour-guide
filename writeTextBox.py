from pygame import *
import pprint

import covid
import WebScrape
import destination

RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

#global font variable
font.init()
title_font = font.SysFont('Comic Sans MS', 60)
body_font = font.SysFont('Comic Sans MS', 30)

'''
params:
country -> string with name
length, width -> dimensions of text box


returns a transparent surface with the text information centered on it
later will need to be blitted to the surface


'''

#thanks stackoverflow for this code (pygame suks)
def blit_text(surface, text, pos, font, color=Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

    return y  #bottom of lowest text written

        

def textBox(country, width, height):

    COL = (10, 3, 74)
    
    covidinfo = covid.getCovidStats(country)
    travelString = WebScrape.getTravelRestrictions(country)
    destinationlist = destination.destinations(country)


    boxSurface = Surface((width,height), SRCALPHA)

    #tester to see border 
    #boxSurface.fill((255,255,0))
    
    #title of country
    countryname = covidinfo['country']
    titlesurface = title_font.render(covidinfo['country'],False, COL)
    title_pos_center = (width//2 - titlesurface.get_width()// 2,int(height//30))
    boxSurface.blit(titlesurface, title_pos_center)


    #track the current position of text
    curwidth = width//30
    curheight = height//6+10
    
    #tourist entry
    offset = blit_text(boxSurface, travelString, (curwidth, curheight), body_font, COL)
    curheight = offset + 15

    #covid rating
    rating = covidinfo['rating']
    cases = covidinfo['cases']

    covidstring = "{} is rated {}/10.0 for pandemic safety. (Active cases: {})".format(covidinfo['country'], rating, cases)
    offset = blit_text(boxSurface, covidstring, (curwidth, curheight), body_font, COL)
    curheight = offset + 15

    #destinations
    offset = blit_text(boxSurface,"Destinations in {}".format(covidinfo['country']), (curwidth, curheight), body_font, COL)
    curheight = offset
    for i in range(len(destinationlist)):
        offset = blit_text(boxSurface, "{}. {}".format(i+1, destinationlist[i]), (curwidth, curheight), body_font, COL)
        curheight = offset

    

    



    return boxSurface


    
    


if __name__ == "__main__":
    
    wow = textBox("china",800, 600)

    size=width,height = 1280,720
    screen=display.set_mode(size)

    
    

    
    clickable = True
    running=True
    while running:
        for evt in event.get():
            if evt.type==QUIT:
                running=False
        mpos=mouse.get_pos()
        mb=mouse.get_pressed()

        
        
        screen.fill((200,200,200))
        screen.blit(wow, (100,100))
        
        
        display.flip() 

    quit()

import pygame as pg
import constants as c
from block import *

score = 0
# from/import: didn't need to do "block = block.Block()"; "import *" imports keywords into your namespace
# innit: gets called when block class called
# when class created: every function has 'self' keyword => refers to instance of class; TBC ~remind L.
# 'self' to be covered 4/31
# A tuple is a list but its contents can't be changed

# 1) Implement block upgrades
# 2) Make sure it substracts from score
# 3) Keep track of costs and click power

button = pygame.image.load('./resources/button.png')
button = pygame.transform.scale(button,(100,100))
upgrade_cost = 5
click_power = 3

def init():
    global screen, font, block
    pg.init()
    screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    pg.display.set_caption('Dirt Clicker')
    screen.fill('white')
    print('Beginning event logging...')
    print()
    block = Block()  
    #left top: (400,300)
    #automatically called "__init__"
    print('Game Start')
    font = pg.font.Font(pg.font.get_default_font(),16)

def main():
    init() 
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                
            if event.type == pg.MOUSEBUTTONDOWN:
                handle_click(event.pos)
        pg.display.update()
        screen.fill("aquamarine")
        screen.blit(block.sprite, (400, 300))
        screen.blit(button, (450,200))
        screen.blit(font.render(str(score),False,"coral1"),(450,100))
        
    pg.quit()
    print("Window closed, game successfully quit")

def handle_click(pos):
    global score, click_power, upgrade_cost
    x,y = pos
    if x in range (400,546) and y in range (300,446):
        score+=click_power
        
    if x in range (450,450 + button.get_width()) and y in range (200, 200 + button.get_height()):

        if score >= upgrade_cost:
            score-=upgrade_cost
            click_power*=2
            upgrade_cost*=2
            block.upgrade()
        

main()
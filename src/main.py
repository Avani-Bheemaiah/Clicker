import pygame as pg
import constants as c
from block import *

score = 0
# from/import: didn't need to do "block = block.Block()"; "import *" imports keywords into your namespace
# innit: gets called when block class called
# when class created: every function has 'self' keyword => refers to instance of class; TBC ~remind L.
# 'self' to be covered 4/31

def init():
    pg.init()
    screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    pg.display.set_caption('Dirt Clicker')
    screen.fill('white')
    print('Beginning event logging...')
    print()
    block = Block()
    screen.blit(block.sprite, (400, 300))
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
                handle_click()
        pg.display.update()
    pg.quit()
    print("Window closed, game successfully quit")

def handle_click(x, y):
    if x in range (400,546) and y in range (300,446):
        score+=1
        
        

main()
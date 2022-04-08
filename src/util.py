import pygame as pg

def load_sprite(sprite_sheet, x, y, width, height) -> pg.Surface:
    """Grabs Sprite from Spritesheet"""
    image = pg.Surface((width, height)) # Create a Surface
    sprite_rect = (x, y, width, height) # The location and size of the sprite on the sheet
    image.blit(sprite_sheet, (0, 0), sprite_rect) # Blit the sprite onto our created surface
    image.set_colorkey('black') # Make all black pixels transparent
    return image
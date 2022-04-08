import pygame
import util
class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = pygame.image.load('./resources/Spritesheet.png')
        self.load_sprites()
        self.sprite = self.sprites['Dirt']
        
    def load_sprites(self):
        self.sprites = {} 
        #x, y, w, h
        self.sprites['Dirt'] = util.load_sprite(self.sprite_sheet, 310, 27, 73, 73)
        self.sprites['Grass'] = util.load_sprite(self.sprite_sheet, 237, 27, 73, 73)
        self.sprites['Stone'] = util.load_sprite(self.sprite_sheet, 383, 27, 73, 73) 
        self.sprites['Coal'] = util.load_sprite(self.sprite_sheet, 310, 173, 73, 73)
        self.sprites['Gold'] = util.load_sprite(self.sprite_sheet, 456, 100, 73, 73)
        self.sprites['Redstone'] = util.load_sprite(self.sprite_sheet, 602, 100, 73, 73)
        self.sprites['Diamond'] = util.load_sprite(self.sprite_sheet, 529, 100, 73, 73)
        
        for state in self.sprites.keys():
            self.sprites[state] = pygame.transform.scale2x(self.sprites[state])

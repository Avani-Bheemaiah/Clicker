import pygame
import util
class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = pygame.image.load('./resources/Spritesheet.png')
        
        self.load_sprites()
        self.sprite = self.sprites[0]
        self.number = 0
        
        
    def load_sprites(self):
        self.sprites = []
        #x, y, w, h
        self.sprites.append(util.load_sprite(self.sprite_sheet, 310, 27, 73, 73))
        self.sprites.append(util.load_sprite(self.sprite_sheet, 237, 27, 73, 73))
        self.sprites.append(util.load_sprite(self.sprite_sheet, 383, 27, 73, 73))
        self.sprites.append(util.load_sprite(self.sprite_sheet, 310, 173, 73, 73))
        self.sprites.append(util.load_sprite(self.sprite_sheet, 456, 100, 73, 73))
        self.sprites.append(util.load_sprite(self.sprite_sheet, 602, 100, 73, 73))
        self.sprites.append(util.load_sprite(self.sprite_sheet, 529, 100, 73, 73))
        
        for i in range (len(self.sprites)):
            self.sprites[i] = pygame.transform.scale2x(self.sprites[i])

    def upgrade(self):
        if self.number < 6:
            self.number+=1
            self.sprite = self.sprites[self.number]
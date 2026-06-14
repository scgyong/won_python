import pygame
import cfg

class Fighter:
    def __init__(self):
        self.x = cfg.screen_width // 2
        self.y = cfg.screen_height // 2
        self.image = pygame.image.load('fighter_small.png').convert_alpha()
        self.half_width = self.image.get_width() // 2
        self.half_height = self.image.get_height() // 2
    def move(self):
        pass
    def draw(self, screen):
        screen.blit(self.image, (self.x - self.half_width, self.y - self.half_height))

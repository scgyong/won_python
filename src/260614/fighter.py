import pygame
import cfg

class Fighter:
    def __init__(self):
        self.x = cfg.screen_width // 2
        self.y = cfg.screen_height // 2
        self.dx, self.dy = 0, 0
        self.image = pygame.image.load('fighter_small.png').convert_alpha()
        self.half_width = self.image.get_width() // 2
        self.half_height = self.image.get_height() // 2
    def move(self):
        self.x += self.dx
        self.y += self.dy
    def draw(self, screen):
        screen.blit(self.image, (self.x - self.half_width, self.y - self.half_height))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.dx = -1
            elif event.key == pygame.K_RIGHT:
                self.dx = 1
            elif event.key == pygame.K_UP:
                self.dy = -1
            elif event.key == pygame.K_DOWN:
                self.dy = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.dx = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                self.dy = 0
    def check_collision(self, meteor):
        dist_sq = (self.x - meteor.x) ** 2 + (self.y - meteor.y) ** 2
        radius_sum = self.half_width + meteor.half_width
        if dist_sq < radius_sum ** 2:
            print("충돌!") 
    def check_collision_aabb(self, meteor):
        if abs(self.x - meteor.x) < self.half_width + meteor.half_width and abs(self.y - meteor.y) < self.half_height + meteor.half_height:
            print("충돌!")
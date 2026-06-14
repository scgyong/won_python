import pygame
import random
import cfg

# Meteor 클래스 정의
class Meteor:
    image = None
    def __init__(self, x=None, y=None, dx=None, dy=None):
        if Meteor.image is None:
            Meteor.image = pygame.image.load('meteor.png').convert_alpha()
            Meteor.min_x = 0
            Meteor.max_x = cfg.screen_width - Meteor.image.get_width()
            Meteor.min_y = 0
            Meteor.max_y = cfg.screen_height - Meteor.image.get_height()
        if x is None: x = random.randint(Meteor.min_x, Meteor.max_x)
        if y is None: y = random.randint(Meteor.min_y, Meteor.max_y)
        if dx is None: dx = random.choice([-1, -0.5, 0.5, 1])
        if dy is None: dy = random.choice([-1, -0.5, 0.5, 1])
        self.x, self.y, self.dx, self.dy = x, y, dx, dy
    def move(self):
        self.x += self.dx
        if self.x >= Meteor.max_x or self.x <= Meteor.min_x:
            self.dx = -self.dx
        self.y += self.dy
        if self.y >= Meteor.max_y or self.y <= Meteor.min_y:
            self.dy = -self.dy
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

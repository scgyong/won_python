import pygame
import random

# Meteor 클래스 정의
class Meteor:
    image = None
    def __init__(self, x=None, y=None, dx=None, dy=None):
        if x is None: x = random.randint(100, 700)
        if y is None: y = random.randint(100, 500)
        if dx is None: dx = random.choice([-1, -0.5, 0.5, 1])
        if dy is None: dy = random.choice([-1, -0.5, 0.5, 1])
        self.x, self.y, self.dx, self.dy = x, y, dx, dy
        if Meteor.image is None:
            Meteor.image = pygame.image.load('meteor.png').convert_alpha()
    def move(self):
        self.x += self.dx
        if self.x >= 736 or self.x <= 0:
            self.dx = -self.dx
        self.y += self.dy
        if self.y >= 536 or self.y <= 0:
            self.dy = -self.dy
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

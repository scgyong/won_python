import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
meteor_image = pygame.image.load("meteor.png").convert_alpha()
airplane_image = pygame.image.load("fighter_small.png").convert_alpha()

class Meteor:
    def __init__(self, x=None, y=None, dx=None, dy=None):
        if x is None:
            self.x = random.randint(100, 700)
        else:
            self.x = x
        if y is None:
            self.y = random.randint(100, 500)
        else:
            self.y = y
        if dx is None:
            self.dx = random.choice([-1, -0.5, 0.5, 1])
        else:
            self.dx = dx
        if dy is None:
            self.dy = random.choice([-1, -0.5, 0.5, 1])
        else:
            self.dy = dy
    def move(self):
        self.x += self.dx
        if self.x >= 736 or self.x <= 0:
            self.dx = -self.dx

        self.y += self.dy
        if self.y >= 536 or self.y <= 0:
            self.dy = -self.dy
    def draw(self, screen):
        screen.blit(meteor_image, (self.x, self.y))

class Airplane:
    def __init__(self, x=400, y=300):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
    def move(self):
        self.x += self.dx
        self.y += self.dy
    def draw(self, screen):
        screen.blit(airplane_image, (self.x, self.y))
meteors = [ Meteor() for _ in range(3)]
airplane = Airplane()

for meteor in meteors:
    meteor.move()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                break
            elif event.key == pygame.K_LEFT:
                airplane.dx = -1
            elif event.key == pygame.K_RIGHT:
                airplane.dx = 1
            elif event.key == pygame.K_UP:
                airplane.dy = -1
            elif event.key == pygame.K_DOWN:
                airplane.dy = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                airplane.dx = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                airplane.dy = 0
    if not running:
        break
    for meteor in meteors:
        meteor.move()
    airplane.move()
    screen.fill((0, 0, 0))
    for meteor in meteors:
        meteor.draw(screen)
    airplane.draw(screen)
    pygame.display.flip()

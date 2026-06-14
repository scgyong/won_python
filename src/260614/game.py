import pygame
import random

# pygame 초기화

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("운석 피하기")

# Meteor 클래스 정의
class Meteor:
    image = pygame.image.load('meteor.png').convert_alpha()
    def __init__(self, x=None, y=None, dx=None, dy=None):
        if x is None: x = random.randint(100, 700)
        if y is None: y = random.randint(100, 500)
        if dx is None: dx = random.choice([-1, -0.5, 0.5, 1])
        if dy is None: dy = random.choice([-1, -0.5, 0.5, 1])
        self.x, self.y, self.dx, self.dy = x, y, dx, dy
    def move(self):
        self.x += self.dx
        if self.x >= 736 or self.x <= 0:
            self.dx = -self.dx
        self.y += self.dy
        if self.y >= 536 or self.y <= 0:
            self.dy = -self.dy
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Fighter 클래스 정의

meteors = [Meteor() for _ in range(5)]

# 게임 루프
running = True
while running:

    ## 업데이트
    for m in meteors:
        m.move()
    
    ## 그리기
    screen.fill((0, 0, 0))
    for m in meteors:
        m.draw(screen)
    pygame.display.flip()

    ## 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()

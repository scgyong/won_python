# 초기작업
 # - 화면생성
 # - 이미지로드

import math
c = math.sqrt(169) # square root
print(c)

# 클래스 정의

# 게임루프
# - 움직이기
# - 그리기
# - 이벤트처리

import pygame
import random

pygame.init() # 초기화
screen = pygame.display.set_mode((800, 600)) # 화면 생성
pygame.display.set_caption("운석피하기") # 게임 제목
# 이미지 로드
airplane_image = pygame.image.load("fighter_small.png").convert_alpha()
meteor_image = pygame.image.load("meteor.png").convert_alpha()
# 클래스 정의
# class Airplane:
#     def __init__(self):
#         self.image = airplane_image
#         self.x = 400
#         self.y = 500
#         self.dx = 0
#         self.dy = 0

#     def draw(self, screen):
#         screen.blit(self.image, (self.x, self.y))

class Airplane:
    def __init__(self):
        self.x = 600
        self.y = 300
        self.dx = 0
        self.dy = 0
    def move(self):
        self.x += self.dx
        self.y += self.dy

plane = Airplane()

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
        screen.blit(
            meteor_image,
            (self.x, self.y)
        )

meteors = [Meteor() for _ in range(5)]

running = True
while running:
    # update
    for meteor in meteors:
        meteor.move()

    plane.move()

    # draw
    for meteor in meteors:
        meteor.draw(screen)
    plane.draw(screen)

    pygame.display.flip()

    # event handling
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
                plane.dx = -1
            elif event.key == pygame.K_RIGHT:
                plane.dx = 1
            elif event.key == pygame.K_UP:
                plane.dy = -1
            elif event.key == pygame.K_DOWN:
                plane.dy = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                plane.dx = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                plane.dy = 0
    if not running:
        break

import pygame
import random
from meteor import Meteor

# pygame 초기화

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("운석 피하기")


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

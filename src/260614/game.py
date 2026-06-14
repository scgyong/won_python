import pygame
import random
import cfg
from meteor import Meteor
from fighter import Fighter

# pygame 초기화

pygame.init()
screen = pygame.display.set_mode((cfg.screen_width, cfg.screen_height))
pygame.display.set_caption("운석 피하기")

# 객체 생성
fighter = Fighter()
meteors = [Meteor() for _ in range(5)]

# 게임 루프
running = True
while running:

    ## 업데이트
    for m in meteors:
        m.move()
    fighter.move()
    
    ## 그리기
    screen.fill((0, 0, 0))
    for m in meteors:
        m.draw(screen)
    fighter.draw(screen)
    pygame.display.flip()

    ## 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

pygame.quit()

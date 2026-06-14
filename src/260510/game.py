import pygame

pygame.init()
airplane = pygame.image.load("fighter_small.png")
meteor = pygame.image.load("meteor.png")
screen = pygame.display.set_mode((800, 600))
x, y = 400, 300
dx, dy = 0, 0
# meteor_x, meteor_y = 736, 536
meteor_x, meteor_y = 100, 100
meteor_dx, meteor_dy = 1, 1
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
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                dx = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                dy = 0

    # x = x + 1
    x += dx
    y += dy
    meteor_x += meteor_dx
    if meteor_x >= 736 or meteor_x <= 0:
        meteor_dx = -meteor_dx
        # meteor_dx = -1 * meteor_dx

    meteor_y += meteor_dy
    if meteor_y >= 536 or meteor_y <= 0:
        meteor_dy = -meteor_dy
 
    screen.fill((0, 0, 0))
    screen.blit(airplane, (x, y))
    screen.blit(meteor, (meteor_x, meteor_y))
    pygame.display.flip()




# score = 87

# if score > 90:
#     print("A")
# elif score > 80:
#     print("B")
# elif score > 70:
#     print("C")

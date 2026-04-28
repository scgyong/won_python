import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

pic = pygame.image.load("fighter_small.png")

screen.fill( (123, 45, 240) )
pygame.draw.rect(screen, (255, 0, 0), (110, 20, 120, 130) )

x, y = 10, 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                break
            elif event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10

    if not running:
        break

    screen.blit(pic, (x, y))
    pygame.display.flip()


print("Program has ended")


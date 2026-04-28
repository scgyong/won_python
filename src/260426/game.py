import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

pic = pygame.image.load("fighter.png")

screen.fill( (123, 45, 240) )
pygame.draw.rect(screen, (255, 0, 0), (110, 20, 120, 130) )
screen.blit(pic, (10, 10, 30, 30))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


print("Hello")

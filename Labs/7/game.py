import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("My title")
# pygame.display.set_icon()

x = 30
y = 30

# game loop
clock = pygame.time.Clock()
color = (0, 128, 255)
done = False
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y <= 0:
            y = 600
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        y -= 5
    if pressed[pygame.K_DOWN]:
        if y >= 600:
            y = 0
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        y += 5
    if pressed[pygame.K_LEFT]:
        if x <= 0:
            x = 800
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x -= 5
    if pressed[pygame.K_RIGHT]:
        if x >= 800:
            x = 0
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x += 5

    screen.fill((255,255,255))
    
    pygame.draw.rect(screen, color , pygame.Rect(x, y, 60, 60)) 
    pygame.display.flip()
    clock.tick(144)

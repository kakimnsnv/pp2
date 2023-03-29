import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Circle won't leave this window")

x = 40
y = 40

clock = pygame.time.Clock()
color = (255, 0, 0)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        if y > 25: y -= 20
    if pressed[pygame.K_DOWN]:
        if y < 575: y += 20
    if pressed[pygame.K_LEFT]:
        if x > 25 : x -= 20 
    if pressed[pygame.K_RIGHT]:
        if x < 775 : x += 20

    screen.fill((255,255,255))

    pygame.draw.circle(screen, color, (x, y) , 25)
    pygame.display.flip()
    clock.tick(144)

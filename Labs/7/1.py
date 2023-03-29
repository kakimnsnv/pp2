import pygame, datetime

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
clock_bg = pygame.image.load("assets/mickeyclock.jpg")
clock_bg = pygame.transform.scale(clock_bg, (500,500))
minute_hand = pygame.image.load("assets/right_hand.png")
second_hand = pygame.image.load("assets/left_hand.png")

dt = datetime.datetime.now()

pygame.transform.rotate(minute_hand, dt.minute * -6)
pygame.transform.rotate(second_hand, dt.second * -6)

screen.blit(clock_bg, (0,0))
screen.blit(second_hand, (250 - int(second_hand.get_width() /2) , 250 - int(second_hand.get_height() / 2)))
screen.blit(minute_hand, (250 - int(minute_hand.get_width() /2) , 250 - int(minute_hand.get_height() / 2)))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    minute_hand = pygame.transform.rotate(minute_hand, int(dt.minute * -6))
    second_hand = pygame.transform.rotate(second_hand, int(dt.second * -6))


    pygame.display.flip()
    clock.tick(60)
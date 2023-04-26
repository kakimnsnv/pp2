import pygame
import os

pygame.mixer.init()
screen = pygame.display.set_mode((300, 500))
clock = pygame.time.Clock()

music = []
os.chdir(r"/Users/kakimbekn/Library/CloudStorage/OneDrive-АОКазахстанско-БританскийТехническийУниверситет/MyFiles/GitHub/pp2/Labs/7")
musicpath = os.listdir("assets")
for i in musicpath:
    if i.endswith(".mp3"):
        music.append(i)


i = 0 
isplaying = False
ispaused = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if not isplaying :
            os.chdir("assets")
            pygame.mixer.music.load(music[i])
            pygame.mixer.music.play()
            isplaying = not isplaying


        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_p]:
            pygame.mixer.music.pause()
        if pressed[pygame.K_u]:
            pygame.mixer.music.unpause()
        if pressed[pygame.K_RIGHT]:
            if i == len(music) - 1: i = 0
            else: i += 1
            pygame.mixer.music.load(music[i])
            pygame.mixer.music.play()
        if pressed[pygame.K_LEFT]:
            if i == 0: i = len(music) -1
            else: i -= 1
            pygame.mixer.music.load(music[i])
            pygame.mixer.music.play()

        screen.fill((10, 10, 10))
        pygame.display.flip()
        clock.tick(144)
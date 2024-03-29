import pygame, os

BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

radius = 5
last_pos = (0, 0)
first_pos = (0, 0)
draw_on = False
color = BLACK
last_color = BLACK
mode = "draw"
firsttap = False
path = r"/Users/kakimbekn/Library/CloudStorage/OneDrive-АОКазахстанско-БританскийТехническийУниверситет/MyFiles/GitHub/pp2/Labs/8/assets"
os.chdir(path)

###
def main():
    global BLUE, GREEN, RED, BLACK, WHITE, radius, last_pos, draw_on, color
    global mode, firsttap, path, first_pos
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen2 = screen.copy()
    pygame.display.set_caption('Paint')
    screen.fill(WHITE)
    clock = pygame.time.Clock()
    
    eraser = pygame.image.load("eraser.png")
    eraser = pygame.transform.scale(eraser, (50, 50))
    
    pen = pygame.image.load("pen.png")
    pen = pygame.transform.scale(pen, (50, 50))

    globalrect = pygame.Rect(895, -5, 150, 260)

    eraserrect = pygame.Rect(950, 0, 50, 50)

    circlerect = pygame.Rect(950, 50, 50, 50)

    rectrect = pygame.Rect(900, 50, 50, 50)

    penrect = pygame.Rect(900, 0, 50, 50)

    redrect = pygame.Rect(950, 150, 50, 50)

    greenrect = pygame.Rect(900, 150, 50, 50)

    bluerect = pygame.Rect(950, 200, 50, 50)

    blackrect = pygame.Rect(900, 200, 50, 50)

    while True:

        pygame.draw.rect(screen, BLACK, globalrect)
        pygame.draw.rect(screen, WHITE, (897, -3, 150, 254))
        
        screen.blit(eraser, (950, 0))
        screen.blit(pen, (900, 0))
       
        pygame.draw.circle(screen, color, (975, 75), 25)
        pygame.draw.circle(screen, WHITE, (975, 75), 22)
        
        pygame.draw.rect(screen, color, (900, 50, 47, 47))
        pygame.draw.rect(screen, WHITE, (903, 53, 41, 41))

        pygame.draw.rect(screen, RED, redrect)
        pygame.draw.rect(screen, GREEN, greenrect)
        pygame.draw.rect(screen, BLUE, bluerect)
        pygame.draw.rect(screen, BLACK, blackrect)
        
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            # determine if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and alt_held:
                    return
                elif event.key == pygame.K_w and ctrl_held:
                    return
                elif event.key == pygame.K_ESCAPE:
                    return

                # to control radius
                elif event.key == pygame.K_UP:
                    radius = min(radius + 2.5, 20)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 2.5)
                
                # determine if a letter key was pressed
                elif event.key == pygame.K_r:
                    color = RED
                    last_color = RED
                elif event.key == pygame.K_g:
                    color = GREEN
                    last_color = GREEN
                elif event.key == pygame.K_b:
                    color = BLUE
                    last_color = BLUE

                # determine if a num was pressed to switch mode
                elif event.key == pygame.K_1:
                    mode = "draw"
                elif event.key == pygame.K_2:
                    mode = "erase"
                elif event.key == pygame.K_3:
                    mode = "draw_rect"
                elif event.key == pygame.K_4:
                    mode = "draw_circle"
                
                
            if event.type == pygame.MOUSEBUTTONDOWN:

            #if was clicked copy our screen to screen2
                screen2 = screen.copy()
                pos = pygame.mouse.get_pos()
                if eraserrect.collidepoint(pos):
                    mode = "erase"
                elif penrect.collidepoint(pos):
                    mode = "draw"
                elif rectrect.collidepoint(pos):
                    mode = "draw_rect"
                elif circlerect.collidepoint(pos):
                    mode = "draw_circle"
                elif redrect.collidepoint(pos):
                    color = RED
                elif greenrect.collidepoint(pos):
                    color = GREEN
                elif blackrect.collidepoint(pos):
                    color = BLACK
                elif bluerect.collidepoint(pos):
                    color = BLUE
                

                if not firsttap:
                    firsttap = True
                    first_pos = event.pos
                draw_on = True
                

            elif event.type == pygame.MOUSEBUTTONUP:

            #stop drawing
                draw_on = False
                firsttap = False
                    
                
            elif event.type == pygame.MOUSEMOTION:

            #to know that we are moving our mouse
                pos = pygame.mouse.get_pos()
                if not globalrect.collidepoint(pos) and draw_on == True:
                    if mode == "draw":
                        drawLineBetween(screen, event.pos, last_pos)
                    if mode == "erase":
                        erase(screen, event.pos, last_pos)
                    if mode == "draw_rect":
                        drawRect(screen, screen2, first_pos, event.pos)
                    if mode == "draw_circle":
                        drawCircle(screen, screen2, first_pos, event.pos)
                        
                last_pos = event.pos                    
                

        
        pygame.display.update()
        clock.tick(10000)

###
        
def drawLineBetween(screen, start, end):

    pygame.draw.circle(screen, color, start, radius)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    dist = max(abs(dx), abs(dy))

    for i in range(dist):
        x = int(start[0] + float(i) / dist * dx)
        y = int(start[1] + float(i) / dist * dy)
        pygame.draw.circle(screen, color, (x, y), radius)
###

def erase(screen, start, end):

    color = WHITE
    pygame.draw.circle(screen, color, start, radius)
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    dist = max(abs(dx), abs(dy))

    for i in range(dist):
        x = int(start[0] + float(i) / dist * dx)
        y = int(start[1] + float(i) / dist * dy)
        pygame.draw.circle(screen, color, (x, y), radius)

    color = last_color
###

def drawRect(screen, screen2, start, end):

    lx = min(end[0], start[0])
    rx = max(end[0], start[0])
    ly = min(end[1], start[1])
    ry = max(end[1], start[1])
    #upd screen backwards
    screen.blit(screen2, (0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(lx, ly, rx - lx, ry - ly))
    
###
    
def drawCircle(screen, screen2, start, end):

    x1 = min(end[0], start[0])
    x2 = max(end[0], start[0])
    y1 = min(end[1], start[1])
    y2 = max(end[1], start[1])
    #(x1, y1) = start
    #(x2, y2) = end 
    r = min((x2 - x1) / 2, (y2 - y1) / 2)
    #upd screen backwards
    screen.blit(screen2, (0, 0))
    pygame.draw.circle(screen, color, (x1 + r, y1 + r), r)
###


main()
pygame.quit()

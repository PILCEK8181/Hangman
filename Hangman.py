import pygame

pygame.init()

#SCREEN
screenWidth = 1200
screenHeight = 1200

screen = pygame.display.set_mode((screenWidth,screenHeight))

player = pygame.Rect(300,250,50,50)
player2 = pygame.Rect(300,250,50,50)

#GAME LOOP
run = True
while run:

    screen.fill((255,255,255))
    pygame.draw.rect(screen,(255,0,0),player)
    pygame.draw.rect(screen,(0,255,0),player2)

    key = pygame.key.get_pressed()
    pygame.draw.circle(screen,(12,34,23),(600,600),30)

    if key[pygame.K_a] == True:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True:
        player.move_ip(1,0)
    elif key[pygame.K_w] == True:
        player.move_ip(0,-1)
    elif key[pygame.K_s] == True:
        player.move_ip(0,1)

    ##elif key[pygame.K_SPACE] == True:
    if key[pygame.K_LEFT] == True:
        player2.move_ip(-1,0)
    elif key[pygame.K_RIGHT] == True:
        player2.move_ip(1,0)
    elif key[pygame.K_UP] == True:
        player2.move_ip(0,-1)
    elif key[pygame.K_DOWN] == True:
        player2.move_ip(0,1)    
    
    
    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()
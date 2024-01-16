import pygame, sys, random
from pygame import Vector2



pygame.init()



clock = pygame.time.Clock()

cellSize = 40
numberOfCells = 27
W = H = cellSize * numberOfCells
screen = pygame.display.set_mode((W,H))

stacksPath = 'graphics/stacks.png'
fruitPath =  'graphics/Minion.png'
snakePath = ''

appleVisualization = pygame.image.load(fruitPath).convert_alpha()
scaledImage = pygame.transform.scale(appleVisualization,(40,40))

class Apple:
    def __init__(self):
        self.positionX = random.randint(0,numberOfCells - 1)
        self.positionY = random.randint(0,numberOfCells - 1)
        self.placement = Vector2(self.positionX, self.positionY)
    
    def refreshCords(self):
        self.positionX = random.randint(0,numberOfCells - 1)
        self.positionY = random.randint(0,numberOfCells - 1)
        return
    
    def spawnApple(self):
        appleShape = pygame.Rect(self.placement.x * cellSize, self.placement.y * cellSize, cellSize, cellSize)
        screen.blit(scaledImage,appleShape)
        ##pygame.draw.rect(screen,(200,40,40),appleShape)

class Snake:
    def __init__ (self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)

    def drawSnake(self):
        for block in self.body:
            piece = pygame.Rect(block.x * cellSize, block.y * cellSize, cellSize, cellSize)
            pygame.draw.rect(screen,(128,23,189),piece)
    
    def moveSnake(self):
        bodyTmp = self.body[:-1]
        bodyTmp.insert(0,bodyTmp + self.direction)

apple = Apple()
snake = Snake()

#def movements():
#    if key[pygame.K_a] == True:
 #       player.move_ip(-1,0)
  #  elif key[pygame.K_d] == True:
   #     player.move_ip(1,0)
    #elif key[pygame.K_w] == True:
     #   player.move_ip(0,-1)
    #elif key[pygame.K_s] == True:
     #   player.move_ip(0,1)

#class snake:


while True:

    screen.fill((50,150,20))
    #key = pygame.key.get_pressed()
    
    apple.spawnApple()  
    snake.drawSnake()
    ##apple.refreshCords()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60) #fps

   


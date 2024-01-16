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
        bodyTmp.insert(0,bodyTmp[0] + self.direction)
        self.body = bodyTmp[:]

##apple = Apple()
##snake = Snake()

def movements():
    if (action[pygame.K_a] == True) or (action[pygame.K_LEFT] == True):
        mainGame.snake.direction = (-1,0)
    elif (action[pygame.K_d] == True) or (action[pygame.K_RIGHT] == True):
        mainGame.snake.direction = (1,0)
    elif (action[pygame.K_w] == True) or (action[pygame.K_UP] == True):
        mainGame.snake.direction = (0,-1)
    elif (action[pygame.K_s] == True) or (action[pygame.K_DOWN] == True):
        mainGame.snake.direction = (0,1)

class MAIN:
    def __init__(self):
        self.snake = Snake()
        self.apple = Apple()
    
    def update(self):
        self.snake.moveSnake()
        
    def draw(self):
        self.snake.drawSnake()
        self.apple.spawnApple()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150) #timer

mainGame = MAIN()

while True:

    ##apple.refreshCords()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            mainGame.update()
        if event.type == pygame.KEYDOWN:
            action = pygame.key.get_pressed()
            movements()

    screen.fill((50,150,20))        
    mainGame.draw()
    pygame.display.update()
    clock.tick(60) #fps

   


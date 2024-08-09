import pygame as pg
import random
from win32api import GetSystemMetrics

#Game Constants
SCREEN_WIDTH, SCREEN_HEIGHT = GetSystemMetrics(0) * 0.6, GetSystemMetrics(1) * 0.8
print(SCREEN_WIDTH, SCREEN_HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

PLAYER_1_WIDTH, PLAYER_1_HEIGHT = 15, 75
PLAYER_2_WIDTH, PLAYER_2_HEIGHT = 15, 75
BALL_WIDTH, BALL_HEIGHT = 15, 15

#Start Screen Class
class StartScreen():
    def __init__(self):
        super(StartScreen).__init__()
        self.font = pg.font.SysFont("agency fb", 175)
        self.position = ((SCREEN_WIDTH / 2) - 225, (SCREEN_HEIGHT / 2) - 200)
        self.surf = self.font.render("P O N G !", False, WHITE)
    def addToScreen(self):
        screen.blit(self.surf, self.position)

#Start Button Class
class StartButton():
    def __init__(self):
        super(StartButton).__init__()
        self.surf = pg.Surface((115, 50))
        self.surf.fill(GRAY)
        self.rect = self.surf.get_rect()
        self.rect.x = (SCREEN_WIDTH / 2) - 65
        self.rect.y = (SCREEN_HEIGHT / 2) - (50 / 5)
        print(self.rect.x)

        self.font = pg.font.SysFont("corbel", 40)
        self.font_position = (self.rect.x + 2, self.rect.y + 5)
        self.font_surf = self.font.render("START", False, WHITE)
    def addToScreen(self):
        screen.blit(self.surf, self.rect)
        screen.blit(self.font_surf, self.font_position)

#Player 1 Class
class Player1(pg.sprite.Sprite):
    def __init__(self):
        super(Player1).__init__()
        self.surf = pg.Surface((PLAYER_1_WIDTH, PLAYER_1_HEIGHT))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.rect.x = 25
        self.rect.y = (SCREEN_HEIGHT / 2) - PLAYER_1_HEIGHT
    def addToScreen(self):
        screen.blit(self.surf, self.rect)
    def playerMove(self):
        self.pressed_keys = pg.key.get_pressed()
        if self.pressed_keys[pg.K_w]:
            self.rect.move_ip(0, -10)
        if self.pressed_keys[pg.K_s]:
            self.rect.move_ip(0, 10)
    def setBoundaries(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > (SCREEN_HEIGHT - PLAYER_1_HEIGHT):
            self.rect.y = SCREEN_HEIGHT - PLAYER_1_HEIGHT

#Player 2 Class
class Player2(pg.sprite.Sprite):
    def __init__(self):
        super(Player2).__init__()
        self.surf = pg.Surface((PLAYER_2_WIDTH, PLAYER_2_HEIGHT))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.rect.x = (SCREEN_WIDTH - 25) - PLAYER_2_WIDTH
        self.rect.y = (SCREEN_HEIGHT / 2) - PLAYER_2_HEIGHT
    def addToScreen(self):
        screen.blit(self.surf, self.rect) 
    def playerMove(self):
        self.pressed_keys = pg.key.get_pressed()
        if self.pressed_keys[pg.K_UP]:
            self.rect.move_ip(0, -10)
        if self.pressed_keys[pg.K_DOWN]:
            self.rect.move_ip(0, 10)
    def setBoundaries(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > (SCREEN_HEIGHT - PLAYER_2_HEIGHT):
            self.rect.y = SCREEN_HEIGHT - PLAYER_2_HEIGHT

#White Line Class
class Line():
    def __init__(self):
        super(Line).__init__()
        self.white_line = pg.image.load("C:/Users/sasen/Desktop/Aidan/Pong Project/Pong Line.png")
    def addToScreen(self):
        screen.blit(self.white_line, (SCREEN_WIDTH / 6, 15))

#Ball Class
class Ball(pg.sprite.Sprite):
    def __init__(self):
        super(Ball).__init__()
        self.surf = pg.Surface((BALL_WIDTH, BALL_HEIGHT))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()
        self.reset_ball()
    def addToScreen(self):
        screen.blit(self.surf, self.rect)
    def ballMove(self):
        self.rect = self.rect.move(self.velocity)
    def collideWithPlayers(self):
        self.collide1 = self.rect.colliderect(p1)
        self.collide2 = self.rect.colliderect(p2)

        if self.collide1:
            self.velocity[0] = 8
        if self.collide2:
            self.velocity[0] = -8
    def setBoundaries(self):
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.velocity[1] = -self.velocity[1]
    def reset_ball(self):
        self.rect.x = (SCREEN_WIDTH / 2) - BALL_WIDTH
        self.rect.y = random.randint(200, 400)
        self.velY = random.uniform(-8, 8)
        while self.velY > -1 and self.velY < 1:
            self.velY = random.uniform(-8, 8)

        self.moveNumber = random.randint(0, 1)
        if self.moveNumber == 0 and self.rect.y > 375:
            self.velY = random.uniform(1, 8)
            self.velocity = [-3, self.velY]
        elif self.moveNumber == 0 and self.rect.y < 225:
            self.velY = random.uniform(-1, -8)
            self.velocity = [-3, self.velY]
        elif self.moveNumber == 0:
            self.velocity = [-3, self.velY]
        elif self.moveNumber == 1 and self.rect.y > 375:
            self.velY = random.uniform(1, 8)
            self.velocity = [3, self.velY]
        elif self.moveNumber == 1 and self.rect.y < 225:
            self.velY = random.uniform(-1, -8)
            self.velocity = [3, self.velY]
        else:
            self.velocity = [3, self.velY]

#Left Score Class
class LeftScore():
    def __init__(self):
        super(LeftScore).__init__()
        self.font = pg.font.SysFont("agency fb", 75)
        self.value = -1
        self.position = ((SCREEN_WIDTH / 4) - 25, 25)
        self.surf = self.font.render(str(self.value), False, WHITE)
    def addToScreen(self):   
        screen.blit(self.surf, self.position)
    def updateScreen(self):
        if ball.rect.right >= SCREEN_WIDTH:
            self.value += 1
            ball.reset_ball()

        self.surf = self.font.render(str(self.value), False, WHITE)
        screen.blit(self.surf, self.position)

#Right Score Class
class RightScore():
    def __init__(self):
        super(RightScore).__init__()
        self.font = pg.font.SysFont("agency fb", 75)
        self.value = -1
        self.position = (SCREEN_WIDTH / 1.33, 25)
        self.surf = self.font.render(str(self.value), False, WHITE)
    def addToScreen(self):  
        screen.blit(self.surf, self.position)
    def updateScreen(self):
        if ball.rect.left <= 0:
            self.value += 1
            ball.reset_ball()

        self.surf = self.font.render(str(self.value), False, WHITE)
        screen.blit(self.surf, self.position)

#Player 1 Wins Class
class Player1Wins():
    def __init__(self):
        super(Player1Wins).__init__()
        self.font = pg.font.SysFont("agency fb", 85)
        self.position = ((SCREEN_WIDTH / 2) - 235, SCREEN_HEIGHT / 4)
        self.surf = self.font.render("PLAYER    1    WINS!", False, WHITE)
    def addToScreen(self):
        screen.blit(self.surf, self.position)

#Player 1 Wins Class
class Player2Wins():
    def __init__(self):
        super(Player2Wins).__init__()
        self.font = pg.font.SysFont("agency fb", 85)
        self.position = ((SCREEN_WIDTH / 2) - 235, SCREEN_HEIGHT / 4)
        self.surf = self.font.render("PLAYER    2    WINS", False, WHITE)
    def addToScreen(self):
        screen.blit(self.surf, self.position)

#Restart Button Class
class RestartButton():
    def __init__(self):
        super(RestartButton).__init__()
        self.surf = pg.Surface((157, 50))
        self.surf.fill(GRAY)
        self.rect = self.surf.get_rect()
        self.rect.x = (SCREEN_WIDTH / 2) - 55
        self.rect.y = (SCREEN_HEIGHT / 4) + 100

        self.font = pg.font.SysFont("corbel", 40)
        self.font_position = (self.rect.x + 2, self.rect.y + 5)
        self.font_surf = self.font.render("RESTART", False, WHITE)
    def addToScreen(self):
        screen.blit(self.surf, self.rect)
        screen.blit(self.font_surf, self.font_position)
        
#Initalize pygame
pg.init()
pg.font.init()

#Create the screen, set the title, and create clock
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Pong!")
clock = pg.time.Clock()

#Instantiate classes
startScreen = StartScreen()
startButton = StartButton()
p1 = Player1()
p2 = Player2()
line = Line()
ball = Ball()
leftScore = LeftScore()
rightScore = RightScore()
p1Wins = Player1Wins()
p2Wins = Player2Wins()
restartButton = RestartButton()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if startButton.rect.collidepoint(event.pos) or restartButton.rect.collidepoint(event.pos):
                leftScore.value = 0
                rightScore.value = 0

                p1.rect.x = 25
                p1.rect.y = (SCREEN_HEIGHT / 2) - PLAYER_1_HEIGHT

                p2.rect.x = (SCREEN_WIDTH - 25) - PLAYER_2_WIDTH
                p2.rect.y = (SCREEN_HEIGHT / 2) - PLAYER_2_HEIGHT

    if leftScore.value < 0 and rightScore.value < 0:
        startScreen.addToScreen()
        startButton.addToScreen()
    elif leftScore.value < 10 and rightScore.value < 10:
        startButton.rect.x = SCREEN_WIDTH + 500
        restartButton.rect.x = SCREEN_WIDTH + 500

        #Add player 1 to the screen and call its methods
        p1.addToScreen()
        p1.playerMove()
        p1.setBoundaries()

        #Add player 2 to the screen and call its methods
        p2.addToScreen()
        p2.playerMove()
        p2.setBoundaries()

        #Add white line to the screen
        line.addToScreen()

        #Add ball to the screen and call its methods
        ball.addToScreen()
        ball.ballMove()
        ball.collideWithPlayers()
        ball.setBoundaries()

        #Add left score to the screen and call its methods
        leftScore.addToScreen()
        leftScore.updateScreen()

        #Add right score to the screen and call its methods
        rightScore.addToScreen()
        rightScore.updateScreen()
    elif leftScore.value == 10:
        restartButton.rect.x = (SCREEN_WIDTH / 2) - 55

        #Changes the window to a player 1 wins screens and adds a restart button
        p1Wins.addToScreen()
        restartButton.addToScreen()
    else:
        restartButton.rect.x = (SCREEN_WIDTH / 2) - 55

        #Changes the window to a player 2 wins screens and adds a restart button
        p2Wins.addToScreen()
        restartButton.addToScreen() 

    pg.display.flip()
    screen.fill(BLACK)
    clock.tick(60)
    
pg.quit()
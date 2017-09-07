import pygame
import serial

def ShowImage(ourScreen, img, x, y):
    ourScreen.blit(img, (x,y))

def Selection_Menu(ourScreen, display_width, display_height):
    finish = False
    clock = pygame.time.Clock()
    Arduino = serial.Serial("COM6", 9600)
    isColored = -1
    pygame.init()

    GameStartPath = ['.\\GameMenu\\GameStart\\GameStart.png',
            '.\\GameMenu\\GameStart\\GameStartSelecting.png']

    OptionPath = ['.\\GameMenu\\Option\\Option.png',
                  '.\\GameMenu\\Option\\OptionSelecting.png']

    GameStart = pygame.image.load(GameStartPath[0])
    Option = pygame.image.load(OptionPath[0])

    GameStartX = (display_width * 0.5) - int(553/2)
    GameStartY = (display_height * 0.5) - 40

    OptionX = (display_width * 0.5) - Option.get_rect().size[0] * 0.5
    OptionY = (display_height * 0.5) - Option.get_rect().size[1] * 0.5 + 100

    while not finish:
        ourScreen.fill((255, 255, 200))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = not finish
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DELETE:
                    if isColored == 1:
                        #print("KEY DOWN!!!!")
                        return Arduino

        temp = str(Arduino.readline()).replace("b\'", "")
        temp = temp.replace("\\r\\n\'", "")
        #print(isColored)

        if(temp == "Down"):
            if(isColored == -1 or isColored == 0):
                GameStart = pygame.image.load(GameStartPath[1])
                Option = pygame.image.load(OptionPath[0])
                clock.tick(150)
                isColored = 1

            elif(isColored == 1)  :
                GameStart = pygame.image.load(GameStartPath[0])
                Option = pygame.image.load(OptionPath[1])
                clock.tick(150)
                isColored = 0

        ShowImage(ourScreen, GameStart, GameStartX, GameStartY)
        ShowImage(ourScreen, Option, OptionX, OptionY)
        pygame.display.flip()
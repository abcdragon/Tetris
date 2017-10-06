# coding = utf-8
import pygame
import SelectionMenu
import DrawAndRemove

pygame.init()

Shapes = [[0, 0, 160, 40], [0, 0, 80, 80]]
inputShape = ""
moveObject = list()
Rects = list()

display_width, display_height = 800, 800
backgorundColor = (255, 255, 200)
GameBoard = pygame.image.load('.\\Texture\\Background\\Background_Image.jpg')

clock = pygame.time
ourScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('테트리스')
ourScreen.fill(backgorundColor)
finish = False
Moving = None

#Arduino = SelectionMenu.Selection_Menu(ourScreen, display_width, display_height) # Selection 메뉴 실행

ourScreen.blit(GameBoard, (0, 0))
pygame.display.update()
'''for i in range(10) :
    for j in range(10):
        Rects.append([j*80, i*80, 80, 80])
        pygame.draw.rect(ourScreen, (0, 0, 0), (j*80, i*80, 80, 80), 4)

print(Rects)'''

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = not finish
        if event.type == pygame.KEYDOWN:
            if Moving is not None and event.key == pygame.K_RIGHT:
                moveObject = Moving.Side(False)
                print("Clicked!")
            if Moving is not None and event.key == pygame.K_LEFT:
                moveObject = Moving.Side(True)
                print("Clicked!")

            if event.key == pygame.K_DELETE:
                inputShape = input("Line, Squre 중에서 입력하세요")
                idx = 0
                if inputShape == "Line": idx = 0
                elif inputShape == "Squre": idx = 1

                #print(Rects[i])
                moveObject = Shapes[idx]
                Moving = DrawAndRemove.Drawing(ourScreen, moveObject, GameBoard)
                Moving.Draw()
                print(moveObject)

            if event.key == pygame.K_ESCAPE:
                finish = not finish

    #temp = str(Arduino.readline()).replace("b\'", "")
    #temp = temp.replace("\\r\\n\S
    #print(temp)

    if(len(moveObject) > 0):
        moveObject = Moving.Down()

        if(inputShape == "Squre"):
            if(moveObject[1] >= 720):
                moveObject = list()
                Moving = None

    clock.delay(400)

    #if(temp == "DOWN"):
        #DrawAndRemove.Down(ourScreen, moveObject, backgorundColor)

    pygame.display.update()

pygame.quit()
quit()
# coding = utf-8
import pygame
import SelectionMenu
import DrawAndRemove
import CustomSpr

pygame.init()

Shapes = [ ".\\Texture\\Block\\Block1.png",
           ".\\Texture\\Block\\Block2.png",
           ".\\Texture\\Block\\Block3.png",
           ".\\Texture\\Block\\Block4.png",
           ".\\Texture\\Block\\Block5.png"  ]

inputShape = ""
moveObject = None
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

downFlag = 0

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

                moveObjectSrc = Shapes[idx]

                moveObject = CustomSpr.SimpleSprite(moveObjectSrc, (0, 0))

                '''print(Moving is None)

                #print(Rects[i])
                moveObject = Shapes[idx]
                Moving = DrawAndRemove.Drawing(ourScreen, moveObject, GameBoard)
                Moving.Draw()
                print(moveObject)'''

            if event.key == pygame.K_ESCAPE:
                finish = not finish

    #temp = str(Arduino.readline()).replace("b\'", "")
    #temp = temp.replace("\\r\\n\S
    #print(temp)

    if(downFlag and moveObject is not None):
        temp = list(moveObject.get_Rect())
        temp[1] += 40
        moveObject.update(0, [temp[0], temp[1]])
        '''if(inputShape == "Squre" or inputShape == "Line"):
            if(moveObject[1] > 720):
                print("Limit")
                moveObject = list()
                Moving = None
                downFlag = not downFlag'''

    clock.delay(700)

    if not downFlag:
        downFlag = not downFlag

    #if(temp == "DOWN"):
        #DrawAndRemove.Down(ourScreen, moveObject, backgorundColor)

    pygame.display.update()

pygame.quit()
quit()
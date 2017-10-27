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
moveObjectGroup = None
Rects = list()

display_width, display_height = 800, 800
backgorundColor = (255, 255, 200, 255)
GameBoard = pygame.image.load('.\\Texture\\Background\\Background_Image.jpg')

clock = pygame.time
ourScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('테트리스')
ourScreen.fill(backgorundColor)
finish = False
Moving = None

BlockData = list()

#Arduino = SelectionMenu.Selection_Menu(ourScreen, display_width, display_height) # Selection 메뉴 실행

pygame.display.update()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = not finish
        if event.type == pygame.KEYDOWN:
            if not (moveObject is None) :
                if event.key == pygame.K_RIGHT:
                    if moveObject.rect.x < 400 :
                        moveObject.rect.x += 40
                    print("Right Clicked!")

                if event.key == pygame.K_LEFT:
                    if moveObject.rect.x > 0 :
                        moveObject.rect.x -= 40
                    print("Left Clicked!")

            if event.key == pygame.K_DELETE:
                inputShape = input("Line, Squre 중에서 입력하세요")
                idx = 0
                if inputShape == "Line": idx = 0
                elif inputShape == "Squre": idx = 1

                moveObjectSrc = Shapes[idx]

                moveObject = CustomSpr.SimpleSprite(moveObjectSrc, (0, 0))
                moveObjectGroup = pygame.sprite.RenderPlain(moveObject)

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

    if(moveObject is not None):
        if(moveObject.rect.y > 760):
            for i in range(1, 21):
                for j in range(1, 11):
                    x = 40 * j - 20
                    y = 40 * i - 20
                    getColor = ourScreen.get_at((x, y))
                    if getColor != backgorundColor :
                        print(getColor)
            print("Limit")
            moveObject = None
            Moving = None
        else :
            moveObject.rect.y += 40
            ourScreen.fill(backgorundColor)
            moveObjectGroup.draw(ourScreen)

    clock.delay(400)

    pygame.display.flip()

pygame.quit()
quit()
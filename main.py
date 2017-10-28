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
backgorundColor = [255, 255, 200, 255]
GameBoard = pygame.image.load('.\\Texture\\Background\\Background_Image.jpg')

clock = pygame.time
ourScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('테트리스')
ourScreen.fill(backgorundColor)
finish = False
Moving = None

BlockData = list()
mapState = []

#Arduino = SelectionMenu.Selection_Menu(ourScreen, display_width, display_height) # Selection 메뉴 실행

mapState = [[0 for i in range(10)] for j in range(20)]

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
                idx = int(input("0 ~ 4를 입력 : "))

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
        nowImageSize = moveObject.user_src_image.get_size()
        if(moveObject.rect.y >= (800 - nowImageSize[1])) :
            for i in range(1, 21):
                cnt = 0

                for j in range(1, 11):
                    x = -40 * j + 420
                    y = -40 * i + 820
                    getColor = list(ourScreen.get_at((x, y)))

                    #print(getColor, end = ' ')
                    if not ( getColor == backgorundColor ):
                        mapState[i-1][10-j] = 1
                        #print(getColor)

                    else :
                        cnt += 1

                if cnt == 10:
                    #print("i : ", i)
                    break

            print("Limit")
            moveObject = None
            Moving = None

            '''for i in range(20):
                for j in range(10):
                    print(mapState[i][j], end = ' ')

                print()'''

            # TODO 1. mapState의 값이 1인 애들은 40x40의 크기로 스프라이트를 생성후 그룹으로 묶기
            # TODO 2. 충돌 이벤트 만들기
        else :
            moveObject.rect.y += 40
            ourScreen.fill(backgorundColor)
            moveObjectGroup.draw(ourScreen)


    clock.delay(400)

    pygame.display.flip()

pygame.quit()
quit()
# coding = utf-8
import pygame
import SelectionMenu
import CustomSpr

pygame.init()

Piece = ".\\Texture\\Piece\\Piece.png"
Shapes = [ ".\\Texture\\Block\\Block1.png",
           ".\\Texture\\Block\\Block2.png",
           ".\\Texture\\Block\\Block3.png",
           ".\\Texture\\Block\\Block4.png",
           ".\\Texture\\Block\\Block5.png"  ]

BlockColors = [ [247, 150, 70, 255],   # Block1
                [ 31, 73, 125, 255],   # Block2
                [  0,  0,   0, 255],   # Block3
                [192,  80, 77, 255],   # Block4
                [112, 173, 71, 255] ]  # Block5
inputShape = ""
moveObject = None
moveObjectGroup = None
mapGroup = None

display_width, display_height = 800, 800
backgorundColor = [255, 255, 255, 255]
GameBoard = pygame.image.load('.\\Texture\\Background\\Background_Image.jpg')

clock = pygame.time
ourScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('테트리스')
ourScreen.fill(backgorundColor)
finish = False

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
                    #print("Right Clicked!")

                if event.key == pygame.K_LEFT:
                    if moveObject.rect.x > 0 :
                        moveObject.rect.x -= 40
                    #print("Left Clicked!")

            if event.key == pygame.K_DELETE:
                idx = int(input("0 ~ 4를 입력 : "))

                moveObjectSrc = Shapes[idx]

                moveObject = CustomSpr.SimpleSprite(moveObjectSrc, (0, 0))
                moveObjectGroup = pygame.sprite.RenderPlain(moveObject)

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
                    getColor = list( ourScreen.get_at((x, y)) )
                    #print(getColor, end = ' ')

                    if not ( getColor == backgorundColor ):
                        blocks = CustomSpr.BlockSprite(Piece, [x, y])
                        if mapGroup is None :
                            mapGroup = pygame.sprite.RenderPlain(blocks)
                        else :
                            mapGroup.add(blocks)

                    else :
                        cnt += 1

                if cnt == 10:
                    #print("i : ", i)
                    break

            print("Limit")
            #print( mapGroup )

            moveObject = None

            # TODO 2. 충돌 이벤트 만들기
        else :
            moveObject.rect.y += 40
            ourScreen.fill(backgorundColor)
            moveObjectGroup.draw(ourScreen)
            if not (mapGroup is None) : mapGroup.draw(ourScreen)

    clock.delay(400)
    pygame.display.flip()

pygame.quit()
quit()
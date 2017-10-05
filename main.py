# coding = utf-8
import pygame
import SelectionMenu
import DrawAndRemove

pygame.init()

Shapes = [[0, 1, 2, 3], [0, 1, 10, 11]]
inputShape = ""
moveObject = list()
Rects = list()

display_width, display_height = 1300, 800
backgorundColor = (255, 255, 200)

clock = pygame.time
ourScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('테트리스')
ourScreen.fill(backgorundColor)
finish = False

#Arduino = SelectionMenu.Selection_Menu(ourScreen, display_width, display_height) # Selection 메뉴 실행

for i in range(10) :
    for j in range(10):
        Rects.append([j*80, i*80, 80, 80])
        pygame.draw.rect(ourScreen, (0, 0, 0), (j*80, i*80, 80, 80), 4)

print(Rects)

pygame.draw.line(ourScreen, (0, 0, 0), (display_height, 0), (display_height, display_height), 2)
pygame.display.flip()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = not finish
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                inputShape = input("Line, Squre 중에서 입력하세요")
                idx = 0
                if inputShape == "Line": idx = 0
                elif inputShape == "Squre": idx = 1

                for i in range(len(Shapes[idx])):
                    #print(Rects[i])
                    RectsIdx = Shapes[idx][i]
                    DrawAndRemove.Draw(ourScreen, Rects[RectsIdx], (0, 0, 0), 0)
                    moveObject.append(Rects[RectsIdx])

            if event.key == pygame.K_ESCAPE:
                finish = not finish

    #temp = str(Arduino.readline()).replace("b\'", "")
    #temp = temp.replace("\\r\\n\S
    #print(temp)

    moveObject = DrawAndRemove.Down(ourScreen, moveObject, backgorundColor)

    print(moveObject)

    if(inputShape == "Squre" and len(moveObject) > 0):
        if(moveObject[3][1] == 720):
            moveObject = list()

    clock.delay(1000)

    #if(temp == "DOWN"):
        #DrawAndRemove.Down(ourScreen, moveObject, backgorundColor)

    pygame.display.flip()

pygame.quit()
quit()
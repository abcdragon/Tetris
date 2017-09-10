# coding = utf-8
import pygame
import SelectionMenu
import DrawAndRemove

pygame.init()

Shapes = [(0, 1, 2, 3), (0, 1, 10, 11)]
moveObject = list()
Rects = list()

display_width, display_height = 1300, 800
backgorundColor = (255, 255, 200)

clock = pygame.time
ourScreen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('테트리스')
ourScreen.fill(backgorundColor)
finish = False

Arduino = SelectionMenu.Selection_Menu(ourScreen, display_width, display_height) # Selection 메뉴 실행

for i in range(10) :
    for j in range(10):
        Rects.append((j*80, i*80, 80, 80))
        pygame.draw.rect(ourScreen, (0, 0, 0), (j*80, i*80, 80, 80), 4)

pygame.draw.line(ourScreen, (0, 0, 0), (display_height, 0), (display_height, display_height), 2)
pygame.display.flip()

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = not finish
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                shape = input("Line, Squre 중에서 입력하세요")
                if shape == "Line":
                    for i in range(len(Shapes[0])):
                        #print(Rects[i])
                        DrawAndRemove.Draw(ourScreen, (0, 0, 0), Rects[i], 0)
                        moveObject.append(Rects[i])
                elif shape == "Squre":
                    for i in range(len(Shapes[1])):
                        pygame.draw.rect(ourScreen, (0, 0, 0), Rects[i], 0)

    temp = str(Arduino.readline()).replace("b\'", "")
    temp = temp.replace("\\r\\n\'", "")
    #print(temp)

    DrawAndRemove.Down(ourScreen, moveObject, backgorundColor)
    clock.delay(1000)

    if(temp == "DOWN"):
        DrawAndRemove.Down(ourScreen, moveObject, backgorundColor)

    pygame.display.flip()

pygame.quit()
quit()
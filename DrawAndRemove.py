import pygame

def Draw(Screen, Color, tempRect, Width):
    #print(tempRect)
    pygame.draw.rect(Screen, Color, tempRect, Width)

def Remove(Screen, Color, tempRect):
    Draw(Screen, tempRect, Color, 0)
    Draw(Screen, tempRect, (0, 0, 0), 4)

def Down(Screen, moveObject, backgoundColor):
    for i in range(len(moveObject)):
        Remove(Screen, backgoundColor, moveObject[i])
        Draw(Screen, backgoundColor, (moveObject[i][0]+80, moveObject[i][1]+80, moveObject[i][2], moveObject[i][3]), 0)

    return
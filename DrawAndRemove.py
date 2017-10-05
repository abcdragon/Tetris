import pygame

def Draw(Screen, moveObject, Color, Width):
    #print(tempRect)
    pygame.draw.rect(Screen, Color, moveObject, Width)

def Remove(Screen, moveObject, Color):
    Draw(Screen, moveObject, Color, 0)
    Draw(Screen, moveObject, (0, 0, 0), 4)

def Down(Screen, moveObject, Color):
    for i in range(len(moveObject)):
        #print("moveObject[i] {}".format(moveObject[i]))
        Remove(Screen, moveObject[i], Color)
        #moveObject[i][0] = moveObject[i][0] + 80
        moveObject[i][1] = moveObject[i][1] + 80

    for i in range(len(moveObject)):
        print("moveObject's elements : {}".format(moveObject[i]))
        Draw(Screen, moveObject[i], (0, 0, 0), 0)

    return moveObject
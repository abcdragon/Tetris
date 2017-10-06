import pygame

Black = (0, 0, 0)

class Drawing:
    DrawScreen, MoveObject, Image = None, None, None

    def __init__(self, _DrawScreen, _MoveObject, _Image):
        self.DrawScreen = _DrawScreen
        self.MoveObject = _MoveObject
        self.Image = _Image

    def Draw(self):
        #print(tempRect)
        pygame.draw.rect(self.DrawScreen, Black, self.MoveObject, 0)

    def Remove(self):
        self.DrawScreen.blit(self.Image, (0, 0))

    def Down(self):
        print("this is DrawAndRemove : {}".format(self.MoveObject))
        self.MoveObject[1] += 40

        self.Remove()
        self.Draw()

        return self.MoveObject

    def Side(self, IsLeft):
        if IsLeft and self.MoveObject[0] > 0  : self.MoveObject[0] -= 40
        if not IsLeft and self.MoveObject[0] <= 280 : self.MoveObject[0] += 40

        self.Remove()
        self.Draw()

        return self.MoveObject

    def turn(self):
        pass # 블럭 회전
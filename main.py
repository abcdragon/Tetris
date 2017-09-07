# coding = utf-8
import pygame
import SelectionMenu

pygame.init()

display_width = 1300
display_height = 800
backgorundColor = (255, 255, 200)
ourScreen = pygame.display.set_mode((display_width, display_height))
ourScreen.fill(backgorundColor)

Arduino = SelectionMenu.Selection_Menu(ourScreen, display_width, display_height) # Selection 메뉴 실행

clock = pygame.time.Clock()
pygame.display.set_caption('테트리스')
finish = False

Rects = list()

for i in range(10) :
    for j in range(10):
        Rects.append((j*80, i*80, 80, 80))
        pygame.draw.rect(ourScreen, (0, 0, 0), (j*80, i*80, 80, 80), 4)


sampleSprite = pygame.sprite.Sprite()
sampleSprite.image = pygame.image.load("다운로드.jpg").convert()
sampleSprite.rect = sampleSprite.image.get_rect()
sampleSprite.rect.topleft = [0, 0]
ourScreen.blit(sampleSprite.image, sampleSprite.rect)

colorBlue = True

x, y, degree = 0, 0, 90

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = not finish


    temp = str(Arduino.readline()).replace("b\'", "")
    temp = temp.replace("\\r\\n\'", "")
    #print(temp)

    if(temp == "UP"):
        #print("DEGREE : {}", degree)
        sampleSprite.image = pygame.transform.rotate(sampleSprite.image, degree)

        if(degree == 270) : degree = 0
        else : degree = degree + 90

    if(temp == "LEFT"):
        x = x - 10

    if(temp == "RIGHT"):
        x = x + 10

    ourScreen.fill(backgorundColor)

    sampleSprite.rect.x = x

    ourScreen.blit(sampleSprite.image, sampleSprite.rect)
    pygame.draw.line(ourScreen, (0, 0, 0), (display_height, 0), (display_height, display_height), 2)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
quit()
import pygame
import CustomSpr

pygame.init()

screen = pygame.display.set_mode((300, 300))

pygame.display.set_caption('테트리스')
screen.fill((255, 255, 255))


simple = CustomSpr.SimpleSprite(".\\Texture\\Block\\Block1.png", (0, 0))
simple_group = pygame.sprite.RenderPlain(simple)


finish = False

while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = not finish

    simple_group.draw(screen)
    pygame.display.update()
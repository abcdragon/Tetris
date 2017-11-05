import pygame

class SimpleSprite( pygame.sprite.Sprite ):
    def __init__(self, image, position):  # 생성자 파라미터로 스프라이트에 사용될 이미지 경로와 스프라이트 초기 위치를 받는다
        pygame.sprite.Sprite.__init__( self )
        self.user_src_image = pygame.image.load( image )  # 스프라이트에 사용될 이미지를 저장할 사용자 변수
        self.user_position = position  # 스프라이트의 위치를 저장할 사용자 변수
        self.user_rotation = 0  # 스프라이트의 회전 각도를 저장할 사용자 변수
        self.image = self.user_src_image
        self.rect = self.image.get_rect()

    def update(self, rotation, position):  # 스프라이트의 상태를 업데이트 하는 함수. 필요에 따라 파라미터가 추가될 수도 있다.
        self.user_position = position

        print("user_position : ", self.user_position)

        self.user_rotation = rotation

        # 출력에 사용될 이미지, 위치를 정한다
        self.image = pygame.transform.rotate( self.user_src_image, self.user_rotation )  # 이미지를 회전 각도 만큼 회전시킨다
        self.rect = self.image.get_rect()
        self.rect.center = self.user_position  # 이미지의 출력 위치를 정한다

class BlockSprite(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__( self )
        self.image = pygame.image.load( image )
        self.position = position

        self.rect = self.image.get_rect()
        self.rect.center = position

#출처: http: // devnauts.tistory.com / 63[devnauts]
import os
import pygame

######################################################################################

# 기본 초기화(반드시 해야 하는 것들)
pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 640
screen_height = 480
screen =pygame.display.set_mode((screen_width, screen_height))   # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("AngryPang")    # 게임 이름 설정

# FPS
clock = pygame.time.Clock()

########################################################################################

# 1. 사용자 게임 초기화 (화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")  # 이미지 폴더 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 스테이지의 높이 위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - stage_height - character_height

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도


# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 / 폰트의 종류와 크기

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 시작 tick을 받아옴

# 이벤트 루프 : 화면이 꺼지지 않게 하는 장치
running = True  # 게임이 진행중인지 확인(True = 게임이 진행 중이다)
while running:
    dt = clock.tick(60)        # 원하는 게임 화면의 초당 프레임 수 입력


    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():     # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:    # 창이 닫히는 이벤트인가? 그렇다면 게임을 종료
            running = False       # 게임이 더이상 진행중이 아님


    # 4. 충돌 처리


    # 5. 화면에 그리기
    # screen.fill((0, 0, 255))   # 이미지 불러오기 대신 색깔로 채우기 - RGB 값으로 
    screen.blit(background, (0, 0))    
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    # 타이머 집어넣기
    # 경과한 시간 계산

    # 시간이 0 이하이면 게임 종료
    
    pygame.display.update()     # 매 프레임마다 게임화면을 다시 그려주기 -> 계속 업데이트해줘야 함

# 종료 전 잠시 대기
pygame.time.delay(2000)   # 2초 정도 대기

# pygame 종료
pygame. quit()

























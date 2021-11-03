import pygame

######################################################################################

# 기본 초기화(반드시 해야 하는 것들)
pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 360   
screen_height = 480
screen =pygame.display.set_mode((screen_width, screen_height))   # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("벌레소피하기")    # 게임 이름 설정

# FPS
clock = pygame.time.Clock()

# # 게임 제목 설정
# title_font = pygame.font.Font(None, 30)  # 폰트 객체 생성 / 폰트의 종류와 크기
# title = title_font.render(str("<AVOID BUGCOW>"), True, (255, 255, 255))
# screen.blit(title, (73, 10))

########################################################################################

# 1. 사용자 게임 초기화 (화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 이미지 불러오기
background = pygame.image.load("C:\\PythonWorkspace\\pygame_basic\\background.png")      # 탈출 문자 때문에 역슬러시 2개씩 넣어주기

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:\\PythonWorkspace\\pygame_basic\\character2.png")
character_size = character.get_rect().size   # 이미지의 크기를 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2   # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height   # 화면 세로의 맨 밑에 해당하는 곳에 위치

# 이동할 좌표
to_x = 0
to_y = 0

enemy_to_x = 0
enemy_to_y = 0

# 이동 속도
character_speed = 0.45
enemy_speed = 0.3

# 적 캐릭터 생성
from random import *

enemy = pygame.image.load("C:\\PythonWorkspace\\pygame_basic\\enemy1.png")
enemy_size = enemy.get_rect().size   # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0   

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 / 폰트의 종류와 크기

# 총 시간
total_time = 30

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 시작 tick을 받아옴

# 이벤트 루프 : 화면이 꺼지지 않게 하는 장치
running = True  # 게임이 진행중인지 확인(True = 게임이 진행 중이다)
while running:
    enemy_to_y = enemy_speed
    dt = clock.tick(60)        # 원하는 게임 화면의 초당 프레임 수 입력
    # print("FPS :" + str(clock.get_fps()))         # fps 값에 따라 유닛의 이동 속도 자체는 바뀌면 안됨. 끊기는지 버벅거리는지 그것만 바뀌어야 함. 

# 캐릭터가 100만큼 이동해야 한다고 가정했을 때, 
# 10fps : 1초에 10번 동작 -> 1번에 10만큼 이동해야 함
# 20fps : 1초에 20번 동작 -> 1번에 5만큼 이동해야 함

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():     # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:    # 창이 닫히는 이벤트인가? 그렇다면 게임을 종료
            running = False       # 게임이 더이상 진행중이 아님

        # 3. 캐릭터 위치 설정
        if event.type == pygame.KEYDOWN:  # 키보드가 눌렸는지 확인
            if event.key == pygame.K_LEFT:   # 왼쪽 키를 누른 경우
                to_x -= character_speed  # 1만큼 왼쪽으로 이동
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            # elif event.key == pygame.K_UP:
            #     enemy_to_y += enemy_speed
            # elif event.key == pygame.K_DOWN:
            #     enemy_to_y += enemy_speed

        if event.type == pygame.KEYUP:    #  키보드에서 손을 뗄 경우
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
                # enemy_to_y += enemy_speed
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    enemy_y_pos += enemy_to_y * dt
    if enemy_y_pos > screen_height:
        enemy_x_pos = randint(0, screen_width - enemy_width)
        enemy_y_pos = 0



    # 가로세로 경곗값 벗어나지 못하게 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos    # 캐릭터의 실제 위치 정보로 rect 정보를 업데이트

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):    # 충돌 여부를 확인   
        print("충돌했습니다.")
        running = False   # 게임 종료, while문 탈출

    # 5. 화면에 그리기
    # screen.fill((0, 0, 255))   # 이미지 불러오기 대신 색깔로 채우기 - RGB 값으로 
    screen.blit(background, (0, 0))    # (0, 0) 위치를 기준으로 background 이미지를 그리겠다
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적 그리기

    # 타이머 집어넣기
    # 경과한 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  # 경과시간을 1000으로 나누어서 초 단위로 표시( 원래 밀리초 단위)

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))   # render을 입력하고 입력할 텍스트를 입력, True, 색상 정보 입력
    screen.blit(timer, (10, 10))

    # 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False
    
    pygame.display.update()     # 매 프레임마다 게임화면을 다시 그려주기 -> 계속 업데이트해줘야 함

# 종료 전 잠시 대기
pygame.time.delay(2000)   # 2초 정도 대기

# pygame 종료
pygame. quit()

















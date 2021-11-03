import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 360   
screen_height = 480
screen =pygame.display.set_mode((screen_width, screen_height))   # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")    # 게임 이름 설정

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

# 이벤트 루프 : 화면이 꺼지지 않게 하는 장치
running = True  # 게임이 진행중인지 확인(True = 게임이 진행 중이다)
while running:
    for event in pygame.event.get():     # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:    # 창이 닫히는 이벤틍인가? 그렇다면 게임을 종료
            running = False       # 게임이 더이상 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키보드가 눌렸는지 확인
            if event.key == pygame.K_LEFT:   # 왼쪽 키를 누른 경우
                to_x -= 0.1  # 1만큼 왼쪽으로 이동
            elif event.key == pygame.K_RIGHT:
                to_x += 0.1
            elif event.key == pygame.K_UP:
                to_y -= 0.1
            elif event.key == pygame.K_DOWN:
                to_y += 0.1

        if event.type == pygame.KEYUP:    #  키보드에서 손을 뗄 경우
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    character_x_pos += to_x
    character_y_pos += to_y

    # 가로세로 경곗값 벗어나지 못하게 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # screen.fill((0, 0, 255))   # 이미지 불러오기 대신 색깔로 채우기 - RGB 값으로 
    screen.blit(background, (0, 0))    # (0, 0) 위치를 기준으로 background 이미지를 그리겠다
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()     # 매 프레임마다 게임화면을 다시 그려주기 -> 계속 업데이트해줘야 함

# pygame 종료
pygame. quit()

















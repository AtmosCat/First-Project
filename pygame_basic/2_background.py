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

# 이벤트 루프 : 화면이 꺼지지 않게 하는 장치
running = True  # 게임이 진행중인지 확인(True = 게임이 진행 중이다)
while running:
    for event in pygame.event.get():     # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:    # 창이 닫히는 이벤틍인가? 그렇다면 게임을 종료
            running = False       # 게임이 더이상 진행중이 아님

    # screen.fill((0, 0, 255))   # 이미지 불러오기 대신 색깔로 채우기 - RGB 값으로 
    screen.blit(background, (0, 0))    # (0, 0) 위치를 기준으로 background 이미지를 그리겠다

    pygame.display.update()     # 매 프레임마다 게임화면을 다시 그려주기 -> 계속 업데이트해줘야 함

# pygame 종료
pygame. quit()

















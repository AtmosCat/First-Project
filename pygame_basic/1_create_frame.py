import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 360   
screen_height = 480
screen =pygame.display.set_mode((screen_width, screen_height))   # 화면 크기 설정

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")    # 게임 이름 설정

# 이벤트 루프 : 화면이 꺼지지 않게 하는 장치
running = True  # 게임이 진행중인지 확인(True = 게임이 진행 중이다)
while running:
    for event in pygame.event.get():     # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:    # 창이 닫히는 이벤틍인가? 그렇다면 게임을 종료
            running = False       # 게임이 더이상 진행중이 아님


# pygame 종료
pygame. quit()

















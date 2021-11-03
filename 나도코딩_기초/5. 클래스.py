## 클래스

# name = "marine"
# hp = 40
# damage = 5

# print("{} 유닛 생성".format(name))
# print("체력 : {}".format(hp))
# print("공격력 : {}\n".format(damage))

# tank_name = "tank"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛 생성".format(tank_name))
# print("체력 : {}".format(tank_hp))
# print("공격력 : {}\n".format(tank_damage))

# tank2_name = "tank2"
# tank2_hp = 200
# tank2_damage = 55

# print("{} 유닛 생성".format(tank2_name))
# print("체력 : {}".format(tank2_hp))
# print("공격력 : {}\n".format(tank2_damage))

# def attack(name, location, damage):
#     print("{} : {} 방향으로 적군을 공격합니다. [공격력 : {}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# # 일반 유닛
# class Unit:  
#     def __init__(self, name, hp, speed):      # 생성자
#         self.name = name      # 멤버 변수 : 클래스 내에서 정의된 변수
#         self.hp = hp
#         self.speed = speed
#         print("{} 유닛이 생성되었습니다.".format(name))
        
#     def move(self, location):
#         print("{} : {} 방향으로 이동합니다. [속도 : {}]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {}입니다".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print("{} : 파괴되었습니다.".format(self.name))


# # marine1 = Unit("마린", 40, 5)     # 객체 : 클래스로부터 만들어지는 녀석들
# # marine2 = Unit("마린", 40, 5)     # init에 주어진 self를 제외한 갯수만큼을 무조건 입력해줘야 객체 생성 가능
# # tank = Unit("탱크", 150, 35)

# # wraith1 = Unit("레이스", 80, 5)
# # print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))        # .을 활용해 멤버변수 호출 가능

# # wraith2 = Unit("뺴앗은 레이스", 80, 5)
# # wraith2.clocking = True      # 외부에서 clocking이라는 객체의 멤버 변수를 추가함.  . wraith2에서만 가능(확장한 객체에서만 적용)

# # if wraith2.clocking == True:
# #     print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))

# # 메소드

# # 공격 유닛
# class AttackUnit(Unit):       # 공격유닛 클래스는 일반 유닛을 상속받아 만들어진 것임
#     def __init__(self, name, hp, speed, damage): 
#         Unit.__init__(self, name, hp, speed)   # 일반 유닛 클래스로부터 name, hp를 상속받음
#         self.damage = damage

#     def attack(self, location):
#         print("{} : {} 방향으로 적군을 공격합니다. 공격력 : {}".format(self.name, location, self.damage))   # name, damage에서는 self를 씀으로써 init에서의 값 사용, 
#                                                                                                             # location에서는 입력받은 값 사용

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩 기능 : 일정 시간 동안 자기 체력 10을 써서 공격 속도와 이동 속도 부스터
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else : 
#             print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜 더 높은 파워로 공격 가능, 이동은 불가
#     seize_developed = False # 시즈모드 개발 여부
    
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return 
#         # 현재 시즈모드가 아닐 떄 -> 활성화
#         if self.seize_mode == False:
#             print("{} : 시즈모드로 전환합니다".format(self.name))
#             self.damage *= self.damage
#             self.seize_mode = True

#         # 현재 시즈모드일 때 -> 해제
#         else :
#             print("{} : 시즈모드를 해제합니다".format(self.name))
#             self.damage /= self.damage
#             self.seize_mode = False

# # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # firebat1.attack("5시")

# # firebat1.damaged(25)
# # firebat1.damaged(25)


# # 다중상속 : 부모가 둘 이상

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{} : {} 방향으로 날아갑니다. [속도 : {}]".format(name, location, self.flying_speed))


# class FlyableAttackUnit(AttackUnit, Flyable):        # 두 클래스로부터 다중상속 : 공격 기능이 있는 공중 유닛
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)       # 공중 유닛이므로 지상 스피드는 0으로 처리
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         self.fly(self.name, location)

# # 레이스 생성
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False   # 클로킹 모드( 처음에는 해제 상태)

#     def clocking(self):
#         # 클로킹 모드일 때
#         if self.clocked == True:
#             print("{} : 클로킹 모드를 해제합니다".format(self.name))
#             self.clocked == False
#         else :
#             print("{} : 클로킹 모드를 설정합니다".format(self.name))
#             self.clocked == True

# def game_start():
#     print("새로운 게임 시작")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다")

# # 실제 게임 진행

# from random import *

# game_start()

# # 유닛 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# # 유닛 일괄 관리
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("탱크 시즈 모드 개발")

# # 공격 모드 준비 (탱크 : 시즈모드, 레이스 : 클로킹, 마린: 스팀팩)
# for unit in attack_units:
#     if isinstance(unit, Marine):     # 특정 유닛이 어느 클래스인지 확인
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21))   # 공격은 랜덤으로 받음, 5~20 사이

# # 게임 종료
# game_over()




# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# # 메소드 오버라이딩

# # 벌쳐 : 지상 유닛, 기동력이 좋음

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중유닛
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")         # 같은 이동 함수인데 공중 유닛과 지상유닛은 함수를 따로따로 써야 함 --> 귀찮음. 오버라이딩 사용 --> line99로 이동(똑같이 move사용)
# battlecruiser.move("9시")     # 공중 유닛에서 move 함수를 써도 오류가 나지 않음 :   


# # pass

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass     # 아무 명령 실행 안 하고 넘어감

# # 서플라이 디폿 : 건물 1개당 8개까지 유닛 생성 가능
# supply_depot = BuildingUnit("서플라이디폿", 500, "7시")

# def game_start():
#     print("새로운 게임 시작")

# def game_over():
#     pass

# game_start()
# game_over()


# # super -> Pracrice_class.py 참고

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0)      # 바로 위 줄 Unit.__init__ 대신 쓸 수 있는 구문, ()와 함께 써야 하고 self는 쓰지 않음
#         self.location = location


# 퀴즈 : 부동산 프로그램 작성
# 총 3대의 매물이 있음
# 출력 예제
# 강남 아파트 매매 10억, 2010
# 마포 오피스텔 전세, 5억 2007
# 송파 빌라 월세, 500/50, 2000
        
class House:
    print("총 3대의 매물이 있습니다.")
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year    
    def show_detail(self):
        print("{} {} {} {} {}".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

gangnam = House("강남", "아파트", "매매", "10억", "2010년")
mapo = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa = House("송파", "빌라", "월세", "500/50", "2000년")

house_list = []
house_list.append(gangnam)
house_list.append(mapo)
house_list.append(songpa)

for i in house_list:
    i.show_detail()

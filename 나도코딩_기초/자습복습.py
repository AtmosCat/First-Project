# 2. 자료구조

# cabinet = {3 : "yoo", 100 : "kim"}
# print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet.get(5, "possible"))

# del(cabinet[3])
# print(cabinet)

# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

# cabinet.clear()
# print(cabinet)

# menu =("pork", "meat")
# print(menu[0])
# print(menu[1])

# name = "kim"
# age = 20
# hobby = "workingout"
# print(name, age, hobby)

# setss = {1, 2, 3, 3, 4, 5}
# print(setss)

# java = {"yoo", "lee", "kim"}
# python = set(["kim", "park"])

# print(java & python)
# print(java.intersection(python))

# print(java|python)
# print(java.union(python))

# print(java - python)
# print(java.difference(python))

# java.add("jeong")
# print(java)

# java.remove("jeong")
# print(java)


# 3. 제어문

# customer = "Thor"
# index = 5
# while index >= 1:
#     print("{}번 손님, 커피가 준비되었습니다. 앞으로 {}분 남았습니다.".format(index, index-1))
#     index -= 1
#     if index == 0:
#         print("커피가 폐기되었습니다.")


# absent = [2, 5]
# nobook = [4]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in nobook:
#         print("잠깐, 오늘 수업 여기까지. {}는 교무실로".format(student))
#         break
#     print("{}, 책 이어서 읽어".format(student))


# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i + 100 for i in students]
# print(students)

# students2 = ['yoo', 'kim', 'jeong']
# students2 = [len(i) for i in students2]
# print(students2)


# from random import *

# people = 0

# for i in range(1, 51):
#     time = randint(5, 51)
#     if 5 <= time <= 15:
#         people += 1

# print(people)


# 4. 함수

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(name, age, end = "")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print(name, age)
#     for lang in language:
#         print(lang, end = " ")

# profile("yoo", 20, "python", "java", "C+", "C++","C++")
# profile("kim", 25, "kotlin", "swift", "", "", "", "")

# gun = 10

# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("left soldiers : {}".format(gun))

# # checkpoint(4)

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("left soldiers : {}".format(gun))
#     return gun

# checkpoint_ret(12, 3)


# def std_weight(gender, height):
#     if gender == "man":
#         weight = round(height*height * 22, 2)
#         print("your std_weight = {}".format(weight))
#     elif gender == "woman":
#         weight = round(height*height * 21, 2)
#         print("your std_weight = {}".format(weight))
#     else:
#         input("enter your gender info again : ")

# std_weight("man", 1.55)
# std_weight("woman", 1.32)
# std_weight("wo", 1.55)


# # 5. 클래스

# name = 'Marine'
# hp = 40
# damage = 5

# print("{} unit made".format(name))
# print("hp : {}".format(hp))
# print("damage : {}".format(damage))

# print("#"*50)

# tank_name = "tank"
# tank_hp = 150
# tank_damage = 35

# print("{} unit made".format(tank_name))
# print("hp : {}".format(tank_hp))
# print("damage : {}".format(tank_damage))

# print("#"*50)

# tank2_name = "tank2"
# tank2_hp = 200
# tank2_damage = 55

# print("{} 유닛 생성".format(tank2_name))
# print("체력 : {}".format(tank2_hp))
# print("공격력 : {}\n".format(tank2_damage))

# print("#"*50)

# def attack(name, location, damage):
#     print("{}, attack to {} direction / damage : {}".format(name, location, damage))
    
# attack(name, 1, damage)
# attack(tank_name, 12, tank_damage)
# attack(tank2_name, 3, tank2_damage)

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{} unit made".format(name))

#     def move(self, location):
#         print("{}, move to {} direction / speed : {}".format(self.name, location, self.speed))
                
#     def damaged(self, damage):
#         print("{}, got {} damage".format(self.name, damage))
#         self.hp -= damage
#         print("now {} hp : {}".format(self.name, self.hp))
#         if self.hp <=0:
#             print('{} : destroyed'.format(self.name))

# marine1 = Unit("marine", 50, 5)
# marine2 = Unit("marine", 50, 5)
# tank1 = Unit("tank", 150, 35)
# wraith1 = Unit("wraith", 80, 5)

# team_a = [marine1, marine2, tank1, wraith1]
# print("<Team A SQUAD>")
# for i in team_a:
#     print("name : {}, hp : {}".format(i.name, i.hp))

# wraith2 = Unit("stolen wraith", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{} : now clocked".format(wraith2.name))

# class AttackUnit(Unit):     # 상속
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)       # 상기 항목 물려받음
#         self.damage = damage   # 상속받지 않은 항목인 damage만 self.damage 새로정의

#     def attack(self, location):
#         print("{} : attack to {} direction / damage : {}".format(self.name, location, self.damage))

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "Marine", 40, 1, 5)
#     def stimpack(self):
#         if self.hp > 10:
#             print("{} : Activate stimpack(hp 10 down)".format(self.name))
#         else:
#             print("{} : lack of hp, inactivate stimpack".format(self.name))

# class Tank(AttackUnit):
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self, "Tank", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         if self.seize_mode == False : 
#             print("{} : activate seize mode".format(self.name))
#             self.damage *= self.damage
#             self.seize_mode = True
#         else:
#             print("{} : inactivate seize mode".format(self.name))
#             self.damage /= self.damage
#             self.seize_mode = False

# firebat1 = AttackUnit("firebat", 50, 16, 6)
# firebat1.attack(1)
# firebat1.damaged(25)
# firebat1.damaged(25)


# # 다중상속
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{} : fly to {} direction / speed : {}".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit(self, name, hp, 0, damage)
#         Flyable(self, flying_speed)
    
#     def move(self, location):
#         self.fly(self.name, location)

# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 6)
#         self.clocked = False

#     def clocking(self):
#         if self.clocked == True:
#             print("{} : inactivate clocking mode".format(self.name))
#             self.clocked = False
#         else:
#             print("{} : activate clocking mode".format(self.name))
#             self.clocked = True

# def game_start():
#     print("Game Start")

# def game_over():
#     print("player : gg")
#     print("Player : game out")
    
# from random import *

# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_developed = True
# print("Tank seize mode on")

# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# for unit in attack_units:
#     unit.attack("1시")

# for unit in attack_units:
#     unit.damaged(randint(5, 21))

# game_over()

# valkyrie = FlyableAttackUnit("Valkyrie", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# vulture = AttackUnit("Vulture", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("BattleCruiser", 500, 25, 3)

# vulture.move('11시')
# battlecruiser.fly(battlecruiser.name, "9시")

# battlecruiser.move("9시")


# #6. 예외처리
# try:
#     print("division only calcultor")
#     nums = []
#     nums.append(int(input("insert first number")))
#     nums.append(int(input("insert second number")))
#     nums.append(nums[0] / nums[1])
#     print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("Error! Wrong Value")
# except ZeroDivisionError as err:
#     print(err)
# # except:
# #     print("Unknown Error")
# except Exception as err:
#     print("Unknown Error")
#     print(err)

# # # 에러 발생시키기 & # 사용자 정의 예외처리 : 에러 정의하기

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("0~9 divisoin only calculator")
#     num1 = int(input("insert first number"))
#     num2 = int(input("insert second number"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("Inserted Number : {}, {}".format(num1, num2))
#     print("{} / {} : {}".format(num1, num2, int(num1, num2)))
# except ValueError:
#     print("Wrong Number! Only insert 0~9")
# except BigNumberError as err:
#     print("Error! Only 0~9")   
#     print(err)
# finally:
#     print("Thank you for using")












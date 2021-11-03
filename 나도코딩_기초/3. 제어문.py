##### 제어문

# # if문

# weather = "비"
# if weather == "비":
#     print("우산챙겨")
# elif weather == "미세먼지":
#     print("마스크챙겨")
# else :
#     print("필요없음")

# temp = int(input("기온은 어때요?:"))

# if 30 <= temp:
#     print("개더워")
# elif 10 <= temp < 30:
#     print("괜찮")
# else : 
#     print("개추워")

# # 반복문 - for문

# for waiting_no in range(5):
#     print("대기번호 : {}".format(waiting_no))

# 반복문 - while문

# customer = "Thor"
# index = 5
# while index >= 1:
#     print("{}, 커피가 준비되었습니다. {}번 남았아요.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피가 폐기되었습니다")

# customer = "ironman"
# index = 1

# while True:
#     print("{}, 커피가 준비되었습니다. 호출 {}번".format(customer, index))
#     index += 1    # 강제종료 : ctrl+c

# customer = "hulk"
# person = "unknown"

# while person != customer :
#     print("{}, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이? : ")

# 반복문 - continue, break

# absent = [2, 5]
# nobook = [7] 
# for student in range(1, 11):
#     if student in absent:
#         continue       # 결석생을 skip
#     elif student in nobook:
#         print("잠깐, 오늘 수업 여기까지, {}는 교무실로".format(student))
#         break          # 더 이상의 반복 중단
#     print("{}, 책 읽어봐".format(student))

# # 한 줄 for문
 
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환

# students = ["ironman", "thor", "babygroot"]
# print(students)
# students = [len(i) for i in students]
# print(students)

# # 학생 이름을 대문자로 변환

# students2 = ["ironman", "thor", "babygroot"]
# print(students2)
# students2 = [i.upper() for i in students2]
# print(students2)

# 제어문 단원 퀴즈

# Quiz : 당신은 cocoa 서비스를 이용하는 택시 기사입니다. 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오
# 조건1 : 승객별 운행 소요 시간은 5~50분 사이의 난수
# 조건2 : 소요 시간 5~15분 사이의 승객만 매칭해야 함

from random import *

people = 0

for i in range(1, 51):
    time = randint(5, 50)
    print("{}번쨰 손님 (소요시간 : {}분)".format(i, time))
    i = i + 1
    if 5 <= time <= 15:
        people = people + 1
print("총 탑승 승객 : {}분".format(people))





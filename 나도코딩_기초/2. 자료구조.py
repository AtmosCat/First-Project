###### 자료구조

# ######## 랜덤함수

# from random import *

# print(random()) # 0~1 사이 임의값
# print(random() * 10) # 0~10 사이 임의값
# print(int(random() * 10))
# print(int(random() * 10 + 1)) 

# print(int(random() * 45 + 1)) 

# print(randrange(1, 46)) # 1 ~ 45 이하의 임의값 생성
# print(randint(1, 45)) # 1, 45 이하의 값 생성

# ####### 퀴즈
# a = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 {}일로 선정되었습니다".format(a))

#######

# ####### 탈출문자
 
# print("백문이 불여일견\n백견이 불여일타") # 줄바꿈

# print("저는 '정호정'입니다") # 큰따옴표 쓰기 대체 -> 작은따옴표 쓰기 or
# print('저는 "정호정"입니다') # 이렇게 쓰기
# print("저는 \"나도코딩\"입니다.") #역슬러시+따옴표 쓰면 문장 내에서 사용 가능

# # \\ : 문장 내에서 \로 사용 가능
# print("C:\\Python")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple \rPine") # PineApple 출력

# # \b : 백스페이스(한 글자 지우기)
# print("Redd\bApple") # RedApple 출력

# # \t : tap 역할 
# print("Red\tApple")

# #퀴즈 : 사이트별로 비밀번호 만들어주는 프로그램 작성하기

# site = "http://google.com"

# pw = site[7:]
# pw1 = pw[:pw.index(".")]
# pw2 = pw1[:3] + str(len(pw1)) + str(pw1.count("e")) + "!"
# print("사이트의 비밀번호는 : ", pw2, "입니다.")

#######

#######리스트

# # 지하철 칸별로 10, 20, 30명

# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway.insert(1, 'A')
# print(subway)

# print(subway.pop())  # 맨 뒤에 한 명 뺌
# print(subway)

# print(subway.pop())  # 맨 뒤에 한 명 뺌
# print(subway)

# print(subway.pop())  # 맨 뒤에 한 명 뺌
# print(subway)

# num_list= [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)  # 정렬하기

# print(num_list.reverse()) # 순서 뒤집기

# # print(num_list.clear())  #모두 지우기
# mix_list = [4, 2, 5, 1, 1]
# print(num_list)
# num_list.extend(mix_list)
# print(num_list)

#############3

########딕셔너리

# cabinet = {3:"유재석", 100:"김태호"}

# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5)) #값이 없어도 오류가 나지 않고 None출력하고 이어서 진행
# print(cabinet.get(5, "사용 가능")) # 5가 앖이 없지만 그 자리에 사용 가능이라는 값이 출력

# print(3 in cabinet) #3이라는 key가 안에 있으면 True 출력

# del cabinet[3]
# print(cabinet)

# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())

# cabinet.clear() # 안의 모든 값 삭제
# print(cabinet)


###### 튜플형

# menu = ("돈가스", "치즈가스")
# print(menu[0])
# print(menu[1])  # 값을 추가, 변경은 불가

# name = "김종국"
# age = 20
# hobby = "coding"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "coding")
# print(name, age, hobby)

# # 세트 자료형
# # 중복 안됨, 순서가 없음
# myset = {1, 2, 3, 3, 3}
# print(myset)

# java = {"재석", "광수", "종국"}
# python = set(["재석", "명수"])

# print(java & python) # 교집합 출력
# print(java.intersection(python))#교집합 출력

# print(java | python)
# print(java.union(python)) # 합집합 출력

# #차집합 
# print(java-python)
# print(java.difference(python))

# java.add("김태호")
# print(java)

# java.remove("김태호")
# print(java)


# #### 자료구조변경

# menu = {"커피", "우유", "주스"}

# print(menu, type(menu))

# menu =list(menu)
# print(menu, type(menu))

# menu =tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

#### 자료구조 단원 퀴즈
# lst = [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17,18,19,20]

# from random import *
# chicken = randint(1, 20)
# coffee1, coffee2, coffee3 = (randint(1,20), randint(1,20), randint(1,20))
# print("--당첨자 발표--")
# print("치킨 당첨자 : {}".format(chicken))
# print("커피 당첨자 : {}, {}, {}".format(coffee1, coffee2, coffee3))
# print("--축하합니다--")

# shuffle(lst)  #리스트 안의 값 섞음
# print(lst)

# print(sample(lst, 1)) # 리스트 안에서 샘플 하나 뽑음

# #정답코드

# users = range(1, 21)
# users = list(users)
# shuffle(users)
# winners = sample(users, 4)

# print("--당첨자 발표--")
# print("치킨 당첨자 : {}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("--축하합니다--")









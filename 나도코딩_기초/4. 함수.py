# 함수

# # 전달값과 반환값

# def open_account():
#     print("새로운 계좌 생성")

# def deposit(balance, money):  # 입금
#     print("입금이 완료되었습니다. 잔액은 {}원입니다.".format(balance + money))
#     return balance + money


# def withdraw(balance, money):  # 출금
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {}원입니다.".format(balance - money))
#     else:
#         print("출금이 불가합니다. 잔액은 {}원입니다.".format(balance))

# balance = 0   # 잔액
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)

# def withdraw_night(balance, money):   # 밤에 출금
#     commission = 100   # 수수료 100원
#     return commission, balance  - money - commission

# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {}원이고, 잔액은 {}원입니다.".format(commission, balance))


# # 기본값

# # def profile(name, age, main_lang):
# #     print("이름 : {}\t나이 : {}\t주 사용 언어 : {}".format(name, age, main_lang))
    
# # profile("유재석", 20, "파이썬")
# # profile("김태호", 35, "자바")

# # 같은 학교 같은 학년 같은 반 같은 수업인 경우 : 이름 빼고는 다 동일할 것임 -> 기본값 설정

# def profile(name, age = 17, main_lang = "파이썬"):
#     print("이름 : {}\t나이 : {}\t주 사용 언어 : {}".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")


# # 키워드값

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석", age = 20, main_lang = "파이썬")
# profile(main_lang = "파이썬", age = 35, name = "김태호")    # 순서 바꿔도 인수 명확히 해주면 똑같이 출력


# # 가변인자

# # def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# #     print("이름 : {}\t나이 : {}".format(name, age), end = " ")   #end 빈칸으로 정의해주면 줄바꿈이 아니고 이어서 그대로 문장 한 줄로 구성
# #     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름 : {}\t나이 : {}".format(name, age), end = " ")   #end 빈칸으로 정의해주면 줄바꿈이 아니고 이어서 그대로 문장 한 줄로 구성
#     for lang in language:
#         print(lang, end = " ")
#     print()

# profile("유재석", 20, "python", "java", "C", "C+,", "C++", "Javascript")  # 인수의 개수에 제한이 없어짐
# profile("김태호", 25, "kotlin", "Swift", "", "", "")        # 인수의 개수에 제한이 없어짐


# # 지역 변수와 전역 변수

# gun = 10      # 전역 변수

# def checkpoint(soldiers):   # 경계근무 나가는 병사 수
#     global gun        # 전역 변수 호출
#     gun = gun - soldiers   #  
#     print("[함수 내] 남은 총 : {}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {}".format(gun))
#     return gun

# print("전체 총 : {}".format(gun))       # 전역 변수 gun 반영
# # checkpoint(2)             
# gun = checkpoint_ret(gun, 2)              # 지역 변수 gun 반영
# print("남은 총 : {}".format(gun))       # 전역 변수 gun 반영


# 함수 파트 퀴즈 
# Quiz : 표준 체중을 구하는 프로그램 / 성별에 따른 공식) 남자 : 키 x 키 x 22, 여자 : 키 x 키 x 21
# 조건 1 : 표준 체중은 별도의 함수 내에서 계산 / 함수명 : std_weight, 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘쨰 자리까지 표시

def std_weight(height, gender):
    if gender == "남자":
        print("키 {}cm 남자의 표준 체중은 {}kg입니다.".format(height, round((height/100)*(height/100)*22, 2)))
    elif gender == "여자":
        print("키 {}cm 여자의 표준 체중은 {}kg입니다.".format(height, round((height/100)*(height/100)*21, 2)))

std_weight(174, "남자")
std_weight(165, "여자")









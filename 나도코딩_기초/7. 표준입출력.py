# 표준입출력

# print("python", "java", "javascript", sep = " vs ", end = "?")
# print("무엇이 더 재밌을까요?")

# import sys
# print("python", "java", file = sys.stdout)   # 표준출력 
# print("python", "java", file = sys.stderr)   # 표준에러 

# scores = {"수학" : 10, "영어" : 100, "코딩" : 50}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep = ":")    # 8개의 공간을 확보하고 왼쪽 정렬해라, 4칸을 확보하고 오른쪽 정렬해라

# 은행 대기순번표
# 001, 002, 003, ...

# for num in range(1,21):
#     print("대기번호 :" + str(num).zfill(3))       # 3만큼의 공간을 확보하고 값을 집어넣되 값이 없는 공간을 0으로 채움

# answer = input("아무 값 : ")     # 사용자 입력 형태로 변수를 받으면 항상 문자열 str형태로 저장됨. 
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다")


# # 다양한 출력포맷

# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬, 총 10공간 확보
# print("{0: >10}".format(500))           
# # 양수일 떄는 +로, 음수일 때는 -로 표시
# print("{0: >+10}".format(500))           
# print("{0: >+10}".format(-500))           
# # 왼쪽 정렬하고 빈칸을 _로
# print("{0:_<+10}".format(500))           
# # 3자리마다 콤마 찍기
# print("{0:,}".format(1000000000000))
# # 3자리마다 콤마 찍기, 부호 붙이기
# print("{0:+,}".format(1000000000000))
# print("{0:+,}".format(-1000000000000))
# # 3자리마다 콤마 찍기, 부호 붙이기, 자릿수 붙이기, 빈 자리는 ^로 채우기
# print("{0:^<+30,}".format(1000000000000))
# # 소수점 출력
# print("{0:f}".format(1/6))
# # 소수점을 특정 자릿수까지만 표시
# print("{0:.2f}".format(1/6))


# 파일 입출력

# score_file = open("score.txt", "w", encoding = "utf8")
# print("수학 : 0", file = score_file)
# print("영어 : 100", file = score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding = "utf8")     # a = append, 이어쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")     # 줄바꿈 해야만 줄바꿈됨
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.read())
# score_file.close()

# # 한 줄씩 불러오기
# score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.readline())  # 줄별로 읽기, 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline(), end = "")   # 줄바꿈 안하기
# print(score_file.readline())

# score_file = open("score.txt", "r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break    # 더 이상 읽을 라인이 없으면
#     print(line)
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# lines = score_file.readlines()  # list 형태로 저장
# for line in lines:
#     print(line, end = "")
# score_file.close()


# pickle : 프로그램상에서 사용하는 데이터를 파일로 저장하는 것

# pickle 파일로 저장하기
# import pickle
# profile_file = open("profile.pickle", "wb")    # wb : binary file
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()

# 저장한 pickle 파일 불러오기
# import pickle

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()

# with 라이브러리

# import pickle

# with open("profile.pickle", "rb") as profile_file:     # 변수에 저장 
#     print(pickle.load(profile_file))     # close를 따로 해줄 필요 없음

# with open("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write("파이썬 조아")

# with open("study.txt", "r", encoding = "utf8") as study_file:
#     print(study_file.read())

# 퀴즈
# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가  있다. 아래와 같은 형태이다. 
# - X 주차 주간보고 - 
# 부서 : 
# 이름 : 
# 업무 요약 : 
# 1~50주차의 보고서 파일을 만드는 프로그램을 작성하라. 
# 조건 : 파일명은 n주차.txt이다

# for x in range(1, 51):
#     docu_file = open(str(x)+"주차.txt", "w", encoding = "utf8")
#     docu_file.write("- X 주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :")
#     docu_file.close()
    
























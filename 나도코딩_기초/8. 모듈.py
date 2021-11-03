# 동 워크스페이스 내에 있는 theater_module 내의 모듈을 불러올 수 있음
# import theater_module
# theater_module.price(3) # 3명의 영화 가격
# theater_module.price_morning(4) # 4명의 조조할인 영화 가격
# theater_module.price_soldier(5) # 5명의 군인할인 영화 가격

# import theater_module as mv 

# mv.price(3) 
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# # # from random import * 와 같은 꼴

# # price(3)
# # price_morning(4)
# # price_soldier(5)

# from theater_module import price, price_morning     # 일부만 임포트
# price(3)
# price_morning(4)


# # 패키지 : 모듈의 집합
# import travel.thailand    # 임포트하는 맨 마지막 대상은 모듈이나 패키지만 가능함
# # from travel.thailand import ThailandPackage     # 이렇게 from import 구문에서는 사용 가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# # # __all__
# from travel import *      # *을 쓴다는 것은 패키지 내의 모든 것을 가져오겠다는 말이지만, __init__.py 안에서 따로 __all__로 정의해준 것만 *을 통해 호출이 가능함. 
# # # trip_to = vietnam.VietnamPackage()
# # trip_to = thailand.ThailandPackage()
# # trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))   # random.py가 어디 위치에 있는지 호출
# print(inspect.getfile(thailand))  #thailand.py 가 어디에 있는지 호출


# # pip install

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# # 터미널에다 pip show 모듈명 =  패키지에 대한 정보 출력 / pip list = 현재 설치된 패키지 리스트 정보 출력 / 업그레이드 : pip install --upgrade 패키지명 / 삭제 : pip uninstall 패키지명


# # 내장함수 - 임포트할 필요 X
# # input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{}은 아주 좋은 언어입니다.".format(language))

# # # dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 갖고 있는지 표시
# # print(dir())
# import random # random : 외장함수
# # print(dir())
# # import pickle
# # print(dir())

# print(dir(random))   # random 함수 내에서 쓸 수 있는 기능들을 출력

# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))


 # https://docs.python.org/ko/3/library/functions.html 내장함수 리스트 / 구글 검색 list of python builtins


# 외장함수 : 임포트해야만 쓸 수 있는 함수 / 구글 검색 list of python modules       https://docs.python.org/3/py-modindex.html

# glob : 경로 내의 폴더 / 파일 목록 조회

# import glob
# print(glob.glob("*.py"))  # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os 
# print(os.getcwd())  # 현재 디렉토리를 표시

# folder = "sample_dir"

# if os.path.exists(folder):    # path상에 folder가 존재하면 if문 실행
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)   # 이미 존재하는 폴더니까 삭제하기
#     print(folder, "폴더를 삭제하였습니다")
# else:
#     os.makedirs(folder)   # 폴더 생성
#     print(folder, "를 생성하였습니다.")

# print(os.listdir())  

# # time : 시간 관련 함수 제공
# import time
# # print(time.localtime())
# # print(time.strftime("%Y-%M-%d %H:%M:%S"))  # 원하는 형태로 출력

# import datetime
# print("오늘 날짜는", datetime.date.today())

# # timedelta : 두 날짜 사이의 간격
# today = datetime.date.today()
# td = datetime.timedelta(days = 100)   # 오늘로부터 100일 뒤의 날짜 출력
# print("우리 만난 지 100일은", today + td)


# 퀴즈
# 프로젝트 내에 나만의 시그니처를 남기는 모듈을 만들기
# 조건 : 모듈 파일명은 byme.py로 작성
# 예제
# import byme
# byme.sign()
# 출력 예제
# 이 프로그램은 하늘냥이에 의해 만들어졌습니다. 
# 유튜브 : http://youtube.com
# 이메일 : jeonghj1127@naver.com

import byme
byme.sign()






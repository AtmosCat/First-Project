# 웹 페이지 가져오기
from bs4 import BeautifulSoup as bs
from pprint import pprint       # 리스트, 딕셔너리의 데이터가 너무 길 때 정돈하여 출력하는 모듈
import requests

html = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8')
# pprint(html.text)    # 텍스트 속성의 자료 프린트(=페이지 소스)

# 파싱 : 단순한 문자열 자료형을 쉽게 변환하기
soup = bs(html.text,'html.parser')  # parser 변환
# pprint(soup)   # 좀더 보기 쉬운 구성으로 출력

# 강수확률 정보만을 빼오기 위해 작업하기
# 페이지 -> 도구 더보기 -> 개발자 도구(F12)로 접근

data1 = soup.find('div', {'class' : 'temperature_info'})   # 태그, {속성 : 속성값} 입력  /  같은 소스 코드에 똑같은 것이 여러개 있을 경우 첫 번째 것만 반환됨
# pprint(data1)

# findAll() 
data2 = data1.findAll('dl')   # 속성과 속성값이 의미없을 경우 생략 가능
# pprint(data2)
find_rain = data2[0].find('dd', {'class' : 'desc'})
print(find_rain)

# 텍스트 부분만 추출(강수량 값만을 추출)
print(find_rain.text)  # 0% 강수량 값 출력
















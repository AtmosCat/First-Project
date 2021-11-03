# 웹 페이지 가져오기
from bs4 import BeautifulSoup as bs
from pprint import pprint      
import requests

#웹 페이지를 열고 소스코드를 읽어오는 작업
html = requests.get("https://comic.naver.com/webtoon/weekday")
soup = bs(html.text, 'html.parser')
html.close()

#월요웹툰영역 추출하기
data1=soup.find('div',{'class':'col_inner'})
# pprint(data1)

#제목 포함영역 추출하기
data2=data1.findAll('a',{'class':'title'})
# pprint(data2)

# title_list = []
# for t in data2:
#     title_list.append(t.text)

title_list = [t.text for t in data2]

# pprint(title_list)

#전체 웹툰 제목 가져오기
data1_list = soup.findAll('div', {'class' : 'col_inner'})
print(len(data1_list)) # 일주일이니까 7 출력

#전체 웹툰 리스트
week_title_list = []

for data in data1_list:
    #제목 포함 영역 추출하기
    data3 = data.findAll('a', {'class' : 'title'})

    # 텍스트만 추출하기
    title_list2 = [t.text for t in data3]

    pprint(title_list2)

    # week_title_list.append(title_list2)
    week_title_list.extend(title_list2)  # append와 다르게 하나의 리스트로 형성

print(week_title_list)


























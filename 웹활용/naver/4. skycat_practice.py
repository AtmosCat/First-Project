# 필요한 모듈 호출
from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests, re, os
from urllib.request import urlretrieve 

# html parsing
html = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4&oquery=%EB%84%A4%EC%9D%B4%EB%B2%84%EC%98%81%ED%99%94&tqi=hRH8usp0JXossmEb4slssssstLd-046630')
soup = bs(html.text, 'html.parser')
html.close()
# pprint(soup)

# 데이터 텍스트로 긁어오기
data1 = soup.find('div', {'class' : 'cm_content_area _cm_content_area_list_boxoffice'})
# pprint(data1)

# 전체 영화 썸네일 리스트
data_thumb = data1.findAll('div', {'class':'thumb'})
# pprint(data_thumb)
# pprint(data_thumb[0])

# 썸네일 링크들로 리스트에 저장
thumb_list = [th.find('img') for th in data_thumb]
img_list = [i['src'] for i in thumb_list]
# print(img_list)

# 전체 영화 타이틀 리스트
data_title = data1.findAll('strong', {'class' : 'name'})
# pprint(data_title)

title_list = [t.text for t in data_title]
for title in title_list:
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)   # [힗] 범위를 벗어나는 값은 []로 치환

# print(title_list)

# 썸네일을 이미지 파일로 저장

for i in range(45):
    urlretrieve(img_list[i], './image/' + title_list[i] + '.jpg')










print("###############################################################")















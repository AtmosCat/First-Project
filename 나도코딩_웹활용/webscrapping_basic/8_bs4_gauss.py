import requests
from bs4 import BeautifulSoup as  bs

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = bs(res.text, "lxml")
# print(soup)

# cartoons = soup.find_all('td', {"class" : "title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com"+link)   # 바로 원하는 화로 이동하는 링크를 출력

# 만화 제목, 링크 가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div", attrs = {"class" : "rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))

## 참고 사이트 : beautifulsoup 구글 검색 -> documentation 한글 안내 문서 있음. 참고하기 .













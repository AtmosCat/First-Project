import requests
from bs4 import BeautifulSoup as  bs

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = bs(res.text, "lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a", attrs = {"class" : "title"})
# a element의 클래스가 title인 모든 a라는 element를 반환
for cartoon in cartoons:
    print(cartoon.get_text())















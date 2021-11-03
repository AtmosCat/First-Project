# http method : 서버에 http 정보를 요청하는 방식, get 방식과 post 방식
# get 방식 : ? 뒤에 있는 변수-값으로 조건을 서술, 각 변수와 값 사이에는 &로 구분 --> 공개적 / 한 번에 보낼 수 있는 양 제한 有
# post 방식 : 아이디와 비밀번호 등 보안이 필요한 정보를 숨겨서 전달 / 

from bs4 import BeautifulSoup as bs
import requests
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = bs(res.text, "lxml")

# print(res.text)

items = soup.find_all("li", attrs = {"class" : re.compile("^search-product")})
# print(items[0].find("div", attrs = {"class" : "name"}).get_text())

for item in items:

    # 광고 제품은 순위에서 제외
    ad_badge = item.find("span", attrs = {"class" : "ad-badge-text"})
    if ad_badge : 
        print("<광고 상품은 제외합니다.>")
        continue

    name = item.find("div", attrs = {"class" : "name"}).get_text()   # 제품명
    
    # 애플 제품 제외
    if "Apple" in name:
        print("<애플 상품은 제외합니다>")
        continue
    price = item.find("strong", attrs =  {"class" : "price-value"})  # 가격
    if price :
        price = price.get_text()
    else:
        price = "가격 없음"

    # 리뷰 100개 이상, 평점 4.5 이상만 조회
    rate = item.find("em", attrs =  {"class" : "rating"})   # 평점  /  평점이 없는 상품에 대해서는 출력하지 않도록 설정(Nonetype 에러 방지)
    if rate :
        rate = rate.get_text()
    else:
        rate = "평점 없음"
        print("<평점 없는 상품은 제외합니다>")
        continue
    rate_cnt = item.find("span", attrs = {"class" : "rating-total-count"})  # 평점 수
    if rate_cnt :
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]  # 숫자 값만 슬라이싱
        print("리뷰 수 : ", rate_cnt)
    else:
        rate_cnt = "리뷰 없음"
        print("<리뷰 없는 상품은 제외합니다>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)




























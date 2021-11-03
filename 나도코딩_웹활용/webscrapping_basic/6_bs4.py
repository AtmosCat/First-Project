import requests
from bs4 import BeautifulSoup as  bs

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = bs(res.text, "lxml")   # lxml : parser   |  가져온 문서를 파서를 통해 soup 객체로 만든 것
# print(soup.title)      # 코드의 title 태그에 접근
# print(soup.title.get_text())  # text만 빼오기
# print(soup.a)   # 코드 내 첫 번째 a태그의 정보 출력
# print(soup.a.attrs)   # attrs : a element의 속성을 딕셔너리 형태로 출력
# print(soup.a["href"])  # a 태그의 속성 중 원하는 속성 값(href)만을 출력

# print(soup.find("a", attrs = {"class" : "Nbtn_upload"}))   # class가 Nbtn_upload인 첫 번째 a태그를 찾아줘
# print(soup.find(attrs = {"class" : "Nbtn_upload"}))   # a 태그가 한 개밖에 없을 떄에는 태그 생략 가능

# print(soup.find("li", attrs  = {"class" : "rank01"}))
# rank1 = soup.find("li", attrs  = {"class" : "rank01"})
# print(rank1.a.get_text())   
# print(rank1.next_sibling)
# rank2 = rank1.next_sibling.next_sibling     # 다음 위치의 형제 관계의 element 출력
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling  # rank3의 이전의 이전의 형제 element로 이동
# print(rank2.a.get_text())

# print(rank1.parent)     # 부모 element로 이동

# rank2 = rank1.find_next_sibling("li")   # rank1태그를 기준으로 다음 항목을 찾는데 태그가 li인 것만 find.  ->  next_sibling을 여러 번 쓸 필요 없음
# print(rank2.a.get_text())

# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())

# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))    # 다음의 li인 형제들을 "모두" 가져옴

webtoon = soup.find("a", text="조조코믹스-럭키포인트 1화")
print(webtoon)










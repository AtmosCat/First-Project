import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding = "utf-8-sig", newline = "")       # newline 저부분 안 쓰면 자동으로 줄바꿈이 됨
writer = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t")
print(type(title))
writer.writerow(title)    # 리스트 형태로 타이틀(열 이름)을 집어넣기 위한 작업

for page in range(1, 5):
    res = requests.get(url+str(page), headers = headers)
    res.raise_for_status()
    soup = bs(res.text, "lxml")

    data_rows = soup.find("table", attrs = {"class" : "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:
            continue
        data = [column.get_text().strip() for column in columns]    # 앞뒤 공백, 불필요한 줄바꿈 제거
        # print(data)
        writer.writerow(data)  # 안에 리스트 형태의 데이터를 넣어야 함












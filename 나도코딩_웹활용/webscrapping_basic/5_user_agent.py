import requests

url = "http://nadocoding.tistory.com/"

# 403 에러는 사람이 아닌 컴퓨터가 접속한다는 것으로 인식하고 접근을 막는 것임. user agent를 활용하면 사람이 들어가는 것으로 됨. 크롬을 통해 들어가는 것처럼 정상적인 접근 가능

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}   # key 값 : https://www.whatismybrowser.com/detect/what-is-my-user-agent 여기서 가져옴
res = requests.get(url, headers)
# res.raise_for_status
with open("nadocoding.html", "w", encoding = "utf-8") as f:       
    f.write(res.text)



















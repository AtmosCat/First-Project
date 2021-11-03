import requests

res = requests.get("http://google.com")
res.raise_for_status    # 오류가 있으면 바로 종료, 정상이면 스크래핑 진행
print("응답코드 : ", res.status_code)  # 200이면 서버 정상, 403이면 비정상

res_error = requests.get("http://nadocoding.tistory.com")
res_error.raise_for_status
print("응답코드 : ", res_error.status_code)

# if res.status_code == 200 or requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. 에러코드 : {}".format(res.status_code))

# res.raise_for_status()
# print("웹 스크래핑을 진행합니다")

# res_error.raise_for_status
# print("웹 스크래핑을 진행합니다")

# print(len(res.text))
# print(res.text)

# with open("mygoogle.html", "w", encoding = "utf-8") as f:           # 소스를 가져와서 html 파일로 만들기 
#     f.write(res.text)



















import time
from selenium import webdriver

browser = webdriver.Chrome()     # 괄호 안에 driver 파일이 설치된 경로를 입력 / 여기서는 디렉토리에 있어서 별도 입력하지 않아도 됨

# 1.네이버 이동
browser.get("http://naver.com")     # 링크로 접속

#2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#3. 아이디, 패스워드 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("naver_pw")

#4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)
#5. id 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

#6. html 정보 출력
print(browser.page_source)

#7. 브라우저 종료
browser.close()   #현재 탭만 종료
browser.quit()    # 전체 탭 종료











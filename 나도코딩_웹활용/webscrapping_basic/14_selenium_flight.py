import time
from selenium import webdriver
browser = webdriver.Chrome("C:\PythonWorkspace\chromedriver.exe")
browser.maximize_window()    # 창 최대화

url = "https://beta-flight.naver.com"
browser.get(url)      #  url로 이동

# time.sleep(5)

# 가는 날 클릭

browser.find_element_by_tag_name("button")[0].click()   #<button type="button" class="tabContent_option__2y4c6 select_Date__1aF7Y" aria-selected="false">가는 날</button>
browser.implicitly_wait(3) 
# 이번 달 27, 28일 선택
browser.find_elements_by_link_text("30")[0].click()    # [0] --> 다음 달 말고 이번 달 27일 선택  
browser.find_elements_by_link_text("30")[0].click()







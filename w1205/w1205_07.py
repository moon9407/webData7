import time
import os
import random
# 웹 스크래핑
import requests
from bs4 import BeautifulSoup
# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# 이메일 발송 라이브러리
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
# 날짜함수
from datetime import datetime
# 마우스제어
import pyautogui

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")


#### selenium 방법
# url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C+%EC%9A%A9%EC%82%B0%EA%B5%AC+%EC%9D%B4%ED%83%9C%EC%9B%90%EB%8F%99+%EC%95%84%ED%8C%8C%ED%8A%B8"
# browser = webdriver.Chrome(options=options) # 창열기
# browser.maximize_window()
# soup = BeautifulSoup(browser.page_source,"lxml")
# # 불러온 페이지 저장
# with open('naver4.html','w',encoding="utf8")as f:
#     f.write(soup.prettify())

# 저장한 페이지 불러오기
with open('naver4.html','r',encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
    
ols = soup.find("ol",{"class":"list_place"})
lis = ols.find_all("li")
al = lis[0].find("em",{"class":"mark_count"}).text.strip().split() #al[1]
name = lis[0].find("div",{"class":"cont_place"}).find("a").text.strip()
price = lis[0].find("dl",{"class":"info_price"}).text.strip().split()
pri = f""
print(price)




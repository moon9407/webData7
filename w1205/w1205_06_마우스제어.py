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


#### selenium 방법
url = "http://www.naver.com"
browser = webdriver.Chrome() # 창열기
browser.maximize_window()
browser.get(url)

pyautogui.sleep(1)           # 1초대기
pyautogui.scroll(-700)       # 스크롤
pyautogui.sleep(1)
pyautogui.scroll(700)
pyautogui.sleep(1)
pyautogui.moveTo(900,300)
pyautogui.click()            # 클릭
# pyautogui.doubleClick()      # 더블클릭

input("대기")



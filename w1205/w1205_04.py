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

# 임시비밀번호 생성 함수
def random_pw():
    arr = [i for i in range(0,10)]
    ranNum = "".join(map(str,random.sample(arr,8)))
    print("임시비밀번호 : "+ranNum)
    return ranNum

content = f'''
임시비밀번호 : {random_pw()}
'''
# 메일내용부분
msg = MIMEText(content)
msg['From'] = "xzc7001@naver.com" # 보내는이   # 네이버는 보내는 주소가 무조건 naver.com 로 끝나야 메일이 전송됨
msg['To'] = "m48995442@gmail.com"   # 받는이
msg['Subject'] = "임시비밀번호를 보내드립니다."
# 메일서버정보
s = smtplib.SMTP("smtp.naver.com",587)
# 메일서버 접근
s.starttls()
# 메일서버 로그인
s.login("xzc7001@naver.com","5GE1S3BEZJ6F")
# 메일서버 발송 - 보내는 이메일 주소, 받는주소, 이메일 내용부분
s.sendmail("xzc7001@naver.com","m48995442@gmail.com",msg.as_string())
print(msg.as_string())
# 메일 닫기
s.close()

print("이메일 발송완료")

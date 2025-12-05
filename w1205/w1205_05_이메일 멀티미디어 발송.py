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

# 임시비밀번호 생성 함수------------------------------------
def random_pw():
    arr = [i for i in range(0,10)]
    ranNum = "".join(map(str,random.sample(arr,8)))
    print("임시비밀번호 : "+ranNum)
    return ranNum


# 메일 발송부분-----------------------------

content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>임시비밀번호 안내</title>
    <style>
    </style>
</head>
<body>
    <table style="width:760px; margin:0 auto;">
        <colgroup>
          <col width="182px">
          <col width="*">
          <col width="135px">
        </colgroup>
        <tr style="width:100%; height:105px;">
            <td style="height:45px;""><img src='https://mediahub.seoul.go.kr/images/newsletter/renew2025/logo_01.png'></td>
            <td></td>
            <td><img src='https://mediahub.seoul.go.kr/images/newsletter/renew2025/logo_02.png'></td>
        </tr>
        <tr style="height:200px; background: #eee;">
            <td colspan="3" style="text-align: center; font-size: 20px;font-weight: 600;">임시비밀번호 : {random_pw()}</td>
        </tr>
    </table>
</body>
</html>
'''
print(content)

# 멀티메일내용부분
msg = MIMEMultipart()
html_part = MIMEText(content,"html","utf-8")
msg.attach(html_part)
msg['From'] = "xzc7001@naver.com"    # 보내는이   # 네이버는 보내는 주소가 무조건 naver.com로 끝나야 메일이 전송됨
msg['To'] = "xzc7001@naver.com"      # 받는이
msg['Subject'] = "멀티페이지 임시비밀번호를 보내드립니다." # 메일 제목

# # 파일첨부
# file_part = MIMEBase('application','octet-stream')
# # 파일 읽어오기
# with open('yeogi.csv',"rb")as f:
#     file_part.set_payload(f.read())
# encoders.encode_base64(file_part)     # encoders.encode_base64() : 파일을 쪼개서 전송할 수 있는 형태로 변경
# file_part.add_header('Content-Disposition','attachment',filename='yeogi.csv')
# msg.attach(file_part)

# 파일첨부 간략히
with open('yeogi.csv','rb')as f:
    attachment = MIMEApplication(f.read())
    
attachment.add_header('Content-Disposition','attachment',filename='yeogi.csv')
msg.attach(attachment)


# 메일서버정보
s = smtplib.SMTP("smtp.naver.com",587)
# 메일서버 접근
s.starttls()
# 메일서버 로그인
s.login("xzc7001@naver.com","5GE1S3BEZJ6F")
# 메일서버 발송 - 보내는 이메일 주소, 받는주소, 이메일 내용부분
s.sendmail("xzc7001@naver.com","xzc7001@naver.com",msg.as_string())
print(msg.as_string())
# 메일 닫기
s.close()

print("이메일 발송완료")

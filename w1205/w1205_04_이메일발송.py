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
# 날짜함수
from datetime import datetime

# 임시비밀번호 생성 함수------------------------------------
# def random_pw():
#     arr = [i for i in range(0,10)]
#     ranNum = "".join(map(str,random.sample(arr,8)))
#     print("임시비밀번호 : "+ranNum)
#     return ranNum


# 네이버날씨 웹스크래핑--------------------------------
## request 방법
# url = "http://www.naver.com/"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
# res=requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

# selenium 방법
# url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90+%EC%A3%BC%EA%B0%80&oquery=%EC%97%94%EB%B9%84%EB%94%94%EC%95%84+%EC%A3%BC%EA%B0%80&tqi=jg584sqosZossT5i4x4-011059&ackey=zxdrvh3v"
# browser = webdriver.Chrome() # 창열기
# browser.get(url)
# soup = BeautifulSoup(browser.page_source,"lxml")
# # 불러온 페이지 저장
# with open('naver3.html','w',encoding="utf8")as f:
#     f.write(soup.prettify())

# 저장한 페이지 불러오기
with open('naver3.html','r',encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
# 삼성전자 주식 가격 --------------------------------------
sam_sub = soup.find("div",{"class":"api_subject_bx"})
sam_title = sam_sub.find("span",{"class":"stk_nm"}).text.strip()
sam_stock = sam_sub.find("span",{"class":"spt_con up"}).find("strong").text.strip().split()
sam_st = f"{sam_stock[0]}{sam_stock[1]}"
sam_last = sam_sub.find("span",{"class":"spt_con up"}).find("span",{"class":"n_ch"}).text.strip().split()
sam_la = f"{sam_last[0]} {sam_last[1]} : {sam_last[2]} / {sam_last[3]}"
print(sam_stock)
    
# 저장한 페이지 불러오기
with open('naver2.html','r',encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
# 엔비디아 주식 가격 ---------------------------------------------------
en_sub = soup.find("div",{"class":"api_subject_bx"})
en_title = en_sub.find("span",{"class":"stk_nm"}).text.strip()
en_stock = en_sub.find("span",{"class":"spt_con up"}).find("strong").text.strip().split()
en_st = f"{en_stock[0]}{en_stock[1]}"
en_last = en_sub.find("span",{"class":"spt_con up"}).find("span",{"class":"n_ch"}).text.strip().split()
en_la = f"{en_last[0]} {en_last[1]} : {en_last[2]} / {en_last[3]}"




# 날씨 부분 웹스크래핑 ----------------------------------------
# 저장한 페이지 불러오기
with open('naver1.html','r',encoding="utf8") as f:
    soup = BeautifulSoup(f,"lxml")
# 날짜
today = datetime.today()
now = today.strftime('%Y-%m-%d %H:%M:%S')
print(now)

# 온도/날씨
weather = soup.find("div",{"class":"DailyBoardView-module__weather_temperature___pOAGy"}).text.strip().replace(" ","").split("\n")
print(weather[0],weather[2])
today_weather = f"기온 : {weather[0]} / 날씨 : {weather[2]}"

# 최저기온
low_temp =  soup.find("span",{"class":"DailyBoardView-module__temperature_low___aC6Fe"}).text.strip().replace(" ","").split("\n")
print(low_temp[0],low_temp[2])
today_low_temp = f"{low_temp[0]} : {low_temp[2]}"

# 최고기온
high_temp =  soup.find("span",{"class":"DailyBoardView-module__temperature_high___QLp_M"}).text.strip().replace(" ","").split("\n")
print(high_temp[0],high_temp[2])

today_high_temp = f"{high_temp[0]} : {high_temp[2]}"



# 메일 발송부분-----------------------------
## 날씨 메일내용
content = f'''{now}
{today_weather}
{today_low_temp}

{en_title}
{en_st}
{en_la} 

{sam_title}
{sam_st}
{sam_la}'''
print(content)

## 임시비밀번호 메일 내용
# content = f'''
# 임시비밀번호 : {random_pw()}
# '''

# 메일내용부분
msg = MIMEText(content)
msg['From'] = "xzc7001@naver.com"    # 보내는이   # 네이버는 보내는 주소가 무조건 naver.com 로 끝나야 메일이 전송됨
msg['To'] = "ounlee@naver.com"      # 받는이
msg['Subject'] = "정보를 보내드립니다." # 메일 제목
# 메일서버정보
s = smtplib.SMTP("smtp.naver.com",587)
# 메일서버 접근
s.starttls()
# 메일서버 로그인
s.login("xzc7001@naver.com","5GE1S3BEZJ6F")
# 메일서버 발송 - 보내는 이메일 주소, 받는주소, 이메일 내용부분
s.sendmail("xzc7001@naver.com","ounlee@naver.com",msg.as_string())
print(msg.as_string())
# 메일 닫기
s.close()

print("이메일 발송완료")

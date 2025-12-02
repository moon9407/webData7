import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
# selenium함수호출


# 파일 읽어오기
with open("webtoon_browser.html","r",encoding="utf8")as f:
    soup = BeautifulSoup(f,"lxml")
    

# asideDiv = soup.find("div",{"class":"Aside__aside_wrap--iF5ju"})
# wraps = asideDiv.find_all("div",{"class":"component_wrap"})
# print(wraps[3].find("h2",{"class":"ComponentHead__title--TjYVo"}))







# print(soup.find("div",{"class":"Aside__aside_wrap--iF5ju"}))


# print(soup.prettify())    
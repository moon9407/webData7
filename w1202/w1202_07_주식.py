import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
# 크롬브라우저 특징 : tbody를 안만들어도 자동으로 만들어 넣음.
trs = soup.find("div",{"class":"box_type_l"}).table.find_all("tr")





import requests # 자바스크립트나 리액트로 개발된 페이지는 못가져옴
from bs4 import BeautifulSoup

url = "https://www.naver.com"
headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

### html태그,css문법으로 검색이 가능
## find() ,find_all() ,find_next_sibling(s)다음형제 find_previous_sibling(s)이전형제
# 태그 입력 시 검색됨.
# text : 태그 안에 글자를 출력
# print(soup.find("title"))       # title 태그 가져오기,    <title>NAVER</title>
# print(soup.title.text)          # title글자 가져오기,      태그를 그대로 넣어도 찾아짐 ,  NAVER
# print(soup.a)                   # a태그 속성값 가져오기,       제일 가까운 정보를 찾아옴, <a href="#topAsideButton"><span>상단영역 바로가기</span></a>
# print(soup.a.attrs)             # .attrs : 속성값을 찾아옴, {'href': '#topAsideButton'}
# print(soup.a['href'])           # href속성값 가져오기         #topAsideButton
# print(soup.find("div"))         # 위에서부터 제일 가까운 div 모든 정보를 불러옴
# print(soup.find_all("div"))     # 모든 div 정보를 모두 불러옴
# print(soup.find_all("div")[0])   # div 0번째 정보를 불러옴
# print(len(soup.find_all("div"))) # div 개수 확인
# print(soup.find_all("div")[1].find("div"))       # div태그 여러개 가져오기
# print(soup.find_all("div")[1].find("div").attrs) # div태그 속성값만 여러개 가져오기
# print(soup.find("div",{"id":"header"}))  # 윗윗줄이랑 같음
# print(soup.find("div",id='header'))                   

# idHeader = soup.find("div",{"id":"header"})
# print(idHeader.find("div",{"id":"header"}))
                 
# print(soup.find("legend",{"class":"blind"}))
# print(soup.find("legend",class_="blind"))





#-----------------------------------------------------------
# 파일 저장
# with open("naver1.html","w",encoding="utf8")as f:
#     f.write(res.text)
    
# with open("naver2.html","w",encoding="utf8")as f:
#     f.write(soup.prettify())

# print("파일저장완료")
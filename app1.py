import requests
from bs4 import BeautifulSoup

url = 'http://kosis.kr/conts/nsportalStats/nsportalStats_0102Body.jsp;jsessionid=PL7tm9exauzEsoeadUcl14CmFKoiakPnQ37BSg4xPQdK1zEjUMGVwEjwZ0oPPq4D.STAT_SIGA1_servlet_engine4?menuId=10&NUM=1001'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

dt = soup.find('div',{'id':'Header'})
date = str(dt)
date = date[date.find("span")+5:date.find("현재")+2]

txt = soup.find('ul', {'id':'menuTop10'})
total_n = str(txt)
total_n = total_n[total_n.find("기대수명"):]
total_n = total_n[total_n.find("textRight")+11:]
total_n = total_n[:total_n.find("년")+1]

print("우리나라의 {0} 기대수명은 {1} 입니다.".format(date,total_n))
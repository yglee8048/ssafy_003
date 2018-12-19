from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs
from datetime import date
import json

app = Flask(__name__)

@app.route('/index')
def index():
    print("hello")
    print("nice to meet you")
    return """
    <h1 style="text-align:center"> Hi! </h1>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTopcG9aTZvFE1qaT02DsoYj4Ch2zabw7uAL6hvNG2HA9oDCH7x" alt="cat" align="center">
    """

@app.route('/naver_toon')
def naver_toon():
    daylist = ['mon','tue','wed','thu','fri','sat','sun']
    daylistforex = ['월','화','수','목','금','토','일']
    today = date.today()
    day = daylist[today.weekday()]
    dayforex = daylistforex[today.weekday()]
    url = 'http://comic.naver.com/webtoon/weekdayList.nhn?week=' + day + '/'
    
    response = requests.get(url).text
    soup = bs(response, 'html.parser')
    
    toons = []
    lstlink = []
    wttitle = []
    imglink = []
    baseurl = 'http://comic.naver.com'
    
    wtlist = soup.find_all('div', {'class':'thumb'})
    
    notdp = 3
    for x in wtlist:
        if notdp > 0 :
            notdp -= 1
            continue
      
        test = str(x)
        dic = {}
        
        tmp = test[test.find('href=')+6:]
        tmp = tmp[:tmp.find('"')]
        dic['url'] = baseurl + tmp
        
        tmp2 = test[test.find('this.src=')+9:]
        tmp2 = tmp2[tmp2.find('src=')+5:tmp2.find('title=')-2]
        dic['img'] = tmp2
        
        tmp3 = test[test.find('title=')+7:]
        tmp3 = tmp3[:tmp3.find('>')-1]
        dic['title'] = tmp3
        
        toons.append(dic)
    
    return render_template('naver_toon.html', t = toons)

@app.route('/daum_toon')
def daum_toon():
    daylist = ['mon','tue','wed','thu','fri','sat','sun']
    daylistforex = ['월','화','수','목','금','토','일']
    today = date.today()
    day = daylist[today.weekday()]
    dayforex = daylistforex[today.weekday()]
    
    url = 'http://webtoon.daum.net/data/pc/webtoon/list_serialized/' + day
    response = requests.get(url).text
    output = json.loads(response)
    docu = output['data']
    
    toons = []
    baseurl = 'http://webtoon.daum.net/webtoon/view/'
    for x in docu:
      toon ={
        'title' : x['title'],
        'url' : baseurl + x['nickname'],
        'img' : x['thumbnailImage2']['url']
      }
      toons.append(toon)
    
    return render_template('daum_toon.html',t = toons)
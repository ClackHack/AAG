#Imports
import requests as rp; from bs4 import BeautifulSoup as soup
from PIL import Image
from io import BytesIO
#Print the date
import time
date = time.strftime("%A, %B %e, %Y")
print(date,"\n")
#Get News
url="https://apnews.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page=rp.get(url,headers=headers)
s = soup(page.content,"html.parser")
story=s.find_all('h1')
print("Top Story:",story[0].text)
parent=story[0].parent.parent.parent
href=s.find('div',class_='Landing').find('img')['src']
im = rp.get(href)
im = Image.open(BytesIO(im.content))
#im.show() #You can uncomment if wanted
print("\nOther Stories:")
for i in story[3:7]:
    print(i.text)
print()
#Weather
url="https://weather.com/weather/today/l/af7ef50ebd6650aa5396e0b2a298c006b1cb34373bb4aecf4f1866711a20d503"
page=rp.get(url,headers=headers)
s=soup(page.content,"html.parser")
card = s.find('div',class_="today_nowcard-section today_nowcard-condition")
temp=card.find('span').text
print("Current temp:",temp)
phrase=card.find('div',class_="today_nowcard-phrase").text
print(phrase)
temps = card.find_all('span',class_="deg-hilo-nowcard")
high = temps[0].text
low=temps[1].text
print("High:",high,"\nLow:",low)
sun = s.find('span',class_="wx-detail-label show-sm")
sun=sun.parent
sunrise=sun.find('span',id="dp0-details-sunrise").text
sunset=sun.find('span',id="dp0-details-sunset").text
print("Sunrise:",sunrise,"\nSunset:",sunset)
url="https://phasesmoon.com/"
page=rp.get(url,headers=headers)
s = soup(page.content,'html.parser')
card=s.find("div",class_="row")
phase=card.find('div').find('div')
print("Moon Phase:",phase.text)
print()
#Get a Quote of the day
url="https://www.brainyquote.com/quote_of_the_day"
page=rp.get(url,headers=headers)
s=soup(page.content,"html.parser")
q=s.find("div",class_="qll-bg")
q1=q.find('a')
print("Quote of the day:",q1.text)
print()
#Get the DOW
url = "https://finance.yahoo.com/quote/%5EDJI/a"
page=rp.get(url,headers=headers)
s = soup(page.content,"html.parser")
card = s.find('div',id="YDC-Lead")
card=card.find('div',class_="D(ib) Mend(20px)")
print("Dow:")
for i in card.find_all('span'):
    print(i.text,end=" ")
print('\n')
#Horoscope
url="https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=7"
page=rp.get(url,headers=headers)
s = soup(page.content,'html.parser')
horoscope = s.find('div',class_="main-horoscope")
h = s.find("p")
h=h.text
ho=""
found=False
for i in h:
    if found:
        ho+=i
    if i == "-":
        found=True
print("Horoscope:",ho)

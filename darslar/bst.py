import requests
from bs4 import BeautifulSoup 

url = requests.get("https://sinoptik.ua/ru/pohoda/urhench")
malumot = BeautifulSoup(url.content,'html.parser')
a = malumot.select('.google-anno-skip')
for i in a:
    shaxar = i.select("._8X9sSr2b")[0].text
    kun = i.select(".xM6dxfW4")[0].text
    Ob_Havo = i.select(".oOVtmpFl")[0].text
print(f"Shaxar {shaxar}\nKun {kun}\nOb-Havo {Ob_Havo}")    










































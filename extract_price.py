import requests
import os
import pandas as pd
from bs4 import BeautifulSoup

url1=["https://www.flipkart.com/realme-buds-air-5-50db-anc-12-4mm-dynamic-bass-driver-upto-38-hours-playback-bluetooth-headset/p/itm8102ba49bb015?pid=ACCGSAP5U93BWXUY&lid=LSTACCGSAP5U93BWXUYFDYDEP&marketplace=FLIPKART&store=0pm%2Ffcn&srno=b_1_10&otracker=browse&fm=organic&iid=a30872ef-89d7-4306-8f4a-213b9e6e037f.ACCGSAP5U93BWXUY.SEARCH&ppt=browse&ppn=browse&ssid=rva2win10g0000001718887677781"]

def extract(url):
    webpages=requests.get(url)
    web=webpages.content
    soup=BeautifulSoup(web,"html.parser")
    value=soup.find("div",{"class":"Nx9bqj CxhGGd"})
    m=value.text
    print(m)

result=[extract(url) for url in url1]
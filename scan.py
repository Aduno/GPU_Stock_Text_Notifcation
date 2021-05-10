import bs4
import threading
import smtplib
from email.message import EmailMessage
from datetime import datetime
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent


def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to'] = to
    msg['from'] = user

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def bestBuy(search):
    link=""
    ua = UserAgent()
    opts = Options()
    opts.add_argument("user-agent="+ua.random)
    driver = webdriver.Chrome(options=opts)
    driver.get(search)
    time.sleep(2)
    loop = True

    while loop:
        html = driver.page_source
        soup = bs4.BeautifulSoup(html,"html.parser")
        item = soup.find_all("span",{"class":"container_3LC03"})
        base_url = "https://www.bestbuy.ca"
        stock = []
        i = 0

        for product in item:
            if("Available" in product.text):
                stock.append(product.find_parent("a")['href'])
                loop=False
        
        for url in stock:
            link += (base_url+url+"\n")
        
        if loop==False:
            email_alert("",link,phone)
            print(link)

        time.sleep(random.randint(17,28))
        driver.refresh()
        
def timer():
    while True:
        print(datetime.now().strftime('%d %H:%M:%S'))
        time.sleep(60)
def readFile():
    f = open("info.txt","r")
    user = f.readline()
    password = f.readline()
    phone = f.readline()

if __name__==  "__main__":
    i=0
    loop=True
    gpuBestBuy ={
        "3060": "https://www.bestbuy.ca/en-ca/category/graphics-cards/20397?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253APC%2BComponents%253Bcategory%253AGraphics%2BCards%253Bcustom0graphicscardmodel%253AGeForce%2BRTX%2B3060",
        "3060ti": "https://www.bestbuy.ca/en-ca/category/graphics-cards/20397?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253APC%2BComponents%253Bcategory%253AGraphics%2BCards%253Bcustom0graphicscardmodel%253AGeForce%2BRTX%2B3060%2BTi",
        "3070": "https://www.bestbuy.ca/en-ca/category/graphics-cards/20397?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253APC%2BComponents%253Bcategory%253AGraphics%2BCards%253Bcustom0graphicscardmodel%253AGeForce%2BRTX%2B3070",
        "3080": "https://www.bestbuy.ca/en-ca/category/graphics-cards/20397?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253APC%2BComponents%253Bcategory%253AGraphics%2BCards%253Bcustom0graphicscardmodel%253AGeForce%2BRTX%2B3080",
        "3090": "https://www.bestbuy.ca/en-ca/category/graphics-cards/20397?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253APC%2BComponents%253Bcategory%253AGraphics%2BCards%253Bcustom0graphicscardmodel%253AGeForce%2BRTX%2B3090"
    }
    gpuMemoryExp ={
        "3060": "https://www.memoryexpress.com/Category/VideoCards?FilterID=f1b0a6e4-f41e-5fea-c242-d1bac7b02bf2",
        "3060ti": "https://www.memoryexpress.com/Category/VideoCards?FilterID=75668704-944f-8e1a-4cca-036beb9638a8",
        "6700xt": "https://www.memoryexpress.com/Category/VideoCards?FilterID=0901d9d6-31e0-987f-382c-e66e7ee23a8a",
        "6800": "https://www.memoryexpress.com/Category/VideoCards?FilterID=8d5ba2df-0447-8b14-4791-aee8db2800b0",
        "6800xt": "https://www.memoryexpress.com/Category/VideoCards?FilterID=9705ada8-e2b2-0ac9-738e-5e92c99a5932",
        "6900xt": "https://www.memoryexpress.com/Category/VideoCards?FilterID=a546466e-2a58-905e-129b-fc735319acbf"
        
    }
    searchList =[]
    currentTime = threading.Thread(target=timer)
    readFile()
    # f = open("info.txt","r")
    # user = f.readline()
    # password = f.readline()
    # phone =  f.readline()

    print("What GPU are you looking for?")
    print("Please enter one at a time. Once done, enter \"done\"")
    print("Available options: 3060,3060ti,3070,3080,3090: ")
    while loop:
        search = input()
        while(search!="3060" and search!="3060ti" and search!="3070" and search!="3080" and search!="3090" and search!="done"):
            search = input("Invalid input. Please select from the list provided: ")
        if (search=="done"):
            loop=False
        else:
            searchList.append(search)

    for product in searchList:
        searchList[i] = gpuLinks[product] 
        i+=1

    for i,name in enumerate(searchList):
        best = threading.Thread(target=bestBuy, args=[searchList[i]])
        best.start()
        time.sleep(2)
    print("Beginning search...")
    currentTime.start()

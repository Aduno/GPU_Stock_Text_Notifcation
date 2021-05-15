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

        #Finds item in stock and takes the href and stops the loop
        for product in item:
            if("Available" in product.text):
                stock.append(product.find_parent("a")['href'])
                loop=False
        #Appends a full url from the href
        for url in stock:
            link += (base_url+url+"\n")
        #Sends a message to the phone
        if loop==False:
            email_alert("",link,phone)
            print(link)

        time.sleep(random.randint(19,24))
        driver.refresh()

def memExp(search):
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
        itemTotal = soup.find_all("div",{"class":"c-shca-icon-item"})
        base_url = "https://www.memoryexpress.com"
        stock = []
        pop = []
        #Different method of extracting info for memory express compared to BB
        #Removes the elements that are out of stock
        for x in range(len(itemTotal)):
            if(itemTotal[x].find("div",{"class":"c-shca-icon-item__body-inventory"})):
                itemTotal[x].decompose()
                pop.insert(0,x)
        for index in pop:
            del itemTotal[index]
        #Extracts the href links from the tag
        for item in itemTotal:
            tag = item.find("a",{"class":"c-shca-add-product-button c-shca-icon-item__summary-buy"})
            stock.append(tag.get("href"))

        #Appends the full url from the href and stops the loop
        for url in stock:
            link += (base_url+url+"\n")
            loop=False

        #Sends a message to the phone if there are items in stock
        if loop==False:
            email_alert("",link,phone)
            print(link) 
        time.sleep(random.randint(20,30))
        driver.refresh()

def timer():
    while True:
        print(datetime.now().strftime('%d %H:%M:%S'))
        time.sleep(60)

def readFile():
    user = f.readline()
    password = f.readline()
    phone = f.readline()
    return (user,password,phone)


if __name__==  "__main__":
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
        "3070": "https://www.memoryexpress.com/Category/VideoCards?FilterID=e3034e65-f2ac-35f1-26eb-277b7a7e9ce9",
        "3080": "https://www.memoryexpress.com/Category/VideoCards?FilterID=45788ec3-6bb1-e460-abe6-afa274b9d30e",
        "3090": "https://www.memoryexpress.com/Category/VideoCards?FilterID=0faf222f-0400-d211-b926-04fdfc0bfa85",
        "6700xt": "https://www.memoryexpress.com/Category/VideoCards?FilterID=0901d9d6-31e0-987f-382c-e66e7ee23a8a",
        "6800": "https://www.memoryexpress.com/Category/VideoCards?FilterID=8d5ba2df-0447-8b14-4791-aee8db2800b0",
        "6800xt": "https://www.memoryexpress.com/Category/VideoCards?FilterID=9705ada8-e2b2-0ac9-738e-5e92c99a5932",
        "6900xt": "https://www.memoryexpress.com/Category/VideoCards?FilterID=a546466e-2a58-905e-129b-fc735319acbf"
        
    }
    validInputs = ["3060","3060ti","3070","3080","3090","6700xt","6800","6800xt","6900xt","done"]
    searchList =[]
    currentTime = threading.Thread(target=timer)
    
    f = open("info.txt","r")
    user,password,phone = readFile()
    f.close()

    print("What GPU are you looking for?")
    print("Please enter one at a time. Once done, enter \"done\"")
    print("Available options:")
    print("Nvidia: 3060,3060ti,3070,3080,3090")
    print("AMD: 6700xt,6800,6800xt,6900xt\n")

    loop=True
    while loop:
        search = input()
        search = search.lower()
        while(search not in validInputs):
            search = input("Invalid input. Please select from the list provided: ")
        if (search=="done"):
            loop=False
        else:
            searchList.append(search)
    
    bestList=[]
    memList=[]
    for product in searchList:
        try:
            bestList.append(gpuBestBuy[product]) 
        except:
            pass
        try:
            memList.append(gpuMemoryExp[product])
        except:
            pass
    del searchList


    if(len(bestList)>0):
        for i,name in enumerate(bestList):
            best = threading.Thread(target=bestBuy, args=[bestList[i]])
            best.start()
            time.sleep(1)

    if(len(memList)>0):
        for i,name in enumerate(memList):
            mem = threading.Thread(target=memExp, args=[memList[i]])
            mem.start()
            time.sleep(1)

    print("Beginning search...")
    currentTime.start()

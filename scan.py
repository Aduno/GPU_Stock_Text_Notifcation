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
    #opts.add_argument("headless")
    #search3070 = https://www.bestbuy.ca/en-ca/search?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253APC%2BComponents%253Bcategory%253AGraphics%2BCards&search=3070
    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.bestbuy.ca/en-ca/collection/rtx-30-series-graphic-cards/316108?path=category%253AComputers%2B%2526%2BTablets%253Bcategory%253APC%2BComponents%253Bcategory%253AGraphics%2BCards%253Bcustom0graphicscardmodel%253AGeForce%2BRTX%2B3070%257CGeForce%2BRTX%2B3060%2BTi%257CGeForce%2BRTX%2B3060")
    time.sleep(3)
    loop = True
    while loop:
        html = driver.page_source
        soup = bs4.BeautifulSoup(html,"html.parser")

        item = soup.find_all("span",{"class":"container_3LC03"})

        stock = []
        i = 0
        for product in item:
            if("Available" in product.text):
                stock.append(product.find_parent("a")['href'])
                loop=False
        base_url = "https://www.bestbuy.ca"
        
        for url in stock:
            link += (base_url+url+"\n")
        
        
        if loop==False:
            email_alert("",link,phone)
            print(link)

        time.sleep(random.randint(15,17))
        driver.refresh()
        
def timer():
    while True:
        print(datetime.now().strftime('%d %H:%M:%S'))
        time.sleep(60)
    
best = threading.Thread(target=bestBuy)
currentTime = threading.Thread(target=timer)
i=0
loop=True
searchList =[]


#The user input can be removed if desired.
user = input("Enter the app email. Format: [youremailhere]@example.com: ")
password = input("Enter the app password: ")
phone = input("Enter phone details. Format: [your phone number]@[carrier domain].ca: ")

print("What GPU are you looking for?")
print("Please enter one at a time. Once done, enter ""done""")
print("Available options: 3060,3060ti,3070,3080,3090: ")
while loop:
    search = input()
    while(search!="3060" and search!="3060ti" and search!="3070" and search!="3080" and search!="3090" and search!="done"):
        search =input("Invalid input. Please select from the list provided: ")
    if (search=="done"):
        loop=False
    else:
        searchList.append(search)

    
#Need to fine a method to pass parameter to function
#Need to run multiple threads in the function depending on the user request OR find a way to select on the best buy page

best.start()
print("Beginning search...")
currentTime.start()

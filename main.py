from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import csv
from time import sleep
import pandas as pd
from openpyxl.workbook import Workbook
service = Service("chromedriver.exe")
option = webdriver.ChromeOptions()
option.add_argument("start-maximized")
driver = webdriver.Chrome(service=service,options=option)
# driver.get("https://www.google.com")
l=[580011, 580007, 580114, 581105, 581204, 801112, 803118, 496551, 496665, 496116, 496111, 496450, 360020]
pincode=[]
a=[]
addr=[]
n=[]
website=[]
ph=[]
count=0
def web():
     try:
          ad=driver.find_element(By.CLASS_NAME,"n1obkb")
          add=ad.get_attribute('href')
          text=add
          website.append(text)
     except:
          website.append(" ")
def phone():
     try:
          ad=driver.find_element(By.CSS_SELECTOR,"[data-dtype='d3ph']")
          text=ad.text
          ph.append(text)
     except:
          ph.append(" ")
def name() :
        try:
            add=driver.find_element(By.CSS_SELECTOR,"[data-attrid='title']")
            text=add.text
            n.append(text)
        except:
            n.append(" ")
def address()   :
        try:
            add=driver.find_element(By.CLASS_NAME,"LrzXr")
            text=add.text
            addr.append(text)
            length=len(text)
            text=text[length-6:]
            a.append(text)
        except:
            a.append(i)
            addr.append(" ")
for i in l:
    def searchplace(count) :
                    try:
                        driver.get("https://www.google.com/search?sca_esv=00e485a4403845c8&sca_upv=1&rlz=1C1CHWL_enIN1089IN1089&tbs=lf:1,lf_ui:2&tbm=lcl&sxsrf=ADLYWILtKagE78nPZDbQH8192XU34_p3MQ:1716484346537&q=dairies+at+"+str(i)+"+in+india")
                        sleep(3)
                        if (count==0):
                          sleep(20)
                        place=driver.find_element(By.ID, "APjFqb")
                        place.clear()
                        if(count%5==0):
                            sleep(5)
                    except:
                        return
                    # if(count%10==0):
                    #       sleep(10)
    searchplace(count)
    count+=1
    try:
         ad=driver.find_element(By.CLASS_NAME,"qrtJgd")
         if(ad.is_displayed()):
            continue
    except:
         pass
    try:
         pages=driver.find_elements(By.CSS_SELECTOR,"a.fl")
         for button in pages:
            try:
                scroll = driver.find_elements(By.CSS_SELECTOR, "a.vwVdIc.wzN8Ac.rllt__link.a-no-hover-decoration")
                for k in scroll :
                    k.click()
                    sleep(2)
                    name()
                    address()
                    web()
                    phone()
                    pincode.append(i)
                button.click()

            except:
                    sleep(1)
                    pass
    except:
         try:
                scroll = driver.find_elements(By.CSS_SELECTOR, "a.vwVdIc.wzN8Ac.rllt__link.a-no-hover-decoration")
                for k in scroll :
                    k.click()
                    sleep(0.75)
                    name()
                    address()
                    web()
                    phone()
                    pincode.append(i)
                button.click()
         except:
            pass
driver.quit()
list_zip=list(zip(n,addr,a,website,ph,pincode))
df=pd.DataFrame(list_zip, columns=['Name',"address",'pincode','website','phone number','scrap'])
file='india_dairy5.csv'
df.to_csv(file,encoding="utf-8")
# print(df)
# print(n)
# print(addr)
# print(a)
# print(ph)
# print(website)
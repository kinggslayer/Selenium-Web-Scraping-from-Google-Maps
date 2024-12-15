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

# some pincode for example we have taken in list
list_of_pincodes =[580011, 580007, 580114, 581105, 581204, 801112, 803118, 496551, 496665, 496116, 496111, 496450, 360020]

# intialized lists to store data
pincode_from_list=[]
pincode_from_address=[]
address=[]
name=[]
website=[]
phone_number=[]
count=0
# made functions for each required entries
def get_website():
     try:
          ad=driver.find_element(By.CLASS_NAME,"n1obkb")
          add=ad.get_attribute('href')
          text=add
          website.append(text)
     except:
          website.append(" ")
def get_phone():
     try:
          ad=driver.find_element(By.CSS_SELECTOR,"[data-dtype='d3ph']")
          text=ad.text
          phone_number.append(text)
     except:
          phone_number.append(" ")
def get_name() :
        try:
            add=driver.find_element(By.CSS_SELECTOR,"[data-attrid='title']")
            text=add.text
            name.append(text)
        except:
            name.append(" ")
def get_address()   :
        try:
            add=driver.find_element(By.CLASS_NAME,"LrzXr")
            text=add.text
            address.append(text)
            length=len(text)
            text=text[length-6:]
            pincode_from_address.append(text)
        except:
            pincode_from_address.append(i)
            address.append(" ")

# for each pincode in list 
for i in list_of_pincodes:
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
    searchplace(count)
    count+=1
    try:
         ad=driver.find_element(By.CLASS_NAME,"qrtJgd")
         if(ad.is_displayed()):
            continue
    except:
         pass
    try:
        # iterating in each page for each query of pincode
         pages=driver.find_elements(By.CSS_SELECTOR,"a.fl")
         for button in pages:
            try:
                scroll = driver.find_elements(By.CSS_SELECTOR, "a.vwVdIc.wzN8Ac.rllt__link.a-no-hover-decoration")
                for k in scroll :
                    k.click()
                    sleep(2)
                    get_name()
                    get_address()
                    get_website()
                    get_phone()
                    pincode_from_list.append(i)
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
                    get_name()
                    get_address()
                    get_website()
                    get_phone()
                    pincode_from_list.append(i)
                button.click()
         except:
            pass
driver.quit()

# zip all data
list_zip=list(zip(name,address,pincode_from_address,website,phone_number,pincode_from_list))
df=pd.DataFrame(list_zip, columns=['Name',"address",'pincode','website','phone number','scrap'])

# give name to data file
file='india_dairy5.csv'

# make csv file
df.to_csv(file,encoding="utf-8")
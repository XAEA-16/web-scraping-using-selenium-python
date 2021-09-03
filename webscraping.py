import datetime

# The main  aim for writing this is to give a start data and end data this code can be use any where you wanting to iterate over date just adjust format accordingly
dates=[]
# 16-Mar-2006
# 31-Dec-2010
start = datetime.datetime.strptime("2006-03-16", "%Y-%m-%d")
end = datetime.datetime.strptime("2010-12-31", "%Y-%m-%d")
date_array = \
    (start + datetime.timedelta(days=x) for x in range(0, (end-start).days))
for date_object in date_array:
    dates.append(date_object.strftime("%d-%b-%Y"))
   

print(len(dates))

# Load selenium components
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import pandas as pd


url = "https://bsestarmf.in/RptNavMaster.aspx"
# ChromeDriverManager().install()
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "E:\Project-data"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = r"E:\Users\rahul\.wdm\drivers\chromedriver\win32\92.0.4515.107\chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)
driver.get(url)
dataa=driver.find_element_by_id("txtToDate").clear()
for i in dates:
    dataa=driver.find_element_by_id("txtToDate").clear()
    dataa=driver.find_element_by_id("txtToDate").send_keys(i)
    dataa=driver.find_element_by_id("txtToDate").click()
    # this is to show the view 
#     frame_ref = driver.find_element_by_id("btnSubmit").click()
    # # this is to download the data 
    down_data=driver.find_element_by_id('btnText').click()
     get_data=driver.find_element_by_class_name("glbTableD")
     ls=[]
     ls.append(get_data.text)
     print(get_data.text)
# i created a list and save the data to in numpy this is totally optional as you can download directly from the website
#     np.savetxt("try1.txt", ls,delimiter =", ",fmt ='% s')

#  code to save data in csv format from a given list 
# np.savetxt("demo2.txt",ls,fmt ='%s')
# data=pd.read_csv("demo.txt")
# data.to_csv("demo1.csv",index=None,delimiter="|")


driver.quit()

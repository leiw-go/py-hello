from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import os

driver = webdriver.Chrome()
driver.get("https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=36")
try:
    element = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"result-item-title"))
    )
except:driver.quit()
else:
    #html = urlopen("https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=36")
    #bsobj = BeautifulSoup(element.read(),"html.parser")
    bsobj = BeautifulSoup(driver)
    print(bsobj.prettify())
    namelist = bsobj.findAll("a")
    for name in namelist:

        f = open("sourcecatch.txt", "a")
        f.write('\n'+name.get_text())
        f.flush()
        f.close
        
#os.system("python qqmail.py")

#<span _ngcontent-gpl-c49="" xplhighlight="" xplmathjax="">IEEE Transactions on Geoscience and Remote Sensing publication information</span>
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#chrome_options = Options()
#driver = webdriver.Chrome(chrome_options=chrome_options)
browser = webdriver.Chrome()
browser.get("https://ieeexplore.ieee.org/xpl/mostRecentIssue.jsp?punumber=36")

#browser.implicitly_wait(30) # seconds 
#te = browser.find_element_by_class_name('result-item-title')
#print(te.text)


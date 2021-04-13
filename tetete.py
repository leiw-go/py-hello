# coding=gbk

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_opt = Options()      # 创建参数设置对象.
#chrome_opt.add_argument('--headless')   # 无界面化.
#chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.

# 创建Chrome对象并传入设置信息.
driver = webdriver.Chrome(chrome_options=chrome_opt)        
# 操作这个对象.
driver.get('https://www.baidu.com')     # get方式访问百度.
time.sleep(2)
print(driver.find_element_by_class_name("mnav c-font-normal c-color-t"))       # 打印加载的page code, 证明(prove) program is right.
driver.quit()
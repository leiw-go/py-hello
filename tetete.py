# coding=gbk

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_opt = Options()      # �����������ö���.
#chrome_opt.add_argument('--headless')   # �޽��滯.
#chrome_opt.add_argument('--disable-gpu')    # ���������޽��滯.
chrome_opt.add_argument('--window-size=1366,768')   # ���ô��ڴ�С, ���ڴ�С����Ӱ��.

# ����Chrome���󲢴���������Ϣ.
driver = webdriver.Chrome(chrome_options=chrome_opt)        
# �����������.
driver.get('https://www.baidu.com')     # get��ʽ���ʰٶ�.
time.sleep(2)
print(driver.find_element_by_class_name("mnav c-font-normal c-color-t"))       # ��ӡ���ص�page code, ֤��(prove) program is right.
driver.quit()
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

html = urlopen("https://www.runoob.com/")
bsobj = BeautifulSoup(html.read(),"html.parser")
namelist = bsobj.findAll("h4")
for name in namelist:

    f = open("sourcecatch.txt", "a")
    f.write('\n'+name.get_text())
    f.flush()
    f.close
    
os.system("python qqmail.py")

#<span _ngcontent-gpl-c49="" xplhighlight="" xplmathjax="">IEEE Transactions on Geoscience and Remote Sensing publication information</span>
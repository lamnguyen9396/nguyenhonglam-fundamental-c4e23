from urllib.request import urlopen #(thư viện)
from bs4 import BeautifulSoup
from collections import OrderedDict
#1. Connect to the page (bước thủ tục)
url='https://dantri.com.vn'
connection = urlopen(url)
#2. Download the page content (bước thủ tục)
raw_data=connection.read()
page_content=raw_data.decode("utf8") #utf8 = unicode - xử lí kí tự có dấu

with open("dantri.html", "wb") as f: #wb write binery = du lieu tho
    f.write(raw_data)

#3. Find ROI (region of interest)
soup=BeautifulSoup(page_content, "html.parser")
ul=soup.find("ul","ul1 ulnew") #href="", id=""
# print(ul.prettify())

#4. Extract data
li_list=ul.find_all("li") #li_list là list soup
# li=li_list[0]
# h4=li.h4
# print(h4)
# a=h4.a
news_list=[]
for li in li_list:
    a=li.h4.a
    title=a.string
    # print(a.string)
    link= url+a["href"]
    news=OrderedDict({
        "title":title,
        "link":link
    })
    news_list.append(news)
print(news_list)

#5. Save data (bước thủ tục)
import pyexcel
pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")

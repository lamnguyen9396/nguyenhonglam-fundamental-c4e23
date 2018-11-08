from urllib.request import urlopen #(thư viện)
from bs4 import BeautifulSoup
from collections import OrderedDict
#1. Connect to the page (bước thủ tục)
url='https://www.apple.com/itunes/charts/songs'
connection = urlopen(url)
#2. Download the page content (bước thủ tục)
raw_data=connection.read()
page_content=raw_data.decode("utf8") #utf8 = unicode - xử lí kí tự có dấu

with open("itunes.html", "wb") as f: #wb write binery = du lieu tho
    f.write(raw_data)

#3. Find ROI (region of interest)
soup=BeautifulSoup(page_content, "html.parser")
ul=soup.find("section","section chart-grid")

# #4. Extract data
li_list=ul.find_all("li") #li_list là list soup
topchart_list=[]
for li in li_list:
    title=li.h3.a.string
    artist=li.h4.a.string


    topchart=OrderedDict({
        "title":title,
        "artist":artist
    })
    topchart_list.append(topchart)
print(topchart_list)

# #5. Save data (bước thủ tục)
import pyexcel
pyexcel.save_as(records=topchart_list, dest_file_name="topchart.xlsx")




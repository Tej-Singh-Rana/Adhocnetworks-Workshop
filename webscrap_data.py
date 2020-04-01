# importing modules
from bs4 import BeautifulSoup   # web scraping
import requests    # replacement of URLLIB
import time

# now taking corona live data set

url="https://www.************.****/coronavirus/"
# now connecting with https protocol
#sourcepage=requests.get(url)
htmlpage=requests.get(url)

# print info
#print(htmlpage.text)
#print(htmlpage.content)
purehtmlpage=htmlpage.content
soup=BeautifulSoup(purehtmlpage,'html5lib')   # this process called souping

#print(type(soup))
#<class 'bs4.BeautifulSoup'>

tb=soup.find_all('table',class_="table table-bordered table-hover main_table_countries")

# finding all tables rows

for trr in tb[0].find_all('tr'):
  for rows in trr.find_all('th'):
    print(rows.text)

# now scraping data for each row with normal country data

# for trr1 in tb[0].find_all('tr'):
#   for rows in trr1.find_all('td'):
#     print(rows.text)
#     time.sleep(1)

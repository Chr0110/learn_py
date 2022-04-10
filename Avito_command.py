from pickle import TRUE
from unicodedata import category
from unittest import result
import requests
from bs4 import BeautifulSoup
import csv
#import re
from datetime import date, datetime
from itertools import zip_longest

pricess_tab = []
description_tab = []
category_tab = []
localisation_tab = []
time_tab = []
links_tab = []
phone_tab = []
result = requests.get("https://www.avito.ma/fr/maroc/%C3%A0_vendre")
src = result.content
soup = BeautifulSoup(src, "lxml")
prices = soup.find_all("div", {"class":"oan6tk-5"})
description = soup.find_all("span", {"class":"oan6tk-17"})
catego = soup.find_all("p", {"class":"sc-1x0vz2r-0 iEJWiq oan6tk-18 bhnuSP"})
localisation = soup.find_all("span", {"class":"sc-1x0vz2r-0 hCOOjL"})
time = soup.find_all("span", {"class":"sc-1x0vz2r-0 hCOOjL"})
links = soup.find_all("div",{"class":"oan6tk-0 gbnYeC", "class":"oan6tk-0 dLOfLV"})
for i in range(len(description)):
    pricess_tab.append(prices[i].text)
    description_tab.append(description[i].text)
    category_tab.append(catego[i].text)
for i in range(len(localisation)):
    if localisation[i].text.find(":") == -1:
        localisation_tab.append(localisation[i].text)
    elif time[i].text.find(":") != -1:
        time_tab.append(time[i].text)

# for link in links_tab:
#     result = requests.get(link)
#     src = result.content  
#     soup = BeautifulSoup(src, "lxml")
#     phone = soup.find("h1", {"class":"sc-1x0vz2r-0 iLDWht"})
#     print(phone.text)

first_file = [category_tab, description_tab, pricess_tab, localisation_tab, time_tab, links_tab, phone_tab]
exported = zip_longest(*first_file)
with open("/Users/eradi-/Desktop/learn_py/first.csv", "w") as file:
    wr = csv.writer(file)
    wr.writerow(["Category", "Description", "Price", "Location", "Time", "Offer link", "Phone"])
    wr.writerows(exported)
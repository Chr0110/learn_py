from pickle import TRUE
from unicodedata import category
from unittest import result
import requests
from bs4 import BeautifulSoup
import csv
import re
from datetime import date, datetime
from itertools import zip_longest
# def is_int(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False
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
catego = soup.find_all("p", {"class":"sc-1x0vz2r-0 eJWySg oan6tk-18 dPesmp"})
localisation = soup.find_all("span", {"class":"sc-1x0vz2r-0 kIeipZ"})
time = soup.find_all("span", {"class":"sc-1x0vz2r-0 kIeipZ"})
links = soup.find_all("div",{"class":"oan6tk-0 hEwuhz"})
a = 0
for i in range(len(description)):
    pricess_tab.append(prices[i].text)
    description_tab.append(description[i].text) 
    category_tab.append(catego[i].text)
for i in range(len(localisation)):
    if localisation[i].text.find(":") == -1:
        localisation_tab.append(localisation[i].text)
    elif time[i].text.find(":") != -1:
        time_tab.append(time[i].text)
for j in range(len(links)):
    links_tab.append(links[j].find("a").attrs['href'])
for link in links_tab:
    result = requests.get(link)
    src = result.content  
    soup = BeautifulSoup(src, "lxml")
    phone = soup.find("h1", {"class":"sc-1x0vz2r-0 iLDWht"})
    print(phone.text)
    #phone_tab.append(phone.text)
    #phone2 = soup1.find("a").attrs['href']
    #a += 1
    #print(a)
    #phone_tab.append(phone[a].text)
    #print(phone2)
#print(a)
# print(pricess_tab)
# print(description_tab)
# print(category_tab)
# print(localisation_tab)
first_file = [category_tab, description_tab, pricess_tab, localisation_tab, time_tab, links_tab, phone_tab]
exported = zip_longest(*first_file)
with open("/Users/eradi-/Desktop/learn_py/first.csv", "w") as file:
    wr = csv.writer(file)
    wr.writerow(["Category", "Description", "Price", "Location", "Time", "Offer link", "Phone"])
    wr.writerows(exported)
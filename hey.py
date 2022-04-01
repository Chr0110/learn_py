from unicodedata import category
from unittest import result
import requests
from bs4 import BeautifulSoup
import csv
import re
from itertools import zip_longest
pricess_tab = []
description_tab = []
category_tab = []
time_localisation_tab = []
result = requests.get("https://www.avito.ma/fr/maroc/%C3%A0_vendre")
src = result.content
soup = BeautifulSoup(src, "lxml")
prices = soup.find_all("div", {"class":"oan6tk-5"})
description = soup.find_all("span", {"class":"oan6tk-17"})
catego = soup.find_all("p", {"class":"sc-1x0vz2r-0 eJWySg oan6tk-18 dPesmp"})
time_localisation = soup.find_all("span", {"class":"sc-1x0vz2r-0 kIeipZ"})
for i in range(len(description)):
    pricess_tab.append(prices[i].text)
    description_tab.append(description[i].text)
    category_tab.append(catego[i].text)
    time_localisation_tab.append(time_localisation[i].text)
# print(pricess_tab)
# print(description_tab)
# print(category_tab)
# print(time_localisation_tab)
first_file = [category_tab, description_tab, pricess_tab, time_localisation_tab]
exported = zip_longest(*first_file)
with open("/Users/eradi-/Desktop/learn_py/first.csv", "w") as file:
    wr = csv.writer(file)
    wr.writerow(exported)
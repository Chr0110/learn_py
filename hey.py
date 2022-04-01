from unicodedata import category
from unittest import result
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
pricess_tab = []
description_tab = []
category_tab = []
localisation_tab = []
result = requests.get("https://www.avito.ma/fr/maroc/%C3%A0_vendre")
src = result.content
soup = BeautifulSoup(src, "lxml")
prices = soup.find_all("div", {"class":"oan6tk-5"})
description = soup.find_all("span", {"class":"oan6tk-17"})
catego = soup.find_all("p", {"class":"sc-1x0vz2r-0 eJWySg oan6tk-18 dPesmp"})
localisation = soup.find_all("span", {"class":"sc-1x0vz2r-0 kIeipZ"})
for i in range(len(description)):
    pricess_tab.append(prices[i].text)
    description_tab.append(description[i].text)
    category_tab.append(catego[i].text)
    if localisation[i].text != int:
        print(localisation[i].text)
# print(pricess_tab)
# print(description_tab)
# print(category_tab)
# print(localisation_tab)
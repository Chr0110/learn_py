#import requests
#from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

with open ("/Users/eradi-/Desktop/learn_py/first.csv", "w") as first:
    wr = csv.writer(first)
    wr.writerow(["one", "two", "three"])